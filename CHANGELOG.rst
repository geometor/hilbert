=========
changelog
=========

0.1.5 (2026-11-15)
------------------

- Rebuilt codex documentation with ``photon-platform/publish`` ``v0.4.6`` so every inline ``.euclid-graphic`` SVG carries explicit ``viewBox`` pixel dimensions, per-diagram scoped ``<style>`` rules, and Nocturnal Codex dark/light theme parity.

0.1.4 (2026-11-15)
------------------

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.3 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2 (2026-11-14)
------------------

- Standardized Book Title Page, top-level header navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author and Translator profiles in People, and English structural terminology.

0.1.1 (2026-11-13)
------------------

* Resolve 100% of marginal ``.. folio::`` source links (83 directives) to primary witness line anchors in ``ia_grundlagendergeo00hilb_teubner_1899.txt`` via ``publish folio-links``.

0.1.0 (2026-11-11)
------------------

* Archive verbatim public-domain primary witnesses in ``resources/grundlagen/sources/`` with SHA-256 verification (``sources_manifest.json``): Hilbert's 1899 B. G. Teubner *Festschrift* German first edition (Internet Archive ``grundlagendergeo00hilb``) and E. J. Townsend's 1902 Open Court English translation (Project Gutenberg ``#17384``).
* Implement ``geometor.hilbert`` Python package (``concordance``, ``chapters_meta``, ``parser_en``, ``parser_de``, ``compile_codex``) targeting Python ``>=3.13``.
* Generate complete 9-unit × 4-track synchronized Book Codex (``English · Deutsch · Summary · Notes``) covering Preface, Epigraph, Introduction, ``§§ 1–39``, all 5 axiom groups, ``Theorems 1–44``, Conclusion, and 1902 Appendix on transformation groups.
* Build 11 calibrated theme-adaptive ``.euclid-graphic`` SVG diagrams via ``scripts/build_figures.py``.
* Curate Master Euclid–Hoenen–Hilbert–Pappus Concordance (``concordance.json`` / ``concordance.rst``), Bibliography (33 works), Index of Persons (47 entries), and Bilingual Mathematical Glossary (34 terms) with offline intersphinx links across ``euclid``, ``elements``, ``hoenen``, and ``pappus``.
