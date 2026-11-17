GEOMETOR • hilbert
==================

**Visit the Online Archive:** https://geometor.github.io/hilbert/

.. image:: docsrc/_static/figures/fig_betweenness_pasch.svg
   :alt: GEOMETOR • hilbert featured geometric construction
   :target: https://geometor.github.io/hilbert/
   :align: center

**David Hilbert • Grundlagen der Geometrie • semantic digital archive**

Mission
-------

``geometor/hilbert`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It liberates David Hilbert's landmark 1899 Göttingen *Festschrift* *Grundlagen der Geometrie* and Townsend's 1902 translation from isolated print bounds into addressable semantic units, four synchronized reading tracks, calibrated theme-adaptive vector diagrams, primary-source folio provenance, and metamathematical concordances across the GEOMETOR corpus.

Books in This Archive
---------------------

- `Foundations of Geometry <https://geometor.github.io/hilbert/grundlagen/>`_ — Grundlagen der Geometrie (1899 / 1902) featuring Hilbert's five axiom groups (incidence, order, congruence, parallels, and continuity), calculus of segments, and non-Pascalian geometry.

Python Package & Modules
------------------------

The ``geometor-hilbert`` Python package (``import geometor.hilbert``) provides the executable symbolic geometry, construction, and compilation modules powering this archive:

- ``chapters_meta.py`` — Canonical structural metadata, figure placements, and scholarly Summary/Notes tracks.
- ``compile_codex.py`` — Compile the complete 4-track Book Codex and scholarly apparatus for ``geometor-hilbert``.
- ``concordance.py`` — Structured loader, query engine, and integrity validator for the Hilbert Codex apparatus.
- ``parser_de.py`` — Diplomatic-critical RST parser for David Hilbert's 1899 Teubner Festschrift German edition.
- ``parser_en.py`` — Verbatim LaTeX-to-RST parser for E. J. Townsend's 1902 English edition (Gutenberg #17384).

See the `API Reference <https://geometor.github.io/hilbert/modules/>`_ for full module documentation.

Repository Contents
-------------------

- ``docsrc/`` — Four-track Book Codex, apparatus registries, and Sphinx docs compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Primary source witnesses, SHA-256 manifest, persons/citations registries, and concordance maps.
- ``src/geometor/hilbert/`` — Codex compiler, TeX-to-RST parsers, and apparatus query API.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
