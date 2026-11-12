:layout: book

.. _grundlagen-chapter-6-notes:

Chapter VI: Pascal's Theorem — Notes
====================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. The Grand Projective-Algebraic Synthesis (`geometor/pappus` Culmination)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapters III, V, and VI together establish the fundamental dictionary of modern synthetic and algebraic geometry—connecting :person:`Pappus <pappus>` (`c. 340 AD`), :person:`Desargues <desargues>` (`1648`), and :person:`Hilbert <hilbert>` (`1899`):

.. list-table:: Hilbert's Geometric ↔ Algebraic Correspondence Dictionary
   :header-rows: 1
   :widths: 36 32 32

   * - Geometric Axiom System
     - Key Projective Theorem
     - Coordinate Algebraic Structure
   * - Planar `I 1–2, II, III` alone
     - Neither Desargues nor Pappus
     - Planar ternary ring (non-associative; § 23 model)
   * - `I 1–7, II, III` *(or planar + Desargues)*
     - :term:`Desargues's Theorem <desarguesscher-satz>` (`Theorem 32`)
     - Ordered **associative skew-field** $D$ (`Theorem 35`, e.g. $\Omega(s, t)$)
   * - `I 1–7, II, III` + **Pappus/Pascal** *(or planar `I 1–2, II–IV`)*
     - :term:`Pappus's / Pascal's Theorem <pascalscher-satz>` (`Theorem 21`)
     - Ordered **commutative field** $F$ ($ab = ba$, e.g. $\Omega(t)$)
   * - `I 1–7, II, III, V` *(with Archimedes, even without Congruence!)*
     - Both Desargues & Pappus (`Theorem 36`)
     - Archimedean **commutative** subfield of $\mathbb{R}$ (`Theorem 38`)
   * - `I–V` + **Completeness** (*Vollständigkeit*)
     - Full Euclidean/Cartesian geometry
     - Unique real field $\mathbb{R}$

*(Subsequent post-1899 footnote: in 1905 Gerhard Hessenberg proved purely synthetically that Pappus's Theorem implies Desargues's Theorem in any projective/affine plane, and in 1905 Joseph Wedderburn proved that every finite skew-field is commutative!)*

2. Hilbert's Twist Skew-Field $\Omega(s, t)$ (`§ 33`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:person:`Hilbert <hilbert>`'s § 33 construction (`Theorem 39`) is a tour de force of algebra: by forming iterated Laurent power series over two non-commuting indeterminates $s, t$ subject to

$$ts = 2st,$$

he created what algebraists today call a **Hilbert–Mal'cev–Neumann twisted Laurent series division ring**. Every nonzero element $S = s^m T_0 + s^{m+1} T_1 + \cdots$ ($T_0 \neq 0$) is invertible by recursive power-series comparison because $T_0$ lies in the commutative Laurent field $\mathbb{Q}((t))$ and conjugation $T(t) s = s T(2t)$ merely rescales $t \mapsto 2t$, preserving positivity of the leading rational coefficient $r_0$! Thus $\Omega(s, t)$ is simultaneously **ordered**, **non-Archimedean**, and **non-commutative**, giving birth to consistent 3D :term:`Non-Pascalian Geometry <nicht-pascalsche-geometrie>`.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 31, § 32, § 33, § 34, § 35** (:ref:`concordance-sec-31-35-pascal-pappus`): Completes the algebraic classification of projective/affine geometries: proves every Archimedean ordered skew-field is commutative (Theorem 38, hence Pappus/Pascal holds under I, II, III, V without Congruence, Theorem 36), and constructs the non-commutative skew-field Ω(s, t) (ts = 2st, Theorem 39) to establish a consistent 3D non-Pascalian geometry (Theorem 37) when both Congruence IV and Archimedes V are dropped.
  - :external+elements:doc:`Euclid — V.Def.4 (Archimedean Commutativity Force) <index>`: Demonstrates that the Archimedean Axiom V forces any ordered division ring to be commutative (Theorem 38), thereby entailing Pappus/Pascal (Theorem 36) even when Congruence IV is entirely omitted!
  - :external+hoenen:doc:`Hoenen — Caput V § 1 & § 4 (Algebraic Models and Non-Commutative Number Systems) <de_noetica_geometriae/caput-5/caput-5-en>`: Exemplifies Hilbert's algebraic model-building through formal Laurent-like power series over non-commuting indeterminates.
  - :external+pappus:doc:`Pappus — Synagoge Book VII, Props. 138–139 & Mystic Hexagram <theorems/pascal-hexagrammum/index>`: Culmination of the GEOMETOR pappus <-> hilbert nexus: proves that Pappus's Hexagon Theorem ('Pascal's Theorem' for degenerate conic = line pair) is strictly equivalent to the commutativity law ab = ba in the coordinate division ring, and constructs the first explicit non-Archimedean non-commutative ordered skew-field Ω(s, t) (with ts = 2st, Theorem 39) to build a 3D Desarguesian, non-Pascalian geometry (§ 34).
