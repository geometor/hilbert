:layout: book
:canonical_id: § 7
:breadcrumb_title: § 7
:order: 7
:folio: § 7
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s7:

.. folio:: § 7
   :page: 16

§ 7: Consequences of the Axioms of Congruence
=============================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

Suppose the segment :math:`AB` is congruent to the segment :math:`A'B'`. Since, according to axiom IV, 1, the segment :math:`AB` is congruent to itself, it follows from axiom IV, 2 that :math:`A'B'` is congruent to :math:`AB`; that is to say, if :math:`AB \equiv A'B'`, then :math:`A'B' \equiv AB`. We say, then, that the two segments are congruent to one another.

Let :math:`A`, :math:`B`, :math:`C`, :math:`D,\ldots,` :math:`K`, :math:`L` and :math:`A'`, :math:`B'`, :math:`C'`, :math:`D',\ldots,` :math:`K'`, :math:`L'` be two series of points on the straight lines :math:`a` and :math:`a'`, respectively, so that all the corresponding segments :math:`AB` and :math:`A'B'`, :math:`AC` and :math:`A'C'`, :math:`BC` and :math:`B'C',\ldots,` :math:`KL` and :math:`K'L'` are respectively congruent, then *the two series of points are said to be congruent to one another*. :math:`A` and :math:`A'`, :math:`B` and :math:`B',\ldots,` :math:`L` and :math:`L'` are called *corresponding points* of the two congruent series of points.

From the linear axioms IV, 1–3, we can easily deduce the following theorems:

.. _grundlagen-en-thm-9:

**Theorem 9.** If the first of two congruent series of points :math:`A`, :math:`B`, :math:`C`, :math:`D,\ldots,` :math:`K`, :math:`L` and :math:`A'`, :math:`B'`, :math:`C'`, :math:`D',\ldots,` :math:`K'`, :math:`L'` is so arranged that :math:`B` lies between :math:`A` and :math:`C`, :math:`D,\ldots,` :math:`K`, :math:`L`, and :math:`C` between :math:`A`, :math:`B` and :math:`D,\ldots,` :math:`K`, :math:`L`, etc., then the points :math:`A'`, :math:`B'`, :math:`C'`, :math:`D',\ldots,` :math:`K'`, :math:`L'` of the second series are arranged in a similar way; that is to say, :math:`B'` lies between :math:`A'` and :math:`C'`, :math:`D',\ldots,` :math:`K'`, :math:`L'`, and :math:`C'` lies between :math:`A'`, :math:`B'` and :math:`D',\ldots,` :math:`K'`, :math:`L'`, etc.

Let the angle :math:`(h,k)` be congruent to the angle :math:`(h',k')`. Since, according to axiom IV, 4, the angle :math:`(h,k)` is congruent to itself, it follows from axiom IV, 5 that the angle :math:`(h',k')` is congruent to the angle :math:`(h,k)`. We say, then, that the angles :math:`(h,k)` and :math:`(h',k')` are *congruent to one another*.

**Definitions**. Two angles having the same vertex and one side in common, while the sides not common form a straight line, are called *supplementary angles*. Two angles having a common vertex and whose sides form straight lines are called *vertical angles*. An angle which is congruent to its supplementary angle is called a *right angle*.

Two triangles :math:`ABC` and :math:`A'B'C'` are said to be *congruent* to one another when all of the following congruences are fulfilled:

.. math::

   \begin{array}{ccc}
   AB \equiv A'B', & AC \equiv A'C', & BC \equiv B'C', \\
   \angle A \equiv \angle A', & \angle B \equiv \angle B', & \angle C \equiv \angle C'.
   \end{array}

.. _grundlagen-en-thm-10:

**Theorem 10.** (First theorem of congruence for triangles). If, for the two triangles :math:`ABC` and :math:`A'B'C'`, the congruences

.. math::

   AB \equiv A'B', \: AC \equiv A'C', \: \angle A \equiv \angle A'

hold, then the two triangles are congruent to each other.

