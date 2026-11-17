:layout: book
:canonical_id: § 6 (Notes)
:breadcrumb_title: Notes
:order: 6
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-notes-s6:

§ 6: Group IV: Axioms of Congruence — Notes
===========================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Hoenen on § 1 (*"Wir denken drei verschiedene Systeme..."*) and *Erklärungen*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter I contains the three loci most intensively analyzed in ``geometor/hoenen`` (:cite:`Hoenen 1954 <hoenen:1954>`):

* **Unformalized Arithmetic in § 1 (`Caput I § 6, fn. 14`)**: :person:`Hoenen <hoenen>` quotes § 1's opening sentence verbatim in German (*„Wir denken drei verschiedene Systeme von Dingen...“*) to point out a foundational asymmetry: while *point*, *straight line*, and *plane* are treated as uninterpreted symbols, **cardinal and ordinal numbers** (*"three distinct systems"*, *"two points"*, *"at least four points"*, *"finite number $A_1, \ldots, A_n$"*) are employed throughout Chapter I in their full intuitive arithmetic meaning.
* **Covert Existential Judgments in *Erklärungen* (`Caput IV, Prelim., fn. 1`)**: Notice how the 1899 German text prefixes §§ 1, 3, 4, 6, 7 with bold **Erklärung** (*Explanation*) and **Definition** headings (often merged or unmarked in Townsend's English). :person:`Hoenen <hoenen>` argues that these *Erklärungen* smuggle in virtual judgments of possibility and spatial structure abstracted from :term:`materia intelligibilis <materia-intelligibilis>`.
* **Linear Order (`II 1–4`), E. H. Moore (1902), and G. H. Hardy (`Caput V § 3.2.A–B, fns. 8–9`)**:
  - **Edition Numbering Shift (1899 vs. 1930 7th ed.)**: In the 1899 *Festschrift* and 1902 English text, Group II has **five** axioms (`II 1–5`), where `II 4` asserts that any four collinear points can be labeled $A, B, C, D$ with $B$ between $A, C$ and $A, D$, and $C$ between $A, D$ and $B, D$; `Theorem 4` then orders any $n$ collinear points $A, B, C, D, E, \ldots, K$. In January 1902 (:cite:`Moore 1902 <moore:1902>`, cited in Townsend's § 3 footnote!), :person:`E. H. Moore <moore>` proved that `II 4` is **redundant**—deducible from planar incidence `I 1–2` and :person:`Pasch <pasch>`'s Axiom `II 5`! Consequently, in later editions (including the 1930 7th ed. cited by :person:`Hoenen <hoenen>`), `II 4` was demoted to *Satz 5*, shifting 1899 `Satz 4` to *Satz 6*!
  - **Typographic Spatial Intuition**: :person:`Hoenen <hoenen>` scrutinizes `Theorem 4` (*Satz 6* in 7th ed.) and Hilbert's terms :term:`einerseits / andererseits <einerseits-andererseits>` (*"on the one hand / on the other hand"*) and *umgekehrt* (*"reverse order"* $K, \ldots, E, D, C, B, A$): to understand what *"reverse sequence"* means for $n$ points, the reader must rely on the **left-to-right visual spatial order** of the printed letters on the page! :person:`Hoenen <hoenen>` crowns this critique by quoting :person:`G. H. Hardy <hardy>` (:cite:`*Mind* 1929, p. 15 <hardy:1929>`): *"If Hilbert's axioms are to mean anything to us, we must draw figures."*

2. Euclid & Heath on §§ 6–7: Superposition, SAS (`I.4`), and Postulate 4 (`Theorem 15`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter I's congruence theory (`§§ 6–7`) is the direct centerpiece of :person:`T. L. Heath <heath>`'s commentary in ``geometor/euclid`` (:cite:`Heath 1908 <heath:1908>`):

* **Eliminating Superposition (`Common Notion 4`, Vol. I, pp. 228–230, folios `0242–0244`; `I.4`, pp. 249–250, folios `0263–0264`)**: Where :person:`Euclid <euclid>` proves `I.4` (SAS) by "applying" (:term:`ἐφαρμόζειν <epharmozein>`) $\triangle ABC$ onto $\triangle DEF$—a move criticized by Peletier, Schopenhauer, and :person:`Bertrand Russell <russell>` (:cite:`Russell 1903, p. 405 <russell:1903>`) as assuming rigid motion without axiom—:person:`Hilbert <hilbert>` posits `Axiom IV 6` (transferring base angles from two sides and included angle) and proves full SAS (`Theorem 10`) by an elegant *reductio ad absurdum* using uniqueness of angle transfer (`IV 4`). :person:`Heath <heath>` reproduces both `Theorem 10` (`0243.g1`) and `Theorem 12` on supplementary angles (`0244.g1`) verbatim!
* **Proving Euclid's Fourth Postulate (`Theorem 15`, Heath Vol. I, p. 200)**: In § 7 (`Satz 15`), :person:`Hilbert <hilbert>` remarks explicitly that :person:`Euclid <euclid>` *"erroneously, in my opinion, placed among the axioms"* the theorem that **all right angles are congruent** (`Postulate 4`), and proves it purely from supplementary angles (`Theorem 12`) and interior ray transfer (`Theorem 13`)!
* **Axiom Group Swap in Later Editions**: Keep in mind when consulting 20th-century commentaries that in 1899/1902 **Group III = Parallels** (§ 5) and **Group IV = Congruence** (§ 6), whereas from the 2nd/7th editions onward Hilbert swapped them so **Group III = Congruence** and **Group IV = Parallels** (matching absolute geometry's independence from parallels).

3. The Axiom of Completeness (*Vollständigkeit*, § 8 Remark & Hoenen Caput V fn. 10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Absent from the June 1899 German *Festschrift*, the :term:`Axiom of Completeness <vollstaendigkeit>` was added by :person:`Hilbert <hilbert>` in his 1900 paper :cite:`*Über den Zahlbegriff* <hilbert:1900:zahlbegriff>` and the 1900 French edition (:cite:`Laugel 1900 <hilbert:1900:french>`), appearing in :person:`Townsend <townsend>`'s 1902 English text at the close of § 8. As :person:`Heath <heath>` notes on `Euclid I.1` (Vol. I, p. 242, folio `0256`), without Continuity circles need not intersect over arbitrary rational subfields (though Chapter VII shows they *do* intersect over Hilbert's Pythagorean field $\Omega$!). And as :person:`Hoenen <hoenen>` emphasizes (`Caput V § 5, fn. 10`), *Vollständigkeit* is openly **second-order and metamathematical**, quantifying over all possible extensions preserving the preceding axioms.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 6, § 7** (:ref:`concordance-sec-06-07-congruence`): Replaces Euclidean superposition and rigid motion by six axioms of segment and angle congruence (IV 1–6), proving SAS (Theorem 10), ASA (Theorem 11), supplementary angles (Theorem 12), Euclid's Postulate 4 on right angles (Theorem 15), SSS (Theorem 16), and the 180° triangle angle sum (Theorem 20).
  - :external+euclid:doc:`Euclid — C.N. 1–4 (esp. C.N. 4 superposition) <heath/volume_I/book_i/common_notions/commentary>`: Heath (Vol. I, pp. 228–230) reproduces Hilbert's § 6–7 congruence axioms and proofs in detail (including diagram 0243.g1 for SAS and 0244.g1 for supplementary angles) to show how Hilbert eliminates Euclid's physical superposition (ἐφαρμόζειν).
  - :external+euclid:doc:`Euclid — I.4 (SAS Triangle Congruence) <heath/volume_I/book_i/propositions/04/commentary>`: Heath (Vol. I, pp. 249–250) cites Russell and Hilbert (p. 9) on why SAS cannot be proved without assuming rigid motion unless Axiom IV 6 posits base-angle transfer from two sides and the included angle, from which full SAS (Theorem 10) follows by reductio ad absurdum.
  - :external+euclid:doc:`Euclid — Post. 4 ('All right angles are equal') <heath/volume_I/book_i/postulates/commentary>`: Heath (Vol. I, p. 200) explicitly notes that Hilbert deduces Euclid's Fourth Postulate as Theorem 15 from the Congruence Axioms via supplementary angles (Theorem 12).
  - :external+euclid:doc:`Euclid — I.2–3, I.5, I.8, I.13, I.15, I.23, I.26, I.27, I.32 <heath/volume_I/book_i/propositions/05/index>`: Direct deductive counterparts: I.2–3 <-> IV 1; I.26 <-> Theorem 11; I.13 <-> Theorem 12; I.5 <-> Isosceles corollary; I.8 <-> Theorem 16; I.23 <-> IV 4; I.27–29 <-> Theorem 19; I.32 <-> Theorem 20.
  - :external+hoenen:doc:`Hoenen — Caput IV § 3; Caput V § 2 <de_noetica_geometriae/caput-4/caput-4-en>`: Discusses congruence, rigid displacement vs. static relational axioms, and the geometric intelligibility of equality of segments and angles.
