"""Canonical structural metadata, figure placements, and scholarly Summary/Notes tracks."""

from __future__ import annotations

from typing import Any

UNITS: list[dict[str, Any]] = [
    {
        "slug": "introduction",
        "num_en": "Introduction",
        "num_de": "Einleitung",
        "title_en": "Preface & Introduction",
        "title_de": "Epigraph & Einleitung",
        "sections": [0],
    },
    {
        "slug": "chapter-1",
        "num_en": "Chapter I",
        "num_de": "Kapitel I",
        "title_en": "The Five Groups of Axioms",
        "title_de": "Die fünf Axiomgruppen",
        "sections": [1, 2, 3, 4, 5, 6, 7, 8],
    },
    {
        "slug": "chapter-2",
        "num_en": "Chapter II",
        "num_de": "Kapitel II",
        "title_en": "The Compatibility and Mutual Independence of the Axioms",
        "title_de": "Die Widerspruchslosigkeit und gegenseitige Unabhängigkeit der Axiome",
        "sections": [9, 10, 11, 12],
    },
    {
        "slug": "chapter-3",
        "num_en": "Chapter III",
        "num_de": "Kapitel III",
        "title_en": "The Theory of Proportion",
        "title_de": "Die Lehre von den Proportionen",
        "sections": [13, 14, 15, 16, 17],
    },
    {
        "slug": "chapter-4",
        "num_en": "Chapter IV",
        "num_de": "Kapitel IV",
        "title_en": "The Theory of Plane Areas",
        "title_de": "Die Lehre von den Flächeninhalten in der Ebene",
        "sections": [18, 19, 20, 21],
    },
    {
        "slug": "chapter-5",
        "num_en": "Chapter V",
        "num_de": "Kapitel V",
        "title_en": "Desargues's Theorem",
        "title_de": "Der Desarguessche Satz",
        "sections": [22, 23, 24, 25, 26, 27, 28, 29, 30],
    },
    {
        "slug": "chapter-6",
        "num_en": "Chapter VI",
        "num_de": "Kapitel VI",
        "title_en": "Pascal's Theorem",
        "title_de": "Der Pascalsche Satz",
        "sections": [31, 32, 33, 34, 35],
    },
    {
        "slug": "chapter-7",
        "num_en": "Chapter VII",
        "num_de": "Kapitel VII",
        "title_en": "Geometrical Constructions Based Upon Axioms I–V",
        "title_de": "Die geometrischen Konstruktionen auf Grund der Axiome I–V",
        "sections": [36, 37, 38, 39],
    },
    {
        "slug": "conclusion",
        "num_en": "Conclusion & Appendix",
        "num_de": "Schlusswort",
        "title_en": "Conclusion & Appendix on Transformation Groups",
        "title_de": "Schlusswort & Editionsanhang",
        "sections": [40],
    },
]