**Proof.**  From axiom IV, 6, it follows that the two congruences

.. math::

   \angle B \equiv \angle B' \quad \text{and} \quad \angle C \equiv \angle C'

are fulfilled, and it is, therefore, sufficient to show that the two sides :math:`BC` and :math:`B'C'` are congruent. We will assume the contrary to be true, namely, that :math:`BC` and :math:`B'C'` are not congruent, and show that this leads to a contradiction. We take upon :math:`B'C'` a point :math:`D'` such that :math:`BC \equiv B'D'`. The two triangles :math:`ABC` and :math:`A'B'D'` have, then, two sides and the included angle of the one agreeing, respectively, to two sides and the included angle of the other. It follows from axiom IV, :math:`6` that the two angles :math:`BAC` and :math:`B'A'D'` are also congruent to each other. Consequently, by aid of axiom IV, :math:`5`, the two angles :math:`B'A'C'` and :math:`B'A'D'` must be congruent.

This, however, is impossible, since, by axiom IV, 4, an angle can be laid off in one and only one way on a given side of a given half-ray of a plane. From this contradiction the theorem follows.

We can also easily demonstrate the following theorem:

.. _grundlagen-en-thm-11:

**Theorem 11.** (Second theorem of congruence for triangles). If in any two triangles one side and the two adjacent angles are respectively congruent, the triangles are congruent.

We are now in a position to demonstrate the following important proposition.

.. _grundlagen-en-thm-12:

**Theorem 12.** If two angles :math:`ABC` and :math:`A'B'C'` are congruent to each other, their supplementary angles :math:`CBD` and :math:`C'B'D'` are also congruent.

**Proof.** Take the points :math:`A'`, :math:`C'`, :math:`D'` upon the sides passing through :math:`B'` in such a way that

.. math::

   A'B' \equiv AB,\ C'B' \equiv CB,\ D'B' \equiv DB.

Then, in the two triangles :math:`ABC` and :math:`A'B'C'`, the sides :math:`AB` and :math:`BC` are respectively congruent to :math:`A'B'` and :math:`C'B'`. Moreover, since the angles included by these sides are congruent to each other by hypothesis, it follows from theorem 10 that these triangles are congruent; that is to say, we have the congruences

.. math::

   AC \equiv A'C,\ \angle BAC \equiv \angle B'A'C'.

On the other hand, since by axiom IV, 3 the segments :math:`AD` and :math:`A'D'` are congruent to each other, it follows again from theorem 10 that the triangles :math:`CAD` and :math:`C'A'D'` are congruent, and, consequently, we have the congruences:

.. math::

   CD \equiv C'D',\ \angle ADC \equiv \angle A'D'C'.

From these congruences and the consideration of the triangles :math:`BCD` and :math:`B'C'D'`, it follows by virtue of axiom IV, 6 that the angles :math:`CBD` and :math:`C'B'D'` are congruent.

As an immediate consequence of theorem 12, we have a similar theorem concerning the congruence of vertical angles.

.. _grundlagen-en-thm-13:

**Theorem 13.** Let the angle (:math:`h`, :math:`k`) of the plane :math:`\alpha` be congruent to the angle (:math:`h'`, :math:`k'`) of the plane :math:`\alpha'`, and, furthermore, let :math:`l` be a half-ray in the plane :math:`\alpha` emanating from the vertex of the angle (:math:`h`, :math:`k`) and lying within this angle. Then, there always exists in the plane :math:`\alpha'` a half-ray :math:`l'` emanating from the vertex of the angle (:math:`h'`, :math:`k'`) and lying within this angle so that we have

.. math::

   \angle (h, l) \equiv \angle (h', l'),\ \angle (k, l) \equiv \angle (k', l').

**Proof**. We will represent the vertices of the angles (:math:`h`, :math:`k`) and (:math:`h'`, :math:`k'`) by :math:`O` and :math:`O'`, respectively, and so select upon the sides :math:`h`, :math:`k`, :math:`h'`, :math:`k'` the points :math:`A`, :math:`B`, :math:`A'`, :math:`B'` that the congruences

