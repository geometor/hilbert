:layout: book

.. _grundlagen-chapter-4-notes:

Chapter IV: The Theory of Plane Areas — Notes
=============================================

.. rubric:: Historical, Philological & Cross-Repository Commentary

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Heath on Euclid `I.35` and Hilbert's Edition Shift (*flächengleich* → *zerlegungsgleich*)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``geometor/euclid`` (`volume_I/book_i/propositions/35/commentary.rst`, folio `0342`, :cite:`Heath 1908, Vol. I, p. 328 <heath:1908>`), :person:`T. L. Heath <heath>` devotes a special section to :person:`Hilbert <hilbert>`'s Chapter IV distinctions. Readers comparing the 1899 German *Festschrift*, :person:`Townsend <townsend>`'s 1902 English, and :person:`Heath <heath>`'s 1908 commentary should note an essential terminological evolution:

.. list-table:: Chapter IV Polygon Area Terminology Across Editions
   :header-rows: 1
   :widths: 28 24 24 24

   * - Mathematical Concept
     - 1899 Teubner (1st ed.)
     - 1902 Townsend (EN)
     - Later German eds. & Heath (1908)
   * - Dissectible into finitely many pairwise congruent triangles
     - :term:`flächengleich <flaechengleich>`
     - *equal area* / *equal by addition*
     - :term:`zerlegungsgleich <zerlegungsgleich>` (*equidecomposable*)
   * - Obtained by subtracting *flächengleich* pieces from *flächengleich* wholes
     - :term:`inhaltsgleich <inhaltsgleich>`
     - *equal content* (*of equal content*)
     - :term:`inhaltsgleich <inhaltsgleich>` / *ergänzungsgleich* (*equicomplementable*)

Why does `Euclid I.35` (*"Parallelograms which are on the same base and in the same parallels are equal to one another"*) work without Archimedes's Axiom only for *inhaltsgleich* and NOT for *flächengleich*? Look at `fig_polygon_equivalence.svg` (`§ 19`): when parallelogram $AB'C'D$ is sheared arbitrarily far to the right—say by the non-Archimedean distance $AF = t$ in $\Omega(t)$ while $AD = 1$—one can still *add* the single triangle $AED$ and *subtract* congruent trapezoids in **one step** (*inhaltsgleich*), whereas dissecting one triangle into congruent pieces to tile the sheared triangle would require $\ge t$ steps, which no finite integer $n$ can reach! With Archimedes's Axiom restored, :person:`Farkas Bolyai <bolyai-farkas>` and Paul Gerwien (1833) proved that *inhaltsgleich* and *zerlegungsgleich* coincide in the plane.

2. Proving Euclid's Common Notion 5 (*De Zolt's Postulate*, `§§ 19–21`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In § 19, :person:`Hilbert <hilbert>` quotes :person:`Euclid <euclid>`'s Greek text of Common Notion 5 verbatim:

    *„Καὶ τὸ ὅλον τοῦ μέρους μεῖζόν ἐστιν“* (*"And the whole is greater than the part"*)

pointing out that when Euclid invokes C.N. 5 in `I.39` to prove equal-area triangles on the same base have equal altitude (`Theorem 28`), it is *not* a purely logical truism—without a proof that polygonal area cannot remain unchanged when a piece is removed (:person:`Antonio De Zolt <de-zolt>`'s 1881 postulate, :cite:`De Zolt 1881 <de-zolt:1881>`), *every* polygon could trivially be *inhaltsgleich* to every other! By constructing the segment-valued area functional $F(P) \in \Omega_{\text{seg}}$ in § 20 via Chapter III's Pappus-based *Streckenrechnung* and proving triangulation invariance (`Theorem 29`), :person:`Hilbert <hilbert>` converts Euclid's Common Notion 5 into a **rigorous theorem (`Theorem 31`)**!

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Euclid–Hoenen–Hilbert–Pappus Master Concordance <concordance>` *for complete tables.)*

* **§ 18, § 19, § 20, § 21** (:ref:`concordance-sec-18-21-areas`): Reconstructs Euclid I.35–45 without Continuity by separating equidecomposability (flächengleich / zerlegungsgleich) from equicomplementability (inhaltsgleich), exhibits a non-Archimedean triangle pair in Ω(t) (§ 19) that is inhaltsgleich without being flächengleich, and defines additive triangle area via Chapter III's segment calculus to prove Common Notion 5 / De Zolt's Theorem (Theorem 31).
  - :external+euclid:doc:`Euclid — C.N. 2, C.N. 3, C.N. 5; Book I, Props. 35–45 <heath/volume_I/book_i/propositions/35/commentary>`: Heath (Vol. I, p. 328 on I.35) directly cites Hilbert's distinction between polygons equal by decomposition (1899 flächengleich / later zerlegungsgleich) and polygons of equal content by subtraction of congruent pieces (inhaltsgleich / ergänzungsgleich). Moreover, Hilbert proves Euclid's Common Notion 5 ('The whole is greater than the part' for polygon area, De Zolt's postulate) as Theorem 31 using segment-algebra area measures!
  - :external+hoenen:doc:`Hoenen — Caput IV (Exact Equality of Magnitude) <de_noetica_geometriae/caput-4/caput-4-en>`: Clarifies the axiomatic vs. intuitive basis of 'The whole is greater than the part' (C.N. 5) in polygonal dissection.
