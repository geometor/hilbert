:layout: book
:canonical_id: Chapter IV
:breadcrumb_title: Chapter IV
:order: 5
:title: Chapter IV: The Theory of Plane Areas

.. _grundlagen-chapter-4:
.. _grundlagen-chapter-4-en:
.. _grundlagen-chapter-4-de:
.. _grundlagen-chapter-4-summary:
.. _grundlagen-chapter-4-notes:

Chapter IV: The Theory of Plane Areas
=====================================

.. rubric:: *Kapitel IV: Die Lehre von den Flächeninhalten in der Ebene* — David Hilbert (1899 / 1902) — §§ 18–21

Building directly upon Chapter III's non-Archimedean :term:`Streckenrechnung <streckenrechnung>`, Chapter IV reconstructs :person:`Euclid <euclid>`'s Book I (`I.35–45`) theory of polygonal area in the plane **solely from planar Axioms `I 1–2, II–IV` without Continuity (`V`)**:

* **§ 18 — Equidecomposability vs. Equicomplementability (Theorem 24)**: Introduces the decisive distinction between two polygons being :term:`flächengleich <flaechengleich>` (1899 term; renamed :term:`zerlegungsgleich <zerlegungsgleich>` in later editions; Townsend: *"equal by addition"* / equidecomposable into pairwise congruent triangles) versus :term:`inhaltsgleich <inhaltsgleich>` (Townsend: *"of equal content"* / equicomplementable by adjoining equidecomposable pieces). Proves transitivity of both relations by common subdivision (`Theorem 24`).
* **§ 19 — Parallelograms and Triangles (Theorems 25–28)**: Reproduces :person:`Euclid <euclid>`'s `I.35–38` trapezoid-subtraction argument to prove that parallelograms and triangles on equal bases with equal altitudes are always *inhaltsgleich* (`Theorems 25–27`), but exhibits a dramatic counterexample in :math:`\Omega(t)` (`§ 12`): two triangles of base :math:`1` and altitude :math:`1` whose apex projection is offset by the non-Archimedean element :math:`t` are *inhaltsgleich* yet **cannot be dissected into congruent triangles** (*not flächengleich*)! Formulates the converse (`Theorem 28`, `Euclid I.39`) and notes that Euclid relied on Common Notion 5 (*„Καὶ τὸ ὅλον τοῦ μέρους μεῖζόν ἐστιν“*) as an unproved area axiom.
* **§ 20 — Measure of Area** (*Flächenmass*, **Theorem 29**): Defines the area measure :math:`F(\Delta) = \tfrac{1}{2} a h_a = \tfrac{1}{2} b h_b` in the segment field via `Theorem 22`, proves invariance of :math:`F(\Delta)` under arbitrary simplicial subdivision by reducing any triangulation to chains of transversal splits (`Theorem 29`), and deduces that *inhaltsgleich* polygons have equal area measure—immediately proving `Theorem 28`.
* **§ 21 — Converse Equivalence and De Zolt's Postulate (Theorems 30–31)**: Proves conversely that any two polygons with equal segment-valued area measure are *inhaltsgleich* (`Theorem 30`), and deduces :person:`Antonio De Zolt <de-zolt>`'s postulate / `Euclid C.N. 5` (`Theorem 31`): if a rectangle is dissected into triangles and even a single triangle is omitted, the remaining triangles can never refill the rectangle!

Sections
--------

.. collection::
   :sort: order

.. toctree::
   :hidden:
   :maxdepth: 1

   sec_18/index
   sec_19/index
   sec_20/index
   sec_21/index
