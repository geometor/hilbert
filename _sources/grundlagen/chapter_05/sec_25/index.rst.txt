:layout: book
:canonical_id: § 25
:breadcrumb_title: § 25
:order: 25
:folio: § 25
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s25:

.. folio:: § 25
   :page: 82

§ 25: The Commutative and the Associative Law of Addition for Our New Algebra of Segments
=========================================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

In this section, we shall investigate the laws of operation, as enumerated in § 13, in order to see which of these hold for our new algebra of segments, when we base our considerations upon a plane geometry in which axioms I 1–2, II–III are all fulfilled, and, moreover, in which Desargues's theorem also holds.

First of all, we shall show that, for the addition of segments as defined in § 24, the commutative law

.. math::

   a+ b = b+a

holds. Let

.. math::

   \begin{aligned}
   &\; a = OA = OA' \; \\
   &\; b = OB = OB' \;
   \end{aligned}

Hence, :math:`AA'` and :math:`BB'` are, according to our convention, parallel to the unit-line. Construct the points :math:`A''` and :math:`B''` by drawing :math:`A'A''` and :math:`B'B''` parallel to :math:`OA` and also :math:`AB''` and :math:`BA'` parallel to :math:`OA`. We see at once that the line :math:`A''B''` is parallel to :math:`AA'` as the commutative law requires. We shall show the validity of this statement by the aid of Desargues's theorem in the following manner. Denote the point of intersection of :math:`AB''` and :math:`A'A''` by :math:`F` and that of :math:`BA''` and :math:`B'B''` by :math:`D`. Then, in the triangles :math:`AA'F` and :math:`BB'D`, the homologous sides are parallel to each other. By Desargues's theorem, it follows that the three points :math:`O`, :math:`F`, :math:`D` lie in a straight line. In consequence of this condition, the two triangles :math:`OAA'` and :math:`DB''A''` lie in such a way that the lines joining the corresponding vertices pass through the same point :math:`F`, and since the homologous sides :math:`OA` and :math:`DB''`, as also :math:`OA'` and :math:`DA''`, are parallel to each other, then, according to the second part of Desargues's theorem (theorem 32), the third sides :math:`AA'` and :math:`B''A''` are parallel to each other.

To prove the associative law of addition

.. math::

   a+(b+c)=(a+b)+c,

we shall make use of figure 44. In consequence of the commutative law of addition just demonstrated, the above formula states that the straight line :math:`A''B''` must be parallel to the unit-line.

The validity of this statement is evident, since the shaded part of figure 44 corresponds exactly with figure 43.

.. picture:: /_static/figures/fig_desargues_segment_algebra.svg
   :alt: Constructing c = a + b and c = ab on fixed axes OX, OY with unit line EE' purely from incidence, parallels, and Desargues's Theorem without Congruence.
   :caption: **Projective-Affine Segment Addition and Skew-Field Multiplication (§§ 24–26).** Constructing c = a + b and c = ab on fixed axes OX, OY with unit line EE' purely from incidence, parallels, and Desargues's Theorem without Congruence.

.. toctree::
   :hidden:

   de
   summary
   notes