.. math::

   OA \equiv O'A',\ OB \equiv O'B'

are fulfilled. Because of the congruence of the triangles :math:`OAB` and :math:`O'A'B'`, we have at once

.. math::

   AB \equiv A'B',\ \angle OAB \equiv O'A'B',\ \angle OBA \equiv \angle O'B'A'.

Let the straight line :math:`AB` intersect :math:`l` in :math:`C`. Take the point :math:`C'` upon the segment :math:`A'B'` so that :math:`A'C' \equiv AC`. Then, :math:`O'C'` is the required half-ray. In fact, it follows directly from these congruences, by aid of axiom IV, 3, that :math:`BC \equiv B'C'`. Furthermore, the triangles :math:`OAC` and :math:`O'A'C'` are congruent to each other, and the same is true also of the triangles :math:`OCB` and :math:`O'B'C'`. With this our proposition is demonstrated.

In a similar manner, we obtain the following proposition.

.. _grundlagen-en-thm-14:

**Theorem 14.** Let :math:`h`, :math:`k`, :math:`l` and :math:`h'`, :math:`k'`, :math:`l'` be two sets of three half-rays, where those of each set emanate from the same point and lie in the same plane. Then, if the congruences

.. math::

   \angle (h, l) \equiv \angle (h', l'),\ \angle (k, l) \equiv \angle (k', l')

are fulfilled, the following congruence is also valid; viz.:

.. math::

   \angle (h,k) \equiv \angle (h', k').

By aid of theorems 12 and 13, it is possible to deduce the following simple theorem, which Euclid held–although it seems to me wrongly–to be an axiom.

.. _grundlagen-en-thm-15:

**Theorem 15.** All right angles are congruent to one another.

**Proof.** Let the angle :math:`BAD` be congruent to its supplementary angle :math:`CAD`, and, likewise, let the angle :math:`B'A'D'` be congruent to its supplementary angle :math:`C'A'D'`. Hence the angles :math:`BAD`, :math:`CAD`, :math:`B'A'D'`, and :math:`C'A'D'` are all right angles. We will assume that the contrary of our proposition is true, namely, that the right angle :math:`B'A'D'` is not congruent to the right angle :math:`BAD`, and will show that this assumption leads to a contradiction. We lay off the angle :math:`B'A'D'` upon the half-ray :math:`AB` in such a manner that the side :math:`AD''` arising from this operation falls either within the angle :math:`BAD` or within the angle :math:`CAD`. Suppose, for example, the first of these possibilities to be true. Because of the congruence of the angles :math:`B'A'D'` and :math:`BAD''`, it follows from theorem 12 that angle :math:`C'A'D'` is congruent to angle :math:`CAD''`, and, as the angles :math:`B'A'D'` and :math:`C'A'D'` are congruent to each other, then, by IV, 5, the angle :math:`BAD''` must be congruent to :math:`CAD''`.

Furthermore, since the angle :math:`BAD` is congruent to the angle :math:`CAD`, it is possible, by theorem 13, to find within the angle :math:`CAD` a half-ray :math:`AD'''` emanating from :math:`A`, so that the angle :math:`BAD''` will be congruent to the angle :math:`CAD'''`, and also the angle :math:`DAD''` will be congruent to the angle :math:`DAD'''`. The angle :math:`BAD''` was shown to be congruent to the angle :math:`CAD''` and, hence, by axiom IV, 5, the angle :math:`CAD''`, is congruent to the angle :math:`CAD'''`. This, however, is not possible; for, according to axiom IV, 4, an angle can be laid off in a plane upon a given side of a given half-ray in only one way. With this our proposition is demonstrated. We can now introduce, in accordance with common usage, the terms “*acute angle*” and “*obtuse angle*.”

The theorem relating to the congruence of the base angles :math:`A` and :math:`B` of an equilateral triangle :math:`ABC` follows immediately by the application of axiom IV, 6 to the triangles :math:`ABC` and :math:`BAC`. By aid of this theorem, in addition to theorem 14, we can easily demonstrate the following proposition.

