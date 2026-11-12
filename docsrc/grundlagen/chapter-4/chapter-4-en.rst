:layout: book

.. _grundlagen-chapter-4-en:

Chapter IV: The Theory of Plane Areas
=====================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-en-s18:

.. folio:: § 18
   :page: 57

§ 18. Equal Area and Equal Content of Polygons
----------------------------------------------

We shall base the investigations of the present chapter upon the same axioms as were made use of in the last chapter, §§ 13–17, namely, upon the plane axioms of all the groups, with the single exception of the axiom of Archimedes. This involves then the axioms I, 1–2 and II–IV.

The theory of proportion as developed in §§ 13–17 together with the algebra of segments introduced in the same chapter, puts us now in a position to establish Euclid's theory of areas by means of the axioms already mentioned; that is to say, *for the plane geometry, and that independently of the axiom of Archimedes.*

Since, by the development given in the last chapter, pp. 37–56, the theory of proportion was made to depend essentially upon Pascal's theorem (theorem 21), the same may then be said here of the theory of areas. This manner of establishing the theory of areas seems to me a very remarkable application of Pascal's theorem to elementary geometry.

If we join two points of a polygon $P$ by any arbitrary broken line lying entirely within the polygon, we shall obtain two new polygons $P_1$ and $P_2$ whose interior points all lie within $P$. We say that $P$ is *decomposed into* $P_1$ and $P_2$, or that the polygon $P$ is *composed of* $P_1$ and $P_2$.

**Definition.** Two polygons are said to be of *equal area* when they can be decomposed into a finite number of triangles which are respectively congruent to one another in pairs.

**Definition.** Two polygons are said to be of *equal content* when it is possible, by the addition of other polygons having equal area, to obtain two resulting polygons having equal area.

From these definitions, it follows at once that by combining polygons having equal area, we obtain as a result polygons having equal area. However, if from polygons having equal area we take polygons having equal area, we obtain polygons which are of equal content.

Furthermore, we have the following propositions:

.. _grundlagen-en-thm-24:

**Theorem 24.** If each of two polygons $P_1$ and $P_2$ is of equal area to a third polygon $P_3$ then $P_1$ and $P_2$ are themselves of equal area. If each of two polygons is of equal content to a third, then they are themselves of equal content.

**Proof.** By hypothesis, we can so decompose each of the polygons $P_1$ and $P_2$ into such a system of triangles that any triangle of either of these systems will be congruent to the corresponding triangle of a system into which $P_3$ may be decomposed. If we consider simultaneously the two decompositions of $P_3$ we see that, in general, each triangle of the one decomposition is broken up into polygons by the segments which belong to the other decomposition. Let ms add to these segments a sufficient number of others to reduce each of these polygons to triangles, and apply the two resulting methods of decompositions to $P_1$ and $P_2$, thus breaking them up into corresponding triangles. Then, evidently the two polygons $P_1$ and $P_2$ are each decomposed into the same number of triangles, which are respectively congruent by pairs. Consequently, the two polygons are, by definition, of equal area.

The proof of the second part of the theorem follows without difficulty.

We define, in the usual manner, the terms: *rectangle*, *base* and *height of a parallelogram*, *base* and *height of a triangle*.

% required for correct placement of Figures 30 and 31

.. _grundlagen-en-s19:

.. folio:: § 19
   :page: 60

§ 19. Parallelograms and Triangles Having Equal Bases and Equal Altitudes
-------------------------------------------------------------------------

The well known reasoning of Euclid, illustrated by the accompanying figure, furnishes a proof for the following theorem:

.. _grundlagen-en-thm-25:

**Theorem 25.** Two parallelograms having equal bases and equal altitudes are also of equal content.

We have also the following well known proposition:

.. _grundlagen-en-thm-26:

**Theorem 26.** Any triangle $ABC$ is always of equal area to a certain parallelogram having an equal base and an altitude half as great as that of the triangle.

**Proof.** Bisect $AC$ in $D$ and $BC$ in $E$, and extend the line $DE$ to $F$, making $EF$ equal to $DE$. Then, the triangles $DEC$ and $FBE$ are congruent to each other, and, consequently, the triangle $ABC$ and the parallelogram $ABFD$ are of equal area.

