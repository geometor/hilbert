"""Compile the complete 4-track Book Codex and scholarly apparatus for `geometor-hilbert`."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path
from typing import Any

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from geometor.hilbert.chapters_meta import NOTES, SECTIONS_META, SUMMARIES, UNITS
from geometor.hilbert.concordance import (
    ConcordanceEntry,
    HilbertApparatus,
    apparatus_slug,
    default_repo_root,
    load_apparatus,
    verify_sources_manifest,
)
from geometor.hilbert.parser_de import build_german_units
from geometor.hilbert.parser_en import build_english_units


def _format_external_doc_link(repo_path: str, label: str | None = None) -> str:
    """Format a verified intersphinx `:external+<repo>:doc:` reference."""
    if ":" not in repo_path:
        return f"``{repo_path}``"
    repo_name, doc_target = repo_path.split(":", 1)
    disp = label or f"geometor/{repo_name} ({doc_target})"
    return f":external+{repo_name}:doc:`{disp} <{doc_target}>`"


def _section_label_to_anchor(sec_label: str) -> tuple[str, str] | None:
    """Map a section label like `'§ 14'` or `'Introduction'` to `(en_ref, de_ref)`."""
    clean = sec_label.strip()
    if clean == "Introduction":
        return ("grundlagen-en-s0", "grundlagen-de-s0")
    if clean == "Conclusion":
        return ("grundlagen-en-s40", "grundlagen-de-s40")
    if clean.startswith("§"):
        num_str = clean.lstrip("§").strip()
        if num_str.isdigit():
            n = int(num_str)
            return (f"grundlagen-en-s{n}", f"grundlagen-de-s{n}")
    return None


def _render_unit_concordance_digest(entries: list[ConcordanceEntry]) -> str:
    """Render a unit-specific Cross-Repository Concordance section for `<slug>-notes.rst`."""
    if not entries:
        return ""
    lines: list[str] = [
        "",
        "Cross-Repository Concordance Links",
        "----------------------------------",
        "",
        "*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*",
        "",
    ]
    for entry in entries:
        sec_str = ", ".join(entry.hilbert_sections)
        lines.append(f"* **{sec_str}** (:ref:`concordance-{entry.id}`): {entry.summary}")
        for ref in entry.euclid_refs:
            link = _format_external_doc_link(ref["repo_path"], f"Euclid — {ref['locus']}")
            lines.append(f"  - {link}: {ref['relation']}")
        for ref in entry.hoenen_refs:
            link = _format_external_doc_link(ref["repo_path"], f"Hoenen — {ref['locus']}")
            lines.append(f"  - {link}: {ref['relation']}")
        for ref in entry.pappus_refs:
            link = _format_external_doc_link(ref["repo_path"], f"Pappus — {ref['locus']}")
            lines.append(f"  - {link}: {ref['relation']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _build_summary_unit(unit: dict[str, Any]) -> str:
    """Generate `<slug>-summary.rst` for a single treatise unit."""
    slug = unit["slug"]
    base_title = (
        f"{unit['num_en']}: {unit['title_en']}" if slug.startswith("chapter-") else unit["title_en"]
    )
    head_title = f"{base_title} — Summary"
    bar = "=" * len(head_title)

    sec_links: list[str] = []
    for sec_num in unit["sections"]:
        smeta = SECTIONS_META[sec_num]
        sec_links.append(
            f"* **{smeta['title_en']}** — "
            f":ref:`English (p. {smeta['page_en']}) <grundlagen-en-s{sec_num}>` · "
            f":ref:`Deutsch 1899 (S. {smeta['page_de']}) <grundlagen-de-s{sec_num}>`"
        )

    parts: list[str] = [
        ":layout: book",
        "",
        f".. _grundlagen-{slug}-summary:",
        "",
        head_title,
        bar,
        "",
        f".. rubric:: Structural & Mathematical Overview — *{unit['num_de']}: {unit['title_de']}*",
        "",
        ".. contents:: In This Summary",
        "   :local:",
        "   :depth: 2",
        "   :backlinks: none",
        "",
        SUMMARIES[slug].strip(),
        "",
        "Parallel Section Navigator",
        "--------------------------",
        "",
        *sec_links,
        "",
    ]
    return "\n".join(parts)


def _build_notes_unit(unit: dict[str, Any], apparatus: HilbertApparatus) -> str:
    """Generate `<slug>-notes.rst` for a single treatise unit."""
    slug = unit["slug"]
    base_title = (
        f"{unit['num_en']}: {unit['title_en']}" if slug.startswith("chapter-") else unit["title_en"]
    )
    head_title = f"{base_title} — Notes"
    bar = "=" * len(head_title)
    unit_entries = apparatus.by_chapter(slug)
    if slug == "conclusion" and not unit_entries:
        unit_entries = [e for e in apparatus.entries if "Conclusion" in e.hilbert_sections]

    digest = _render_unit_concordance_digest(unit_entries)
    parts: list[str] = [
        ":layout: book",
        "",
        f".. _grundlagen-{slug}-notes:",
        "",
        head_title,
        bar,
        "",
        ".. rubric:: Historical, Philological & Cross-Repository Commentary",
        "",
        ".. contents:: In These Notes",
        "   :local:",
        "   :depth: 2",
        "   :backlinks: none",
        "",
        NOTES[slug].strip(),
    ]
    if digest:
        parts.append(digest.rstrip())
    parts.append("")
    return "\n".join(parts)


def _build_grundlagen_index() -> str:
    """Generate `docsrc/grundlagen/index.rst` (`:layout: book` Conspectus & hidden track toctrees)."""
    parts: list[str] = [
        ":layout: book",
        "",
        ".. _grundlagen-index:",
        "",
        "GRUNDLAGEN DER GEOMETRIE",
        "========================",
        "",
        ".. rubric:: *The Foundations of Geometry* — David Hilbert (1899 / 1902)",
        "",
        "| **Editio Princeps (Deutsch, 1899):** *Festschrift zur Feier der Enthüllung des Gauss-Weber-Denkmals in Göttingen*, Erster Theil, B. G. Teubner, Leipzig, 1899.",
        "| **Authorized English Edition (1902):** Translated by *Edgar Jerome Townsend*, Ph.D., The Open Court Publishing Company, Chicago, 1902 (with Hilbert's 1900–1902 additions).",
        "| **Digital Critical Codex:** Synchronized 4-track edition (*English · Deutsch · Summary · Notes*) curated within the GEOMETOR canon.",
        "",
        ".. epigraph::",
        "",
        "   „So fängt denn alle menschliche Erkenntnis mit Anschauungen an, geht von da zu Begriffen und endigt mit Ideen.“",
        "",
        "   “All human knowledge begins with intuitions, thence passes to concepts and ends with ideas.”",
        "",
        "   — :person:`Immanuel Kant <kant>`, :cite:`*Kritik der reinen Vernunft* <kant:1781>`, *Elementarlehre*, 2. Teil, 2. Abt. (*A 702 / B 730*)",
        "",
        "----",
        "",
        "Conspectus Totius Operis",
        "------------------------",
        "",
    ]

    for unit in UNITS:
        slug = unit["slug"]
        en_head = (
            f"{unit['num_en']}: {unit['title_en']}"
            if slug.startswith("chapter-")
            else unit["title_en"]
        )
        de_head = (
            f"{unit['num_de']}: {unit['title_de']}"
            if slug.startswith("chapter-")
            else unit["title_de"]
        )
        secs = unit["sections"]
        if secs == [0]:
            sec_span = "Preface, Epigraph & Introduction"
        elif secs == [40]:
            sec_span = "Conclusion (*Schlusswort*) & 1902 Appendix"
        else:
            sec_span = f"§§ {secs[0]}–{secs[-1]}"

        parts.extend(
            [
                f"**{en_head}** (*{de_head}* — {sec_span})",
                (f"   :ref:`English (1902) <grundlagen-{slug}-en>` · "
                f":ref:`Deutsch (1899) <grundlagen-{slug}-de>` · "
                f":ref:`Summary <grundlagen-{slug}-summary>` · "
                f":ref:`Notes <grundlagen-{slug}-notes>`"),
                "",
            ]
        )

    parts.extend(
        [
            "----",
            "",
            "Apparatus Criticus & Cross-Repository Indices",
            "---------------------------------------------",
            "",
            ("* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` — "
            "Section-by-section cross-mapping across ``geometor/euclid``, ``geometor/elements``, "
            "``geometor/hoenen``, and ``geometor/pappus``, including the 1899/1902 vs. 1930 7th-edition numbering table."),
            ("* :ref:`Systematic Bibliography <bibliography>` — "
            "Primary editions, historical sources, and foundational commentaries."),
            ("* :ref:`Prosopographical Index of Persons <persons>` — "
            "Geometers, algebraists, and philosophers cited across treatise and commentary."),
            ("* :ref:`Bilingual Mathematical & Philosophical Glossary <glossary>` — "
            "Technical German, Greek, Latin, and metamathematical terminology."),
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: English Edition (1902)",
            "",
        ]
    )
    for unit in UNITS:
        s = unit["slug"]
        parts.append(f"   {s}/{s}-en")

    parts.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Deutsche Festschrift (1899)",
            "",
        ]
    )
    for unit in UNITS:
        s = unit["slug"]
        parts.append(f"   {s}/{s}-de")

    parts.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Summaries & Commentary",
            "",
        ]
    )
    for unit in UNITS:
        s = unit["slug"]
        parts.append(f"   {s}/{s}-summary")
        parts.append(f"   {s}/{s}-notes")

    parts.extend(
        [
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            "   :caption: Critical Apparatus",
            "",
            "   concordance",
            "   bibliography",
            "   persons",
            "   glossary",
            "",
        ]
    )
    return "\n".join(parts)


def _build_concordance_rst(apparatus: HilbertApparatus) -> str:
    """Generate `docsrc/grundlagen/concordance.rst` from `concordance.json`."""
    meta = apparatus.concordance_meta
    parts: list[str] = [
        ":layout: book",
        "",
        ".. _concordance:",
        "",
        "Euclid–Hoenen–Hilbert–Pappus Concordance",
        "========================================",
        "",
        f".. rubric:: {meta.get('description', '')}",
        "",
        ".. contents:: Concordance Sections",
        "   :local:",
        "   :depth: 2",
        "   :backlinks: none",
        "",
        "Editions Aligned",
        "----------------",
        "",
    ]
    for key, desc in meta.get("editions_aligned", {}).items():
        parts.append(f"* **``{key}``**: {desc}")
    parts.extend(
        [
            "",
            "Edition & Axiom-Numbering Shifts (1899 / 1902 vs. 1930 7th Edition)",
            "-------------------------------------------------------------------",
            "",
            "Because :person:`Fr. Peter Hoenen, S.J. <hoenen>` (:cite:`*De Noetica Geometriae*, 1954 <hoenen:1954>`) cites :person:`Hilbert <hilbert>`'s **7th German edition (1930)** (:cite:`Teubner 1930 <hilbert:1930>`) while :person:`T. L. Heath <heath>` (:cite:`Heath 1908 <heath:1908>`) cites both the 1899 *Festschrift* and early revised editions, the following table reconciles every numbering and terminological shift:",
            "",
            ".. list-table:: 1899 / 1902 vs. 1930 (7th Edition) Structural Concordance",
            "   :header-rows: 1",
            "   :widths: 24 38 38",
            "",
            "   * - Feature / Locus",
            "     - 1899 Teubner (1st ed.) & 1902 Townsend (EN)",
            "     - 1930 Teubner (7th ed., cited by Hoenen 1954)",
        ]
    )
    for shift in meta.get("edition_shifts", []):
        parts.extend(
            [
                f"   * - **{shift['feature']}**",
                f"     - {shift['1899_1902']}",
                f"     - {shift['1930_7ed']}",
            ]
        )

    parts.extend(
        [
            "",
            "Master Cross-Repository Overview",
            "--------------------------------",
            "",
            ".. list-table:: Synopsis of Hilbert's *Grundlagen* Across the GEOMETOR Canon",
            "   :header-rows: 1",
            "   :widths: 16 28 28 28",
            "",
            "   * - Hilbert Locus",
            "     - Euclid (*Elements* & Heath)",
            "     - Hoenen (*De Noetica Geometriae*)",
            "     - Pappus (*Synagoge* VII)",
        ]
    )

    for entry in apparatus.entries:
        sec_str = ", ".join(entry.hilbert_sections)
        euc_short = "; ".join(r["locus"] for r in entry.euclid_refs) or "—"
        hoe_short = "; ".join(r["locus"] for r in entry.hoenen_refs) or "—"
        pap_short = "; ".join(r["locus"] for r in entry.pappus_refs) or "—"
        parts.extend(
            [
                f"   * - :ref:`{sec_str} <concordance-{entry.id}>`",
                f"     - {euc_short}",
                f"     - {hoe_short}",
                f"     - {pap_short}",
            ]
        )

    parts.extend(
        [
            "",
            "Detailed Analytical Concordance",
            "-------------------------------",
            "",
        ]
    )

    for entry in apparatus.entries:
        sec_str = ", ".join(entry.hilbert_sections)
        head = f"{sec_str} ({entry.chapter})"
        parts.extend(
            [
                f".. _concordance-{entry.id}:",
                "",
                head,
                "~" * len(head),
                "",
                f"{entry.summary}",
                "",
            ]
        )

        # Direct links into Hilbert EN & DE section anchors
        sec_refs: list[str] = []
        for slabel in entry.hilbert_sections:
            pair = _section_label_to_anchor(slabel)
            if pair:
                en_a, de_a = pair
                sec_refs.append(
                    f":ref:`{slabel} (EN) <{en_a}>` / :ref:`(DE) <{de_a}>`"
                )
        if sec_refs:
            parts.append(
                "* **Codex Loci**: "
                + " · ".join(sec_refs)
                + f" · :ref:`Unit Notes <grundlagen-{entry.chapter}-notes>`"
            )
        if entry.hilbert_axioms_theorems:
            items_joined = "; ".join(f"``{x}``" for x in entry.hilbert_axioms_theorems)
            parts.append(f"* **Axioms & Theorems**: {items_joined}")

        for ref in entry.euclid_refs:
            link = _format_external_doc_link(ref["repo_path"], ref["locus"])
            folio = f" *(Heath folio {ref['heath_folio']})*" if ref.get("heath_folio") else ""
            parts.append(f"* **Euclid / Elements** — {link}{folio}: {ref['relation']}")
        for ref in entry.hoenen_refs:
            link = _format_external_doc_link(ref["repo_path"], ref["locus"])
            parts.append(f"* **Hoenen (1954)** — {link}: {ref['relation']}")
        for ref in entry.pappus_refs:
            link = _format_external_doc_link(ref["repo_path"], ref["locus"])
            parts.append(f"* **Pappus** — {link}: {ref['relation']}")
        parts.append("")

    return "\n".join(parts)


def _build_bibliography_rst(citations: dict[str, dict[str, Any]]) -> str:
    """Generate `docsrc/grundlagen/bibliography.rst` with exact `.. _cite-<slug>:` anchors."""
    parts: list[str] = [
        ":layout: book",
        "",
        ".. _bibliography:",
        "",
        "Systematic Bibliography",
        "=======================",
        "",
        ".. rubric:: Primary Editions, Classical Treatises & Foundational Commentaries",
        "",
    ]
    sorted_items = sorted(
        citations.items(),
        key=lambda kv: (kv[1].get("author", "").lower(), str(kv[1].get("year", "")), kv[0]),
    )
    for key, item in sorted_items:
        slug = apparatus_slug(key)
        author = item.get("author", "")
        work = item.get("work", "")
        year = item.get("year", "")
        locus = item.get("locus", "")
        publisher = item.get("publisher", "")
        note = item.get("note", "")
        meta_bits = [b for b in (locus, publisher, year) if b]
        meta_str = ", ".join(meta_bits)
        parts.extend(
            [
                f".. _cite-{slug}:",
                "",
                f"**{author}** — *{work}*",
                f"   {meta_str}.",
                "",
            ]
        )
        if note:
            parts.extend([f"   {note}", ""])
    return "\n".join(parts)


def _build_persons_rst(persons: dict[str, dict[str, Any]]) -> str:
    """Generate `docsrc/grundlagen/persons.rst` with exact `.. _person-<slug>:` anchors."""
    parts: list[str] = [
        ":layout: book",
        "",
        ".. _persons:",
        "",
        "Index of Persons",
        "================",
        "",
        ".. rubric:: Prosopographical Registry of Mathematicians & Philosophers",
        "",
    ]
    sorted_items = sorted(persons.items(), key=lambda kv: kv[0])
    for key, item in sorted_items:
        slug = apparatus_slug(key)
        name = item.get("name", key)
        dates = item.get("dates", "")
        role = item.get("role", "")
        bio = item.get("bio", "")
        header = f"**{name}** ({dates})" if dates else f"**{name}**"
        if role:
            header += f" — *{role}*"
        parts.extend(
            [
                f".. _person-{slug}:",
                "",
                header,
                f"   {bio}",
                "",
            ]
        )
    return "\n".join(parts)


def _build_glossary_rst(glossary: dict[str, dict[str, Any]]) -> str:
    """Generate `docsrc/grundlagen/glossary.rst` with exact `.. _term-<slug>:` anchors."""
    parts: list[str] = [
        ":layout: book",
        "",
        ".. _glossary:",
        "",
        "Mathematical & Philosophical Glossary",
        "=====================================",
        "",
        ".. rubric:: Bilingual & Classical Technical Terminology (*Deutsch · English · Greek · Latin*)",
        "",
    ]
    sorted_items = sorted(glossary.items(), key=lambda kv: kv[0])
    for key, item in sorted_items:
        slug = apparatus_slug(key)
        headword = item.get("headword", key)
        lang = item.get("language", "")
        trans = item.get("translation", "")
        defn = item.get("definition", "")
        header = f"**{headword}**"
        if lang or trans:
            qual = " · ".join(x for x in (lang, f"*{trans}*" if trans else "") if x)
            header += f" ({qual})"
        parts.extend(
            [
                f".. _term-{slug}:",
                "",
                header,
                f"   {defn}",
                "",
            ]
        )
    return "\n".join(parts)


def compile_codex(repo_root: Path | None = None) -> dict[str, Any]:
    """Verify archival sources and compile all 41 RST files under `docsrc/grundlagen/`."""
    root = repo_root or default_repo_root()
    verified = verify_sources_manifest(root)
    apparatus = load_apparatus(root)

    # Keep top-level resources/{persons,glossary,citations}.json synchronized
    res_base = root / "resources" / "grundlagen"
    for fname in ("persons.json", "glossary.json", "citations.json"):
        src_json = res_base / fname
        dst_json = root / "resources" / fname
        if src_json.is_file():
            shutil.copyfile(src_json, dst_json)

    tex_path = res_base / "sources" / "gutenberg_17384_townsend_1902.tex"
    txt_path = res_base / "sources" / "ia_grundlagendergeo00hilb_teubner_1899.txt"
    en_units = build_english_units(tex_path)
    de_units = build_german_units(txt_path)

    out_base = root / "docsrc" / "grundlagen"
    out_base.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    def _write(rel_path: str, content: str) -> None:
        target = out_base / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        written.append(target)

    _write("index.rst", _build_grundlagen_index())
    _write("concordance.rst", _build_concordance_rst(apparatus))
    _write("bibliography.rst", _build_bibliography_rst(apparatus.citations))
    _write("persons.rst", _build_persons_rst(apparatus.persons))
    _write("glossary.rst", _build_glossary_rst(apparatus.glossary))

    for unit in UNITS:
        slug = unit["slug"]
        _write(f"{slug}/{slug}-en.rst", en_units[slug])
        _write(f"{slug}/{slug}-de.rst", de_units[slug])
        _write(f"{slug}/{slug}-summary.rst", _build_summary_unit(unit))
        _write(f"{slug}/{slug}-notes.rst", _build_notes_unit(unit, apparatus))

    return {
        "verified_sources": verified,
        "written_count": len(written),
        "output_dir": str(out_base),
    }


def main() -> None:
    """CLI entrypoint for `geometor-hilbert` codex compilation."""
    summary = compile_codex()
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
