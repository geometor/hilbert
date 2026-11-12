:layout: book

.. _grundlagen-chapter-6-summary:

Chapter VI: Pascal's Theorem — Summary
======================================

.. rubric:: Structural & Mathematical Overview — *Kapitel VI: Der Pascalsche Satz*

.. contents:: In This Summary
   :local:
   :depth: 2
   :backlinks: none

Architectural Summary of Chapter VI (§§ 31–35)
----------------------------------------------

Chapter VI brings the projective-algebraic hierarchy to its climax by isolating the exact axiomatic and algebraic meaning of :term:`Pascal's (Pappus's) Theorem <pascalscher-satz>` when **Congruence (`IV`) is omitted**:

* **§ 31 — Two Fundamental Theorems on Pappus/Pascal (Theorems 36–37)**: Announces two complementary results in 3D space without Congruence:
  1. `Theorem 36`: Pappus/Pascal **is provable** from `I, II, III, V` (i.e., with Archimedes's Axiom, even without Congruence!).
  2. `Theorem 37`: Pappus/Pascal **is unprovable** from `I, II, III` alone (when both Congruence `IV` and Archimedes `V` are dropped).
* **§ 32 — Hilbert's Commutativity Theorem for Archimedean Skew-Fields (Theorem 38)**: Proves a landmark theorem of pure algebra: **every Archimedean ordered division ring is necessarily commutative**! Assuming $a > 0, b > 0$, and $ab - ba > 0$, :person:`Hilbert <hilbert>` traps $a$ and $b$ between consecutive multiples $md < a < (m+1)d$ and $nd < b < (n+1)d$ using Archimedes's Axiom (`17`) and shows $ab - ba < (m + n + 1)d^2 < (a + b + 1)c = ab - ba$, an outright contradiction!
* **§ 33 — Hilbert's Non-Commutative Twist Laurent Skew-Field $\Omega(s, t)$ (Theorem 39)**: Constructs the first explicit example in mathematics of an ordered non-Archimedean skew-field (`Theorem 39`): formal Laurent series $S = s^m T_0 + s^{m+1} T_1 + \cdots$ whose coefficients $T_k = r_0 t^n + r_1 t^{n+1} + \cdots$ are formal Laurent series in $t$ over $\mathbb{Q}$, governed by the non-commutative twist relation

  $$ts = 2st,$$

  and ordered lexicographically by the leading rational coefficient $r_0$ of $T_0$.
* **§§ 34–35 — Non-Pascalian Geometry and Intersection Completeness**: Building 3-space over $\Omega(s, t)$ via § 29 immediately proves `Theorem 37`, exhibiting a consistent 3D :term:`Non-Pascalian Geometry <nicht-pascalsche-geometrie>` (which by `Theorem 36` is necessarily non-Archimedean). Conversely, § 35 proves that every planar incidence/intersection theorem holding under `I–V` reduces synthetically to a finite combination of Desargues's and Pascal's (Pappus's) theorems without needing Congruence!

Parallel Section Navigator
--------------------------

* **§ 31. Two Theorems Concerning the Possibility of Proving Pascal's Theorem** — :ref:`English (p. 103) <grundlagen-en-s31>` · :ref:`Deutsch 1899 (S. 71) <grundlagen-de-s31>`
* **§ 32. The Commutative Law of Multiplication for an Archimedean Number System** — :ref:`English (p. 105) <grundlagen-en-s32>` · :ref:`Deutsch 1899 (S. 72) <grundlagen-de-s32>`
* **§ 33. The Commutative Law of Multiplication for a Non-Archimedean Number System** — :ref:`English (p. 107) <grundlagen-en-s33>` · :ref:`Deutsch 1899 (S. 73) <grundlagen-de-s33>`
* **§ 34. Proof of the Two Propositions Concerning Pascal's Theorem (Non-Pascalian Geometry)** — :ref:`English (p. 110) <grundlagen-en-s34>` · :ref:`Deutsch 1899 (S. 75) <grundlagen-de-s34>`
* **§ 35. The Demonstration, by Means of the Theorems of Pascal and Desargues, of Any Theorem Relating to Points of Intersection** — :ref:`English (p. 112) <grundlagen-en-s35>` · :ref:`Deutsch 1899 (S. 76) <grundlagen-de-s35>`
