:layout: book
:canonical_id: § 23
:breadcrumb_title: § 23
:order: 23
:folio: § 23
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s23:

.. folio:: § 23
   :page: 74

§ 23: The Impossibility of Demonstrating Desargues's Theorem for the Plane Without the Help of the Axioms of Congruence
=======================================================================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

We shall now investigate the question whether or no in plane geometry Desargues's theorem may be deduced without the assistance of the axioms of congruence. This leads us to the following result:

.. _grundlagen-en-thm-33:

**Theorem 33.** A plane geometry exists in which the axioms I 1–2, II–III, IV 1–5, V, that is to say, all linear and all plane axioms with the exception of axiom IV, 6 of congruence, are fulfilled, but in which the theorem of Desargues (theorem 32) is not valid. Desargues's theorem is not, therefore, a consequence solely of the axioms mentioned; for, its demonstration necessitates either the space axioms or all of the axioms of congruence.

**Proof.** Select in the ordinary plane geometry (the possibility of which has already been demonstrated in § 9, pp. 27–30) any two straight lines perpendicular to each other as the axes of $x$ and $y$. Construct about the origin $O$ of this system of co-ordinates an ellipse having the major and minor axes equal to 1 and $\frac{1}{2}$, respectively. Finally, let $F$ denote the point situated upon the positive $x$-axis at the distance $\frac{3}{2}$ from $O$. Consider all of the circles which cut the ellipse in four real points. These points may be either distinct or in any way coincident. Of all the points situated upon these circles, we shall attempt to determine the one which lies upon the $x$-axis farthest from the origin. For this purpose, let us begin with an arbitrary circle cutting the ellipse in four distinct points and intersecting the positive $x$-axis in the point $C$. Suppose this circle then turned about the point $C$ in such a manner that two or more of the four points of intersection with the ellipse finally coincide in a single point $A$, while the rest of them remain real. Increase now the resulting tangent circle in such a way that $A$ always remains a point of tangency with the ellipse. In this way we obtain a circle which is either tangent to the ellipse in also a second point $B$, or which has with the ellipse a four-point contact in $A$. Moreover, this circle cuts the positive $x$-axis in a point more remote than $C$. The desired farthest point will accordingly be found among those points of intersection of the positive $x$-axis by circles lying exterior to the ellipse and being doubly tangent to it. All such circles must lie, as we can easily see, symmetrically with respect to the $y$-axis. Let $a$, $b$ be the co-ordinates of any point on the ellipse. Then an easy calculation shows that the circle, which is symmetrical with respect to $y$-axis and tangent to the ellipse at this point, cuts off from the positive $x$-axis the segment

$$
x = \mid \sqrt{1 + 3b^2} \mid.
$$

The greatest possible value of this expression occurs for $b = \frac{1}{2}$ and, hence, is equal to $\frac{1}{2}\mid\sqrt{7}\mid$. Since the point on the $x$-axis which we have denoted by $F$ has for its abscissa the value $\frac{3}{2} > \frac{1}{2} \mid\sqrt{7}\mid$, it follows that *among the circles cutting the ellipse four times there is certainly none which passes through the point $F$.*

We will now construct a new plane geometry in the following manner. As points in this new geometry, let us take the points of the $(xy)$-plane. We will define a straight line of our new geometry in the following manner. Every straight line of the $(xy)$-plane which is either tangent to the fixed ellipse, or does not cut it at all, is taken unchanged as a straight line of the new geometry. However, when any straight line $g$ of the $(xy)$-plane cuts the ellipse, say in the points $P$ and $Q$, we will then define the corresponding

straight line of the new geometry as follows. Construct a circle passing through the points $P$ and $Q$ and the fixed point $F$. From what has just been said, this circle will have no other point in common with the ellipse. We will now take the broken line, consisting of the arc $PQ$ just mentioned and the two parts of the straight line $g$ extending outward indefinitely from the points $P$ and $Q$, as the required straight line in our new geometry. Let us suppose all of the broken lines constructed which correspond to straight lines of the $(xy)$-plane. We have then a system of broken lines which, considered as straight lines of our new geometry, evidently satisfy the axioms I, 1–2 and III. By a convention as to the actual arrangement of the points and the straight lines in our new geometry, we have also the axioms II fulfilled.

Moreover, we will call two segments $AB$ and $A'B'$ congruent in this new geometry, if the broken line extending between $A$ and $B$ has equal length, in the ordinary sense of the word, with the broken line extending from $A'$ to $B'$.

Finally, we need a convention concerning the congruence of angles. So long as neither of the vertices of the angles to be compared lies upon the ellipse, we call the two angles congruent to each other, if they are equal in the ordinary sense. In all other cases we make the following convention. Let $A, B, C$ be points which follow one another in this order upon a straight line of our new geometry, and let $A', B', C'$ be also points which lie in this order upon another straight line of our new geometry. Let $D$ be a point lying outside of the straight line $ABC$ and $D'$ be a point outside of the straight $A'B'C'$. We will now say that, in our new geometry, the angles between these straight lines fulfill the congruences

$$
\angle ABD \equiv \angle A'B'D'  \text{and}  \angle CBD \equiv \angle C'B'D'
$$

whenever the natural angles between the corresponding broken lines of the ordinary geometry fulfill the proportion

$$
\angle ABD: \angle CBD = \angle A'B'D' : \angle C'B'D'.
$$

These conventions render the axioms IV, 1–5 and V valid.

In order to see that Desargues's theorem does not hold for our new geometry, let us consider the following three ordinary straight lines of the $(xy)$-plane; viz., the axis of $x$, the axis of $y$, and the straight line joining the two points of the ellipse $(\frac{3}{5},\frac{2}{5})$ and $(-\frac{3}{5},-\frac{2}{5})$. Since these three ordinary straight lines pass through the origin, we can easily construct two triangles so that their vertices shall lie respectively upon these three straight lines and their homologous sides shall be parallel and all three sides shall lie exterior to the ellipse. As we may see from figure 40, or show

by an easy calculation, the broken lines arising from the three straight lines in question do not intersect in a common point. Hence, it follows that Desargues's theorem certainly does not hold for this particular plane geometry in which we have constructed the two triangles just considered.

This new geometry serves at the same time as an example of a plane geometry in which the axioms I, 1–2, II–III, IV, 1–5, V all hold, but which cannot be considered as a part of a geometry of space.

.. picture:: /_static/figures/fig_non_desarguesian_plane.svg
   :alt: Theorem 33: Euclidean lines cutting the ellipse are replaced inside the boundary by circular arcs through F, satisfying planar I 1–2, II, III, IV 1–5, V while violating Desargues.
   :caption: **Hilbert's 1899 Non-Desarguesian Plane via Ellipse Arc Refraction (§ 23).** Theorem 33: Euclidean lines cutting the ellipse are replaced inside the boundary by circular arcs through F, satisfying planar I 1–2, II, III, IV 1–5, V while violating Desargues.

.. toctree::
   :hidden:

   de
   summary
   notes
