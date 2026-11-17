:layout: book
:canonical_id: § 20
:breadcrumb_title: § 20
:order: 20
:folio: p. 63
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s20:

.. folio:: § 20
   :page: 63

§ 20: The Measure of Area of Triangles and Polygons
===================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

**Definition.**  If in a triangle $ABC$, having the sides $a$, $b$, $c$, we construct the two altitudes $h_a = AD$, $h_b = BE$, then, according to theorem 22, it follows from the similarity of the triangles $BCE$ and $ACD$, that we have the proportion

$$
a: h_b = b: ha;
$$

that is, we have

$$
a \cdot h_a = b \cdot h_b.
$$

This shows that the product of the base and the corresponding altitude of a triangle is the same whichever side is selected as the base. The half of this product of the base and the altitude of a triangle $\Delta$ is called the *measure of area of the triangle $\Delta$* and we denote it by $F(\Delta)$. A segment joining a vertex of a triangle with a point of the opposite side is called *a transversal.* A transversal divides the given triangle into two others having the same altitude and having bases which lie in the same straight line. Such a decomposition is called a *transversal decomposition of the triangle.*

.. _grundlagen-en-thm-29:

**Theorem 29.** If a triangle $\Delta$ is decomposed by means of arbitrary straight lines into a finite number of triangles $\Delta_k$, then the measure of area of $\Delta$ is equal to the sum of the measures of area of the separate triangles $\Delta_k$.

**Proof.** From the distributive law of our algebra of segments, it follows immediately that the measure of area of an arbitrary triangle is equal to the sum of the measures of area of two such triangles as arise from any transversal decomposition of the given triangle. The repeated application of this proposition shows that the measure of area of any triangle is equal to the sum of the measures of area of all the triangles arising by applying the transversal decomposition an arbitrary number of times in succession.

In order to establish the corresponding proof for an arbitrary decomposition of the triangle $\Delta$ into the triangles $\Delta_k$, draw from the vertex $A$ of the given triangle $\Delta$ a transversal through each of the points of division of the required decomposition; that is to say, draw a transversal through each vertex of the triangles $\Delta_k$. By means of these transversals, the given triangle $\Delta$ is decomposed into certain triangles $\Delta_t$. Each of these triangles $\Delta_t$ is broken up by the segments which determined this decomposition into certain triangles and quadrilaterals. If, now, in each of the quadrilaterals, we draw a diagonal, then each triangle $\Delta_t$ is decomposed into certain other triangles $\Delta_{ts}$. We shall now show that the decomposition into the triangles $\Delta_{ts}$ is for the triangles $\Delta_t$, as well as for the triangles $\Delta_k$, nothing else than a series of transversal decompositions. In fact, it is at once evident that any decomposition of a triangle into partial triangles may always be affected by a series of transversal decompositions, providing, in this decomposition, points of division do not exist within the triangle, and further, that at least one side of the triangle remains free from points of division.

We easily see that these conditions hold for the triangles $\Delta_t$. In fact, the interior of each of these triangles, as also one side, namely, the side opposite the point $A$, contains no points of division.

Likewise, for each of the triangles $\Delta_k$, the decomposition into $\Delta_{ts}$ is reducible to transversal decompositions. Let us consider a triangle $\Delta_k$. Among the transversals of the triangle $\Delta$ emanating from the point $A$, there is always a definite one to be found which either coincides with a side of $\Delta_k$, or which itself divides $\Delta_k$ into two triangles. In the first case, the side in question always remains free from further points of division by the decomposition into the triangles $\Delta_{ts}$. In the second case, the segment of the transversal contained within the triangle $\Delta_k$ is a side of the two triangles arising from the division, and this side certainly remains free from further points of division.

According to the considerations set forth at the beginning of this demonstration, the measure of area $F(\Delta)$ of the triangle $\Delta$ is equal to the sum of the measures of area $F(\Delta_t)$ of all the triangles $\Delta_t$ and this sum is in turn equal to the sum of all the measures of area $F(\Delta_{ts})$. However, the sum of the measures of area $F(\Delta_k)$ of all the triangles $\Delta_k$ is also equal to the sum of the measures of area $F(\Delta_{ts})$. Consequently, we have finally that the measure of area $F(\Delta)$ is also equal to the sum of all the measures of area $F(\Delta_k)$, and with this conclusion our demonstration is completed.

**Definition.** If we define the measure of area $F(P)$ of a polygon as the sum of the measures of area of all the triangles into which the polygon is, by a definite decomposition, divided, then upon the basis of theorem 29 and by a process of reasoning similar to that which we have employed in § 18 to prove theorem 24, we know that the measure of area of a polygon is independent of the manner of decomposition into triangles and, consequently, is definitely determined by the polygon itself. From this we obtain, by aid of theorem 29, the result that *polygons of equal area have also equal measures of area*.

Furthermore, if $P$ and $Q$ are two polygons of equal content, then there must exist, according to the above definition, two other polygons $P'$ and $Q'$ of equal area, such that the polygon composed of $P$ and $P'$ shall be of equal area with the polygon formed by combining the polygons $Q$ and $Q'$. From the two equations

$$
\begin{aligned}
F(P+P') &= F(Q + Q') \\
F(P') &= F(Q'),
\end{aligned}
$$

we easily deduce the equation

$$
F(P) = F(Q);
$$

that is to say, *polygons of equal content have also equal measure of area*.

From this last statement, we obtain immediately the proof of theorem 28. If we denote the equal bases of the two triangles by $g$ and the corresponding altitudes by $h$ and $h'$, respectively, then we may conclude from the assumed equality of content of the two triangles that they must also have equal measures of area; that is to say, it follows that

$$
\frac{1}{2}gh = \frac{1}{2}gh'
$$

and, consequently, dividing by $\frac{1}{2}g$, we get

$$
h = h',
$$

which is the statement made in theorem 28.

.. toctree::
   :hidden:

   de
   summary
   notes
