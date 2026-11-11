:layout: book

.. _concordance:

Euclid–Hoenen–Hilbert–Pappus Concordance
========================================

.. rubric:: Structured cross-repository concordance mapping David Hilbert's Grundlagen der Geometrie (1899 / 1902) across Euclid's Elements (Heath 1908 & GEOMETOR elements), Petrus Hoenen's De Noetica Geometriae (1954), and Pappus of Alexandria's Synagoge Book VII.

.. contents:: Concordance Sections
   :local:
   :depth: 2
   :backlinks: none

Editions Aligned
----------------

* **``teubner_1899``**: Festschrift zur Feier der Enthüllung des Gauss-Weber-Denkmals in Göttingen, Erster Theil: Grundlagen der Geometrie (Leipzig: B. G. Teubner, 1899)
* **``townsend_1902``**: The Foundations of Geometry, trans. E. J. Townsend (Chicago: Open Court, 1902; Project Gutenberg #17384)
* **``teubner_1930_7ed``**: Grundlagen der Geometrie, 7. Auflage (Leipzig: B. G. Teubner, 1930) — edition cited by P. Hoenen, S.J. (1954)

Edition & Axiom-Numbering Shifts (1899 / 1902 vs. 1930 7th Edition)
-------------------------------------------------------------------

Because :person:`Fr. Peter Hoenen, S.J. <hoenen>` (:cite:`*De Noetica Geometriae*, 1954 <hoenen:1954>`) cites :person:`Hilbert <hilbert>`'s **7th German edition (1930)** (:cite:`Teubner 1930 <hilbert:1930>`) while :person:`T. L. Heath <heath>` (:cite:`Heath 1908 <heath:1908>`) cites both the 1899 *Festschrift* and early revised editions, the following table reconciles every numbering and terminological shift:

.. list-table:: 1899 / 1902 vs. 1930 (7th Edition) Structural Concordance
   :header-rows: 1
   :widths: 24 38 38

   * - Feature / Locus
     - 1899 Teubner (1st ed.) & 1902 Townsend (EN)
     - 1930 Teubner (7th ed., cited by Hoenen 1954)
   * - **Axiom Groups III and IV**
     - Group III = Axiom of Parallels (§ 5); Group IV = Axioms of Congruence IV 1–6 (§ 6)
     - Group III = Axioms of Congruence III 1–5; Group IV = Axiom of Parallels
   * - **Linear Order Axiom II 4 & Collinear Point Theorems**
     - Axiom II 4 (4-point linear order implication) + Theorem 4 (ordering any finite number of collinear points A, B, C, D, E, ..., K)
     - Axiom II 4 dropped after E. H. Moore (1902) proved its redundancy, becoming Satz 5; 1899 Satz 4 becomes 7th ed. Satz 6 (both analyzed by Hoenen in Caput V § 3.2.A)
   * - **Axiom of Completeness (Vollständigkeit)**
     - Absent from 1899 German 1st ed.; added by Hilbert in 1900 French ed. and included by Townsend (1902) as the concluding Remark in § 8
     - Formalized as Axiom V 2 (Axiom der Vollständigkeit; later Line Completeness), analyzed by Hoenen in Caput V § 3.2 & § 5 fn. 10
   * - **Polygon Equivalence Terminology (Chapter IV, § 18)**
     - flächengleich (decomposable into congruent triangles; Townsend: 'equal area' / 'equal by addition') vs. inhaltsgleich (equicomplementable; Townsend: 'of equal content')
     - zerlegungsgleich (equidecomposable) vs. ergänzungsgleich / inhaltsgleich (cited by Heath on Euclid I.35, Vol. I p. 328)
   * - **Restricted Construction Instrument (Chapter VII, § 36)**
     - Lineal (straightedge) + Streckenübertrager (Townsend: 'transferer of segments')
     - Lineal (straightedge) + Eichmass (fixed-unit segment gauge)

Master Cross-Repository Overview
--------------------------------

.. list-table:: Synopsis of Hilbert's *Grundlagen* Across the GEOMETOR Canon
   :header-rows: 1
   :widths: 16 28 28 28

   * - Hilbert Locus
     - Euclid (*Elements* & Heath)
     - Hoenen (*De Noetica Geometriae*)
     - Pappus (*Synagoge* VII)
   * - :ref:`Introduction <concordance-epigraph-intro>`
     - Book I, Def. 1–23, Post. 1–5, C.N. 1–5
     - Caput I § 5–6; Caput V § 1.1–1.3
     - —
   * - :ref:`§ 1 <concordance-sec-01-primitives>`
     - I.Def.1, I.Def.2, I.Def.4, I.Def.7
     - Caput I § 6 & fn. 14; Caput IV, Preliminaries & fn. 1
     - —
   * - :ref:`§ 2 <concordance-sec-02-connection>`
     - Post. 1, Post. 2, C.N. 9, XI.1–3
     - Caput IV § 1–2
     - Projective Incidence Foundation
   * - :ref:`§ 3, § 4 <concordance-sec-03-04-order>`
     - I.1, I.10, I.16 (tacit betweenness & planar separation)
     - Caput V § 3.2.A–B & fns. 8–9
     - —
   * - :ref:`§ 5 <concordance-sec-05-parallels>`
     - Post. 5; I.27–32
     - Caput II § 4; Caput VI
     - Affine specialization of line at infinity
   * - :ref:`§ 6, § 7 <concordance-sec-06-07-congruence>`
     - C.N. 1–4 (esp. C.N. 4 superposition); I.4 (SAS Triangle Congruence); Post. 4 ('All right angles are equal'); I.2–3, I.5, I.8, I.13, I.15, I.23, I.26, I.27, I.32
     - Caput IV § 3; Caput V § 2
     - —
   * - :ref:`§ 8 <concordance-sec-08-continuity>`
     - V.Def.4; X.1; I.1 & I.22
     - Caput V § 3.2 & § 5, fn. 10
     - —
   * - :ref:`§ 9, § 10, § 11, § 12 <concordance-sec-09-12-metamathematics>`
     - Post. 5; I.4; V.Def.4
     - Caput I § 6 fn. 14; Caput V § 1.1 & § 4
     - —
   * - :ref:`§ 13, § 14, § 15, § 16, § 17 <concordance-sec-13-17-proportion>`
     - Book V (V.Def.4–5) & Book VI (VI.1–4)
     - Caput III–IV (Incommensurables & Exact Ratios)
     - Synagoge Book VII, Props. 138–139 (Pappus's Hexagon Theorem)
   * - :ref:`§ 18, § 19, § 20, § 21 <concordance-sec-18-21-areas>`
     - C.N. 2, C.N. 3, C.N. 5; Book I, Props. 35–45
     - Caput IV (Exact Equality of Magnitude)
     - —
   * - :ref:`§ 22, § 23, § 24, § 25, § 26, § 27, § 28, § 29, § 30 <concordance-sec-22-30-desargues>`
     - Book XI (Spatial Incidence vs. Book I Planar Congruence)
     - Caput II & Caput VI (Dimensionality of Intelligible Space)
     - Desargues–Pappus Projective Hierarchy
   * - :ref:`§ 31, § 32, § 33, § 34, § 35 <concordance-sec-31-35-pascal-pappus>`
     - V.Def.4 (Archimedean Commutativity Force)
     - Caput V § 1 & § 4 (Algebraic Models and Non-Commutative Number Systems)
     - Synagoge Book VII, Props. 138–139 & Mystic Hexagram
   * - :ref:`§ 36, § 37, § 38, § 39, Conclusion <concordance-sec-36-39-constructions>`
     - Post. 1–3; Book I, Props. 1–3, 9–12, 22–23, 31; Book XI (Polyhedra)
     - Caput III–V (Constructibility, Existence, and Purity of Method)
     - Synagoge Book III & VII (Plane, Solid, and Linear Construction Problems)

Detailed Analytical Concordance
-------------------------------

.. _concordance-epigraph-intro:

Introduction (introduction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hilbert opens with Kant's triad of sense, understanding, and reason, formulating the modern metamathematical program: simplicity, completeness, mutual independence, and consistency of geometric axioms.

* **Codex Loci**: :ref:`Introduction (EN) <grundlagen-en-s0>` / :ref:`(DE) <grundlagen-de-s0>` · :ref:`Unit Notes <grundlagen-introduction-notes>`
* **Axioms & Theorems**: ``Kant Epigraph (KrV A 702 / B 730)``; ``Problem of Axiomatic Investigation``
* **Euclid / Elements** — :external+euclid:doc:`Book I, Def. 1–23, Post. 1–5, C.N. 1–5 <heath/volume_I/book_i/definitions/commentary>` *(Heath folio 0209–0246)*: Hilbert recasts Euclid's three-tier foundation (Definitions, Postulates, Common Notions) into implicit axiomatic definitions across five independent groups.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput I § 5–6; Caput V § 1.1–1.3 <de_noetica_geometriae/caput-5/caput-5-en>`: Contrasts Hilbert's purely formal hypothetico-deductive axiomatics (logical correctness and non-contradiction) with Aristotle's Posterior Analytics (demonstrative truth from intelligible principles) and Freudenthal's semi-axiomatics.

.. _concordance-sec-01-primitives:

§ 1 (chapter-1)
~~~~~~~~~~~~~~~

Eliminates explicit definitions of primitive geometric objects in favor of implicit relational characterization across five axiom groups: Connection, Order, Parallels, Congruence, and Continuity.

* **Codex Loci**: :ref:`§ 1 (EN) <grundlagen-en-s1>` / :ref:`(DE) <grundlagen-de-s1>` · :ref:`Unit Notes <grundlagen-chapter-1-notes>`
* **Axioms & Theorems**: ``Erklärung (Points, Straight Lines, Planes)``
* **Euclid / Elements** — :external+euclid:doc:`I.Def.1, I.Def.2, I.Def.4, I.Def.7 <heath/volume_I/book_i/definitions/commentary>` *(Heath folio 0209–0223)*: Replaces Euclid's descriptive definitions ('A point is that which has no part', 'A straight line lies evenly with the points on itself') by three unspecified systems of things bound solely by relational axioms.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput I § 6 & fn. 14 <de_noetica_geometriae/caput-1/caput-1-en>`: Quotes Hilbert's opening sentence verbatim in German ('Wir denken drei verschiedene Systeme von Dingen...') and highlights that Hilbert leaves numbers ('two points', 'three planes', real coordinates) unformalized in their intuitive sense.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput IV, Preliminaries & fn. 1 <de_noetica_geometriae/caput-4/caput-4-en>`: Analyzes Hilbert's recurring heading 'Erklärung' ('Definition/Explanation') as concealing existential and intuitive judgments abstracted from spatial extension (materia intelligibilis).

.. _concordance-sec-02-connection:

§ 2 (chapter-1)
~~~~~~~~~~~~~~~

Establishes the planar (I 1–2) and spatial (I 3–7) incidence axioms and proves intersection uniqueness and existence of non-collinear triples (Theorems 1–2).

* **Codex Loci**: :ref:`§ 2 (EN) <grundlagen-en-s2>` / :ref:`(DE) <grundlagen-de-s2>` · :ref:`Unit Notes <grundlagen-chapter-1-notes>`
* **Axioms & Theorems**: ``Axioms I 1–7 (Connection / Verknüpfung)``; ``Theorem 1``; ``Theorem 2``
* **Euclid / Elements** — :external+euclid:doc:`Post. 1, Post. 2, C.N. 9, XI.1–3 <heath/volume_I/book_i/postulates/index>` *(Heath folio 0229, 0246)*: Formalizes both existence (I 1: Postulate 1) and uniqueness (I 2: Common Notion 9, two lines do not enclose a space) of the straight line through two points, together with planar and 3D incidence (XI.1–3) and dimensional lower bounds (I 6–7).
* **Hoenen (1954)** — :external+hoenen:doc:`Caput IV § 1–2 <de_noetica_geometriae/caput-4/caput-4-en>`: Investigates how the unique determination of a straight line by two points is grasped by intuitive formal abstraction prior to axiomatic postulation.
* **Pappus** — :external+pappus:doc:`Projective Incidence Foundation <index>`: Planar incidence I 1–2 and spatial plane-intersection I 3–6 provide the projective incidence skeleton upon which spatial Desargues (§ 22) rests.

.. _concordance-sec-03-04-order:

§ 3, § 4 (chapter-1)
~~~~~~~~~~~~~~~~~~~~

Formalizes ternary collinear betweenness (II 1–4) and Pasch's planar separation axiom (II 5), deriving segment density, total linear ordering of finite point-sets, half-planes, rays, Jordan polygon separation, and spatial plane separation (Theorems 3–7).

* **Codex Loci**: :ref:`§ 3 (EN) <grundlagen-en-s3>` / :ref:`(DE) <grundlagen-de-s3>` · :ref:`§ 4 (EN) <grundlagen-en-s4>` / :ref:`(DE) <grundlagen-de-s4>` · :ref:`Unit Notes <grundlagen-chapter-1-notes>`
* **Axioms & Theorems**: ``Axioms II 1–5 (Order / Anordnung)``; ``Pasch's Axiom (II 5)``; ``Theorems 3–7 (Density, Linear Order of n Points, Plane & Polygon Separation)``
* **Euclid / Elements** — :external+euclid:doc:`I.1, I.10, I.16 (tacit betweenness & planar separation) <heath/volume_I/book_i/propositions/01/commentary>` *(Heath folio 0256, 0280)*: Supplies the entire linear betweenness and planar side-separation apparatus (Pasch's Axiom II 5) absent from Euclid's explicit postulates, blocking fallacies like the 'all triangles are isosceles' sophism.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput V § 3.2.A–B & fns. 8–9 <de_noetica_geometriae/caput-5/caput-5-en>`: Hoenen's centerpiece critique of pure formalism: examines II 1–4 and Theorem 4 (7th ed. Satz 5 & Satz 6: ordering n collinear points 'A, B, C, D, E, ..., K'), notes E. H. Moore's 1902 proof that II 4 is redundant, exposes Hilbert's tacit reliance on the visual left-to-right spatial order of typographic symbols and terms like 'einerseits / andererseits' and 'umgekehrt', and endorses G. H. Hardy's 1929 Mind verdict: 'If Hilbert's axioms are to mean anything to us, we must draw figures.'

.. _concordance-sec-05-parallels:

§ 5 (chapter-1)
~~~~~~~~~~~~~~~

States the Euclidean Axiom of Parallels (Group III in 1899/1902; Group IV in later editions) and derives parallel transitivity (Theorem 8), preparing § 7's alternate-angle and 180° triangle angle-sum theorems.

* **Codex Loci**: :ref:`§ 5 (EN) <grundlagen-en-s5>` / :ref:`(DE) <grundlagen-de-s5>` · :ref:`Unit Notes <grundlagen-chapter-1-notes>`
* **Axioms & Theorems**: ``Axiom III (Euclidean Parallel Axiom / Parallelenaxiom)``; ``Theorem 8 (Transitivity of Parallelism)``
* **Euclid / Elements** — :external+euclid:doc:`Post. 5; I.27–32 <heath/volume_I/book_i/postulates/commentary>` *(Heath folio 0236–0241, 0320–0335)*: Adopts Playfair's uniqueness formulation in a given plane (at most one non-intersecting line through A to a), while existence of at least one parallel follows from exterior/alternate angle congruence (§ 7 / § 10, Euclid I.27).
* **Hoenen (1954)** — :external+hoenen:doc:`Caput II § 4; Caput VI <de_noetica_geometriae/caput-2/caput-2-en>`: Evaluates the epistemological status of Euclidean vs. Lobachevskian/Riemannian parallel postulates with respect to intelligible extension.
* **Pappus** — :external+pappus:doc:`Affine specialization of line at infinity <theorems/index>`: Axiom III enables Hilbert's affine formulations of Pascal's (Pappus's) Theorem (§ 14, § 31) and Desargues's Theorem (§ 22), where intersections on the line at infinity become parallel lines.

.. _concordance-sec-06-07-congruence:

§ 6, § 7 (chapter-1)
~~~~~~~~~~~~~~~~~~~~

Replaces Euclidean superposition and rigid motion by six axioms of segment and angle congruence (IV 1–6), proving SAS (Theorem 10), ASA (Theorem 11), supplementary angles (Theorem 12), Euclid's Postulate 4 on right angles (Theorem 15), SSS (Theorem 16), and the 180° triangle angle sum (Theorem 20).

* **Codex Loci**: :ref:`§ 6 (EN) <grundlagen-en-s6>` / :ref:`(DE) <grundlagen-de-s6>` · :ref:`§ 7 (EN) <grundlagen-en-s7>` / :ref:`(DE) <grundlagen-de-s7>` · :ref:`Unit Notes <grundlagen-chapter-1-notes>`
* **Axioms & Theorems**: ``Axioms IV 1–6 (Congruence / Congruenz)``; ``Theorem 9 (Congruent Point Series)``; ``Theorem 10 (SAS Congruence)``; ``Theorem 11 (ASA Congruence)``; ``Theorem 12 (Supplementary Angles)``; ``Theorems 13–14 (Angle Ray Addition & Decomposition)``; ``Theorem 15 (All Right Angles Are Congruent)``; ``Theorem 16 (SSS Congruence)``; ``Theorems 17–20 (Figure Extension, Parallel Angles, Triangle Angle Sum)``
* **Euclid / Elements** — :external+euclid:doc:`C.N. 1–4 (esp. C.N. 4 superposition) <heath/volume_I/book_i/common_notions/commentary>` *(Heath folio 0242–0244)*: Heath (Vol. I, pp. 228–230) reproduces Hilbert's § 6–7 congruence axioms and proofs in detail (including diagram 0243.g1 for SAS and 0244.g1 for supplementary angles) to show how Hilbert eliminates Euclid's physical superposition (ἐφαρμόζειν).
* **Euclid / Elements** — :external+euclid:doc:`I.4 (SAS Triangle Congruence) <heath/volume_I/book_i/propositions/04/commentary>` *(Heath folio 0263–0264)*: Heath (Vol. I, pp. 249–250) cites Russell and Hilbert (p. 9) on why SAS cannot be proved without assuming rigid motion unless Axiom IV 6 posits base-angle transfer from two sides and the included angle, from which full SAS (Theorem 10) follows by reductio ad absurdum.
* **Euclid / Elements** — :external+euclid:doc:`Post. 4 ('All right angles are equal') <heath/volume_I/book_i/postulates/commentary>` *(Heath folio 0214)*: Heath (Vol. I, p. 200) explicitly notes that Hilbert deduces Euclid's Fourth Postulate as Theorem 15 from the Congruence Axioms via supplementary angles (Theorem 12).
* **Euclid / Elements** — :external+euclid:doc:`I.2–3, I.5, I.8, I.13, I.15, I.23, I.26, I.27, I.32 <heath/volume_I/book_i/propositions/05/index>` *(Heath folio 0258–0335)*: Direct deductive counterparts: I.2–3 <-> IV 1; I.26 <-> Theorem 11; I.13 <-> Theorem 12; I.5 <-> Isosceles corollary; I.8 <-> Theorem 16; I.23 <-> IV 4; I.27–29 <-> Theorem 19; I.32 <-> Theorem 20.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput IV § 3; Caput V § 2 <de_noetica_geometriae/caput-4/caput-4-en>`: Discusses congruence, rigid displacement vs. static relational axioms, and the geometric intelligibility of equality of segments and angles.

.. _concordance-sec-08-continuity:

§ 8 (chapter-1)
~~~~~~~~~~~~~~~

Introduces the Axiom of Archimedes (Group V) and—in the 1900/1902 Remark—the categorical Axiom of Completeness fixing the Cartesian real continuum.

* **Codex Loci**: :ref:`§ 8 (EN) <grundlagen-en-s8>` / :ref:`(DE) <grundlagen-de-s8>` · :ref:`Unit Notes <grundlagen-chapter-1-notes>`
* **Axioms & Theorems**: ``Axiom V / V 1 (Axiom of Archimedes)``; ``Remark / V 2 (Axiom of Completeness / Vollständigkeit, 1900/1902)``
* **Euclid / Elements** — :external+euclid:doc:`V.Def.4; X.1; I.1 & I.22 <heath/volume_I/book_i/propositions/01/commentary>` *(Heath folio 0256)*: Formalizes the Eudoxus–Archimedes exhaustion principle (V.Def.4, X.1); Heath (Vol. I, p. 242 on I.1) notes that Dedekind/Hilbert Continuity is required to guarantee circle-circle and line-circle intersections, though Chapter VII (§§ 36–39) proves Euclidean ruler-and-compass intersections already exist over Hilbert's Pythagorean field Ω without full Continuity.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput V § 3.2 & § 5, fn. 10 <de_noetica_geometriae/caput-5/caput-5-en>`: Examines Hilbert's Axiom of Completeness (Vollständigkeitsaxiom, added 1900/1903) as a metamathematical maximality postulate over all preceding axioms, demonstrating its dependence on intuitive arithmetic and set-theoretic concepts.

.. _concordance-sec-09-12-metamathematics:

§ 9, § 10, § 11, § 12 (chapter-2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Constructs Hilbert's minimal countable Pythagorean field Ω (closed under +, −, ×, ÷, and √(1+ω²)) to prove relative consistency of Axioms I–V, and builds explicit analytic countermodels establishing the mutual independence of Parallels (III), SAS Congruence (IV 6), and Continuity (V).

* **Codex Loci**: :ref:`§ 9 (EN) <grundlagen-en-s9>` / :ref:`(DE) <grundlagen-de-s9>` · :ref:`§ 10 (EN) <grundlagen-en-s10>` / :ref:`(DE) <grundlagen-de-s10>` · :ref:`§ 11 (EN) <grundlagen-en-s11>` / :ref:`(DE) <grundlagen-de-s11>` · :ref:`§ 12 (EN) <grundlagen-en-s12>` / :ref:`(DE) <grundlagen-de-s12>` · :ref:`Unit Notes <grundlagen-chapter-2-notes>`
* **Axioms & Theorems**: ``Countable Pythagorean Coordinate Domain Ω (§ 9)``; ``Independence of Parallel Axiom III (§ 10)``; ``Independence of SAS Congruence Axiom IV 6 (§ 11)``; ``Independence of Archimedes's Axiom V via Non-Archimedean Field Ω(t) (§ 12)``
* **Euclid / Elements** — :external+euclid:doc:`Post. 5; I.4; V.Def.4 <heath/volume_I/book_i/postulates/commentary>` *(Heath folio 0236, 0263)*: Proves rigorously by analytic models that neither Euclid's Parallel Postulate (Post. 5), nor SAS Congruence (I.4 / IV 6), nor Archimedes's Principle (V.Def.4) can be deduced from the remaining axioms.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput I § 6 fn. 14; Caput V § 1.1 & § 4 <de_noetica_geometriae/caput-5/caput-5-en>`: Demonstrates Hoenen's thesis that Hilbert proves geometric non-contradiction only relative to the arithmetic of algebraic/real numbers Ω, leaving the consistency and intuition of number foundational.

.. _concordance-sec-13-17-proportion:

§ 13, § 14, § 15, § 16, § 17 (chapter-3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Develops a purely geometric segment arithmetic (Streckenrechnung) from planar Axioms I–IV, proving Pappus's (Pascal's) Hexagon Theorem via cyclic-quadrilateral congruences to establish commutative multiplication ab = ba and Euclid's Book VI theory of similar triangles without Archimedes's Axiom.

* **Codex Loci**: :ref:`§ 13 (EN) <grundlagen-en-s13>` / :ref:`(DE) <grundlagen-de-s13>` · :ref:`§ 14 (EN) <grundlagen-en-s14>` / :ref:`(DE) <grundlagen-de-s14>` · :ref:`§ 15 (EN) <grundlagen-en-s15>` / :ref:`(DE) <grundlagen-de-s15>` · :ref:`§ 16 (EN) <grundlagen-en-s16>` / :ref:`(DE) <grundlagen-de-s16>` · :ref:`§ 17 (EN) <grundlagen-en-s17>` / :ref:`(DE) <grundlagen-de-s17>` · :ref:`Unit Notes <grundlagen-chapter-3-notes>`
* **Axioms & Theorems**: ``Theorem 21 (Affine Pascal's / Pappus's Theorem from Planar I–IV)``; ``Segment Calculus (Streckenrechnung: a + b, ab)``; ``Theorems 22–23 (Similar Triangles & Fundamental Theorem of Proportion)``; ``Linear Equations of Straight Lines and Planes (§ 17)``
* **Euclid / Elements** — :external+elements:doc:`Book V (V.Def.4–5) & Book VI (VI.1–4) <elements2/index>` *(Heath folio Vol. II, Book V–VI)*: Resolves a 2,200-year structural gulf in Euclid: whereas Book V–VI rests similarity on Eudoxus's Archimedean Definition V.Def.4–5, Hilbert constructs an exact geometric field of segments from planar Axioms I–IV alone, proving Thales's similarity theorem (VI.2 / Theorem 23) without Continuity.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput III–IV (Incommensurables & Exact Ratios) <de_noetica_geometriae/caput-4/caput-4-en>`: Illuminates the purely geometric vs. arithmetic nature of ratio and proportion without infinite limiting processes (Grenzprozesse).
* **Pappus** — :external+pappus:doc:`Synagoge Book VII, Props. 138–139 (Pappus's Hexagon Theorem) <theorems/hexagon-theorem/index>`: Direct cornerstone bridge: Hilbert's 'Pascal's Theorem' (Theorem 21, § 14) IS Pappus's Hexagon Theorem for two intersecting lines with parallel opposite sides! Hilbert gives an ingenious cyclic-quadrilateral congruence proof of αβc ≡ βαc and uses it in § 15 to prove commutativity of segment multiplication ab = ba.

.. _concordance-sec-18-21-areas:

§ 18, § 19, § 20, § 21 (chapter-4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reconstructs Euclid I.35–45 without Continuity by separating equidecomposability (flächengleich / zerlegungsgleich) from equicomplementability (inhaltsgleich), exhibits a non-Archimedean triangle pair in Ω(t) (§ 19) that is inhaltsgleich without being flächengleich, and defines additive triangle area via Chapter III's segment calculus to prove Common Notion 5 / De Zolt's Theorem (Theorem 31).

* **Codex Loci**: :ref:`§ 18 (EN) <grundlagen-en-s18>` / :ref:`(DE) <grundlagen-de-s18>` · :ref:`§ 19 (EN) <grundlagen-en-s19>` / :ref:`(DE) <grundlagen-de-s19>` · :ref:`§ 20 (EN) <grundlagen-en-s20>` / :ref:`(DE) <grundlagen-de-s20>` · :ref:`§ 21 (EN) <grundlagen-en-s21>` / :ref:`(DE) <grundlagen-de-s21>` · :ref:`Unit Notes <grundlagen-chapter-4-notes>`
* **Axioms & Theorems**: ``Theorem 24: flächengleich / zerlegungsgleich vs. inhaltsgleich (§ 18)``; ``Theorems 25–28 (Parallelogram & Triangle Equicomplementability; Non-Archimedean Counterexample)``; ``Theorem 29 (Triangulation Invariance of Area Measure / Flächenmass)``; ``Theorems 30–31 (Equal Area Measure <-> Equal Content & De Zolt's Postulate / Euclid C.N. 5)``
* **Euclid / Elements** — :external+euclid:doc:`C.N. 2, C.N. 3, C.N. 5; Book I, Props. 35–45 <heath/volume_I/book_i/propositions/35/commentary>` *(Heath folio 0342)*: Heath (Vol. I, p. 328 on I.35) directly cites Hilbert's distinction between polygons equal by decomposition (1899 flächengleich / later zerlegungsgleich) and polygons of equal content by subtraction of congruent pieces (inhaltsgleich / ergänzungsgleich). Moreover, Hilbert proves Euclid's Common Notion 5 ('The whole is greater than the part' for polygon area, De Zolt's postulate) as Theorem 31 using segment-algebra area measures!
* **Hoenen (1954)** — :external+hoenen:doc:`Caput IV (Exact Equality of Magnitude) <de_noetica_geometriae/caput-4/caput-4-en>`: Clarifies the axiomatic vs. intuitive basis of 'The whole is greater than the part' (C.N. 5) in polygonal dissection.

.. _concordance-sec-22-30-desargues:

§ 22, § 23, § 24, § 25, § 26, § 27, § 28, § 29, § 30 (chapter-5)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proves Desargues's Theorem from spatial incidence (I–III) or planar congruence, constructs Hilbert's celebrated non-Desarguesian plane (§ 23, Theorem 33) by refracting lines across an ellipse to prove planar Desargues unprovable from planar I 1–2, II, III, IV 1–5, V alone, and shows that planar Desargues characterizes embeddability in 3-space and coordinatizability over an associative skew-field (Theorems 34–35).

* **Codex Loci**: :ref:`§ 22 (EN) <grundlagen-en-s22>` / :ref:`(DE) <grundlagen-de-s22>` · :ref:`§ 23 (EN) <grundlagen-en-s23>` / :ref:`(DE) <grundlagen-de-s23>` · :ref:`§ 24 (EN) <grundlagen-en-s24>` / :ref:`(DE) <grundlagen-de-s24>` · :ref:`§ 25 (EN) <grundlagen-en-s25>` / :ref:`(DE) <grundlagen-de-s25>` · :ref:`§ 26 (EN) <grundlagen-en-s26>` / :ref:`(DE) <grundlagen-de-s26>` · :ref:`§ 27 (EN) <grundlagen-en-s27>` / :ref:`(DE) <grundlagen-de-s27>` · :ref:`§ 28 (EN) <grundlagen-en-s28>` / :ref:`(DE) <grundlagen-de-s28>` · :ref:`§ 29 (EN) <grundlagen-en-s29>` / :ref:`(DE) <grundlagen-de-s29>` · :ref:`§ 30 (EN) <grundlagen-en-s30>` / :ref:`(DE) <grundlagen-de-s30>` · :ref:`Unit Notes <grundlagen-chapter-5-notes>`
* **Axioms & Theorems**: ``Theorem 32 (Affine Desargues's Theorem)``; ``Theorem 33 (Hilbert's Non-Desarguesian Plane)``; ``Theorems 34–35 (Associative Skew-Field / Desarguessches Zahlensystem & 3D Embeddability)``
* **Euclid / Elements** — :external+elements:doc:`Book XI (Spatial Incidence vs. Book I Planar Congruence) <index>` *(Heath folio Vol. III, Book XI)*: Reveals that a 2D affine plane satisfying I 1–2, II, III can be embedded into a 3D incidence space satisfying I 3–7 if and only if Desargues's Theorem holds.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput II & Caput VI (Dimensionality of Intelligible Space) <de_noetica_geometriae/caput-6/caput-6-en>`: Illustrates the structural constraint exerted by three-dimensional spatial incidence upon two-dimensional planar geometry.
* **Pappus** — :external+pappus:doc:`Desargues–Pappus Projective Hierarchy <theorems/collection-book-vii/index>`: Establishes the first rung of projective coordinatization: planar Incidence + Order + Parallels + Desargues (without Congruence IV!) generates an associative division ring (skew-field, Desarguessches Zahlensystem), whereas dropping Congruence in 2D allows Hilbert's ellipse-arc non-Desarguesian plane (§ 23).

.. _concordance-sec-31-35-pascal-pappus:

§ 31, § 32, § 33, § 34, § 35 (chapter-6)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Completes the algebraic classification of projective/affine geometries: proves every Archimedean ordered skew-field is commutative (Theorem 38, hence Pappus/Pascal holds under I, II, III, V without Congruence, Theorem 36), and constructs the non-commutative skew-field Ω(s, t) (ts = 2st, Theorem 39) to establish a consistent 3D non-Pascalian geometry (Theorem 37) when both Congruence IV and Archimedes V are dropped.

* **Codex Loci**: :ref:`§ 31 (EN) <grundlagen-en-s31>` / :ref:`(DE) <grundlagen-de-s31>` · :ref:`§ 32 (EN) <grundlagen-en-s32>` / :ref:`(DE) <grundlagen-de-s32>` · :ref:`§ 33 (EN) <grundlagen-en-s33>` / :ref:`(DE) <grundlagen-de-s33>` · :ref:`§ 34 (EN) <grundlagen-en-s34>` / :ref:`(DE) <grundlagen-de-s34>` · :ref:`§ 35 (EN) <grundlagen-en-s35>` / :ref:`(DE) <grundlagen-de-s35>` · :ref:`Unit Notes <grundlagen-chapter-6-notes>`
* **Axioms & Theorems**: ``Theorem 36 (Pappus/Pascal Provable from I, II, III, V via Archimedes)``; ``Theorem 37 (Pappus/Pascal Unprovable from I, II, III Alone)``; ``Theorem 38 (Commutativity of Every Archimedean Ordered Skew-Field)``; ``Theorem 39 (Non-Commutative Non-Archimedean Skew-Field Ω(s, t) with ts = 2st)``
* **Euclid / Elements** — :external+elements:doc:`V.Def.4 (Archimedean Commutativity Force) <index>` *(Heath folio Vol. II, Book V)*: Demonstrates that the Archimedean Axiom V forces any ordered division ring to be commutative (Theorem 38), thereby entailing Pappus/Pascal (Theorem 36) even when Congruence IV is entirely omitted!
* **Hoenen (1954)** — :external+hoenen:doc:`Caput V § 1 & § 4 (Algebraic Models and Non-Commutative Number Systems) <de_noetica_geometriae/caput-5/caput-5-en>`: Exemplifies Hilbert's algebraic model-building through formal Laurent-like power series over non-commuting indeterminates.
* **Pappus** — :external+pappus:doc:`Synagoge Book VII, Props. 138–139 & Mystic Hexagram <theorems/pascal-hexagrammum/index>`: Culmination of the GEOMETOR pappus <-> hilbert nexus: proves that Pappus's Hexagon Theorem ('Pascal's Theorem' for degenerate conic = line pair) is strictly equivalent to the commutativity law ab = ba in the coordinate division ring, and constructs the first explicit non-Archimedean non-commutative ordered skew-field Ω(s, t) (with ts = 2st, Theorem 39) to build a 3D Desarguesian, non-Pascalian geometry (§ 34).

.. _concordance-sec-36-39-constructions:

§ 36, § 37, § 38, § 39, Conclusion (chapter-7)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Characterizes geometric constructions executable with straightedge and segment-transferer (Streckenübertrager / Eichmass) via totally positive algebraic extensions and sums of squares (Theorems 40–44), closing with Hilbert's manifesto on 'purity of method' (Reinheit der Methode), Dehn's 1900 solution of Hilbert's Third Problem on polyhedral volume, and Townsend's 1902 Appendix on Hilbert's topological Lie-group foundations.

* **Codex Loci**: :ref:`§ 36 (EN) <grundlagen-en-s36>` / :ref:`(DE) <grundlagen-de-s36>` · :ref:`§ 37 (EN) <grundlagen-en-s37>` / :ref:`(DE) <grundlagen-de-s37>` · :ref:`§ 38 (EN) <grundlagen-en-s38>` / :ref:`(DE) <grundlagen-de-s38>` · :ref:`§ 39 (EN) <grundlagen-en-s39>` / :ref:`(DE) <grundlagen-de-s39>` · :ref:`Conclusion (EN) <grundlagen-en-s40>` / :ref:`(DE) <grundlagen-de-s40>` · :ref:`Unit Notes <grundlagen-chapter-7-notes>`
* **Axioms & Theorems**: ``Theorem 40 (Fundamental Constructions with Straightedge & Segment-Transferer)``; ``Theorem 41 (Pythagorean Radical Criterion & Non-Constructible Compass Right Triangle)``; ``Theorem 42 (Totally Positive Algebraic Numbers as Sums of Four Squares)``; ``Theorem 43 (Definite Rational Polynomials as Quotients of Sums of Squares)``; ``Theorem 44 (2^n Real Solutions Criterion for Straightedge & Segment-Transferer)``; ``Conclusion & Appendix: Purity of Method (Reinheit der Methode), Dehn's Polyhedra, Lie Groups``
* **Euclid / Elements** — :external+euclid:doc:`Post. 1–3; Book I, Props. 1–3, 9–12, 22–23, 31; Book XI (Polyhedra) <heath/volume_I/book_i/propositions/01/commentary>` *(Heath folio 0229–0235, 0256)*: Determines exactly which Euclidean straightedge-and-compass problems (Post. 1–3) can be solved without circle-circle intersections using only a straightedge and segment-transferer (Streckenübertrager / Eichmass), linking geometry to totally real quadratic number towers and sums of squares.
* **Hoenen (1954)** — :external+hoenen:doc:`Caput III–V (Constructibility, Existence, and Purity of Method) <de_noetica_geometriae/caput-5/caput-5-en>`: Echoes Hilbert's concluding methodological principle of 'purity of method' (Reinheit der Methode): employing in every proof only those axioms intrinsically demanded by the nature of the proposition.
* **Pappus** — :external+pappus:doc:`Synagoge Book III & VII (Plane, Solid, and Linear Construction Problems) <theorems/cross-ratios-harmonics/index>`: Refines Pappus's ancient classification of plane (ruler-and-compass) problems by splitting quadratic extensions √α into Pythagorean sums of squares (constructible by ruler + segment-transferer) vs. general positive radicals requiring full compass intersections.
