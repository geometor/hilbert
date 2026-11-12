:layout: book

.. _grundlagen-chapter-1-notes:

Chapter I: The Five Groups of Axioms — Notes
============================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

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

* **§ 1** (:ref:`concordance-sec-01-primitives`): Eliminates explicit definitions of primitive geometric objects in favor of implicit relational characterization across five axiom groups: Connection, Order, Parallels, Congruence, and Continuity.
  - :external+euclid:doc:`Euclid — I.Def.1, I.Def.2, I.Def.4, I.Def.7 <heath/volume_I/book_i/definitions/commentary>`: Replaces Euclid's descriptive definitions ('A point is that which has no part', 'A straight line lies evenly with the points on itself') by three unspecified systems of things bound solely by relational axioms.
  - :external+hoenen:doc:`Hoenen — Caput I § 6 & fn. 14 <de_noetica_geometriae/caput-1/caput-1-en>`: Quotes Hilbert's opening sentence verbatim in German ('Wir denken drei verschiedene Systeme von Dingen...') and highlights that Hilbert leaves numbers ('two points', 'three planes', real coordinates) unformalized in their intuitive sense.
  - :external+hoenen:doc:`Hoenen — Caput IV, Preliminaries & fn. 1 <de_noetica_geometriae/caput-4/caput-4-en>`: Analyzes Hilbert's recurring heading 'Erklärung' ('Definition/Explanation') as concealing existential and intuitive judgments abstracted from spatial extension (materia intelligibilis).

* **§ 2** (:ref:`concordance-sec-02-connection`): Establishes the planar (I 1–2) and spatial (I 3–7) incidence axioms and proves intersection uniqueness and existence of non-collinear triples (Theorems 1–2).
  - :external+euclid:doc:`Euclid — Post. 1, Post. 2, C.N. 9, XI.1–3 <heath/volume_I/book_i/postulates/index>`: Formalizes both existence (I 1: Postulate 1) and uniqueness (I 2: Common Notion 9, two lines do not enclose a space) of the straight line through two points, together with planar and 3D incidence (XI.1–3) and dimensional lower bounds (I 6–7).
  - :external+hoenen:doc:`Hoenen — Caput IV § 1–2 <de_noetica_geometriae/caput-4/caput-4-en>`: Investigates how the unique determination of a straight line by two points is grasped by intuitive formal abstraction prior to axiomatic postulation.
  - :external+pappus:doc:`Pappus — Projective Incidence Foundation <index>`: Planar incidence I 1–2 and spatial plane-intersection I 3–6 provide the projective incidence skeleton upon which spatial Desargues (§ 22) rests.

