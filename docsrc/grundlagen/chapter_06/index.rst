:layout: book
:canonical_id: Chapter VI
:breadcrumb_title: Chapter VI
:order: 7
:title: Chapter VI: Pascal's Theorem

.. _grundlagen-chapter-6:
.. _grundlagen-chapter-6-en:
.. _grundlagen-chapter-6-de:
.. _grundlagen-chapter-6-summary:
.. _grundlagen-chapter-6-notes:

Chapter VI: Pascal's Theorem
============================

.. rubric:: *Kapitel VI: Der Pascalsche Satz* — David Hilbert (1899 / 1902) — §§ 31–35

Chapter VI brings the projective-algebraic hierarchy to its climax by isolating the exact axiomatic and algebraic meaning of :term:`Pascal's (Pappus's) Theorem <pascalscher-satz>` when **Congruence (`IV`) is omitted**:

* **§ 31 — Two Fundamental Theorems on Pappus/Pascal (Theorems 36–37)**: Announces two complementary results in 3D space without Congruence:
  1. `Theorem 36`: Pappus/Pascal **is provable** from `I, II, III, V` (i.e., with Archimedes's Axiom, even without Congruence!).
  2. `Theorem 37`: Pappus/Pascal **is unprovable** from `I, II, III` alone (when both Congruence `IV` and Archimedes `V` are dropped).
* **§ 32 — Hilbert's Commutativity Theorem for Archimedean Skew-Fields (Theorem 38)**: Proves a landmark theorem of pure algebra: **every Archimedean ordered division ring is necessarily commutative**! Assuming :math:`a > 0, b > 0`, and :math:`ab - ba > 0`, :person:`Hilbert <hilbert>` traps :math:`a` and :math:`b` between consecutive multiples :math:`md < a < (m+1)d` and :math:`nd < b < (n+1)d` using Archimedes's Axiom (`17`) and shows :math:`ab - ba < (m + n + 1)d^2 < (a + b + 1)c = ab - ba`, an outright contradiction!
* **§ 33 — Hilbert's Non-Commutative Twist Laurent Skew-Field** :math:`\Omega(s, t)` (**Theorem 39**): Constructs the first explicit example in mathematics of an ordered non-Archimedean skew-field (`Theorem 39`): formal Laurent series :math:`S = s^m T_0 + s^{m+1} T_1 + \cdots` whose coefficients :math:`T_k = r_0 t^n + r_1 t^{n+1} + \cdots` are formal Laurent series in :math:`t` over :math:`\mathbb{Q}`, governed by the non-commutative twist relation

  .. math::

     ts = 2st,

  and ordered lexicographically by the leading rational coefficient :math:`r_0` of :math:`T_0`.
* **§§ 34–35 — Non-Pascalian Geometry and Intersection Completeness**: Building 3-space over :math:`\Omega(s, t)` via § 29 immediately proves `Theorem 37`, exhibiting a consistent 3D :term:`Non-Pascalian Geometry <nicht-pascalsche-geometrie>` (which by `Theorem 36` is necessarily non-Archimedean). Conversely, § 35 proves that every planar incidence/intersection theorem holding under `I–V` reduces synthetically to a finite combination of Desargues's and Pascal's (Pappus's) theorems without needing Congruence!

Sections
--------

.. collection::
   :sort: order

.. toctree::
   :hidden:
   :maxdepth: 1

   sec_31/index
   sec_32/index
   sec_33/index
   sec_34/index
   sec_35/index