From theorems 25 and 26, we have at once, by aid of theorem 24, the following proposition.

.. _grundlagen-en-thm-27:

**Theorem 27.** Two triangles having equal bases and equal altitudes have also equal content.

It is usual to show that two triangles having equal bases and equal altitudes are always of equal area. It is to be remarked, however, that *this demonstration cannot be made without the aid of the axiom of Archimedes.* In fact, we may easily construct in our non-archimedean geometry (see § 12, p. 34) two triangles so that they shall have equal bases and equal altitudes and, consequently, by theorem 27, must be of equal content, but which are not, however, of equal area. As such an example, we may take the two triangles $ABC$ and $ABD$ having each the base $AB=1$ and the altitude $1$, where the vertex of the first triangle is situated perpendicularly above $A$, and in the second triangle the foot $F$ of the perpendicular let fall from the vertex $D$ upon the base is so situated that $AF=t$. The remaining propositions of elementary geometry concerning the equal content of polygons, and in particular the pythagorean theorem, are all simple consequences of the theorems which we have already given. In the further development of the theory of area, we meet, however, with an essential difficulty. In fact, the discussion so far leaves it still in doubt whether all polygons are not, perhaps, of equal content. In this case, all of the propositions which we have given would be devoid of meaning and hence of no value. Furthermore, the more general question also arises as to whether two rectangles of equal content and having one side in common, do not also have their other sides congruent; that is to say, whether a rectangle is not definitely determined by means of a side and its area. As a closer investigation shows, in order to answer this question, we need to make use of the converse of theorem 27. This may be stated as follows:

.. _grundlagen-en-thm-28:

**Theorem 28.** If two triangles have equal content and equal bases, they have also equal altitudes.

This fundamental theorem is to be found in the first book of Euclid's Elements as proposition 39. In the demonstration of this theorem, however, Euclid appeals to the general proposition relating to magnitudes: “$K \alpha \grave{\iota} \ \tau \grave{o} \ \check{o} \lambda o \upsilon \ \tau o \hat{\nu} \ \mu \acute{\epsilon} \rho o \upsilon \varsigma \ \mu \epsilon \hat{\iota} \zeta \acute{o} \nu \ \grave{\epsilon} \sigma \tau \iota \nu$”—a method of procedure which amounts to the same thing as introducing a new geometrical axiom concerning areas.

It is now possible to establish the above theorem and hence the theory of areas in the manner we have proposed, that is to say, with the help of the plane axioms and without making use of the axiom of Archimedes. In order to show this, it is necessary to introduce the idea of the measure of area.

.. picture:: /_static/figures/fig_polygon_equivalence.svg
   :alt: Euclid I.35 reconstructed in § 19: parallelograms ABCD and AB'C'D are inhaltsgleich unconditionally, though flächengleich (zerlegungsgleich) requires Archimedes.
   :caption: **Equicomplementability (Inhaltsgleichheit) of Parallelograms on Equal Base (§ 19).** Euclid I.35 reconstructed in § 19: parallelograms ABCD and AB'C'D are inhaltsgleich unconditionally, though flächengleich (zerlegungsgleich) requires Archimedes.


.. _grundlagen-en-s20:

.. folio:: § 20
   :page: 63

§ 20. The Measure of Area of Triangles and Polygons
---------------------------------------------------

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

.. _grundlagen-en-s21:

.. folio:: § 21
   :page: 67

§ 21. Equality of Content and the Measure of Area
-------------------------------------------------

In § 20 we have found that polygons having equal content have also equal measures of area. The converse of this is also true.

In order to prove the converse, let us consider two triangles $ABC$ and $AB'C'$ having a common right angle at $A$. The measures of area of these two triangles are expressed by the formulæ

$$
\begin{aligned}
F(ABC) &= \frac{1}{2}AB \cdot AC, \\
F(AB'C') &= \frac{1}{2}AB' \cdot AC'.
\end{aligned}
$$

We now assume that these measures of area are equal to each other, and consequently we have

$$
AB \cdot AC = AB' \cdot AC',
$$

or

$$
AB:AB' = AC':AC.
$$

