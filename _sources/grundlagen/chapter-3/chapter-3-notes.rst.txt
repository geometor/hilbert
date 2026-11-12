:layout: book

.. _grundlagen-chapter-3-notes:

Chapter III: The Theory of Proportion — Notes
=============================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. The Pappus–Pascal Bridge (`geometor/pappus` ↔ `geometor/hilbert`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 14 is one of the crown jewels of the entire GEOMETOR workspace, uniting ``geometor/pappus``, ``geometor/euclid``, and ``geometor/hilbert``:

* **Terminological Clarification (*Pascalscher Satz* = Pappus's Hexagon Theorem)**: Following :person:`Hermann Wiener <wiener>` (:cite:`Wiener 1891 <wiener:1891>`) and :person:`Friedrich Schur <schur>` (:cite:`Schur 1898 <schur:1898>`), :person:`Hilbert <hilbert>` calls `Theorem 21` *"Pascal's Theorem"* (*der Pascalsche Satz*) because two intersecting straight lines form a degenerate conic section in :person:`Blaise Pascal <pascal>`'s 1640 mystic hexagram theorem. Historically, however, this exact theorem on two straight lines was discovered and proved 1,300 years earlier by **:person:`Pappus of Alexandria <pappus>`** in Book VII, Propositions 138–139 of his *Mathematical Collection* (:cite:`*Synagoge* <pappus:synagoge>`, modeled in ``geometor/pappus``!).
* **Affine Specialization**: In projective space (``geometor/pappus``), if $A, B, C$ and $A', B', C'$ lie on two lines, the three cross-join intersections $L = CB' \cap BC'$, $M = CA' \cap AC'$, and $N = BA' \cap AB'$ are collinear. Sending the line $LM$ to the line at infinity via the Parallel Axiom (`III`) yields Hilbert's affine `Theorem 21`:

  $$CB' \parallel BC' \;\land\; CA' \parallel AC' \implies BA' \parallel AB'.$$

* **Why Congruence Proves Pappus Without Continuity**: In `Euclid` Book V, :person:`Eudoxus <eudoxus>`'s proportion definition (`V.Def.5`) invokes arbitrary integer multiples $mA \gtreqless nB$, which tacitly presupposes `V.Def.4` (**Archimedes's Axiom**). :person:`Hilbert <hilbert>` bypasses Book V completely! Using only right-angle congruence and inscribed cyclic quadrilaterals (`Euclid III.21–22`, proved from `I–IV` at the end of § 7), he proves right-triangle projection operators commute ($\alpha\beta c \equiv \beta\alpha c$), which immediately forces `Theorem 21`, which in § 15 forces **commutativity of segment multiplication** $ab = ba$!

2. From *Streckenrechnung* to Book VI Similarity (`§§ 15–17`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Look at the sheer elegance of §§ 15–16:

1. :person:`René Descartes <descartes>` (*La Géométrie*, 1637) defined segment multiplication via Thales's parallel-line proportion—assuming proportion was already known from Book V!
2. :person:`Hilbert <hilbert>` reverses the logical arrow: he *defines* $c = ab$ geometrically by the parallel construction (`§ 15`), proves the field laws `(1–16)` directly from Pappus's Theorem (`Theorem 21`), *defines* proportion $a : b = a' : b'$ as $ab' = ba'$ (`§ 16`), and *deduces* general triangle similarity (`Theorem 22`, `Euclid VI.4`) via a stunning symmetric construction using the incenter $S$ (intersection of the three angle bisectors) and the distributive law!

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 13, § 14, § 15, § 16, § 17** (:ref:`concordance-sec-13-17-proportion`): Develops a purely geometric segment arithmetic (Streckenrechnung) from planar Axioms I–IV, proving Pappus's (Pascal's) Hexagon Theorem via cyclic-quadrilateral congruences to establish commutative multiplication ab = ba and Euclid's Book VI theory of similar triangles without Archimedes's Axiom.
  - :external+elements:doc:`Euclid — Book V (V.Def.4–5) & Book VI (VI.1–4) <elements2/index>`: Resolves a 2,200-year structural gulf in Euclid: whereas Book V–VI rests similarity on Eudoxus's Archimedean Definition V.Def.4–5, Hilbert constructs an exact geometric field of segments from planar Axioms I–IV alone, proving Thales's similarity theorem (VI.2 / Theorem 23) without Continuity.
  - :external+hoenen:doc:`Hoenen — Caput III–IV (Incommensurables & Exact Ratios) <de_noetica_geometriae/caput-4/caput-4-en>`: Illuminates the purely geometric vs. arithmetic nature of ratio and proportion without infinite limiting processes (Grenzprozesse).
  - :external+pappus:doc:`Pappus — Synagoge Book VII, Props. 138–139 (Pappus's Hexagon Theorem) <theorems/hexagon-theorem/index>`: Direct cornerstone bridge: Hilbert's 'Pascal's Theorem' (Theorem 21, § 14) IS Pappus's Hexagon Theorem for two intersecting lines with parallel opposite sides! Hilbert gives an ingenious cyclic-quadrilateral congruence proof of αβc ≡ βαc and uses it in § 15 to prove commutativity of segment multiplication ab = ba.