# Exact 1899 Teubner Festschrift & 1902 Open Court page numbers and titles for §§ 1-39
SECTIONS_META: dict[int, dict[str, Any]] = {
    0: {
        "title_en": "Introduction",
        "title_de": "Einleitung",
        "page_en": "1",
        "page_de": "3",
    },
    1: {
        "title_en": "§ 1. The Elements of Geometry and the Five Groups of Axioms",
        "title_de": "§ 1. Die Elemente der Geometrie und die fünf Axiomgruppen",
        "page_en": "3",
        "page_de": "4",
    },
    2: {
        "title_en": "§ 2. Group I: Axioms of Connection",
        "title_de": "§ 2. Die Axiomgruppe I: Axiome der Verknüpfung",
        "page_en": "4",
        "page_de": "5",
    },
    3: {
        "title_en": "§ 3. Group II: Axioms of Order",
        "title_de": "§ 3. Die Axiomgruppe II: Axiome der Anordnung",
        "page_en": "6",
        "page_de": "6",
        "figure": (
            "fig_betweenness_pasch.svg",
            "Linear Betweenness (II 1–4) and Pasch's Planar Separation Axiom (II 5)",
            "Linear order of collinear points A, B, C, D and Pasch's Axiom (II 5) with secant a piercing side AB at P and side AC at Q.",
        ),
    },
    4: {
        "title_en": "§ 4. Consequences of the Axioms of Connection and Order",
        "title_de": "§ 4. Folgerungen aus den Axiomen der Verknüpfung und der Anordnung",
        "page_en": "8",
        "page_de": "7",
    },
    5: {
        "title_en": "§ 5. Group III: Axiom of Parallels (Euclid's Axiom)",
        "title_de": "§ 5. Die Axiomgruppe III: Axiom der Parallelen (Euklidisches Axiom)",
        "page_en": "12",
        "page_de": "9",
    },
    6: {
        "title_en": "§ 6. Group IV: Axioms of Congruence",
        "title_de": "§ 6. Die Axiomgruppe IV: Axiome der Congruenz",
        "page_en": "13",
        "page_de": "10",
    },
    7: {
        "title_en": "§ 7. Consequences of the Axioms of Congruence",
        "title_de": "§ 7. Folgerungen aus den Axiomen der Congruenz",
        "page_en": "16",
        "page_de": "12",
        "figure": (
            "fig_sas_supplementary.svg",
            "Hilbert's SAS Reductio (Theorem 10) and Supplementary Angle Congruence (Theorem 12)",
            "Eliminating Euclidean superposition: SAS congruence (Theorem 10) via Axiom IV 6 and supplementary angles (Theorem 12; cf. Heath on Euclid C.N. 4, folios 0243–0244).",
        ),
    },
    8: {
        "title_en": "§ 8. Group V: Axiom of Continuity (Archimedes's Axiom)",
        "title_de": "§ 8. Die Axiomgruppe V: Axiom der Stetigkeit (Archimedisches Axiom)",
        "page_en": "24",
        "page_de": "19",
    },
    9: {
        "title_en": "§ 9. Compatibility of the Axioms",
        "title_de": "§ 9. Die Widerspruchslosigkeit der Axiome",
        "page_en": "27",
        "page_de": "19",
    },
    10: {
        "title_en": "§ 10. Independence of the Axiom of Parallels (Non-Euclidean Geometry)",
        "title_de": "§ 10. Die Unabhängigkeit des Parallelenaxioms (Nicht-Euklidische Geometrie)",
        "page_en": "30",
        "page_de": "21",
    },
    11: {
        "title_en": "§ 11. Independence of the Axioms of Congruence",
        "title_de": "§ 11. Die Unabhängigkeit der Congruenzaxiome",
        "page_en": "32",
        "page_de": "23",
        "figure": (
            "fig_non_congruence_model.svg",
            "Anisotropic Countermodel to Congruence Axiom IV 6 (§ 11)",
            "Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).",
        ),
    },
    12: {
        "title_en": "§ 12. Independence of the Axiom of Continuity (Non-Archimedean Geometry)",
        "title_de": "§ 12. Die Unabhängigkeit des Stetigkeitsaxioms V (Nicht-Archimedische Geometrie)",
        "page_en": "34",
        "page_de": "24",
    },
    13: {
        "title_en": "§ 13. Complex Number-Systems",
        "title_de": "§ 13. Complexe Zahlensysteme",
        "page_en": "37",
        "page_de": "26",
    },
    14: {
        "title_en": "§ 14. Demonstration of Pascal's Theorem",
        "title_de": "§ 14. Beweis des Pascalschen Satzes",
        "page_en": "40",
        "page_de": "28",
        "figure": (
            "fig_pascal_orthogonal.svg",
            "Affine Pascal's (Pappus's) Hexagon Theorem (Theorem 21)",
            "Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.",
        ),
    },
    15: {
        "title_en": "§ 15. An Algebra of Segments, Based Upon Pascal's Theorem",
        "title_de": "§ 15. Die Streckenrechnung auf Grund des Pascalschen Satzes",
        "page_en": "46",
        "page_de": "32",
        "figure": (
            "fig_segment_multiplication.svg",
            "Hilbert's Segment Multiplication c = ab and Commutativity ab = ba (§ 15)",
            "Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.",
        ),
        "figure_extra": (
            "fig_segment_distributive.svg",
            "Geometric Proof of the Distributive Law a(b + c) = ab + ac (§ 15)",
            "Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.",
        ),
    },
    16: {
        "title_en": "§ 16. Proportion and the Theorems of Similitude",
        "title_de": "§ 16. Die Proportionen und die Aehnlichkeitssätze",
        "page_en": "50",
        "page_de": "35",
    },
    17: {
        "title_en": "§ 17. Equations of Straight Lines and of Planes",
        "title_de": "§ 17. Die Gleichungen der Geraden und Ebenen",
        "page_en": "53",
        "page_de": "37",
    },
    18: {
        "title_en": "§ 18. Equal Area and Equal Content of Polygons",
        "title_de": "§ 18. Die Flächengleichheit und Inhaltsgleichheit von Polygonen",
        "page_en": "57",
        "page_de": "40",
    },
    19: {
        "title_en": "§ 19. Parallelograms and Triangles Having Equal Bases and Equal Altitudes",
        "title_de": "§ 19. Parallelogramme und Dreiecke mit gleicher Grundlinie und Höhe",
        "page_en": "60",
        "page_de": "41",
        "figure": (
            "fig_polygon_equivalence.svg",
            "Equicomplementability (Inhaltsgleichheit) of Parallelograms on Equal Base (§ 19)",
            "Euclid I.35 reconstructed in § 19: parallelograms ABCD and AB'C'D are inhaltsgleich unconditionally, though flächengleich (zerlegungsgleich) requires Archimedes.",
        ),
    },
    20: {
        "title_en": "§ 20. The Measure of Area of Triangles and Polygons",
        "title_de": "§ 20. Das Flächenmass von Dreiecken und Polygonen",
        "page_en": "63",
        "page_de": "43",
    },
    21: {
        "title_en": "§ 21. Equality of Content and the Measure of Area",
        "title_de": "§ 21. Die Inhaltsgleichheit und das Flächenmass",
        "page_en": "67",
        "page_de": "46",
    },
    22: {
        "title_en": "§ 22. Desargues's Theorem and Its Demonstration for Plane Geometry by Aid of the Axioms of Congruence",
        "title_de": "§ 22. Der Desarguessche Satz und der Beweis desselben in der Ebene mit Hülfe der Congruenzaxiome",
        "page_en": "71",
        "page_de": "49",
        "figure": (
            "fig_desargues_configuration.svg",
            "Affine Desargues Configuration of Perspective Triangles (Theorem 32)",
            "Theorem 32: triangles ABC and A'B'C' perspective from O with AB ∥ A'B' and BC ∥ B'C' satisfy AC ∥ A'C'.",
        ),
    },
    23: {
        "title_en": "§ 23. The Impossibility of Demonstrating Desargues's Theorem for the Plane Without the Help of the Axioms of Congruence",
        "title_de": "§ 23. Die Nichtbeweisbarkeit des Desarguesschen Satzes in der Ebene ohne Hülfe der Congruenzaxiome",
        "page_en": "74",
        "page_de": "51",
        "figure": (
            "fig_non_desarguesian_plane.svg",
            "Hilbert's 1899 Non-Desarguesian Plane via Ellipse Arc Refraction (§ 23)",
            "Theorem 33: Euclidean lines cutting the ellipse are replaced inside the boundary by circular arcs through F, satisfying planar I 1–2, II, III, IV 1–5, V while violating Desargues.",
        ),
    },
    24: {
        "title_en": "§ 24. Introduction of an Algebra of Segments Based Upon Desargues's Theorem and Independent of the Axioms of Congruence",
        "title_de": "§ 24. Einführung einer Streckenrechnung ohne Hülfe der Congruenzaxiome auf Grund des Desarguesschen Satzes",
        "page_en": "79",
        "page_de": "55",
    },
    25: {
        "title_en": "§ 25. The Commutative and the Associative Law of Addition for Our New Algebra of Segments",
        "title_de": "§ 25. Das commutative und associative Gesetz der Addition in der neuen Streckenrechnung",
        "page_en": "82",
        "page_de": "57",
        "figure": (
            "fig_desargues_segment_algebra.svg",
            "Projective-Affine Segment Addition and Skew-Field Multiplication (§§ 24–26)",
            "Constructing c = a + b and c = ab on fixed axes OX, OY with unit line EE' purely from incidence, parallels, and Desargues's Theorem without Congruence.",
        ),
    },
    26: {
        "title_en": "§ 26. The Associative Law of Multiplication and the Two Distributive Laws for the New Algebra of Segments",
        "title_de": "§ 26. Das associative Gesetz der Multiplikation und die beiden distributiven Gesetze in der neuen Streckenrechnung",
        "page_en": "84",
        "page_de": "59",
    },
    27: {
        "title_en": "§ 27. Equation of the Straight Line, Based Upon the New Algebra of Segments",
        "title_de": "§ 27. Die Gleichung der Geraden auf Grund der neuen Streckenrechnung",
        "page_en": "90",
        "page_de": "63",
    },
    28: {
        "title_en": "§ 28. The Totality of Segments Regarded as a Complex Number System",
        "title_de": "§ 28. Der Inbegriff der Strecken aufgefasst als complexes Zahlensystem",
        "page_en": "95",
        "page_de": "66",
    },
    29: {
        "title_en": "§ 29. Construction of a Geometry of Space by Aid of a Desarguesian Number System",
        "title_de": "§ 29. Aufbau einer räumlichen Geometrie mit Hülfe eines Desarguesschen Zahlensystems",
        "page_en": "97",
        "page_de": "67",
    },
    30: {
        "title_en": "§ 30. Significance of Desargues's Theorem",
        "title_de": "§ 30. Die Bedeutung des Desarguesschen Satzes",
        "page_en": "101",
        "page_de": "70",
    },
    31: {
        "title_en": "§ 31. Two Theorems Concerning the Possibility of Proving Pascal's Theorem",
        "title_de": "§ 31. Zwei Sätze über die Beweisbarkeit des Pascalschen Satzes",
        "page_en": "103",
        "page_de": "71",
    },
    32: {
        "title_en": "§ 32. The Commutative Law of Multiplication for an Archimedean Number System",
        "title_de": "§ 32. Das commutative Gesetz der Multiplikation im Archimedischen Zahlensystem",
        "page_en": "105",
        "page_de": "72",
    },
    33: {
        "title_en": "§ 33. The Commutative Law of Multiplication for a Non-Archimedean Number System",
        "title_de": "§ 33. Das commutative Gesetz der Multiplikation im Nicht-Archimedischen Zahlensystem",
        "page_en": "107",
        "page_de": "73",
    },
    34: {
        "title_en": "§ 34. Proof of the Two Propositions Concerning Pascal's Theorem (Non-Pascalian Geometry)",
        "title_de": "§ 34. Beweis der beiden Sätze über den Pascalschen Satz (Nicht-Pascalsche Geometrie)",
        "page_en": "110",
        "page_de": "75",
    },
    35: {
        "title_en": "§ 35. The Demonstration, by Means of the Theorems of Pascal and Desargues, of Any Theorem Relating to Points of Intersection",
        "title_de": "§ 35. Beweis eines beliebigen Schnittpunktsatzes mittelst des Desarguesschen und des Pascalschen Satzes",
        "page_en": "112",
        "page_de": "76",
    },
    36: {
        "title_en": "§ 36. Geometrical Constructions by Means of a Straight-Edge and a Transferer of Segments",
        "title_de": "§ 36. Die geometrischen Konstruktionen mittelst Lineals und Streckenübertragers",
        "page_en": "115",
        "page_de": "78",
        "figure": (
            "fig_gauge_constructions.svg",
            "Orthocenter Perpendicular Construction with Straightedge and Segment-Transferer (§ 36)",
            "Dropping a perpendicular from P to line AB using only a straightedge and Streckenübertrager (Eichmass) via Thales's semicircle right angles at C and D and orthocenter H.",
        ),
    },
    37: {
        "title_en": "§ 37. Analytical Representation of the Co-ordinates of Points Which Can Be So Constructed",
        "title_de": "§ 37. Analytische Darstellung der Coordinaten konstruirbarer Punkte",
        "page_en": "119",
        "page_de": "80",
    },
    38: {
        "title_en": "§ 38. The Representation of Algebraic Numbers and of Integral Rational Functions as Sums of Squares",
        "title_de": "§ 38. Die Darstellung algebraischer Zahlen und ganzer rationaler Funktionen als Summe von Quadraten",
        "page_en": "122",
        "page_de": "82",
    },
    39: {
        "title_en": "§ 39. Criterion for the Possibility of a Geometrical Construction by Means of a Straight-Edge and a Transferer of Segments",
        "title_de": "§ 39. Kriterium für die Ausführbarkeit geometrischer Konstruktionen mittelst Lineals und Streckenübertragers",
        "page_en": "126",
        "page_de": "85",
    },
    40: {
        "title_en": "Conclusion & Appendix",
        "title_de": "Schlusswort",
        "page_en": "130",
        "page_de": "89",
    },
}

