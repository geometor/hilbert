:layout: book
:canonical_id: Chapter III
:breadcrumb_title: Chapter III
:order: 4
:title: Chapter III: The Theory of Proportion

.. _grundlagen-chapter-3:
.. _grundlagen-chapter-3-en:
.. _grundlagen-chapter-3-de:
.. _grundlagen-chapter-3-summary:
.. _grundlagen-chapter-3-notes:

Chapter III: The Theory of Proportion
=====================================

.. rubric:: *Kapitel III: Die Lehre von den Proportionen* — David Hilbert (1899 / 1902) — §§ 13–17

Chapter III resolves one of the deepest structural problems in the history of geometry: reconstructing :person:`Euclid <euclid>`'s Book V–VI theory of proportion and similar triangles **purely in the plane (`I 1–2, II–IV`) without the Axiom of Archimedes (`V`)**:

* **§ 13 — Complex Number Systems**: Catalogues 17 algebraic axioms (`1–12` field laws, `13–16` ordered ring laws, `17` Archimedean property), framing the central question of geometric algebra: which geometric axioms correspond to which algebraic field laws?
* **§ 14 — Proof of Pascal's (Pappus's) Theorem (Theorem 21)**: States the affine two-line specialization of :person:`Pascal <pascal>`'s hexagram—historically :person:`Pappus <pappus>`'s Hexagon Theorem (:cite:`*Synagoge* VII.138–139 <pappus:synagoge>`): if :math:`A, B, C` and :math:`A', B', C'` lie on two intersecting lines through :math:`O` with :math:`CB' \parallel BC'` and :math:`CA' \parallel AC'`, then :math:`BA' \parallel AB'`. Using right-triangle projection operators :math:`a = \alpha c` and inscribed cyclic quadrilaterals (:math:`ABCD` on a diameter circle), :person:`Hilbert <hilbert>` proves operator commutativity :math:`\alpha\beta c \equiv \beta\alpha c` and deduces `Theorem 21` (adding a second direct four-circle proof).
* **§ 15 — Geometric Calculus of Segments** (*Streckenrechnung*): Defines segment addition :math:`c = a + b` by collinear juxtaposition and segment multiplication :math:`c = ab` on perpendicular rays from :math:`O` via a fixed unit segment :math:`1` and parallel lines. Crucially, `Theorem 21` (:term:`Pascalscher Satz <pascalscher-satz>`) immediately yields **commutativity** :math:`ab = ba` and **associativity** :math:`a(bc) = (ab)c`, while congruent right triangles establish **distributivity** :math:`a(b + c) = ab + ac`.
* **§ 16 — Proportion and Similitude (Theorems 22–23)**: Defines :math:`a : b = a' : b'` algebraically as :math:`ab' = ba'`, proves proportionality of corresponding sides in similar triangles (`Theorem 22`, first for right triangles and then generally via the incenter :math:`S` of the three angle bisectors!), and deduces the Fundamental Theorem of Proportion (`Theorem 23`, Thales's intercept theorem `Euclid VI.2`).
* **§ 17 — Linear Equations of Lines and Planes**: Extends positive segments to signed segments (:math:`+, 0, -`) forming an ordered commutative field, establishes rectangular coordinates :math:`(x, y)`, proves every straight line has a linear equation :math:`bx - ay - bc = 0`, and shows how adjoining Archimedes (`V`) embeds the coordinate domain into :math:`\mathbb{R}^3`.

Sections
--------

.. collection::
   :sort: order

.. toctree::
   :hidden:
   :maxdepth: 1

   sec_13/index
   sec_14/index
   sec_15/index
   sec_16/index
   sec_17/index
