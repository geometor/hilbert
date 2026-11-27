:layout: book
:canonical_id: § 21
:breadcrumb_title: § 21
:order: 21
:folio: § 21
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s21:

.. folio:: § 21
   :page: 67

§ 21: Equality of Content and the Measure of Area
=================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

In § 20 we have found that polygons having equal content have also equal measures of area. The converse of this is also true.

In order to prove the converse, let us consider two triangles :math:`ABC` and :math:`AB'C'` having a common right angle at :math:`A`. The measures of area of these two triangles are expressed by the formulæ

.. math::

   \begin{aligned}
   F(ABC) &= \frac{1}{2}AB \cdot AC, \\
   F(AB'C') &= \frac{1}{2}AB' \cdot AC'.
   \end{aligned}

We now assume that these measures of area are equal to each other, and consequently we have

.. math::

   AB \cdot AC = AB' \cdot AC',

or

.. math::

   AB:AB' = AC':AC.

From this proposition, it follows, according to theorem 23, that the two straight lines :math:`BC'` and :math:`B'C` are parallel, and hence, by theorem 27, the two triangles :math:`BC'B'` and :math:`BC'C` are of equal content. By the addition of the triangle :math:`ABC'`, it follows that the two triangles :math:`ABC` and :math:`AB'C'` are of equal content. We have then shown that two right triangles having the same measure of area are always of equal content.

Take now any arbitrary triangle having the base :math:`g` and the altitude :math:`h`. Then, according to theorem 27, it has equal content with a right triangle having the two sides :math:`g` and :math:`h`. Since the original triangle had evidently the same measure of area as the right triangle, it follows that, in the above consideration, the restriction to right triangles was not necessary. Hence, two *arbitrary triangles with equal measures of area are also of equal content*.

Moreover, let us suppose :math:`P` to be any polygon having the measure of area :math:`g` and let :math:`P` be decomposed into :math:`n` triangles having respectively the measures of area :math:`g_1`, :math:`g_2`, :math:`g_3`, :math:`\ldots`, :math:`g_n`. Then, we have

.. math::

   g = g_1 + g_2 + g_3 + \cdots + g_n.

Construct now a triangle :math:`ABC` having the base :math:`AB=g` and the altitude :math:`h = 1`. Take, upon the base of this triangle, the points :math:`A_1`, :math:`A_2`, :math:`\ldots`, :math:`A_{n-1}` so that :math:`g_1=AA_1`, :math:`g_1=A_1A_2`, :math:`\ldots`, :math:`g_{n-1}=A_{n-2}A_{n-1}`, :math:`g_n=A_{n-1}B`.

Since the triangles composing the polygon :math:`P` have respectively the same measures of area as the triangles :math:`AA_1C`, :math:`A_1A_2C`, :math:`\ldots`, :math:`A_{n-2}A_{n-1}C`, :math:`A_{n-1}BC`, it follows from what has already been demonstrated that they have also the same content as these triangles. Consequently, the polygon :math:`P` and a triangle, having the base :math:`g` and the altitude :math:`h = 1` are of equal content. From this, it follows, by the application of theorem 24, that two polygons having equal measures of area are always of equal content.

We can now combine the proposition of this section with that demonstrated in the last, and thus obtain the following theorem:

.. _grundlagen-en-thm-30:

**Theorem 30.** Two polygons of equal content have always equal measures of area. Conversely, two polygons having equal measures of area are always of equal content.

In particular, if two rectangles are of equal content and have one side in common, then their remaining sides are respectively congruent. Hence, we have the following proposition:

.. _grundlagen-en-thm-31:

**Theorem 31.** If we decompose a rectangle into several triangles by means of straight lines and then omit one of these triangles, we can no longer make up completely the rectangle from the triangles which remain.

This theorem has been demonstrated by F. Schur [#fn1]_ and by W. Killing, [#fn2]_ but by making use of the axiom of Archimedes. By O. Stolz, [#fn3]_ it has been regarded as an axiom. In the foregoing discussion, it has been shown that it is completely independent of the axiom of Archimedes. However, when we disregard the axiom of Archimedes, this theorem (31) is not sufficient of itself to enable us to demonstrate Euclid's theorem concerning the equality of altitudes of triangles having equal content and equal bases. (Theorem 28.)

In the demonstration of theorems 28, 29, and 30, we have employed essentially the algebra of segments introduced in § 15, p. 46, and as this depends substantially upon Pascal's theorem (theorem 21), we see that this theorem is really the corner-stone in the theory of areas. We may, by the aid of theorems 27 and 28, easily establish the converse of Pascal's theorem.

Of two polygons :math:`P` and :math:`Q`, we call :math:`P` the smaller or larger in content according as the measure of area

:math:`F(P)` is less or greater than the measure of area :math:`F(Q)`. From what has already been said, it is clear that the notions, equal content, smaller content, larger content, are mutually exclusive. Moreover, we easily see that a polygon, which lies wholly within another polygon, must always be of smaller content than the exterior one.

With this we have established the important theorems in the theory of areas.

----

.. rubric:: Footnotes

.. [#fn1] *Sitzungsberichte der Dorpater Naturf. Ges.* 1892.

.. [#fn2] *Grundlagen der Geometrie*, Vol. 2, Chapter 5, § 5, 1898.

.. [#fn3] *Monatshefte für Math, und Phys.* 1894.

.. toctree::
   :hidden:

   de
   summary
   notes