SUMMARIES: dict[str, str] = {
    "introduction": """
Executive Overview
------------------

:person:`David Hilbert <hilbert>`'s *Grundlagen der Geometrie* (*The Foundations of Geometry*, June 1899; authorized English translation by :person:`E. J. Townsend <townsend>`, 1902) opens with a celebrated epigraph from :person:`Immanuel Kant <kant>`'s :cite:`*Kritik der reinen Vernunft* <kant:1781>` (*A 702 / B 730*):

    *"All human knowledge begins with intuitions, thence passes to concepts and ends with ideas."*

    *(„So fängt denn alle menschliche Erkenntnis mit Anschauungen an, geht von da zu Begriffen und endigt mit Ideen.“)*

In two concise paragraphs, :person:`Hilbert <hilbert>` formulates the charter of modern axiomatics:

1. **Logical Analysis of Spatial Intuition**: Just as arithmetic rests on a small number of fundamental principles, geometry requires a rigorous logical analysis of our :term:`spatial intuition <anschauung>`—a problem pursued from :person:`Euclid <euclid>` down to :person:`Moritz Pasch <pasch>`, :person:`Giuseppe Veronese <veronese>`, and :person:`Felix Klein <klein>`.
2. **Simplicity, Completeness, and Mutual Independence**: Rather than treating axioms merely as self-evident starting points, :person:`Hilbert <hilbert>` demands a *simple* and *complete* set of *mutually independent* (:term:`unabhängig <unabhaengigkeit>`) axioms partitioned into five natural groups.
3. **Architectural Scope of Individual Axiom Groups**: Each major theorem of elementary and projective geometry must be traced to the *minimal* subset of axiom groups required for its proof—anticipating the concluding maxim of :term:`purity of method <reinheit-der-methode>`.

Townsend's 1902 Preface
-----------------------

In the English edition, :person:`Townsend <townsend>` situates the treatise historically: delivered first as a winter-semester lecture course at Göttingen (1898–1899, autographed by :person:`Hans von Schaper <schaper>`), rearranged for the June 1899 unveiling of the :person:`Gauss <gauss>`–:person:`Weber <weber>` Monument in Göttingen, and expanded in :person:`Léonce Laugel <laugel>`'s 1900 French edition with the :term:`Axiom of Completeness <vollstaendigkeit>` and :person:`Max Dehn <dehn>`'s polyhedral researches.
""",
    "chapter-1": """
Architectural Summary of Chapter I (§§ 1–8)
-------------------------------------------

Chapter I constructs the complete deductive foundation of three-dimensional Euclidean space across eight sections and **twenty foundational theorems (Theorems 1–20)**:

* **§ 1 — Primitive Systems**: Replaces :person:`Euclid <euclid>`'s descriptive definitions of point, line, and plane (`I.Def.1, 4, 7`) with three unspecified systems of things bound solely by mutual relations across five axiom groups.
* **§ 2 — Group I: Connection (I 1–7, Theorems 1–2)**: Separates *planar* incidence (`I 1–2`: existence and uniqueness of the straight line joining two distinct points) from *spatial* incidence (`I 3–7`: plane determination by three non-collinear points, line-in-plane containment, two-plane intersection dimension, and existence of four non-coplanar points). Deduces unique intersection properties (`Theorem 1`) and plane determination by a line and external point or two intersecting lines (`Theorem 2`).
* **§ 3 — Group II: Order (II 1–5)**: Axiomatizes the ternary collinear relation :term:`between <zwischen>` (`II 1–4`), defines the :term:`segment <strecke>` $AB$, and introduces :person:`Moritz Pasch <pasch>`'s planar triangle-piercing postulate (`II 5`, :term:`Axiom von Pasch <pasch-axiom>`).
* **§ 4 — Consequences of Order (Theorems 3–7)**: Proves unlimited linear density (`Theorem 3`), total ordering of any finite collinear point set $A, B, C, D, E, \\ldots, K$ (`Theorem 4`), planar half-plane separation (`Theorem 5`), :term:`half-rays <halbstrahl>`, :person:`Camille Jordan <jordan>`'s polygonal separation theorem (`Theorem 6`), and spatial half-space separation (`Theorem 7`) without needing any spatial order axiom.
* **§ 5 — Group III: Parallels (Axiom III, Theorem 8)**: Adopts Playfair's uniqueness form of :person:`Euclid <euclid>`'s Fifth Postulate in a plane $\\alpha$ and proves transitivity of non-intersection (`Theorem 8`). *(Note: renumbered Group IV in later editions.)*
* **§ 6 — Group IV: Congruence (IV 1–6)**: Eliminates physical motion and superposition (:term:`ἐφαρμόζειν <epharmozein>`) via six static axioms: segment transfer (`IV 1`), congruence transitivity (`IV 2`), segment additivity (`IV 3`), angle transfer (`IV 4`), angle transitivity (`IV 5`), and the triangle bridge axiom (`IV 6`) deriving base-angle congruence from two congruent sides and the included angle. *(Note: renumbered Group III in later editions.)*
* **§ 7 — Consequences of Congruence (Theorems 9–20)**: Proves congruent point-series order preservation (`Theorem 9`), SAS triangle congruence (`Theorem 10`, `Euclid I.4`), ASA congruence (`Theorem 11`), supplementary angle congruence (`Theorem 12`, `Euclid I.13`), interior/exterior angle ray decomposition (`Theorems 13–14`), **congruence of all right angles** (`Theorem 15`, proving `Euclid Postulate 4`!), SSS congruence (`Theorem 16`, `Euclid I.8`), rigid figure extension in the plane and 3-space (`Theorems 17–18`), alternate/interior angle parallelism (`Theorem 19`), and the $180^\\circ$ triangle angle-sum theorem (`Theorem 20`).
* **§ 8 — Group V: Continuity**: Formulates the linear :term:`Axiom of Archimedes <archimedisches-axiom>` (`V`) and—in the 1900/1902 *Remark*—the metamathematical :term:`Axiom of Completeness <vollstaendigkeit>` (*Vollständigkeit*, later `V 2`).
""",
    "chapter-2": """
Architectural Summary of Chapter II (§§ 9–12)
---------------------------------------------

Having erected the five axiom groups in Chapter I, :person:`Hilbert <hilbert>` inaugurates **model-theoretic metamathematics** in Chapter II, establishing both :term:`compatibility <widerspruchslosigkeit>` (*Widerspruchslosigkeit*) and mutual :term:`independence <unabhaengigkeit>` (*Unabhängigkeit*) through four explicit analytic coordinate models:

* **§ 9 — Relative Consistency via the Pythagorean Field $\\Omega$**: Constructs the countable algebraic number domain $\\Omega \\subset \\mathbb{R}$ generated from $1$ by finite applications of $+, -, \\times, \\div$ and the fifth operation $\\sqrt{1 + \\omega^2}$. Defining points as $(x, y) \\in \\Omega^2$, lines as homogeneous ratios $(u : v : w)$, order via algebraic inequalities, and displacements via rational/Pythagorean orthogonal rotations, :person:`Hilbert <hilbert>` proves that every contradiction deducible from Axioms `I–V` would already appear in the arithmetic of $\\Omega$.
* **§ 10 — Independence of the Parallel Axiom III**: Proves first that existence of parallels follows from `I, II, IV` alone (via alternate angles, `Euclid I.27`), and then restricts the $\\Omega$-space of § 9 to the interior of a fixed sphere equipped with projective Cayley–:person:`Klein <klein>` collineations preserving the sphere, yielding a consistent :person:`Bolyai <bolyai>`–:person:`Lobachevsky <lobachevsky>` hyperbolic geometry in which `I, II, IV, V` hold while `III` fails.
* **§ 11 — Independence of Congruence Axiom IV 6 (SAS)**: Retains ordinary points, lines, planes, and angles, but redefines segment length between $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$ by the anisotropic norm

  $$\\sqrt{(x_1 - x_2 + y_1 - y_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}.$$

  Linear parameter proportionality preserves segment additivity (`IV 3`), so `I, II, III, IV 1–5, V` all hold, yet right triangles $OAC$ and $OBC$ with $O(0,0), A(1,0), B(0,1), C(\\tfrac{1}{2}, \\tfrac{1}{2})$ share $\\angle C$, $OC$, and $AC = BC = \\tfrac{1}{\\sqrt{2}}$ while $OA = 1 \\neq \\sqrt{2} = OB$, falsifying SAS (`Theorem 10` and `IV 6`).
* **§ 12 — Independence of Archimedes's Axiom V**: Replaces numbers by the countable field $\\Omega(t)$ of real algebraic functions of a parameter $t$ generated by $+, -, \\times, \\div$ and $\\sqrt{1 + \\omega^2}$, ordered by sign for sufficiently large $t > 0$. Since $n - t < 0$ for every positive integer $n$ as $t \\to +\\infty$, the segment $1$ laid off $n$ times never reaches $t$, establishing a consistent :term:`non-Archimedean geometry <nicht-archimedische-geometrie>` satisfying `I–IV` while violating `V`.
""",
    "chapter-3": """
Architectural Summary of Chapter III (§§ 13–17)
-----------------------------------------------

Chapter III resolves one of the deepest structural problems in the history of geometry: reconstructing :person:`Euclid <euclid>`'s Book V–VI theory of proportion and similar triangles **purely in the plane (`I 1–2, II–IV`) without the Axiom of Archimedes (`V`)**:

* **§ 13 — Complex Number Systems**: Catalogues 17 algebraic axioms (`1–12` field laws, `13–16` ordered ring laws, `17` Archimedean property), framing the central question of geometric algebra: which geometric axioms correspond to which algebraic field laws?
* **§ 14 — Proof of Pascal's (Pappus's) Theorem (Theorem 21)**: States the affine two-line specialization of :person:`Pascal <pascal>`'s hexagram—historically :person:`Pappus <pappus>`'s Hexagon Theorem (:cite:`*Synagoge* VII.138–139 <pappus:synagoge>`): if $A, B, C$ and $A', B', C'$ lie on two intersecting lines through $O$ with $CB' \\parallel BC'$ and $CA' \\parallel AC'$, then $BA' \\parallel AB'$. Using right-triangle projection operators $a = \\alpha c$ and inscribed cyclic quadrilaterals ($ABCD$ on a diameter circle), :person:`Hilbert <hilbert>` proves operator commutativity $\\alpha\\beta c \\equiv \\beta\\alpha c$ and deduces `Theorem 21` (adding a second direct four-circle proof).
* **§ 15 — Geometric Calculus of Segments (*Streckenrechnung*)**: Defines segment addition $c = a + b$ by collinear juxtaposition and segment multiplication $c = ab$ on perpendicular rays from $O$ via a fixed unit segment $1$ and parallel lines. Crucially, `Theorem 21` (:term:`Pascalscher Satz <pascalscher-satz>`) immediately yields **commutativity** $ab = ba$ and **associativity** $a(bc) = (ab)c$, while congruent right triangles establish **distributivity** $a(b + c) = ab + ac$.
* **§ 16 — Proportion and Similitude (Theorems 22–23)**: Defines $a : b = a' : b'$ algebraically as $ab' = ba'$, proves proportionality of corresponding sides in similar triangles (`Theorem 22`, first for right triangles and then generally via the incenter $S$ of the three angle bisectors!), and deduces the Fundamental Theorem of Proportion (`Theorem 23`, Thales's intercept theorem `Euclid VI.2`).
* **§ 17 — Linear Equations of Lines and Planes**: Extends positive segments to signed segments ($+, 0, -$) forming an ordered commutative field, establishes rectangular coordinates $(x, y)$, proves every straight line has a linear equation $bx - ay - bc = 0$, and shows how adjoining Archimedes (`V`) embeds the coordinate domain into $\\mathbb{R}^3$.
""",
    "chapter-4": """
Architectural Summary of Chapter IV (§§ 18–21)
----------------------------------------------

Building directly upon Chapter III's non-Archimedean :term:`Streckenrechnung <streckenrechnung>`, Chapter IV reconstructs :person:`Euclid <euclid>`'s Book I (`I.35–45`) theory of polygonal area in the plane **solely from planar Axioms `I 1–2, II–IV` without Continuity (`V`)**:

* **§ 18 — Equidecomposability vs. Equicomplementability (Theorem 24)**: Introduces the decisive distinction between two polygons being :term:`flächengleich <flaechengleich>` (1899 term; renamed :term:`zerlegungsgleich <zerlegungsgleich>` in later editions; Townsend: *"equal by addition"* / equidecomposable into pairwise congruent triangles) versus :term:`inhaltsgleich <inhaltsgleich>` (Townsend: *"of equal content"* / equicomplementable by adjoining equidecomposable pieces). Proves transitivity of both relations by common subdivision (`Theorem 24`).
* **§ 19 — Parallelograms and Triangles (Theorems 25–28)**: Reproduces :person:`Euclid <euclid>`'s `I.35–38` trapezoid-subtraction argument to prove that parallelograms and triangles on equal bases with equal altitudes are always *inhaltsgleich* (`Theorems 25–27`), but exhibits a dramatic counterexample in $\\Omega(t)$ (`§ 12`): two triangles of base $1$ and altitude $1$ whose apex projection is offset by the non-Archimedean element $t$ are *inhaltsgleich* yet **cannot be dissected into congruent triangles** (*not flächengleich*)! Formulates the converse (`Theorem 28`, `Euclid I.39`) and notes that Euclid relied on Common Notion 5 (*„Καὶ τὸ ὅλον τοῦ μέρους μεῖζόν ἐστιν“*) as an unproved area axiom.
* **§ 20 — Measure of Area (*Flächenmass*, Theorem 29)**: Defines the area measure $F(\\Delta) = \\tfrac{1}{2} a h_a = \\tfrac{1}{2} b h_b$ in the segment field via `Theorem 22`, proves invariance of $F(\\Delta)$ under arbitrary simplicial subdivision by reducing any triangulation to chains of transversal splits (`Theorem 29`), and deduces that *inhaltsgleich* polygons have equal area measure—immediately proving `Theorem 28`.
* **§ 21 — Converse Equivalence and De Zolt's Postulate (Theorems 30–31)**: Proves conversely that any two polygons with equal segment-valued area measure are *inhaltsgleich* (`Theorem 30`), and deduces :person:`Antonio De Zolt <de-zolt>`'s postulate / `Euclid C.N. 5` (`Theorem 31`): if a rectangle is dissected into triangles and even a single triangle is omitted, the remaining triangles can never refill the rectangle!
""",
    "chapter-5": """
Architectural Summary of Chapter V (§§ 22–30)
---------------------------------------------

Chapters V and VI pivot from metric Euclidean geometry to projective-affine foundations, investigating what happens when **Congruence (`IV`) is dropped altogether**:

* **§ 22 — Desargues's Theorem (Theorem 32)**: Formulates the affine :term:`Desargues's Theorem <desarguesscher-satz>` (`Theorem 32`) for perspective triangles with parallel sides, observing that it follows effortlessly either from 3D spatial incidence (`I 1–7, II, III`) or from 2D planar congruence (`I 1–2, II–IV` via Chapter III coordinates).
* **§ 23 — Hilbert's Non-Desarguesian Plane (Theorem 33)**: Constructs a celebrated planar countermodel inside the Euclidean $XY$-plane: straight lines cutting the ellipse $x^2 + 4y^2 = 1$ have their interior chord replaced by the circular arc passing through the two boundary intersections $P, Q$ and the exterior point $F(\\tfrac{3}{2}, 0)$ (since $\\tfrac{3}{2} > \\tfrac{\\sqrt{7}}{2}$, no circle meeting the ellipse four times can pass through $F$). This deformed plane satisfies **all planar axioms `I 1–2, II, III, IV 1–5, V`** while violating Desargues's Theorem—proving planar Desargues unprovable without either 3D spatial incidence (`I 3–7`) or triangle congruence (`IV 6`)!
* **§§ 24–26 — Congruence-Free Segment Calculus**: Fixes two intersecting axes $OE, OE'$ and a unit line $EE'$ in any plane satisfying `I 1–2, II, III` + Desargues (`Theorem 32`), defining addition $c = a + b$ and multiplication $c = ab$ purely by parallel projections. Using intricate multi-triangle Desargues configurations (Figures 41–45, drafted with :person:`Hans von Schaper <schaper>`), :person:`Hilbert <hilbert>` proves commutative and associative addition (`§ 25`), associative multiplication $a(bc) = (ab)c$, and both left and right distributive laws (`§ 26`)—**all without Congruence**!
* **§§ 27–30 — Skew-Field Coordinatization and 3D Embeddability (Theorems 34–35)**: Proves every line has a *left*-linear equation $ax + by + c = 0$ (`Theorem 34`, whereas $xa + yb + c = 0$ need not be a line when multiplication is non-commutative!), shows the segments form an ordered associative division ring (:term:`Desarguessches Zahlensystem <desarguessches-zahlensystem>`, rules `1–11, 13–16` of § 13), reconstructs 3D space over any Desarguesian division ring (`§ 29`), and crowns the chapter with `Theorem 35`: Desargues's Theorem is the **necessary and sufficient condition** for a planar geometry (`I 1–2, II, III`) to be embeddable as a plane inside a 3D space (`I, II, III`).
""",
    "chapter-6": """
Architectural Summary of Chapter VI (§§ 31–35)
----------------------------------------------

Chapter VI brings the projective-algebraic hierarchy to its climax by isolating the exact axiomatic and algebraic meaning of :term:`Pascal's (Pappus's) Theorem <pascalscher-satz>` when **Congruence (`IV`) is omitted**:

* **§ 31 — Two Fundamental Theorems on Pappus/Pascal (Theorems 36–37)**: Announces two complementary results in 3D space without Congruence:
  1. `Theorem 36`: Pappus/Pascal **is provable** from `I, II, III, V` (i.e., with Archimedes's Axiom, even without Congruence!).
  2. `Theorem 37`: Pappus/Pascal **is unprovable** from `I, II, III` alone (when both Congruence `IV` and Archimedes `V` are dropped).
* **§ 32 — Hilbert's Commutativity Theorem for Archimedean Skew-Fields (Theorem 38)**: Proves a landmark theorem of pure algebra: **every Archimedean ordered division ring is necessarily commutative**! Assuming $a > 0, b > 0$, and $ab - ba > 0$, :person:`Hilbert <hilbert>` traps $a$ and $b$ between consecutive multiples $md < a < (m+1)d$ and $nd < b < (n+1)d$ using Archimedes's Axiom (`17`) and shows $ab - ba < (m + n + 1)d^2 < (a + b + 1)c = ab - ba$, an outright contradiction!
* **§ 33 — Hilbert's Non-Commutative Twist Laurent Skew-Field $\\Omega(s, t)$ (Theorem 39)**: Constructs the first explicit example in mathematics of an ordered non-Archimedean skew-field (`Theorem 39`): formal Laurent series $S = s^m T_0 + s^{m+1} T_1 + \\cdots$ whose coefficients $T_k = r_0 t^n + r_1 t^{n+1} + \\cdots$ are formal Laurent series in $t$ over $\\mathbb{Q}$, governed by the non-commutative twist relation

  $$ts = 2st,$$

  and ordered lexicographically by the leading rational coefficient $r_0$ of $T_0$.
* **§§ 34–35 — Non-Pascalian Geometry and Intersection Completeness**: Building 3-space over $\\Omega(s, t)$ via § 29 immediately proves `Theorem 37`, exhibiting a consistent 3D :term:`Non-Pascalian Geometry <nicht-pascalsche-geometrie>` (which by `Theorem 36` is necessarily non-Archimedean). Conversely, § 35 proves that every planar incidence/intersection theorem holding under `I–V` reduces synthetically to a finite combination of Desargues's and Pascal's (Pappus's) theorems without needing Congruence!
""",
    "chapter-7": """
Architectural Summary of Chapter VII (§§ 36–39)
-----------------------------------------------

In the final chapter, :person:`Hilbert <hilbert>` returns to :person:`Euclid <euclid>`'s constructive postulates (`Postulates 1–3`), asking precisely which geometric construction problems solvable by straightedge and compass can already be executed using only Axioms `I–V`—implemented physically by a **straightedge** (*Lineal*) and a **transferer of segments** (:term:`Streckenübertrager <streckenuebertrager>`, specialized in later editions to the fixed-unit gauge :term:`Eichmass <eichmass>`):

* **§ 36 — Elementary Constructions Without Full Circles (Theorem 40)**: Reduces the five fundamental planar constructions—joining points/intersecting lines (`Problem 1`), drawing parallels (`Problem 2`), transferring segments (`Problem 3`), transferring angles (`Problem 4`), and dropping perpendiculars (`Problem 5`, solved via semicircle chords and the triangle orthocenter!)—to `Problems 1` and `3` alone (`Theorem 40`).
* **§ 37 — Pythagorean Radical Criterion (Theorem 41)**: Proves that a construction problem is solvable by straightedge and segment-transferer if and only if the coordinates of the sought points belong to the domain $\\Omega(R)$ generated from the given coordinates $R$ by $+, -, \\times, \\div$ and $\\sqrt{\\alpha^2 + \\beta^2}$ (`Theorem 41`). Exhibits an explicit compass-constructible right triangle (hypotenuse $1$, leg $|\\sqrt{2}| - 1$, second leg $\\sqrt{2|\\sqrt{2}| - 2}$) **impossible** with straightedge and segment-transferer because its conjugate $\\sqrt{-2|\\sqrt{2}| - 2}$ is imaginary, whereas every number in $\\Omega$ is totally real!
* **§ 38 — Totally Positive Numbers and Sums of Squares (Theorems 42–43)**: Generalizes :person:`Lagrange <lagrange>`'s / Fermat's four-square theorem to algebraic number fields via relative quadratic field theory: every :term:`totally positive <total-positiv>` element of a number field $k$ is a sum of four squares in $k$ (`Theorem 42`), and every positive-definite univariate polynomial $f(x) \\in \\mathbb{Q}[x]$ is a quotient of two sums of squares of polynomials in $\\mathbb{Q}[x]$ (`Theorem 43`—the direct progenitor of **Hilbert's Seventeenth Problem**, 1900!).
* **§ 39 — Geometric Multiplicity Criterion (Theorem 44)**: Combines `Theorems 41–43` to establish a purely geometric necessary and sufficient criterion (`Theorem 44`, proved for 1-parameter problems): a ruler-and-compass problem requiring $n$ minimal square roots is solvable by straightedge and segment-transferer if and only if it possesses **exactly $2^n$ real solutions** for all real parameter positions of the given points! Concludes that all Gauss-constructible regular polygons and Malfatti's problem are solvable with straightedge and segment-transferer, whereas Apollonius's circle-tangency problem is not.
""",
    "conclusion": """
Architectural Summary of the Conclusion & Appendix
--------------------------------------------------

* **Purity of Method (*Reinheit der Methode*)**: In the *Schlusswort* (*Conclusion*), :person:`Hilbert <hilbert>` distills the philosophical moral of the entire treatise: mathematics is satisfied only when either a rigorous proof is achieved or **the reason for the impossibility of a proof under prescribed means** is demonstrated—linking geometric independence proofs directly to Abel's quintic impossibility theorem and Hermite–Lindemann's transcendence of $e$ and $\\pi$, and grounding the demand for :term:`purity of method <reinheit-der-methode>` in exact axiomatic dependency analysis.
* **Max Dehn's 1900 Additions (Townsend 1902 Conclusion)**: Incorporates :person:`Max Dehn <dehn>`'s two 1900 Göttingen breakthroughs:
  1. *Non-Legendrian & Semi-Euclidean Geometries* (:cite:`Dehn 1900 <dehn:1900:legendre>`): analyzing triangle angle-sum vs. parallel multiplicity when Archimedes's Axiom is omitted (producing the famous $3 \\times 3$ table showing elliptic/angle-sum $> 2R$ coexisting with infinitely many parallels once Archimedes is dropped!).
  2. *Polyhedral Volume / Hilbert's Third Problem* (:cite:`Dehn 1900 <dehn:1900>`): proving that, unlike planar polygons (Chapter IV), three-dimensional tetrahedra of equal base and equal altitude **cannot** in general be made *flächengleich* (equidecomposable) or even *inhaltsgleich* (equicomplementable), even *with* Archimedes's Axiom!
* **Townsend's 1902 Appendix — Topological Transformation Groups**: Summarizes :person:`Hilbert <hilbert>`'s 1902 *Mathematische Annalen* memoir (:cite:`Hilbert 1902 <hilbert:1902:lie>`), re-founding plane Euclidean and Bolyai–Lobachevsky geometry from :person:`Sophus Lie <lie>`'s transformation-group standpoint *without assuming differentiability*, using :person:`Georg Cantor <cantor>`'s point-set topology, :person:`Camille Jordan <jordan>`'s closed curves, and three topological group axioms (`Axioms I–III`)—the inaugural step toward solving **Hilbert's Fifth Problem**.
""",
}

