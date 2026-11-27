:layout: book
:canonical_id: § 20
:breadcrumb_title: § 20
:order: 20
:folio: § 20
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s20:

.. folio:: § 20
   :page: 63

§ 20: The Measure of Area of Triangles and Polygons
===================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

**Definition.**  If in a triangle :math:`ABC`, having the sides :math:`a`, :math:`b`, :math:`c`, we construct the two altitudes :math:`h_a = AD`, :math:`h_b = BE`, then, according to theorem 22, it follows from the similarity of the triangles :math:`BCE` and :math:`ACD`, that we have the proportion

.. math::

   a: h_b = b: ha;

that is, we have

.. math::

   a \cdot h_a = b \cdot h_b.

This shows that the product of the base and the corresponding altitude of a triangle is the same whichever side is selected as the base. The half of this product of the base and the altitude of a triangle :math:`\Delta` is called the *measure of area of the triangle* :math:`\Delta` and we denote it by :math:`F(\Delta)`. A segment joining a vertex of a triangle with a point of the opposite side is called *a transversal.* A transversal divides the given triangle into two others having the same altitude and having bases which lie in the same straight line. Such a decomposition is called a *transversal decomposition of the triangle.*

.. _grundlagen-en-thm-29:

**Theorem 29.** If a triangle :math:`\Delta` is decomposed by means of arbitrary straight lines into a finite number of triangles :math:`\Delta_k`, then the measure of area of :math:`\Delta` is equal to the sum of the measures of area of the separate triangles :math:`\Delta_k`.

**Proof.** From the distributive law of our algebra of segments, it follows immediately that the measure of area of an arbitrary triangle is equal to the sum of the measures of area of two such triangles as arise from any transversal decomposition of the given triangle. The repeated application of this proposition shows that the measure of area of any triangle is equal to the sum of the measures of area of all the triangles arising by applying the transversal decomposition an arbitrary number of times in succession.

In order to establish the corresponding proof for an arbitrary decomposition of the triangle :math:`\Delta` into the triangles :math:`\Delta_k`, draw from the vertex :math:`A` of the given triangle :math:`\Delta` a transversal through each of the points of division of the required decomposition; that is to say, draw a transversal through each vertex of the triangles :math:`\Delta_k`. By means of these transversals, the given triangle :math:`\Delta` is decomposed into certain triangles :math:`\Delta_t`. Each of these triangles :math:`\Delta_t` is broken up by the segments which determined this decomposition into certain triangles and quadrilaterals. If, now, in each of the quadrilaterals, we draw a diagonal, then each triangle :math:`\Delta_t` is decomposed into certain other triangles :math:`\Delta_{ts}`. We shall now show that the decomposition into the triangles :math:`\Delta_{ts}` is for the triangles :math:`\Delta_t`, as well as for the triangles :math:`\Delta_k`, nothing else than a series of transversal decompositions. In fact, it is at once evident that any decomposition of a triangle into partial triangles may always be affected by a series of transversal decompositions, providing, in this decomposition, points of division do not exist within the triangle, and further, that at least one side of the triangle remains free from points of division.

We easily see that these conditions hold for the triangles :math:`\Delta_t`. In fact, the interior of each of these triangles, as also one side, namely, the side opposite the point :math:`A`, contains no points of division.

Likewise, for each of the triangles :math:`\Delta_k`, the decomposition into :math:`\Delta_{ts}` is reducible to transversal decompositions. Let us consider a triangle :math:`\Delta_k`. Among the transversals of the triangle :math:`\Delta` emanating from the point :math:`A`, there is always a definite one to be found which either coincides with a side of :math:`\Delta_k`, or which itself divides :math:`\Delta_k` into two triangles. In the first case, the side in question always remains free from further points of division by the decomposition into the triangles :math:`\Delta_{ts}`. In the second case, the segment of the transversal contained within the triangle :math:`\Delta_k` is a side of the two triangles arising from the division, and this side certainly remains free from further points of division.

According to the considerations set forth at the beginning of this demonstration, the measure of area :math:`F(\Delta)` of the triangle :math:`\Delta` is equal to the sum of the measures of area :math:`F(\Delta_t)` of all the triangles :math:`\Delta_t` and this sum is in turn equal to the sum of all the measures of area :math:`F(\Delta_{ts})`. However, the sum of the measures of area :math:`F(\Delta_k)` of all the triangles :math:`\Delta_k` is also equal to the sum of the measures of area :math:`F(\Delta_{ts})`. Consequently, we have finally that the measure of area :math:`F(\Delta)` is also equal to the sum of all the measures of area :math:`F(\Delta_k)`, and with this conclusion our demonstration is completed.

**Definition.** If we define the measure of area :math:`F(P)` of a polygon as the sum of the measures of area of all the triangles into which the polygon is, by a definite decomposition, divided, then upon the basis of theorem 29 and by a process of reasoning similar to that which we have employed in § 18 to prove theorem 24, we know that the measure of area of a polygon is independent of the manner of decomposition into triangles and, consequently, is definitely determined by the polygon itself. From this we obtain, by aid of theorem 29, the result that *polygons of equal area have also equal measures of area*.

Furthermore, if :math:`P` and :math:`Q` are two polygons of equal content, then there must exist, according to the above definition, two other polygons :math:`P'` and :math:`Q'` of equal area, such that the polygon composed of :math:`P` and :math:`P'` shall be of equal area with the polygon formed by combining the polygons :math:`Q` and :math:`Q'`. From the two equations

.. math::

   \begin{aligned}
   F(P+P') &= F(Q + Q') \\
   F(P') &= F(Q'),
   \end{aligned}

we easily deduce the equation

.. math::

   F(P) = F(Q);

that is to say, *polygons of equal content have also equal measure of area*.

From this last statement, we obtain immediately the proof of theorem 28. If we denote the equal bases of the two triangles by :math:`g` and the corresponding altitudes by :math:`h` and :math:`h'`, respectively, then we may conclude from the assumed equality of content of the two triangles that they must also have equal measures of area; that is to say, it follows that

.. math::

   \frac{1}{2}gh = \frac{1}{2}gh'

and, consequently, dividing by :math:`\frac{1}{2}g`, we get

.. math::

   h = h',

which is the statement made in theorem 28.

.. toctree::
   :hidden:

   de
   summary
   notes
