:layout: book
:canonical_id: § 1 (Notes)
:breadcrumb_title: Notes
:order: 1
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-notes-s1:

§ 1: The Elements of Geometry and the Five Groups of Axioms — Notes
===================================================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Hoenen on § 1 (*"Wir denken drei verschiedene Systeme..."*) and *Erklärungen*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter I contains the three loci most intensively analyzed in ``geometor/hoenen`` (:cite:`Hoenen 1954 <hoenen:1954>`):

* **Unformalized Arithmetic in § 1 (`Caput I § 6, fn. 14`)**: :person:`Hoenen <hoenen>` quotes § 1's opening sentence verbatim in German (*„Wir denken drei verschiedene Systeme von Dingen...“*) to point out a foundational asymmetry: while *point*, *straight line*, and *plane* are treated as uninterpreted symbols, **cardinal and ordinal numbers** (*"three distinct systems"*, *"two points"*, *"at least four points"*, "*finite number* :math:`A_1, \ldots, A_n`") are employed throughout Chapter I in their full intuitive arithmetic meaning.
* **Covert Existential Judgments in** *Erklärungen* (`Caput IV, Prelim., fn. 1`): Notice how the 1899 German text prefixes §§ 1, 3, 4, 6, 7 with bold **Erklärung** (*Explanation*) and **Definition** headings (often merged or unmarked in Townsend's English). :person:`Hoenen <hoenen>` argues that these *Erklärungen* smuggle in virtual judgments of possibility and spatial structure abstracted from :term:`materia intelligibilis <materia-intelligibilis>`.
* **Linear Order (`II 1–4`), E. H. Moore (1902), and G. H. Hardy (`Caput V § 3.2.A–B, fns. 8–9`)**:
  - **Edition Numbering Shift (1899 vs. 1930 7th ed.)**: In the 1899 *Festschrift* and 1902 English text, Group II has **five** axioms (`II 1–5`), where `II 4` asserts that any four collinear points can be labeled :math:`A, B, C, D` with :math:`B` between :math:`A, C` and :math:`A, D`, and :math:`C` between :math:`A, D` and :math:`B, D`; `Theorem 4` then orders any :math:`n` collinear points :math:`A, B, C, D, E, \ldots, K`. In January 1902 (:cite:`Moore 1902 <moore:1902>`, cited in Townsend's § 3 footnote!), :person:`E. H. Moore <moore>` proved that `II 4` is **redundant**—deducible from planar incidence `I 1–2` and :person:`Pasch <pasch>`'s Axiom `II 5`! Consequently, in later editions (including the 1930 7th ed. cited by :person:`Hoenen <hoenen>`), `II 4` was demoted to *Satz 5*, shifting 1899 `Satz 4` to *Satz 6*!
  - **Typographic Spatial Intuition**: :person:`Hoenen <hoenen>` scrutinizes `Theorem 4` (*Satz 6* in 7th ed.) and Hilbert's terms :term:`einerseits / andererseits <einerseits-andererseits>` (*"on the one hand / on the other hand"*) and *umgekehrt* (*"reverse order"* :math:`K, \ldots, E, D, C, B, A`): to understand what *"reverse sequence"* means for :math:`n` points, the reader must rely on the **left-to-right visual spatial order** of the printed letters on the page! :person:`Hoenen <hoenen>` crowns this critique by quoting :person:`G. H. Hardy <hardy>` (:cite:`*Mind* 1929, p. 15 <hardy:1929>`): *"If Hilbert's axioms are to mean anything to us, we must draw figures."*

2. Euclid & Heath on §§ 6–7: Superposition, SAS (`I.4`), and Postulate 4 (`Theorem 15`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter I's congruence theory (`§§ 6–7`) is the direct centerpiece of :person:`T. L. Heath <heath>`'s commentary in ``geometor/euclid`` (:cite:`Heath 1908 <heath:1908>`):

* **Eliminating Superposition (`Common Notion 4`, Vol. I, pp. 228–230, folios `0242–0244`; `I.4`, pp. 249–250, folios `0263–0264`)**: Where :person:`Euclid <euclid>` proves `I.4` (SAS) by "applying" (:term:`ἐφαρμόζειν <epharmozein>`) :math:`\triangle ABC` onto :math:`\triangle DEF`—a move criticized by Peletier, Schopenhauer, and :person:`Bertrand Russell <russell>` (:cite:`Russell 1903, p. 405 <russell:1903>`) as assuming rigid motion without axiom—:person:`Hilbert <hilbert>` posits `Axiom IV 6` (transferring base angles from two sides and included angle) and proves full SAS (`Theorem 10`) by an elegant *reductio ad absurdum* using uniqueness of angle transfer (`IV 4`). :person:`Heath <heath>` reproduces both `Theorem 10` (`0243.g1`) and `Theorem 12` on supplementary angles (`0244.g1`) verbatim!
* **Proving Euclid's Fourth Postulate (`Theorem 15`, Heath Vol. I, p. 200)**: In § 7 (`Satz 15`), :person:`Hilbert <hilbert>` remarks explicitly that :person:`Euclid <euclid>` *"erroneously, in my opinion, placed among the axioms"* the theorem that **all right angles are congruent** (`Postulate 4`), and proves it purely from supplementary angles (`Theorem 12`) and interior ray transfer (`Theorem 13`)!
* **Axiom Group Swap in Later Editions**: Keep in mind when consulting 20th-century commentaries that in 1899/1902 **Group III = Parallels** (§ 5) and **Group IV = Congruence** (§ 6), whereas from the 2nd/7th editions onward Hilbert swapped them so **Group III = Congruence** and **Group IV = Parallels** (matching absolute geometry's independence from parallels).

3. The Axiom of Completeness (*Vollständigkeit*, § 8 Remark & Hoenen Caput V fn. 10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Absent from the June 1899 German *Festschrift*, the :term:`Axiom of Completeness <vollstaendigkeit>` was added by :person:`Hilbert <hilbert>` in his 1900 paper :cite:`*Über den Zahlbegriff* <hilbert:1900:zahlbegriff>` and the 1900 French edition (:cite:`Laugel 1900 <hilbert:1900:french>`), appearing in :person:`Townsend <townsend>`'s 1902 English text at the close of § 8. As :person:`Heath <heath>` notes on `Euclid I.1` (Vol. I, p. 242, folio `0256`), without Continuity circles need not intersect over arbitrary rational subfields (though Chapter VII shows they *do* intersect over Hilbert's Pythagorean field :math:`\Omega`!). And as :person:`Hoenen <hoenen>` emphasizes (`Caput V § 5, fn. 10`), *Vollständigkeit* is openly **second-order and metamathematical**, quantifying over all possible extensions preserving the preceding axioms.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 1** (:ref:`concordance-sec-01-primitives`): Eliminates explicit definitions of primitive geometric objects in favor of implicit relational characterization across five axiom groups: Connection, Order, Parallels, Congruence, and Continuity.
  - :external+euclid:doc:`Euclid — I.Def.1, I.Def.2, I.Def.4, I.Def.7 <heath/volume_I/book_i/definitions/commentary>`: Replaces Euclid's descriptive definitions ('A point is that which has no part', 'A straight line lies evenly with the points on itself') by three unspecified systems of things bound solely by relational axioms.
  - :external+hoenen:doc:`Hoenen — Caput I § 6 & fn. 14 <de_noetica_geometriae/caput-1/caput-1-en>`: Quotes Hilbert's opening sentence verbatim in German ('Wir denken drei verschiedene Systeme von Dingen...') and highlights that Hilbert leaves numbers ('two points', 'three planes', real coordinates) unformalized in their intuitive sense.
  - :external+hoenen:doc:`Hoenen — Caput IV, Preliminaries & fn. 1 <de_noetica_geometriae/caput-4/caput-4-en>`: Analyzes Hilbert's recurring heading 'Erklärung' ('Definition/Explanation') as concealing existential and intuitive judgments abstracted from spatial extension (materia intelligibilis).
