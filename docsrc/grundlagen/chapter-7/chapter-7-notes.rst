:layout: book

.. _grundlagen-chapter-7-notes:

Chapter VII: Geometrical Constructions Based Upon Axioms I–V — Notes
====================================================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. From *Streckenübertrager* (1899) to *Eichmass* (Later Editions) & `geometor/elements`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``geometor/elements`` and :person:`Euclid <euclid>`'s Book I, straightedge (`Postulates 1–2`) and collapsible/modern compass (`Postulate 3`, `I.2–3`) generate quadratic field extensions via line-circle and circle-circle intersections (`Euclid I.1, I.22`). Why does Chapter VII replace the full compass with a **transferer of segments** (:term:`Streckenübertrager <streckenuebertrager>` in 1899; Townsend: *"transferer of segments"*)?

* Because **Axioms `I–V` (without *Vollständigkeit*) never mention circles intersecting circles!** Axiom `IV 1` only guarantees laying off a given segment $AB$ along a given straight line from a point $A'$.
* In later editions (e.g., 7th ed., 1930), :person:`Hilbert <hilbert>` sharpened this instrument even further to the **fixed-unit gauge** (:term:`Eichmass <eichmass>`), which can only lay off a *single fixed unit segment* $1$ along any ray—because once parallel lines (`Problem 2`) are constructible, any segment ratio can be transferred via parallels using a single fixed unit!
* Look at `fig_gauge_constructions.svg` (`§ 36`, `Problem 5`): to drop a perpendicular without drawing intersecting circles (`Euclid I.11–12`), :person:`Hilbert <hilbert>` lays off four equal radii $AB = AC = AD = AE$ from $A$ along the base line and two oblique rays through $A$; by Thales's semicircle theorem (`Euclid III.31`), $\angle BDC$ and $\angle BEC$ are right angles, so $BD$ and $CE$ are two altitudes of $\triangle BCF$ meeting at its orthocenter $H$, making the third line $FH$ strictly perpendicular to $BC$ using **straightedge and segment-transferer alone**!

2. Birth of Real Algebraic Geometry & Hilbert's 17th Problem (`§§ 37–39`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sections 37–39 bridge synthetic constructive geometry (`geometor/elements`) with deep algebraic number theory:

* **Why Compass > Segment-Transferer (`§ 37`)**: Every coordinate in $\Omega$ (`§ 9`) is built from sums of squares $\sqrt{\alpha^2 + \beta^2}$, so *all algebraic conjugates* of every number in $\Omega$ are real (**totally real**). By contrast, a circle can intersect a line whenever $\alpha > 0$ numerically, even if an algebraic conjugate of $\alpha$ is negative! Thus $\sqrt{2\sqrt{2} - 2}$ (constructible by intersecting a unit circle with $x = \sqrt{2} - 1$) has imaginary conjugate $\sqrt{-2\sqrt{2} - 2}$ and **cannot** lie in $\Omega$!
* **Hilbert's 17th Problem (`§ 38`, `Theorem 43`)**: Proving `Theorem 43` (every positive-definite univariate polynomial over $\mathbb{Q}$ is a quotient of sums of squares) led :person:`Hilbert <hilbert>` at the end of § 38 to ask whether every positive-definite rational function in $n$ variables over $\mathbb{Q}$ is a sum of squares of rational functions—posed one year later in Paris as **Hilbert's Seventeenth Problem (1900)** and solved affirmatively in 1927 by Emil Artin via Artin–Schreier real closed fields!

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 36, § 37, § 38, § 39, Conclusion** (:ref:`concordance-sec-36-39-constructions`): Characterizes geometric constructions executable with straightedge and segment-transferer (Streckenübertrager / Eichmass) via totally positive algebraic extensions and sums of squares (Theorems 40–44), closing with Hilbert's manifesto on 'purity of method' (Reinheit der Methode), Dehn's 1900 solution of Hilbert's Third Problem on polyhedral volume, and Townsend's 1902 Appendix on Hilbert's topological Lie-group foundations.
  - :external+euclid:doc:`Euclid — Post. 1–3; Book I, Props. 1–3, 9–12, 22–23, 31; Book XI (Polyhedra) <heath/volume_I/book_i/propositions/01/commentary>`: Determines exactly which Euclidean straightedge-and-compass problems (Post. 1–3) can be solved without circle-circle intersections using only a straightedge and segment-transferer (Streckenübertrager / Eichmass), linking geometry to totally real quadratic number towers and sums of squares.
  - :external+hoenen:doc:`Hoenen — Caput III–V (Constructibility, Existence, and Purity of Method) <de_noetica_geometriae/caput-5/caput-5-en>`: Echoes Hilbert's concluding methodological principle of 'purity of method' (Reinheit der Methode): employing in every proof only those axioms intrinsically demanded by the nature of the proposition.
  - :external+pappus:doc:`Pappus — Synagoge Book III & VII (Plane, Solid, and Linear Construction Problems) <theorems/cross-ratios-harmonics/index>`: Refines Pappus's ancient classification of plane (ruler-and-compass) problems by splitting quadratic extensions √α into Pythagorean sums of squares (constructible by ruler + segment-transferer) vs. general positive radicals requiring full compass intersections.
