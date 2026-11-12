"""Structured loader, query engine, and integrity validator for the Hilbert Codex apparatus."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def apparatus_slug(key: str) -> str:
    """Compute the deterministic anchor slug matching `photon_platform.publish.roles.geometry`."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


@dataclass(frozen=True)
class ConcordanceEntry:
    """Single cross-repository entry in the Euclid–Hoenen–Hilbert–Pappus concordance."""

    id: str
    chapter: str
    hilbert_sections: tuple[str, ...]
    hilbert_axioms_theorems: tuple[str, ...]
    euclid_refs: tuple[dict[str, str], ...]
    hoenen_refs: tuple[dict[str, str], ...]
    pappus_refs: tuple[dict[str, str], ...]
    summary: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> ConcordanceEntry:
        """Construct a `ConcordanceEntry` from a parsed JSON dictionary."""
        return cls(
            id=str(raw["id"]),
            chapter=str(raw["chapter"]),
            hilbert_sections=tuple(raw.get("hilbert_sections", ())),
            hilbert_axioms_theorems=tuple(raw.get("hilbert_axioms_theorems", ())),
            euclid_refs=tuple(raw.get("euclid_refs", ())),
            hoenen_refs=tuple(raw.get("hoenen_refs", ())),
            pappus_refs=tuple(raw.get("pappus_refs", ())),
            summary=str(raw.get("summary", "")),
        )


@dataclass(frozen=True)
class HilbertApparatus:
    """Complete loaded scholarly apparatus for `geometor-hilbert`."""

    concordance_meta: dict[str, Any]
    entries: tuple[ConcordanceEntry, ...]
    persons: dict[str, dict[str, Any]]
    glossary: dict[str, dict[str, Any]]
    citations: dict[str, dict[str, Any]]
    sources_manifest: dict[str, Any]

    def by_chapter(self, chapter_slug: str) -> list[ConcordanceEntry]:
        """Return all concordance entries belonging to `chapter_slug` (e.g. `'chapter-1'`)."""
        return [entry for entry in self.entries if entry.chapter == chapter_slug]

    def by_section(self, section_label: str) -> list[ConcordanceEntry]:
        """Return concordance entries covering `section_label` (e.g. `'§ 14'` or `'14'`)."""
        norm = section_label.strip()
        if norm.isdigit():
            norm = f"§ {norm}"
        return [entry for entry in self.entries if norm in entry.hilbert_sections]

    def search_euclid(self, query: str) -> list[ConcordanceEntry]:
        """Search concordance entries whose Euclid references match `query` case-insensitively."""
        needle = query.lower()
        return [
            e
            for e in self.entries
            if any(
                needle in ref.get("locus", "").lower() or needle in ref.get("relation", "").lower()
                for ref in e.euclid_refs
            )
        ]

    def search_hoenen(self, query: str) -> list[ConcordanceEntry]:
        """Search concordance entries whose Hoenen references match `query` case-insensitively."""
        needle = query.lower()
        return [
            e
            for e in self.entries
            if any(
                needle in ref.get("locus", "").lower() or needle in ref.get("relation", "").lower()
                for ref in e.hoenen_refs
            )
        ]

    def search_pappus(self, query: str = "") -> list[ConcordanceEntry]:
        """Return concordance entries linked to Pappus (optionally filtered by `query`)."""
        needle = query.lower()
        if not needle:
            return [e for e in self.entries if e.pappus_refs]
        return [
            e
            for e in self.entries
            if any(
                needle in ref.get("locus", "").lower() or needle in ref.get("relation", "").lower()
                for ref in e.pappus_refs
            )
        ]


def default_repo_root() -> Path:
    """Resolve the repository root `/home/phi/PROJECTS/geometor/hilbert`."""
    return Path(__file__).resolve().parents[3]


def load_apparatus(repo_root: Path | None = None) -> HilbertApparatus:
    """Load `concordance.json`, `persons.json`, `glossary.json`, `citations.json`, and manifest."""
    root = repo_root or default_repo_root()
    base = root / "resources" / "grundlagen"
    conc_raw = json.loads((base / "concordance.json").read_text(encoding="utf-8"))
    persons = json.loads((base / "persons.json").read_text(encoding="utf-8"))
    glossary = json.loads((base / "glossary.json").read_text(encoding="utf-8"))
    citations = json.loads((base / "citations.json").read_text(encoding="utf-8"))
    manifest = json.loads((base / "sources_manifest.json").read_text(encoding="utf-8"))
    entries = tuple(ConcordanceEntry.from_dict(item) for item in conc_raw.get("entries", []))
    return HilbertApparatus(
        concordance_meta=conc_raw.get("metadata", {}),
        entries=entries,
        persons=persons,
        glossary=glossary,
        citations=citations,
        sources_manifest=manifest,
    )


def verify_sources_manifest(repo_root: Path | None = None) -> list[dict[str, Any]]:
    """Verify SHA-256 digests and byte sizes of all archival primary sources on disk."""
    root = repo_root or default_repo_root()
    manifest_path = root / "resources" / "grundlagen" / "sources_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    results: list[dict[str, Any]] = []
    for src in manifest.get("sources", []):
        fpath = root / src["filename"]
        if not fpath.is_file():
            raise FileNotFoundError(f"Missing primary source file: {fpath}")
        data = fpath.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        size = len(data)
        if digest != src["sha256"]:
            raise ValueError(
                f"SHA-256 mismatch for {src['id']}: expected {src['sha256']}, got {digest}"
            )
        if size != src["bytes"]:
            raise ValueError(
                f"Byte-count mismatch for {src['id']}: expected {src['bytes']}, got {size}"
            )
        results.append({"id": src["id"], "sha256": digest, "bytes": size, "verified": True})
    return results