From this proposition, it follows, according to theorem 23, that the two straight lines $BC'$ and $B'C$ are parallel, and hence, by theorem 27, the two triangles $BC'B'$ and $BC'C$ are of equal content. By the addition of the triangle $ABC'$, it follows that the two triangles $ABC$ and $AB'C'$ are of equal content. We have then shown that two right triangles having the same measure of area are always of equal content.

Take now any arbitrary triangle having the base $g$ and the altitude $h$. Then, according to theorem 27, it has equal content with a right triangle having the two sides $g$ and $h$. Since the original triangle had evidently the same measure of area as the right triangle, it follows that, in the above consideration, the restriction to right triangles was not necessary. Hence, two *arbitrary triangles with equal measures of area are also of equal content*.

Moreover, let us suppose $P$ to be any polygon having the measure of area $g$ and let $P$ be decomposed into $n$ triangles having respectively the measures of area $g_1$, $g_2$, $g_3$, $\ldots$, $g_n$. Then, we have

$$
g = g_1 + g_2 + g_3 + \cdots + g_n.
$$

Construct now a triangle $ABC$ having the base $AB=g$ and the altitude $h = 1$. Take, upon the base of this triangle, the points $A_1$, $A_2$, $\ldots$, $A_{n-1}$ so that $g_1=AA_1$, $g_1=A_1A_2$, $\ldots$, $g_{n-1}=A_{n-2}A_{n-1}$, $g_n=A_{n-1}B$.

Since the triangles composing the polygon $P$ have respectively the same measures of area as the triangles $AA_1C$, $A_1A_2C$, $\ldots$, $A_{n-2}A_{n-1}C$, $A_{n-1}BC$, it follows from what has already been demonstrated that they have also the same content as these triangles. Consequently, the polygon $P$ and a triangle, having the base $g$ and the altitude $h = 1$ are of equal content. From this, it follows, by the application of theorem 24, that two polygons having equal measures of area are always of equal content.

We can now combine the proposition of this section with that demonstrated in the last, and thus obtain the following theorem:

.. _grundlagen-en-thm-30:

**Theorem 30.** Two polygons of equal content have always equal measures of area. Conversely, two polygons having equal measures of area are always of equal content.

In particular, if two rectangles are of equal content and have one side in common, then their remaining sides are respectively congruent. Hence, we have the following proposition:

.. _grundlagen-en-thm-31:

**Theorem 31.** If we decompose a rectangle into several triangles by means of straight lines and then omit one of these triangles, we can no longer make up completely the rectangle from the triangles which remain.

This theorem has been demonstrated by F. Schur [#fn1]_ and by W. Killing, [#fn2]_ but by making use of the axiom of Archimedes. By O. Stolz, [#fn3]_ it has been regarded as an axiom. In the foregoing discussion, it has been shown that it is completely independent of the axiom of Archimedes. However, when we disregard the axiom of Archimedes, this theorem (31) is not sufficient of itself to enable us to demonstrate Euclid's theorem concerning the equality of altitudes of triangles having equal content and equal bases. (Theorem 28.)

In the demonstration of theorems 28, 29, and 30, we have employed essentially the algebra of segments introduced in § 15, p. 46, and as this depends substantially upon Pascal's theorem (theorem 21), we see that this theorem is really the corner-stone in the theory of areas. We may, by the aid of theorems 27 and 28, easily establish the converse of Pascal's theorem.

Of two polygons $P$ and $Q$, we call $P$ the smaller or larger in content according as the measure of area

$F(P)$ is less or greater than the measure of area $F(Q)$. From what has already been said, it is clear that the notions, equal content, smaller content, larger content, are mutually exclusive. Moreover, we easily see that a polygon, which lies wholly within another polygon, must always be of smaller content than the exterior one.

With this we have established the important theorems in the theory of areas.


----

.. rubric:: Footnotes

.. [#fn1] *Sitzungsberichte der Dorpater Naturf. Ges.* 1892.

.. [#fn2] *Grundlagen der Geometrie*, Vol. 2, Chapter 5, § 5, 1898.

.. [#fn3] *Monatshefte für Math, und Phys.* 1894.
