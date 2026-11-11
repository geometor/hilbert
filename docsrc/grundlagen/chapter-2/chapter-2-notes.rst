:layout: book

.. _grundlagen-chapter-2-notes:

Chapter II: The Compatibility and Mutual Independence of the Axioms — Notes
===========================================================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Relative Consistency and the Arithmetic Foundation (`§ 9`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter II marks a watershed in mathematical logic: before 1899, consistency of non-Euclidean geometries (Beltrami, :person:`Klein <klein>`, :person:`Poincaré <poincare>`) was argued by modeling hyperbolic space *inside Euclidean geometry*. :person:`Hilbert <hilbert>` goes one level deeper in § 9 by modeling **Euclidean geometry itself** inside a countable algebraic subfield $\Omega \subset \mathbb{R}$:

$$\Omega = \mathbb{Q}\text{-closure under } \omega \mapsto \sqrt{1 + \omega^2}.$$

Two profound consequences emerge for the GEOMETOR ecosystem:

* **Exact Symbolic Algebra (`geometor/model` Resonance)**: Notice that :person:`Hilbert <hilbert>` does *not* need the uncountable Dedekind-Cantor real continuum $\mathbb{R}$ to satisfy Axioms `I–V` (prior to *Vollständigkeit*)! His minimal model $\Omega$ consists entirely of **exact symbolic algebraic radicals**—precisely the mathematical universe inhabited by `geometor/model` and SymPy!
* **Hoenen's Epistemological Observation (`Caput I § 6, fn. 14` & `Caput V § 4`)**: By reducing geometric compatibility to *"the arithmetic of the domain $\Omega$"*, § 9 confirms :person:`Hoenen <hoenen>`'s diagnosis that *Grundlagen der Geometrie* relies on the prior consistency and intuitive intelligibility of arithmetic; pushing the Consistency Problem one step further to arithmetic itself launched **Hilbert's Second Problem (1900)**—and eventually collided with Kurt Gödel's Second Incompleteness Theorem (1931).

2. Why Axiom IV 6 Cannot Be Proved (`§ 11` & Euclid `I.4`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare § 11 with :person:`Heath <heath>`'s commentary on `Euclid I.4` (Vol. I, pp. 249–250): for two thousand years geometers tried to *prove* SAS from linear segment equality and angle equality alone. :person:`Hilbert <hilbert>`'s § 11 model settles why every such attempt was doomed: the norm $\|(dx, dy, dz)\| = \sqrt{(dx + dy)^2 + dy^2 + dz^2}$ is a bona fide translation-invariant normed space (Minkowski/Banach norm whose unit ball in $z=0$ is the tilted ellipse $(x+y)^2 + y^2 = 1$), so segments add linearly along every line (`IV 3`) while Euclidean angle measure satisfies `IV 4–5`, yet rotation fails to preserve segment length! Hence without `IV 6`, linear congruence and angular congruence remain uncoupled.

3. Hilbert's Algebraic Non-Archimedean Field $\Omega(t)$ (`§ 12`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where :person:`Giuseppe Veronese <veronese>` (:cite:`Veronese 1891/1894 <veronese:1894>`) required hundreds of pages of intricate synthetic intuition to build a non-Archimedean continuum, :person:`Hilbert <hilbert>` constructs $\Omega(t)$ in two pages by letting $t$ be an indeterminate larger than every integer $n \in \mathbb{N}$, so $1/t$ acts as an exact algebraic **infinitesimal**. In Chapter IV (`§ 19`), this very field $\Omega(t)$ will separate *inhaltsgleich* from *flächengleich* triangles!

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 9, § 10, § 11, § 12** (:ref:`concordance-sec-09-12-metamathematics`): Constructs Hilbert's minimal countable Pythagorean field Ω (closed under +, −, ×, ÷, and √(1+ω²)) to prove relative consistency of Axioms I–V, and builds explicit analytic countermodels establishing the mutual independence of Parallels (III), SAS Congruence (IV 6), and Continuity (V).
  - :external+euclid:doc:`Euclid — Post. 5; I.4; V.Def.4 <heath/volume_I/book_i/postulates/commentary>`: Proves rigorously by analytic models that neither Euclid's Parallel Postulate (Post. 5), nor SAS Congruence (I.4 / IV 6), nor Archimedes's Principle (V.Def.4) can be deduced from the remaining axioms.
  - :external+hoenen:doc:`Hoenen — Caput I § 6 fn. 14; Caput V § 1.1 & § 4 <de_noetica_geometriae/caput-5/caput-5-en>`: Demonstrates Hoenen's thesis that Hilbert proves geometric non-contradiction only relative to the arithmetic of algebraic/real numbers Ω, leaving the consistency and intuition of number foundational.
