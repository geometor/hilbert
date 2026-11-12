=========
changelog
=========

0.1.0 (2026-11-11)
------------------

* Archive verbatim public-domain primary witnesses in ``resources/grundlagen/sources/`` with SHA-256 verification (``sources_manifest.json``): Hilbert's 1899 B. G. Teubner *Festschrift* German first edition (Internet Archive ``grundlagendergeo00hilb``) and E. J. Townsend's 1902 Open Court English translation (Project Gutenberg ``#17384``).
* Implement ``geometor.hilbert`` Python package (``concordance``, ``chapters_meta``, ``parser_en``, ``parser_de``, ``compile_codex``) targeting Python ``>=3.13``.
* Generate complete 9-unit × 4-track synchronized Book Codex (``English · Deutsch · Summary · Notes``) covering Preface, Epigraph, Introduction, ``§§ 1–39``, all 5 axiom groups, ``Theorems 1–44``, Conclusion, and 1902 Appendix on transformation groups.
* Build 11 calibrated theme-adaptive ``.euclid-graphic`` SVG diagrams via ``scripts/build_figures.py``.
* Curate Master Euclid–Hoenen–Hilbert–Pappus Concordance (``concordance.json`` / ``concordance.rst``), Bibliography (33 works), Index of Persons (47 entries), and Bilingual Mathematical Glossary (34 terms) with offline intersphinx links across ``euclid``, ``elements``, ``hoenen``, and ``pappus``.
