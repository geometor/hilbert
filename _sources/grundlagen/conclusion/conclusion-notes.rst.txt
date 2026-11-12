:layout: book

.. _grundlagen-conclusion-notes:

Conclusion & Appendix on Transformation Groups — Notes
======================================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. *Reinheit der Methode* (Purity of Method) and Impossibility Proofs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:person:`Hilbert <hilbert>`'s *Schlusswort* (*Conclusion*) articulates two enduring pillars of modern mathematical philosophy:

1. **Epistemological Value of Impossibility Proofs**: Just as Abel proved the quintic unsolvable by radicals and Lindemann proved $\pi$ transcendental (settling circle-squaring), Chapters II, IV, V, VI, and VII prove the **impossibility** of deducing Parallels (`§ 10`), SAS (`§ 11`), Archimedes (`§ 12`), polygon equidecomposability without Archimedes (`§ 19`), planar Desargues without space or congruence (`§ 23`), Pappus/Pascal without congruence or Archimedes (`§ 34`), and general compass constructions from segment transfer (`§ 37`).
2. **Purity of Method (:term:`Reinheit der Methode <reinheit-der-methode>`)**: Rather than leaving "purity" as a vague aesthetic preference (e.g., forbidding 3D space or continuity in planar proofs), *Grundlagen der Geometrie* converts purity into an exact scientific question: *what is the minimal subset of axioms required by the truth of a proposition?*

2. Max Dehn's 1900 Breakthroughs: Non-Legendrian Geometry & Hilbert's 3rd Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Between the June 1899 German *Festschrift* and :person:`Townsend <townsend>`'s 1902 English translation, :person:`Hilbert <hilbert>`'s student :person:`Max Dehn <dehn>` completed two celebrated investigations summarized in the English Conclusion:

* **The $3 \times 3$ Angle-Sum / Parallel Table (:cite:`Dehn 1900 <dehn:1900:legendre>`)**: Classical Legendre theorems state (1) triangle angle-sum $\le 2R$, and (2) if angle-sum $= 2R$, Euclid's Parallel Postulate holds. :person:`Dehn <dehn>` showed using Hilbert's non-Archimedean geometry (`§ 12`) that *without Archimedes's Axiom*:
  - **Semi-Euclidean Geometry** exists: angle-sum $= 2R$ everywhere, yet infinitely many parallels pass through a point (differing by infinitesimal angles)!
  - **Non-Legendrian Geometry** exists: angle-sum $> 2R$, yet infinitely many lines through a point fail to meet a given line (located at infinite non-Archimedean distance)!
* **Polyhedral Volume & Hilbert's Third Problem (:cite:`Dehn 1900 <dehn:1900>`)**: Extending Chapter IV from 2D polygons to 3D polyhedra, :person:`Hilbert <hilbert>` posed as his **Third Paris Problem (1900)** whether two tetrahedra of equal base and altitude are always *zerlegungsgleich* or *ergänzungsgleich* (*inhaltsgleich*). Within months, :person:`Dehn <dehn>` proved the answer is **NO** (introducing the tensor-product *Dehn invariant* $\sum \ell_i \otimes \theta_i \in \mathbb{R} \otimes_{\mathbb{Q}} (\mathbb{R}/\pi\mathbb{Q})$, showing a regular tetrahedron is neither equidecomposable nor equicomplementable with a cube of equal volume!).

3. Townsend's 1902 Appendix and Hilbert's Fifth Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 1902 English edition concludes with :person:`Townsend <townsend>`'s translation/summary of :person:`Hilbert <hilbert>`'s 1902 *Mathematische Annalen* paper (:cite:`Hilbert 1902 <hilbert:1902:lie>`), offering a radically different—**topological and group-theoretic**—foundation of plane geometry. Replacing :person:`Sophus Lie <lie>`'s analytic differentiability hypotheses (:cite:`Lie–Engel 1893 <lie:1893>`) with :person:`Camille Jordan <jordan>`'s closed curves and three topological axioms for orientation-preserving homeomorphisms (`Axioms I–III`: group closure, infinite orbits on true circles, and topological closure of displacements), :person:`Hilbert <hilbert>` recovers Euclidean and Bolyai–Lobachevsky geometry without a single derivative—launching topological group theory and the half-century quest culminating in Gleason, Montgomery, and Zippin's 1952 solution of **Hilbert's Fifth Problem**.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 36, § 37, § 38, § 39, Conclusion** (:ref:`concordance-sec-36-39-constructions`): Characterizes geometric constructions executable with straightedge and segment-transferer (Streckenübertrager / Eichmass) via totally positive algebraic extensions and sums of squares (Theorems 40–44), closing with Hilbert's manifesto on 'purity of method' (Reinheit der Methode), Dehn's 1900 solution of Hilbert's Third Problem on polyhedral volume, and Townsend's 1902 Appendix on Hilbert's topological Lie-group foundations.
  - :external+euclid:doc:`Euclid — Post. 1–3; Book I, Props. 1–3, 9–12, 22–23, 31; Book XI (Polyhedra) <heath/volume_I/book_i/propositions/01/commentary>`: Determines exactly which Euclidean straightedge-and-compass problems (Post. 1–3) can be solved without circle-circle intersections using only a straightedge and segment-transferer (Streckenübertrager / Eichmass), linking geometry to totally real quadratic number towers and sums of squares.
  - :external+hoenen:doc:`Hoenen — Caput III–V (Constructibility, Existence, and Purity of Method) <de_noetica_geometriae/caput-5/caput-5-en>`: Echoes Hilbert's concluding methodological principle of 'purity of method' (Reinheit der Methode): employing in every proof only those axioms intrinsically demanded by the nature of the proposition.
  - :external+pappus:doc:`Pappus — Synagoge Book III & VII (Plane, Solid, and Linear Construction Problems) <theorems/cross-ratios-harmonics/index>`: Refines Pappus's ancient classification of plane (ruler-and-compass) problems by splitting quadratic extensions √α into Pythagorean sums of squares (constructible by ruler + segment-transferer) vs. general positive radicals requiring full compass intersections.
