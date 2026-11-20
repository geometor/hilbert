<a href="https://geometor.github.io/hilbert/"><img src="docsrc/_static/logo.png" alt="GEOMETOR • hilbert Medallion" align="right" width="150"></a>

# GEOMETOR • hilbert

**Visit the Online Archive:** https://geometor.github.io/hilbert/

<p align="center">
  <a href="https://geometor.github.io/hilbert/"><img src="docsrc/_static/figures/fig_betweenness_pasch.svg" alt="GEOMETOR • hilbert featured geometric construction"></a>
</p>

**David Hilbert • Grundlagen der Geometrie • semantic digital archive**

## Mission

`geometor/hilbert` is part of the interconnected [GEOMETOR](https://geometor.com) semantic digital archive. It liberates David Hilbert's landmark 1899 Göttingen *Festschrift* *Grundlagen der Geometrie* and Townsend's 1902 translation from isolated print bounds into addressable semantic units, four synchronized reading tracks, calibrated theme-adaptive vector diagrams, primary-source folio provenance, and metamathematical concordances across the GEOMETOR corpus.

## Books in This Archive

- [Foundations of Geometry](https://geometor.github.io/hilbert/grundlagen/) — Grundlagen der Geometrie (1899 / 1902) featuring Hilbert's five axiom groups (incidence, order, congruence, parallels, and continuity), calculus of segments, and non-Pascalian geometry.

## Repository Contents

- `docsrc/` — Four-track Book Codex, apparatus registries, and Sphinx docs compiled by [PHOTON publish](https://github.com/photon-platform/publish).
- `resources/` — Primary source witnesses, SHA-256 manifest, persons/citations registries, and concordance maps.
- `src/geometor/hilbert/` — Codex compiler, TeX-to-RST parsers, and apparatus query API.

## Local Build & Verification

```bash
publish build
uv run --no-sync pytest
```
## Part of the GEOMETOR Knowledge Archive

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
