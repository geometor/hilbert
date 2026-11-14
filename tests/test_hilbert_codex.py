"""Comprehensive test suite for `geometor-hilbert` Book Codex, parsers, figures, and apparatus."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path

from geometor.hilbert import (
    __version__,
    apparatus_slug,
    load_apparatus,
    verify_sources_manifest,
)
from geometor.hilbert.chapters_meta import SECTIONS_META, UNITS

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCSRC = REPO_ROOT / "docsrc"
GRUNDLAGEN_DIR = DOCSRC / "grundlagen"
FIGURES_DIR = DOCSRC / "_static" / "figures"

EXPECTED_FIGURES = {
    "fig_betweenness_pasch.svg",
    "fig_sas_supplementary.svg",
    "fig_non_congruence_model.svg",
    "fig_pascal_orthogonal.svg",
    "fig_segment_multiplication.svg",
    "fig_segment_distributive.svg",
    "fig_polygon_equivalence.svg",
    "fig_desargues_configuration.svg",
    "fig_non_desarguesian_plane.svg",
    "fig_desargues_segment_algebra.svg",
    "fig_gauge_constructions.svg",
}


def test_package_version() -> None:
    """Package exposes a semantic version string."""
    assert __version__ == "0.1.1"


def test_sources_manifest_sha256_integrity() -> None:
    """Both verbatim primary witnesses match SHA-256 digests and byte lengths."""
    results = verify_sources_manifest(REPO_ROOT)
    assert len(results) == 2
    ids = {r["id"] for r in results}
    assert ids == {"townsend-1902-en", "teubner-1899-de"}
    assert all(r["verified"] is True for r in results)


def test_scholarly_apparatus_and_concordance_queries() -> None:
    """Concordance loader and cross-repository search helpers return accurate entries."""
    app = load_apparatus(REPO_ROOT)
    assert len(app.entries) == 13
    assert len(app.concordance_meta.get("edition_shifts", [])) == 5
    assert len(app.persons) >= 40
    assert len(app.glossary) >= 30
    assert len(app.citations) >= 30

    ch1 = app.by_chapter("chapter-1")
    assert len(ch1) == 6
    sec14 = app.by_section("14")
    assert len(sec14) == 1 and sec14[0].id == "sec-13-17-proportion"
    assert app.by_section("§ 14") == sec14

    assert any(e.id == "sec-06-07-congruence" for e in app.search_euclid("superposition"))
    assert any(e.id == "sec-06-07-congruence" for e in app.search_euclid("Post. 4"))
    assert any(e.id == "sec-03-04-order" for e in app.search_hoenen("Moore"))
    assert any(e.id == "sec-03-04-order" for e in app.search_hoenen("Hardy"))
    assert len(app.search_pappus()) >= 5
    assert any(e.id == "sec-13-17-proportion" for e in app.search_pappus("Hexagon"))


def test_codex_four_track_file_tree_and_book_layout() -> None:
    """All 41 Book Codex RST files exist, begin with `:layout: book`, and declare anchors."""
    apparatus_pages = [
        ("index.rst", ".. _grundlagen-index:"),
        ("concordance.rst", ".. _concordance:"),
        ("bibliography.rst", ".. _bibliography:"),
        ("persons.rst", ".. _persons:"),
        ("glossary.rst", ".. _glossary:"),
    ]
    for fname, anchor in apparatus_pages:
        fpath = GRUNDLAGEN_DIR / fname
        assert fpath.is_file(), f"Missing apparatus page: {fpath}"
        txt = fpath.read_text(encoding="utf-8")
        assert txt.startswith(":layout: book\n"), f"{fname} missing :layout: book header"
        assert anchor in txt, f"{fname} missing anchor {anchor}"

    assert len(UNITS) == 9
    for unit in UNITS:
        slug = unit["slug"]
        for track in ("en", "de", "summary", "notes"):
            tpath = GRUNDLAGEN_DIR / slug / f"{slug}-{track}.rst"
            assert tpath.is_file(), f"Missing track file: {tpath}"
            txt = tpath.read_text(encoding="utf-8")
            assert txt.startswith(":layout: book\n"), f"{tpath.name} missing :layout: book"
            assert f".. _grundlagen-{slug}-{track}:" in txt


def test_all_sections_and_44_theorems_present_in_both_languages() -> None:
    """Both EN and DE tracks contain all 41 section blocks (0..40) and all 44 theorems."""
    assert len(SECTIONS_META) == 41
    en_blob = "\n".join(
        (GRUNDLAGEN_DIR / u["slug"] / f"{u['slug']}-en.rst").read_text(encoding="utf-8")
        for u in UNITS
    )
    de_blob = "\n".join(
        (GRUNDLAGEN_DIR / u["slug"] / f"{u['slug']}-de.rst").read_text(encoding="utf-8")
        for u in UNITS
    )

    en_secs = {int(m) for m in re.findall(r"\.\. _grundlagen-en-s(\d+):", en_blob)}
    de_secs = {int(m) for m in re.findall(r"\.\. _grundlagen-de-s(\d+):", de_blob)}
    assert en_secs == set(range(41))
    assert de_secs == set(range(41))

    en_thms = {int(m) for m in re.findall(r"\.\. _grundlagen-en-thm-(\d+):", en_blob)}
    de_thms = {int(m) for m in re.findall(r"\.\. _grundlagen-de-thm-(\d+):", de_blob)}
    assert en_thms == set(range(1, 45))
    assert de_thms == set(range(1, 45))

    assert ".. _grundlagen-en-preface:" in en_blob
    assert ".. _grundlagen-en-appendix:" in en_blob


def test_calibrated_svg_figures_and_picture_directives() -> None:
    """All 11 SVGs are valid XML `.euclid-graphic` diagrams referenced in both EN and DE tracks."""
    actual_svgs = {p.name for p in FIGURES_DIR.glob("*.svg")}
    assert actual_svgs == EXPECTED_FIGURES

    for svg_name in sorted(EXPECTED_FIGURES):
        svg_path = FIGURES_DIR / svg_name
        raw = svg_path.read_text(encoding="utf-8")
        assert "prefers-color-scheme: dark" in raw, f"{svg_name} missing dark-theme CSS"
        root = ET.fromstring(raw)
        assert "euclid-graphic" in root.attrib.get("class", ""), (
            f"{svg_name} missing euclid-graphic class"
        )

    for track in ("en", "de"):
        blob = "\n".join(
            (GRUNDLAGEN_DIR / u["slug"] / f"{u['slug']}-{track}.rst").read_text(encoding="utf-8")
            for u in UNITS
        )
        referenced = set(re.findall(r"\.\. picture:: /_static/figures/(\S+)", blob))
        assert referenced == EXPECTED_FIGURES


def test_no_residual_latex_or_embedded_python_and_balanced_math() -> None:
    """Generated codex RST files have zero raw LaTeX artifacts, balanced `$`, and no `.py` blocks."""
    forbidden_latex = re.compile(
        r"\\(?:begin\{(?:itemize|center|tabular|flushright|scshape|small)\}|"
        r"emph\{|textit\{|textbf\{|scshape\b|pageref\{|footnote\{|rfa\{)"
    )

    for rst_path in sorted(GRUNDLAGEN_DIR.rglob("*.rst")):
        txt = rst_path.read_text(encoding="utf-8")
        assert "@@" not in txt, f"Unresolved placeholder in {rst_path}"
        assert ".. code-block:: python" not in txt, f"Embedded python block in {rst_path}"
        assert ".. literalinclude::" not in txt, f"Embedded literalinclude in {rst_path}"

        # Strip $$...$$ and $...$ math before scanning for raw TeX structural commands
        no_math = re.sub(r"\$\$.*?\$\$", "DISPLAYMATH", txt, flags=re.DOTALL)
        for lineno, line in enumerate(no_math.splitlines(), 1):
            dollars = [m.start() for m in re.finditer(r"(?<!\\)\$", line)]
            assert len(dollars) % 2 == 0, (
                f"Unbalanced inline $ at {rst_path.name}:{lineno}: {line}"
            )
            prose_only = re.sub(r"(?<!\\)\$.*?(?<!\\)\$", "INLINEMATH", line)
            match = forbidden_latex.search(prose_only)
            assert match is None, (
                f"Residual LaTeX {match.group(0)!r} in {rst_path.name}:{lineno}"
            )


def _extract_role_target(body: str) -> str:
    m = re.search(r"<([^>]+)>\s*$", body.strip())
    return m.group(1).strip() if m else body.strip()


def test_all_scholarly_roles_resolve_to_json_and_rst_anchors() -> None:
    """Every `:person:`, `:term:`, and `:cite:` role resolves to registry keys and RST anchors."""
    app = load_apparatus(REPO_ROOT)
    bib_rst = (GRUNDLAGEN_DIR / "bibliography.rst").read_text(encoding="utf-8")
    per_rst = (GRUNDLAGEN_DIR / "persons.rst").read_text(encoding="utf-8")
    glo_rst = (GRUNDLAGEN_DIR / "glossary.rst").read_text(encoding="utf-8")

    role_re = re.compile(r":(person|term|cite):`([^`]+)`")
    count = 0
    for rst_path in sorted(DOCSRC.rglob("*.rst")):
        if "modules/api" in str(rst_path):
            continue
        txt = rst_path.read_text(encoding="utf-8")
        for role_name, raw_body in role_re.findall(txt):
            # Ignore literal mentions like ``:cite:`` (which have empty/non-matching bodies anyway)
            target = _extract_role_target(raw_body)
            if not target:
                continue
            count += 1
            slug = apparatus_slug(target)
            if role_name == "person":
                assert target in app.persons, f"Missing person {target!r} in {rst_path.name}"
                assert f".. _person-{slug}:" in per_rst
            elif role_name == "term":
                assert target in app.glossary, f"Missing term {target!r} in {rst_path.name}"
                assert f".. _term-{slug}:" in glo_rst
            elif role_name == "cite":
                assert target in app.citations, f"Missing citation {target!r} in {rst_path.name}"
                assert f".. _cite-{slug}:" in bib_rst

    assert count >= 100