NOTES: dict[str, str] = {
    "introduction": """
GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Kant's Epigraph and the Triadic Architecture of the *Grundlagen*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Why does the founding manifesto of formal axiomatics open with :person:`Immanuel Kant <kant>`'s dictum from the *Transcendental Dialectic* (:cite:`*Kritik der reinen Vernunft*, A 702 / B 730 <kant:1781>`)? Far from an ornamental flourish, :person:`Hilbert <hilbert>` maps Kant's three faculties onto the three stages of his treatise:

* **Anschauungen (*Intuitions*)**: The five pre-formal experiential clusters of spatial intuition—incidence, betweenness, parallelism, rigid congruence, and continuity—from which geometry historically arises.
* **Begriffe (*Concepts*)**: Chapter I's relational axiomatization (`§§ 1–8`), where primitive geometric terms (*Punkt*, *Gerade*, *Ebene*) are stripped of sensory content and implicitly defined purely through logical axioms.
* **Ideen (*Regulative Ideas*)**: Chapters II–VII's metamathematical investigations into consistency (*Widerspruchslosigkeit*), mutual independence (*Unabhängigkeit*), completeness (*Vollständigkeit*), and :term:`purity of method <reinheit-der-methode>`.

2. Hoenen's Epistemological Critique (*De Noetica Geometriae*, Caput I & V)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :cite:`*De Noetica Geometriae* <hoenen:1954>` (`Caput I §§ 5–6` and `Caput V § 1`), :person:`Fr. Peter Hoenen, S.J. <hoenen>` places :person:`Hilbert <hilbert>`'s *Einleitung* at the center of a three-way comparison between:

1. **Aristotle and Euclid** (:cite:`*Posterior Analytics* <aristotle:anal-post>`): Science (:term:`episteme <phantasma>`) requires *demonstration* from *true, necessary, and intelligible* first principles grasped by intellectual insight (*nous*) through formal abstraction from the imaginative diagram (:term:`phantasma <phantasma>`).
2. **Freudenthal's Semi-Axiomatics** (:cite:`Freudenthal 1957 <freudenthal:1957>`): A prior "pre-geometry" (*la doctrine préalable* / noetics) establishes a complete set of intuitively true axioms at the outset, after which deduction must proceed blindly without further appeal to the diagram.
3. **Hilbert's Strict Formal Axiomatics**: Within the deductive calculus, geometric words function purely as uninterpreted placeholders; the sole internal criterion is logical non-contradiction. Yet, as :person:`Hoenen <hoenen>` demonstrates from Chapter II (`§ 9`), :person:`Hilbert <hilbert>` establishes non-contradiction only by mapping geometry back onto intuitive real/algebraic arithmetic ($\\Omega$), proving that formal axiomatics cannot be self-grounding without pre-axiomatic intellectual intuition!

3. Archival & Textual Note on the 1899 and 1902 Sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Deutsch Track**: Presents the verbatim June 1899 Göttingen *Festschrift* First Edition (:cite:`Teubner 1899 <hilbert:1899>`, Internet Archive ``grundlagendergeo00hilb``). *(Note: Project Gutenberg eBook ``#22062`` is John Dee's 1570 *Mathematicall Praeface* to Euclid, not Hilbert; ``grundlagendergeo00hilb`` is the authentic 1899 German *editio princeps*.)*
* **English Track**: Presents :person:`E. J. Townsend <townsend>`'s verbatim 1902 Open Court translation (:cite:`Townsend 1902 <hilbert:1902:en>`, Project Gutenberg ``#17384``), including Townsend's Preface and the 1900 French additions.
""",
    "chapter-1": """
GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Hoenen on § 1 (*"Wir denken drei verschiedene Systeme..."*) and *Erklärungen*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter I contains the three loci most intensively analyzed in ``geometor/hoenen`` (:cite:`Hoenen 1954 <hoenen:1954>`):

* **Unformalized Arithmetic in § 1 (`Caput I § 6, fn. 14`)**: :person:`Hoenen <hoenen>` quotes § 1's opening sentence verbatim in German (*„Wir denken drei verschiedene Systeme von Dingen...“*) to point out a foundational asymmetry: while *point*, *straight line*, and *plane* are treated as uninterpreted symbols, **cardinal and ordinal numbers** (*"three distinct systems"*, *"two points"*, *"at least four points"*, *"finite number $A_1, \\ldots, A_n$"*) are employed throughout Chapter I in their full intuitive arithmetic meaning.
* **Covert Existential Judgments in *Erklärungen* (`Caput IV, Prelim., fn. 1`)**: Notice how the 1899 German text prefixes §§ 1, 3, 4, 6, 7 with bold **Erklärung** (*Explanation*) and **Definition** headings (often merged or unmarked in Townsend's English). :person:`Hoenen <hoenen>` argues that these *Erklärungen* smuggle in virtual judgments of possibility and spatial structure abstracted from :term:`materia intelligibilis <materia-intelligibilis>`.
* **Linear Order (`II 1–4`), E. H. Moore (1902), and G. H. Hardy (`Caput V § 3.2.A–B, fns. 8–9`)**:
  - **Edition Numbering Shift (1899 vs. 1930 7th ed.)**: In the 1899 *Festschrift* and 1902 English text, Group II has **five** axioms (`II 1–5`), where `II 4` asserts that any four collinear points can be labeled $A, B, C, D$ with $B$ between $A, C$ and $A, D$, and $C$ between $A, D$ and $B, D$; `Theorem 4` then orders any $n$ collinear points $A, B, C, D, E, \\ldots, K$. In January 1902 (:cite:`Moore 1902 <moore:1902>`, cited in Townsend's § 3 footnote!), :person:`E. H. Moore <moore>` proved that `II 4` is **redundant**—deducible from planar incidence `I 1–2` and :person:`Pasch <pasch>`'s Axiom `II 5`! Consequently, in later editions (including the 1930 7th ed. cited by :person:`Hoenen <hoenen>`), `II 4` was demoted to *Satz 5*, shifting 1899 `Satz 4` to *Satz 6*!
  - **Typographic Spatial Intuition**: :person:`Hoenen <hoenen>` scrutinizes `Theorem 4` (*Satz 6* in 7th ed.) and Hilbert's terms :term:`einerseits / andererseits <einerseits-andererseits>` (*"on the one hand / on the other hand"*) and *umgekehrt* (*"reverse order"* $K, \\ldots, E, D, C, B, A$): to understand what *"reverse sequence"* means for $n$ points, the reader must rely on the **left-to-right visual spatial order** of the printed letters on the page! :person:`Hoenen <hoenen>` crowns this critique by quoting :person:`G. H. Hardy <hardy>` (:cite:`*Mind* 1929, p. 15 <hardy:1929>`): *"If Hilbert's axioms are to mean anything to us, we must draw figures."*

2. Euclid & Heath on §§ 6–7: Superposition, SAS (`I.4`), and Postulate 4 (`Theorem 15`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter I's congruence theory (`§§ 6–7`) is the direct centerpiece of :person:`T. L. Heath <heath>`'s commentary in ``geometor/euclid`` (:cite:`Heath 1908 <heath:1908>`):

* **Eliminating Superposition (`Common Notion 4`, Vol. I, pp. 228–230, folios `0242–0244`; `I.4`, pp. 249–250, folios `0263–0264`)**: Where :person:`Euclid <euclid>` proves `I.4` (SAS) by "applying" (:term:`ἐφαρμόζειν <epharmozein>`) $\\triangle ABC$ onto $\\triangle DEF$—a move criticized by Peletier, Schopenhauer, and :person:`Bertrand Russell <russell>` (:cite:`Russell 1903, p. 405 <russell:1903>`) as assuming rigid motion without axiom—:person:`Hilbert <hilbert>` posits `Axiom IV 6` (transferring base angles from two sides and included angle) and proves full SAS (`Theorem 10`) by an elegant *reductio ad absurdum* using uniqueness of angle transfer (`IV 4`). :person:`Heath <heath>` reproduces both `Theorem 10` (`0243.g1`) and `Theorem 12` on supplementary angles (`0244.g1`) verbatim!
* **Proving Euclid's Fourth Postulate (`Theorem 15`, Heath Vol. I, p. 200)**: In § 7 (`Satz 15`), :person:`Hilbert <hilbert>` remarks explicitly that :person:`Euclid <euclid>` *"erroneously, in my opinion, placed among the axioms"* the theorem that **all right angles are congruent** (`Postulate 4`), and proves it purely from supplementary angles (`Theorem 12`) and interior ray transfer (`Theorem 13`)!
* **Axiom Group Swap in Later Editions**: Keep in mind when consulting 20th-century commentaries that in 1899/1902 **Group III = Parallels** (§ 5) and **Group IV = Congruence** (§ 6), whereas from the 2nd/7th editions onward Hilbert swapped them so **Group III = Congruence** and **Group IV = Parallels** (matching absolute geometry's independence from parallels).

3. The Axiom of Completeness (*Vollständigkeit*, § 8 Remark & Hoenen Caput V fn. 10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Absent from the June 1899 German *Festschrift*, the :term:`Axiom of Completeness <vollstaendigkeit>` was added by :person:`Hilbert <hilbert>` in his 1900 paper :cite:`*Über den Zahlbegriff* <hilbert:1900:zahlbegriff>` and the 1900 French edition (:cite:`Laugel 1900 <hilbert:1900:french>`), appearing in :person:`Townsend <townsend>`'s 1902 English text at the close of § 8. As :person:`Heath <heath>` notes on `Euclid I.1` (Vol. I, p. 242, folio `0256`), without Continuity circles need not intersect over arbitrary rational subfields (though Chapter VII shows they *do* intersect over Hilbert's Pythagorean field $\\Omega$!). And as :person:`Hoenen <hoenen>` emphasizes (`Caput V § 5, fn. 10`), *Vollständigkeit* is openly **second-order and metamathematical**, quantifying over all possible extensions preserving the preceding axioms.
""",
    "chapter-2": """
GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Relative Consistency and the Arithmetic Foundation (`§ 9`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chapter II marks a watershed in mathematical logic: before 1899, consistency of non-Euclidean geometries (Beltrami, :person:`Klein <klein>`, :person:`Poincaré <poincare>`) was argued by modeling hyperbolic space *inside Euclidean geometry*. :person:`Hilbert <hilbert>` goes one level deeper in § 9 by modeling **Euclidean geometry itself** inside a countable algebraic subfield $\\Omega \\subset \\mathbb{R}$:

$$\\Omega = \\mathbb{Q}\\text{-closure under } \\omega \\mapsto \\sqrt{1 + \\omega^2}.$$

Two profound consequences emerge for the GEOMETOR ecosystem:

* **Exact Symbolic Algebra (`geometor/model` Resonance)**: Notice that :person:`Hilbert <hilbert>` does *not* need the uncountable Dedekind-Cantor real continuum $\\mathbb{R}$ to satisfy Axioms `I–V` (prior to *Vollständigkeit*)! His minimal model $\\Omega$ consists entirely of **exact symbolic algebraic radicals**—precisely the mathematical universe inhabited by `geometor/model` and SymPy!
* **Hoenen's Epistemological Observation (`Caput I § 6, fn. 14` & `Caput V § 4`)**: By reducing geometric compatibility to *"the arithmetic of the domain $\\Omega$"*, § 9 confirms :person:`Hoenen <hoenen>`'s diagnosis that *Grundlagen der Geometrie* relies on the prior consistency and intuitive intelligibility of arithmetic; pushing the Consistency Problem one step further to arithmetic itself launched **Hilbert's Second Problem (1900)**—and eventually collided with Kurt Gödel's Second Incompleteness Theorem (1931).

2. Why Axiom IV 6 Cannot Be Proved (`§ 11` & Euclid `I.4`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare § 11 with :person:`Heath <heath>`'s commentary on `Euclid I.4` (Vol. I, pp. 249–250): for two thousand years geometers tried to *prove* SAS from linear segment equality and angle equality alone. :person:`Hilbert <hilbert>`'s § 11 model settles why every such attempt was doomed: the norm $\\|(dx, dy, dz)\\| = \\sqrt{(dx + dy)^2 + dy^2 + dz^2}$ is a bona fide translation-invariant normed space (Minkowski/Banach norm whose unit ball in $z=0$ is the tilted ellipse $(x+y)^2 + y^2 = 1$), so segments add linearly along every line (`IV 3`) while Euclidean angle measure satisfies `IV 4–5`, yet rotation fails to preserve segment length! Hence without `IV 6`, linear congruence and angular congruence remain uncoupled.

3. Hilbert's Algebraic Non-Archimedean Field $\\Omega(t)$ (`§ 12`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where :person:`Giuseppe Veronese <veronese>` (:cite:`Veronese 1891/1894 <veronese:1894>`) required hundreds of pages of intricate synthetic intuition to build a non-Archimedean continuum, :person:`Hilbert <hilbert>` constructs $\\Omega(t)$ in two pages by letting $t$ be an indeterminate larger than every integer $n \\in \\mathbb{N}$, so $1/t$ acts as an exact algebraic **infinitesimal**. In Chapter IV (`§ 19`), this very field $\\Omega(t)$ will separate *inhaltsgleich* from *flächengleich* triangles!
""",
    "chapter-3": """
GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. The Pappus–Pascal Bridge (`geometor/pappus` ↔ `geometor/hilbert`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 14 is one of the crown jewels of the entire GEOMETOR workspace, uniting ``geometor/pappus``, ``geometor/euclid``, and ``geometor/hilbert``:

* **Terminological Clarification (*Pascalscher Satz* = Pappus's Hexagon Theorem)**: Following :person:`Hermann Wiener <wiener>` (:cite:`Wiener 1891 <wiener:1891>`) and :person:`Friedrich Schur <schur>` (:cite:`Schur 1898 <schur:1898>`), :person:`Hilbert <hilbert>` calls `Theorem 21` *"Pascal's Theorem"* (*der Pascalsche Satz*) because two intersecting straight lines form a degenerate conic section in :person:`Blaise Pascal <pascal>`'s 1640 mystic hexagram theorem. Historically, however, this exact theorem on two straight lines was discovered and proved 1,300 years earlier by **:person:`Pappus of Alexandria <pappus>`** in Book VII, Propositions 138–139 of his *Mathematical Collection* (:cite:`*Synagoge* <pappus:synagoge>`, modeled in ``geometor/pappus``!).
* **Affine Specialization**: In projective space (``geometor/pappus``), if $A, B, C$ and $A', B', C'$ lie on two lines, the three cross-join intersections $L = CB' \\cap BC'$, $M = CA' \\cap AC'$, and $N = BA' \\cap AB'$ are collinear. Sending the line $LM$ to the line at infinity via the Parallel Axiom (`III`) yields Hilbert's affine `Theorem 21`:

  $$CB' \\parallel BC' \\;\\land\\; CA' \\parallel AC' \\implies BA' \\parallel AB'.$$

* **Why Congruence Proves Pappus Without Continuity**: In `Euclid` Book V, :person:`Eudoxus <eudoxus>`'s proportion definition (`V.Def.5`) invokes arbitrary integer multiples $mA \\gtreqless nB$, which tacitly presupposes `V.Def.4` (**Archimedes's Axiom**). :person:`Hilbert <hilbert>` bypasses Book V completely! Using only right-angle congruence and inscribed cyclic quadrilaterals (`Euclid III.21–22`, proved from `I–IV` at the end of § 7), he proves right-triangle projection operators commute ($\\alpha\\beta c \\equiv \\beta\\alpha c$), which immediately forces `Theorem 21`, which in § 15 forces **commutativity of segment multiplication** $ab = ba$!

2. From *Streckenrechnung* to Book VI Similarity (`§§ 15–17`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Look at the sheer elegance of §§ 15–16:

1. :person:`René Descartes <descartes>` (*La Géométrie*, 1637) defined segment multiplication via Thales's parallel-line proportion—assuming proportion was already known from Book V!
2. :person:`Hilbert <hilbert>` reverses the logical arrow: he *defines* $c = ab$ geometrically by the parallel construction (`§ 15`), proves the field laws `(1–16)` directly from Pappus's Theorem (`Theorem 21`), *defines* proportion $a : b = a' : b'$ as $ab' = ba'$ (`§ 16`), and *deduces* general triangle similarity (`Theorem 22`, `Euclid VI.4`) via a stunning symmetric construction using the incenter $S$ (intersection of the three angle bisectors) and the distributive law!
""",
    "chapter-4": """
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

Why does `Euclid I.35` (*"Parallelograms which are on the same base and in the same parallels are equal to one another"*) work without Archimedes's Axiom only for *inhaltsgleich* and NOT for *flächengleich*? Look at `fig_polygon_equivalence.svg` (`§ 19`): when parallelogram $AB'C'D$ is sheared arbitrarily far to the right—say by the non-Archimedean distance $AF = t$ in $\\Omega(t)$ while $AD = 1$—one can still *add* the single triangle $AED$ and *subtract* congruent trapezoids in **one step** (*inhaltsgleich*), whereas dissecting one triangle into congruent pieces to tile the sheared triangle would require $\\ge t$ steps, which no finite integer $n$ can reach! With Archimedes's Axiom restored, :person:`Farkas Bolyai <bolyai-farkas>` and Paul Gerwien (1833) proved that *inhaltsgleich* and *zerlegungsgleich* coincide in the plane.

2. Proving Euclid's Common Notion 5 (*De Zolt's Postulate*, `§§ 19–21`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In § 19, :person:`Hilbert <hilbert>` quotes :person:`Euclid <euclid>`'s Greek text of Common Notion 5 verbatim:

    *„Καὶ τὸ ὅλον τοῦ μέρους μεῖζόν ἐστιν“* (*"And the whole is greater than the part"*)

pointing out that when Euclid invokes C.N. 5 in `I.39` to prove equal-area triangles on the same base have equal altitude (`Theorem 28`), it is *not* a purely logical truism—without a proof that polygonal area cannot remain unchanged when a piece is removed (:person:`Antonio De Zolt <de-zolt>`'s 1881 postulate, :cite:`De Zolt 1881 <de-zolt:1881>`), *every* polygon could trivially be *inhaltsgleich* to every other! By constructing the segment-valued area functional $F(P) \\in \\Omega_{\\text{seg}}$ in § 20 via Chapter III's Pappus-based *Streckenrechnung* and proving triangulation invariance (`Theorem 29`), :person:`Hilbert <hilbert>` converts Euclid's Common Notion 5 into a **rigorous theorem (`Theorem 31`)**!
""",
    "chapter-5": """
GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. Dimensionality and the Meaning of Spatial Incidence (`§§ 22–23, 30`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Why can Desargues's Theorem (`Theorem 32`) be proved in three lines in 3D projective/affine space using only incidence axioms (`I 1–7, II, III`), yet **cannot be proved at all** in 2D planar incidence-order-parallel geometry (`I 1–2, II, III, V`)?

* **In 3-Space**: Given two perspective triangles in plane $\\alpha$, one lifts the perspective rays into a triangular pyramid in 3-space so corresponding sides lie in two planes $\\beta, \\gamma$; the intersection line $\\beta \\cap \\gamma$ (guaranteed by spatial Axiom `I 6`!) meets $\\alpha$ in the Desargues axis (or parallel direction).
* **In the Plane Alone (`§ 23`, `Theorem 33`)**: Without a third spatial dimension (`I 3–7`) or planar triangle congruence (`IV 6`), :person:`Hilbert <hilbert>`'s refracted ellipse model bends straight lines locally inside $x^2 + 4y^2 = 1$ along circular arcs through $F(\\tfrac{3}{2}, 0)$, destroying perspective concurrency while preserving all planar incidence, order, parallel, and continuity axioms! *(Historical note: in 1902 Forest Ray Moulton simplified Hilbert's ellipse construction to refracted broken lines across the $X$-axis—the "Moulton plane"—after Hilbert's 1899 breakthrough showed such planes exist.)*
* **Elimination of Spatial Axioms (`§ 30`, `Theorem 35`)**: As :person:`Hilbert <hilbert>` summarizes memorably in § 30, Desargues's Theorem is *"the result of the elimination of the space axioms"* for planar geometry, and simultaneously unlocks embedding into projective/affine spaces of **arbitrary dimension $n$**!

2. Non-Commutative Geometry Before Quantum Mechanics (`§§ 24–29`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notice the astonishing modernity of §§ 24–29: twenty-six years before Heisenberg, Born, and Jordan introduced non-commutative matrix mechanics in Göttingen (1925), :person:`Hilbert <hilbert>` constructs coordinate geometry over a **non-commutative division ring** (*skew-field*, :term:`Desarguessches Zahlensystem <desarguessches-zahlensystem>`). In `Theorem 34` (`§ 27`), left-multiplication vs. right-multiplication becomes geometrically decisive:

* $ax + by + c = 0$ (coefficients on the **left**) defines a straight line;
* $xa + yb + c = 0$ (coefficients on the **right**) in general **does not** define a straight line unless multiplication commutes—i.e., unless Pappus's/Pascal's Theorem holds!
""",
    "chapter-6": """
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
     - Ordered **associative skew-field** $D$ (`Theorem 35`, e.g. $\\Omega(s, t)$)
   * - `I 1–7, II, III` + **Pappus/Pascal** *(or planar `I 1–2, II–IV`)*
     - :term:`Pappus's / Pascal's Theorem <pascalscher-satz>` (`Theorem 21`)
     - Ordered **commutative field** $F$ ($ab = ba$, e.g. $\\Omega(t)$)
   * - `I 1–7, II, III, V` *(with Archimedes, even without Congruence!)*
     - Both Desargues & Pappus (`Theorem 36`)
     - Archimedean **commutative** subfield of $\\mathbb{R}$ (`Theorem 38`)
   * - `I–V` + **Completeness** (*Vollständigkeit*)
     - Full Euclidean/Cartesian geometry
     - Unique real field $\\mathbb{R}$

*(Subsequent post-1899 footnote: in 1905 Gerhard Hessenberg proved purely synthetically that Pappus's Theorem implies Desargues's Theorem in any projective/affine plane, and in 1905 Joseph Wedderburn proved that every finite skew-field is commutative!)*

2. Hilbert's Twist Skew-Field $\\Omega(s, t)$ (`§ 33`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:person:`Hilbert <hilbert>`'s § 33 construction (`Theorem 39`) is a tour de force of algebra: by forming iterated Laurent power series over two non-commuting indeterminates $s, t$ subject to

$$ts = 2st,$$

he created what algebraists today call a **Hilbert–Mal'cev–Neumann twisted Laurent series division ring**. Every nonzero element $S = s^m T_0 + s^{m+1} T_1 + \\cdots$ ($T_0 \\neq 0$) is invertible by recursive power-series comparison because $T_0$ lies in the commutative Laurent field $\\mathbb{Q}((t))$ and conjugation $T(t) s = s T(2t)$ merely rescales $t \\mapsto 2t$, preserving positivity of the leading rational coefficient $r_0$! Thus $\\Omega(s, t)$ is simultaneously **ordered**, **non-Archimedean**, and **non-commutative**, giving birth to consistent 3D :term:`Non-Pascalian Geometry <nicht-pascalsche-geometrie>`.
""",
    "chapter-7": """
GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. From *Streckenübertrager* (1899) to *Eichmass* (Later Editions) & `geometor/elements`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``geometor/elements`` and :person:`Euclid <euclid>`'s Book I, straightedge (`Postulates 1–2`) and collapsible/modern compass (`Postulate 3`, `I.2–3`) generate quadratic field extensions via line-circle and circle-circle intersections (`Euclid I.1, I.22`). Why does Chapter VII replace the full compass with a **transferer of segments** (:term:`Streckenübertrager <streckenuebertrager>` in 1899; Townsend: *"transferer of segments"*)?

* Because **Axioms `I–V` (without *Vollständigkeit*) never mention circles intersecting circles!** Axiom `IV 1` only guarantees laying off a given segment $AB$ along a given straight line from a point $A'$.
* In later editions (e.g., 7th ed., 1930), :person:`Hilbert <hilbert>` sharpened this instrument even further to the **fixed-unit gauge** (:term:`Eichmass <eichmass>`), which can only lay off a *single fixed unit segment* $1$ along any ray—because once parallel lines (`Problem 2`) are constructible, any segment ratio can be transferred via parallels using a single fixed unit!
* Look at `fig_gauge_constructions.svg` (`§ 36`, `Problem 5`): to drop a perpendicular without drawing intersecting circles (`Euclid I.11–12`), :person:`Hilbert <hilbert>` lays off four equal radii $AB = AC = AD = AE$ from $A$ along the base line and two oblique rays through $A$; by Thales's semicircle theorem (`Euclid III.31`), $\\angle BDC$ and $\\angle BEC$ are right angles, so $BD$ and $CE$ are two altitudes of $\\triangle BCF$ meeting at its orthocenter $H$, making the third line $FH$ strictly perpendicular to $BC$ using **straightedge and segment-transferer alone**!

2. Birth of Real Algebraic Geometry & Hilbert's 17th Problem (`§§ 37–39`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sections 37–39 bridge synthetic constructive geometry (`geometor/elements`) with deep algebraic number theory:

* **Why Compass > Segment-Transferer (`§ 37`)**: Every coordinate in $\\Omega$ (`§ 9`) is built from sums of squares $\\sqrt{\\alpha^2 + \\beta^2}$, so *all algebraic conjugates* of every number in $\\Omega$ are real (**totally real**). By contrast, a circle can intersect a line whenever $\\alpha > 0$ numerically, even if an algebraic conjugate of $\\alpha$ is negative! Thus $\\sqrt{2\\sqrt{2} - 2}$ (constructible by intersecting a unit circle with $x = \\sqrt{2} - 1$) has imaginary conjugate $\\sqrt{-2\\sqrt{2} - 2}$ and **cannot** lie in $\\Omega$!
* **Hilbert's 17th Problem (`§ 38`, `Theorem 43`)**: Proving `Theorem 43` (every positive-definite univariate polynomial over $\\mathbb{Q}$ is a quotient of sums of squares) led :person:`Hilbert <hilbert>` at the end of § 38 to ask whether every positive-definite rational function in $n$ variables over $\\mathbb{Q}$ is a sum of squares of rational functions—posed one year later in Paris as **Hilbert's Seventeenth Problem (1900)** and solved affirmatively in 1927 by Emil Artin via Artin–Schreier real closed fields!
""",
    "conclusion": """
GEOMETOR Commentary & Cross-Repository Notes
--------------------------------------------

1. *Reinheit der Methode* (Purity of Method) and Impossibility Proofs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:person:`Hilbert <hilbert>`'s *Schlusswort* (*Conclusion*) articulates two enduring pillars of modern mathematical philosophy:

1. **Epistemological Value of Impossibility Proofs**: Just as Abel proved the quintic unsolvable by radicals and Lindemann proved $\\pi$ transcendental (settling circle-squaring), Chapters II, IV, V, VI, and VII prove the **impossibility** of deducing Parallels (`§ 10`), SAS (`§ 11`), Archimedes (`§ 12`), polygon equidecomposability without Archimedes (`§ 19`), planar Desargues without space or congruence (`§ 23`), Pappus/Pascal without congruence or Archimedes (`§ 34`), and general compass constructions from segment transfer (`§ 37`).
2. **Purity of Method (:term:`Reinheit der Methode <reinheit-der-methode>`)**: Rather than leaving "purity" as a vague aesthetic preference (e.g., forbidding 3D space or continuity in planar proofs), *Grundlagen der Geometrie* converts purity into an exact scientific question: *what is the minimal subset of axioms required by the truth of a proposition?*

2. Max Dehn's 1900 Breakthroughs: Non-Legendrian Geometry & Hilbert's 3rd Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Between the June 1899 German *Festschrift* and :person:`Townsend <townsend>`'s 1902 English translation, :person:`Hilbert <hilbert>`'s student :person:`Max Dehn <dehn>` completed two celebrated investigations summarized in the English Conclusion:

* **The $3 \\times 3$ Angle-Sum / Parallel Table (:cite:`Dehn 1900 <dehn:1900:legendre>`)**: Classical Legendre theorems state (1) triangle angle-sum $\\le 2R$, and (2) if angle-sum $= 2R$, Euclid's Parallel Postulate holds. :person:`Dehn <dehn>` showed using Hilbert's non-Archimedean geometry (`§ 12`) that *without Archimedes's Axiom*:
  - **Semi-Euclidean Geometry** exists: angle-sum $= 2R$ everywhere, yet infinitely many parallels pass through a point (differing by infinitesimal angles)!
  - **Non-Legendrian Geometry** exists: angle-sum $> 2R$, yet infinitely many lines through a point fail to meet a given line (located at infinite non-Archimedean distance)!
* **Polyhedral Volume & Hilbert's Third Problem (:cite:`Dehn 1900 <dehn:1900>`)**: Extending Chapter IV from 2D polygons to 3D polyhedra, :person:`Hilbert <hilbert>` posed as his **Third Paris Problem (1900)** whether two tetrahedra of equal base and altitude are always *zerlegungsgleich* or *ergänzungsgleich* (*inhaltsgleich*). Within months, :person:`Dehn <dehn>` proved the answer is **NO** (introducing the tensor-product *Dehn invariant* $\\sum \\ell_i \\otimes \\theta_i \\in \\mathbb{R} \\otimes_{\\mathbb{Q}} (\\mathbb{R}/\\pi\\mathbb{Q})$, showing a regular tetrahedron is neither equidecomposable nor equicomplementable with a cube of equal volume!).

3. Townsend's 1902 Appendix and Hilbert's Fifth Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 1902 English edition concludes with :person:`Townsend <townsend>`'s translation/summary of :person:`Hilbert <hilbert>`'s 1902 *Mathematische Annalen* paper (:cite:`Hilbert 1902 <hilbert:1902:lie>`), offering a radically different—**topological and group-theoretic**—foundation of plane geometry. Replacing :person:`Sophus Lie <lie>`'s analytic differentiability hypotheses (:cite:`Lie–Engel 1893 <lie:1893>`) with :person:`Camille Jordan <jordan>`'s closed curves and three topological axioms for orientation-preserving homeomorphisms (`Axioms I–III`: group closure, infinite orbits on true circles, and topological closure of displacements), :person:`Hilbert <hilbert>` recovers Euclidean and Bolyai–Lobachevsky geometry without a single derivative—launching topological group theory and the half-century quest culminating in Gleason, Montgomery, and Zippin's 1952 solution of **Hilbert's Fifth Problem**.
""",
}
