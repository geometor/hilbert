:layout: book

.. _grundlagen-chapter-5-notes:

Chapter V: Desargues's Theorem — Notes
======================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Dimensionality and the Meaning of Spatial Incidence (`§§ 22–23, 30`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Why can Desargues's Theorem (`Theorem 32`) be proved in three lines in 3D projective/affine space using only incidence axioms (`I 1–7, II, III`), yet **cannot be proved at all** in 2D planar incidence-order-parallel geometry (`I 1–2, II, III, V`)?

* **In 3-Space**: Given two perspective triangles in plane $\alpha$, one lifts the perspective rays into a triangular pyramid in 3-space so corresponding sides lie in two planes $\beta, \gamma$; the intersection line $\beta \cap \gamma$ (guaranteed by spatial Axiom `I 6`!) meets $\alpha$ in the Desargues axis (or parallel direction).
* **In the Plane Alone (`§ 23`, `Theorem 33`)**: Without a third spatial dimension (`I 3–7`) or planar triangle congruence (`IV 6`), :person:`Hilbert <hilbert>`'s refracted ellipse model bends straight lines locally inside $x^2 + 4y^2 = 1$ along circular arcs through $F(\tfrac{3}{2}, 0)$, destroying perspective concurrency while preserving all planar incidence, order, parallel, and continuity axioms! *(Historical note: in 1902 Forest Ray Moulton simplified Hilbert's ellipse construction to refracted broken lines across the $X$-axis—the "Moulton plane"—after Hilbert's 1899 breakthrough showed such planes exist.)*
* **Elimination of Spatial Axioms (`§ 30`, `Theorem 35`)**: As :person:`Hilbert <hilbert>` summarizes memorably in § 30, Desargues's Theorem is *"the result of the elimination of the space axioms"* for planar geometry, and simultaneously unlocks embedding into projective/affine spaces of **arbitrary dimension $n$**!

2. Non-Commutative Geometry Before Quantum Mechanics (`§§ 24–29`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notice the astonishing modernity of §§ 24–29: twenty-six years before Heisenberg, Born, and Jordan introduced non-commutative matrix mechanics in Göttingen (1925), :person:`Hilbert <hilbert>` constructs coordinate geometry over a **non-commutative division ring** (*skew-field*, :term:`Desarguessches Zahlensystem <desarguessches-zahlensystem>`). In `Theorem 34` (`§ 27`), left-multiplication vs. right-multiplication becomes geometrically decisive:

* $ax + by + c = 0$ (coefficients on the **left**) defines a straight line;
* $xa + yb + c = 0$ (coefficients on the **right**) in general **does not** define a straight line unless multiplication commutes—i.e., unless Pappus's/Pascal's Theorem holds!

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 22, § 23, § 24, § 25, § 26, § 27, § 28, § 29, § 30** (:ref:`concordance-sec-22-30-desargues`): Proves Desargues's Theorem from spatial incidence (I–III) or planar congruence, constructs Hilbert's celebrated non-Desarguesian plane (§ 23, Theorem 33) by refracting lines across an ellipse to prove planar Desargues unprovable from planar I 1–2, II, III, IV 1–5, V alone, and shows that planar Desargues characterizes embeddability in 3-space and coordinatizability over an associative skew-field (Theorems 34–35).
  - :external+elements:doc:`Euclid — Book XI (Spatial Incidence vs. Book I Planar Congruence) <index>`: Reveals that a 2D affine plane satisfying I 1–2, II, III can be embedded into a 3D incidence space satisfying I 3–7 if and only if Desargues's Theorem holds.
  - :external+hoenen:doc:`Hoenen — Caput II & Caput VI (Dimensionality of Intelligible Space) <de_noetica_geometriae/caput-6/caput-6-en>`: Illustrates the structural constraint exerted by three-dimensional spatial incidence upon two-dimensional planar geometry.
  - :external+pappus:doc:`Pappus — Desargues–Pappus Projective Hierarchy <theorems/collection-book-vii/index>`: Establishes the first rung of projective coordinatization: planar Incidence + Order + Parallels + Desargues (without Congruence IV!) generates an associative division ring (skew-field, Desarguessches Zahlensystem), whereas dropping Congruence in 2D allows Hilbert's ellipse-arc non-Desarguesian plane (§ 23).