.. _grundlagen-en-thm-16:

**Theorem 16.** (Third theorem of congruence for triangles.) If two triangles have the three sides of one congruent respectively to the corresponding three sides of the other, the triangles are congruent.

Any finite number of points is called a *figure*. If all of the points lie in a plane, the figure is called a *plane figure*.

Two figures are said to be *congruent* if their points can be arranged in a one-to-one correspondence so that the corresponding segments and the corresponding angles of the two figures are in every case congruent to each other.

Congruent figures have, as may be seen from theorems 9 and 12, the following properties: Three points of a figure lying in a straight line are likewise in a straight line in every figure congruent to it. In congruent figures, the arrangement of the points in corresponding planes with respect to corresponding lines is always the same. The same is true of the sequence of corresponding points situated on corresponding lines.

The most general theorems relating to congruences in a plane and in space may be expressed as follows:

.. _grundlagen-en-thm-17:

**Theorem 17.** If :math:`(A, B, C,\ldots)` and :math:`(A', B', C',\ldots)` are congruent plane figures and P is a point in the plane of the first, then it is always possible to find a point :math:`P` in the plane of the second figure so that :math:`(A, B, C,\ldots , P)` and :math:`(A', B', C', \ldots , P')` shall likewise be congruent figures. If the two figures have at least three points not lying in a straight line, then the selection of :math:`P'` can be made in only one way.

.. _grundlagen-en-thm-18:

**Theorem 18.** If :math:`(A, B, C, \ldots)` and :math:`(A', B', C',\ldots=` are congruent figures and :math:`P` represents any arbitrary point, then there can always be found a point :math:`P'` so that the two figures :math:`(A, B, C, \ldots, P)` and :math:`(A', B', C', \ldots, P')` shall likewise be congruent. If the figure :math:`(A, B, C, \ldots , P)` contains at least four points not lying in the same plane, then the determination of :math:`P'` can be made in but one way.

This theorem contains an important result; namely, that all the facts concerning space which have reference to congruence, that is to say, to displacements in space, are (by the addition of the axioms of groups I and II) exclusively the consequences of the six linear and plane axioms mentioned above. Hence, it is not necessary to assume the axiom of parallels in order to establish these facts.

If we take, in addition to the axioms of congruence, the axiom of parallels, we can then easily establish the following propositions:

.. _grundlagen-en-thm-19:

**Theorem 19.** If two parallel lines are cut by a third straight line, the alternate-interior angles and also the exterior-interior angles are congruent.

Conversely, if the alternate-interior or the exterior-interior angles are congruent, the given lines are parallel.

.. _grundlagen-en-thm-20:

**Theorem 20.** The sum of the angles of a triangle is two right angles.

**Definitions.** If :math:`M` is an arbitrary point in the plane :math:`a`, the totality of all points :math:`A`, for which the segments :math:`MA` are congruent to one another, is called *a circle*. :math:`M` is called the *centre of the circle*.

From this definition can be easily deduced, with the help of the axioms of groups III and IV, the known properties of the circle; in particular, the possibility of constructing a circle through any three points not lying in a straight line, as also the congruence of all angles inscribed in the same segment of a circle, and the theorem relating to the angles of an inscribed quadrilateral.

.. picture:: /_static/figures/fig_sas_supplementary.svg
   :alt: Eliminating Euclidean superposition: SAS congruence (Theorem 10) via Axiom IV 6 and supplementary angles (Theorem 12; cf. Heath on Euclid C.N. 4, folios 0243–0244).
   :caption: **Hilbert's SAS Reductio (Theorem 10) and Supplementary Angle Congruence (Theorem 12).** Eliminating Euclidean superposition: SAS congruence (Theorem 10) via Axiom IV 6 and supplementary angles (Theorem 12; cf. Heath on Euclid C.N. 4, folios 0243–0244).

.. toctree::
   :hidden:

   de
   summary
   notes
