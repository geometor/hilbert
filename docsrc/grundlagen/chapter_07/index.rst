:layout: book
:canonical_id: Chapter VII
:breadcrumb_title: Chapter VII
:order: 8
:title: Chapter VII: Geometrical Constructions Based Upon Axioms I–V

.. _grundlagen-chapter-7:
.. _grundlagen-chapter-7-en:
.. _grundlagen-chapter-7-de:
.. _grundlagen-chapter-7-summary:
.. _grundlagen-chapter-7-notes:

Chapter VII: Geometrical Constructions Based Upon Axioms I–V
============================================================

.. rubric:: *Kapitel VII: Die geometrischen Konstruktionen auf Grund der Axiome I–V* — David Hilbert (1899 / 1902) — §§ 36–39

In the final chapter, :person:`Hilbert <hilbert>` returns to :person:`Euclid <euclid>`'s constructive postulates (`Postulates 1–3`), asking precisely which geometric construction problems solvable by straightedge and compass can already be executed using only Axioms `I–V`—implemented physically by a **straightedge** (*Lineal*) and a **transferer of segments** (:term:`Streckenübertrager <streckenuebertrager>`, specialized in later editions to the fixed-unit gauge :term:`Eichmass <eichmass>`):

* **§ 36 — Elementary Constructions Without Full Circles (Theorem 40)**: Reduces the five fundamental planar constructions—joining points/intersecting lines (`Problem 1`), drawing parallels (`Problem 2`), transferring segments (`Problem 3`), transferring angles (`Problem 4`), and dropping perpendiculars (`Problem 5`, solved via semicircle chords and the triangle orthocenter!)—to `Problems 1` and `3` alone (`Theorem 40`).
* **§ 37 — Pythagorean Radical Criterion (Theorem 41)**: Proves that a construction problem is solvable by straightedge and segment-transferer if and only if the coordinates of the sought points belong to the domain $\Omega(R)$ generated from the given coordinates $R$ by $+, -, \times, \div$ and $\sqrt{\alpha^2 + \beta^2}$ (`Theorem 41`). Exhibits an explicit compass-constructible right triangle (hypotenuse $1$, leg $|\sqrt{2}| - 1$, second leg $\sqrt{2|\sqrt{2}| - 2}$) **impossible** with straightedge and segment-transferer because its conjugate $\sqrt{-2|\sqrt{2}| - 2}$ is imaginary, whereas every number in $\Omega$ is totally real!
* **§ 38 — Totally Positive Numbers and Sums of Squares (Theorems 42–43)**: Generalizes :person:`Lagrange <lagrange>`'s / Fermat's four-square theorem to algebraic number fields via relative quadratic field theory: every :term:`totally positive <total-positiv>` element of a number field $k$ is a sum of four squares in $k$ (`Theorem 42`), and every positive-definite univariate polynomial $f(x) \in \mathbb{Q}[x]$ is a quotient of two sums of squares of polynomials in $\mathbb{Q}[x]$ (`Theorem 43`—the direct progenitor of **Hilbert's Seventeenth Problem**, 1900!).
* **§ 39 — Geometric Multiplicity Criterion (Theorem 44)**: Combines `Theorems 41–43` to establish a purely geometric necessary and sufficient criterion (`Theorem 44`, proved for 1-parameter problems): a ruler-and-compass problem requiring $n$ minimal square roots is solvable by straightedge and segment-transferer if and only if it possesses **exactly $2^n$ real solutions** for all real parameter positions of the given points! Concludes that all Gauss-constructible regular polygons and Malfatti's problem are solvable with straightedge and segment-transferer, whereas Apollonius's circle-tangency problem is not.

Sections
--------

.. collection::
   :sort: order

.. toctree::
   :hidden:
   :maxdepth: 1

   sec_36/index
   sec_37/index
   sec_38/index
   sec_39/index
