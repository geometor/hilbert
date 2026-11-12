# GEOMETOR • hilbert

Scholarly bilingual **Book Codex** (`English · Deutsch · Summary · Notes`), calibrated SVG geometric diagrams, and cross-repository metamathematical concordance for **David Hilbert's** *Grundlagen der Geometrie* (*The Foundations of Geometry*, 1899 / 1902).

---

## Overview

`geometor-hilbert` brings David Hilbert's foundational June 1899 Göttingen *Festschrift* (*editio princeps*, B. G. Teubner, Leipzig) and E. J. Townsend's authorized 1902 English translation (Open Court, Chicago) into the **GEOMETOR** classical canon alongside:

* **`geometor/euclid`** & **`geometor/elements`**: Euclid's *Elements* and T. L. Heath's commentary on superposition (`C.N. 4`), SAS (`I.4`), right-angle congruence (`Postulate 4` / Hilbert `Theorem 15`), continuity (`I.1`), and polygonal area dissection (`I.35`, `C.N. 5` / Hilbert `Theorem 31`).
* **`geometor/hoenen`**: Fr. Peter Hoenen S.J.'s *De Noetica Geometriae* (1954), analyzing Hilbert's implicit definitions (`§ 1`), *Erklärungen*, collinear order axioms (`II 1–4` & `Theorem 4`), unformalized arithmetic (`§ 9`), and the *Vollständigkeitsaxiom* (`§ 8`).
* **`geometor/pappus`**: Pappus of Alexandria's *Synagoge* Book VII (`Props. 138–139`), directly bridged to Hilbert's affine *"Pascal's Theorem"* (`Theorem 21`, `§ 14`), segment multiplication commutativity (`ab = ba`, `§ 15`), Desarguesian skew-fields (`§§ 22–30`), and the non-Pascalian twisted Laurent skew-field $\Omega(s, t)$ with $ts = 2st$ (`§§ 31–34`).

## Repository Layout

* `resources/grundlagen/sources/`: Verbatim archival primary sources verified by SHA-256 checksums (`sources_manifest.json`).
* `resources/grundlagen/`: Structured JSON registries (`concordance.json`, `citations.json`, `persons.json`, `glossary.json`).
* `src/geometor/hilbert/`:
  * `concordance.py`: Dataclasses, query API (`load_apparatus`, `by_chapter`, `by_section`, `search_euclid`, `search_hoenen`, `search_pappus`), and SHA-256 archival verifier.
  * `chapters_meta.py`: Canonical metadata for all 9 treatise units, 41 section blocks, 11 SVG figure placements, and scholarly `Summary` and `Notes` tracks.
  * `parser_en.py`: Verbatim TeX-to-RST parser for Townsend's 1902 English edition (`Preface`, `Epigraph`, `§§ 1–39`, `Theorems 1–44`, `Conclusion`, and `Appendix`).
  * `parser_de.py`: Verbatim diplomatic-critical parser for Hilbert's 1899 Teubner German *Festschrift*.
  * `compile_codex.py`: Deterministic compiler generating all 41 RST documents in `docsrc/grundlagen/`.
* `scripts/build_figures.py`: Generates 11 theme-adaptive `.euclid-graphic` SVG figures in `docsrc/_static/figures/`.
* `docsrc/`: Sphinx Book Codex source published via `photon-platform/publish`.
* `tests/`: Automated integrity, concordance, SVG, parser, and role-resolution test suite.

## Development & Build Commands

```bash
# Regenerate calibrated SVG figures
python3 scripts/build_figures.py

# Recompile the 4-track Book Codex RST tree from primary sources
python3 src/geometor/hilbert/compile_codex.py

# Run linting and test suite
ruff check src scripts tests
pytest

# Build the HTML Book Codex into docs/
publish build
```