* **§ 3, § 4** (:ref:`concordance-sec-03-04-order`): Formalizes ternary collinear betweenness (II 1–4) and Pasch's planar separation axiom (II 5), deriving segment density, total linear ordering of finite point-sets, half-planes, rays, Jordan polygon separation, and spatial plane separation (Theorems 3–7).
  - :external+euclid:doc:`Euclid — I.1, I.10, I.16 (tacit betweenness & planar separation) <heath/volume_I/book_i/propositions/01/commentary>`: Supplies the entire linear betweenness and planar side-separation apparatus (Pasch's Axiom II 5) absent from Euclid's explicit postulates, blocking fallacies like the 'all triangles are isosceles' sophism.
  - :external+hoenen:doc:`Hoenen — Caput V § 3.2.A–B & fns. 8–9 <de_noetica_geometriae/caput-5/caput-5-en>`: Hoenen's centerpiece critique of pure formalism: examines II 1–4 and Theorem 4 (7th ed. Satz 5 & Satz 6: ordering n collinear points 'A, B, C, D, E, ..., K'), notes E. H. Moore's 1902 proof that II 4 is redundant, exposes Hilbert's tacit reliance on the visual left-to-right spatial order of typographic symbols and terms like 'einerseits / andererseits' and 'umgekehrt', and endorses G. H. Hardy's 1929 Mind verdict: 'If Hilbert's axioms are to mean anything to us, we must draw figures.'

* **§ 5** (:ref:`concordance-sec-05-parallels`): States the Euclidean Axiom of Parallels (Group III in 1899/1902; Group IV in later editions) and derives parallel transitivity (Theorem 8), preparing § 7's alternate-angle and 180° triangle angle-sum theorems.
  - :external+euclid:doc:`Euclid — Post. 5; I.27–32 <heath/volume_I/book_i/postulates/commentary>`: Adopts Playfair's uniqueness formulation in a given plane (at most one non-intersecting line through A to a), while existence of at least one parallel follows from exterior/alternate angle congruence (§ 7 / § 10, Euclid I.27).
  - :external+hoenen:doc:`Hoenen — Caput II § 4; Caput VI <de_noetica_geometriae/caput-2/caput-2-en>`: Evaluates the epistemological status of Euclidean vs. Lobachevskian/Riemannian parallel postulates with respect to intelligible extension.
  - :external+pappus:doc:`Pappus — Affine specialization of line at infinity <theorems/index>`: Axiom III enables Hilbert's affine formulations of Pascal's (Pappus's) Theorem (§ 14, § 31) and Desargues's Theorem (§ 22), where intersections on the line at infinity become parallel lines.

* **§ 6, § 7** (:ref:`concordance-sec-06-07-congruence`): Replaces Euclidean superposition and rigid motion by six axioms of segment and angle congruence (IV 1–6), proving SAS (Theorem 10), ASA (Theorem 11), supplementary angles (Theorem 12), Euclid's Postulate 4 on right angles (Theorem 15), SSS (Theorem 16), and the 180° triangle angle sum (Theorem 20).
  - :external+euclid:doc:`Euclid — C.N. 1–4 (esp. C.N. 4 superposition) <heath/volume_I/book_i/common_notions/commentary>`: Heath (Vol. I, pp. 228–230) reproduces Hilbert's § 6–7 congruence axioms and proofs in detail (including diagram 0243.g1 for SAS and 0244.g1 for supplementary angles) to show how Hilbert eliminates Euclid's physical superposition (ἐφαρμόζειν).
  - :external+euclid:doc:`Euclid — I.4 (SAS Triangle Congruence) <heath/volume_I/book_i/propositions/04/commentary>`: Heath (Vol. I, pp. 249–250) cites Russell and Hilbert (p. 9) on why SAS cannot be proved without assuming rigid motion unless Axiom IV 6 posits base-angle transfer from two sides and the included angle, from which full SAS (Theorem 10) follows by reductio ad absurdum.
  - :external+euclid:doc:`Euclid — Post. 4 ('All right angles are equal') <heath/volume_I/book_i/postulates/commentary>`: Heath (Vol. I, p. 200) explicitly notes that Hilbert deduces Euclid's Fourth Postulate as Theorem 15 from the Congruence Axioms via supplementary angles (Theorem 12).
  - :external+euclid:doc:`Euclid — I.2–3, I.5, I.8, I.13, I.15, I.23, I.26, I.27, I.32 <heath/volume_I/book_i/propositions/05/index>`: Direct deductive counterparts: I.2–3 <-> IV 1; I.26 <-> Theorem 11; I.13 <-> Theorem 12; I.5 <-> Isosceles corollary; I.8 <-> Theorem 16; I.23 <-> IV 4; I.27–29 <-> Theorem 19; I.32 <-> Theorem 20.
  - :external+hoenen:doc:`Hoenen — Caput IV § 3; Caput V § 2 <de_noetica_geometriae/caput-4/caput-4-en>`: Discusses congruence, rigid displacement vs. static relational axioms, and the geometric intelligibility of equality of segments and angles.

* **§ 8** (:ref:`concordance-sec-08-continuity`): Introduces the Axiom of Archimedes (Group V) and—in the 1900/1902 Remark—the categorical Axiom of Completeness fixing the Cartesian real continuum.
  - :external+euclid:doc:`Euclid — V.Def.4; X.1; I.1 & I.22 <heath/volume_I/book_i/propositions/01/commentary>`: Formalizes the Eudoxus–Archimedes exhaustion principle (V.Def.4, X.1); Heath (Vol. I, p. 242 on I.1) notes that Dedekind/Hilbert Continuity is required to guarantee circle-circle and line-circle intersections, though Chapter VII (§§ 36–39) proves Euclidean ruler-and-compass intersections already exist over Hilbert's Pythagorean field Ω without full Continuity.
  - :external+hoenen:doc:`Hoenen — Caput V § 3.2 & § 5, fn. 10 <de_noetica_geometriae/caput-5/caput-5-en>`: Examines Hilbert's Axiom of Completeness (Vollständigkeitsaxiom, added 1900/1903) as a metamathematical maximality postulate over all preceding axioms, demonstrating its dependence on intuitive arithmetic and set-theoretic concepts.
