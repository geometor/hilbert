:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive Four-Track Codex & Axiomatic Geometry Engine

The GEOMETOR edition of David Hilbert's :cite:`*Grundlagen der Geometrie* <hilbert:1899>` integrates philological fidelity to the 1899 Göttingen *Festschrift* and 1902 authorized English translation with synchronized reading tracks and exact axiomatic foundations.

Interactive Codex Features
--------------------------

1. Synchronized Reading Tracks
   Every unit across the nine chapters and appendices provides four synchronized parallel tracks selectable directly from the reading header:
   
   * **English (1902):** Authorized English translation by :person:`Edgar Jerome Townsend <townsend>` (Open Court, 1902), incorporating Hilbert's additions and appendix.
   * **Deutsch (1899):** Verbatim German text from the 1899 Göttingen *Festschrift* (*editio princeps*, B. G. Teubner).
   * **Summary:** Chapter summaries, axiom classifications, and deductive outlines.
   * **Notes:** Scholarly commentary on non-Archimedean fields, model theory, Hoenen's epistemological critique, and 7th-edition (1930) shifts.

2. Primary-Source Folio Milestones
   Marginal page markers (such as ``[p. 1]``, ``[p. 20]``, ``[p. 50]``) link directly to high-resolution archival scans of the 1899 Teubner printing at Internet Archive. Clicking header **Folio** badges opens the corresponding primary witness.

3. Interactive Diagrams & Deductive Links
   All eleven geometric figures are rendered as scalable, theme-adaptive ``.euclid-graphic`` SVGs:
   
   * Pasch's axiom, Desargues's 10-point configuration, and segment arithmetic (:math:`a+b`, :math:`a \cdot b`) adapt dynamically to light and dark reader modes.
   * Axiomatic terms link into the technical glossary (:term:`Streckenrechnung <streckenrechnung>`, :term:`Anordnung <anordnung>`, :term:`Vollständigkeit <vollstaendigkeit>`).
   * Citations connect directly to classical authorities like :cite:`Euclid's *Elements* <euclid:elements>`, :cite:`Kant's *Kritik* <kant:1781>`, and :cite:`Hoenen's *De Noetica* <hoenen:1954>`.

4. Full-Text Search with In-Page Highlighting
   Use the sidebar search bar to query the complete German and English texts and critical notes. Clicking any result automatically opens the section with the search term highlighted in context.

5. Faceted Navigation & Collection Views
   Browse mathematical units, topics, and historical figures via the sidebar taxonomy. Collection pages provide **Cards**, **Banners**, and **List** layout switches.

6. People, Bibliography & Glossary Tooltips
   Hovering over any historical person (:person:`David Hilbert <hilbert>`, :person:`Edgar Jerome Townsend <townsend>`, :person:`Immanuel Kant <kant>`, :person:`Moritz Pasch <pasch>`), citation (:cite:`hilbert:1899`, :cite:`hilbert:1902:en`), or term (:term:`Streckenrechnung <streckenrechnung>`, :term:`Eichmass <eichmass>`) surfaces rich tooltip cards.

----

Command-Line & Python Verification API
--------------------------------------

All figures, concordance queries, and archival checksums are executable locally via Python.

Building Calibrated Figures
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Regenerate and verify the eleven theme-adaptive ``.euclid-graphic`` SVGs:

.. code-block:: bash

   python3 scripts/build_figures.py

Python API Usage
~~~~~~~~~~~~~~~~

Import the apparatus loader and concordance query engine directly in Python:

.. code-block:: python

   from geometor.hilbert import load_apparatus, verify_sources_manifest

   # Verify archival source checksums
   results = verify_sources_manifest()
   assert all(r["verified"] for r in results)

   # Query the Euclid-Hoenen-Hilbert-Pappus concordance
   app = load_apparatus()
   sec14_matches = app.by_section("14")
   for match in sec14_matches:
       print(f"Section {match.hilbert_sections}: {match.summary}")
