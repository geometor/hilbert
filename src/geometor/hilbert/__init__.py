"""GEOMETOR • hilbert — Bilingual Book Codex of David Hilbert's *Grundlagen der Geometrie* (1899 / 1902).

Provides structured concordance queries, primary-source verification utilities, and
deterministic compilation of the synchronized four-track Book Codex (`English`,
`Deutsch`, `Summary`, `Notes`) across Euclid, Hoenen, Hilbert, and Pappus.
"""

from __future__ import annotations

from geometor.hilbert.concordance import (
    ConcordanceEntry,
    HilbertApparatus,
    apparatus_slug,
    load_apparatus,
    verify_sources_manifest,
)

__version__ = "0.1.1"

__all__ = [
    "ConcordanceEntry",
    "HilbertApparatus",
    "__version__",
    "apparatus_slug",
    "load_apparatus",
    "verify_sources_manifest",
]
