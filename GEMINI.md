# GEMINI.md — `geometor/hilbert`

## Purpose

`geometor/hilbert` (`geometor-hilbert`) is the scholarly bilingual **Book Codex** and metamathematical concordance repository for **David Hilbert's *Grundlagen der Geometrie* (*The Foundations of Geometry*, 1899 / 1902)** within the GEOMETOR ecosystem.

## Architectural Principles

1. **100% Verbatim Primary Sources**:
   * **English Track (`-en.rst`)**: Parsed deterministically by `src/geometor/hilbert/parser_en.py` from Project Gutenberg `#17384` (`resources/grundlagen/sources/gutenberg_17384_townsend_1902.tex`), preserving E. J. Townsend's 1902 Open Court translation, Preface, Kant Epigraph, `§§ 1–39`, `Theorems 1–44`, 1900/1902 Conclusion (with Dehn's theorems), and 1902 Appendix on Lie transformation groups.
   * **German Track (`-de.rst`)**: Parsed deterministically by `src/geometor/hilbert/parser_de.py` from Internet Archive `grundlagendergeo00hilb` (`resources/grundlagen/sources/ia_grundlagendergeo00hilb_teubner_1899.txt`), preserving Hilbert's June 1899 Göttingen *Festschrift* (*editio princeps*, B. G. Teubner) with clearly bracketed philological notes marking 1900–1902 additions. *(Note: Gutenberg `#22062` is John Dee's 1570 *Mathematicall Praeface*, not Hilbert.)*
2. **Synchronized 4-Track Book Codex (`:layout: book`)**:
   * Every unit (`introduction`, `chapter-1`..`chapter-7`, `conclusion`) provides four companion tracks detected automatically by `photon_platform.publish.book`: `-en.rst`, `-de.rst`, `-summary.rst`, and `-notes.rst`.
3. **Standalone Theme-Adaptive SVG Figures**:
   * `scripts/build_figures.py` generates 11 `.euclid-graphic` SVGs in `docsrc/_static/figures/` included via `.. picture::` directives. Never embed Python scripts inside treatise RST tracks.
4. **Cross-Repository Concordance**:
   * `resources/grundlagen/concordance.json` and `src/geometor/hilbert/concordance.py` link Hilbert's sections and theorems directly to `geometor/euclid`, `geometor/elements`, `geometor/hoenen`, and `geometor/pappus` (including reconciliation with the 1930 7th German edition cited by Hoenen).

## Key Workflows

* **Rebuild Figures**: `/home/phi/.local/bin/python3 scripts/build_figures.py`
* **Compile Codex**: `/home/phi/.local/bin/python3 src/geometor/hilbert/compile_codex.py`
* **Lint & Test**: `/home/phi/.local/bin/ruff check src scripts tests` and `/home/phi/.local/bin/pytest`
* **Build Documentation**: `/home/phi/.local/bin/publish build`
