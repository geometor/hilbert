:layout: book

.. _grundlagen-chapter-5-en:

Chapter V: Desargues's Theorem
==============================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-en-s22:

.. folio:: § 22
   :page: 71

§ 22. Desargues's Theorem and Its Demonstration for Plane Geometry by Aid of the Axioms of Congruence
-----------------------------------------------------------------------------------------------------

Of the axioms given in §§ 1–8, pp. 1–26, those of groups II–V are in part linear and in part plane axioms. Axioms 3–7 of group I are the only space axioms. In order to show clearly the significance of these axioms of space, let us assume a plane geometry and investigate, in general, the conditions for which this plane geometry may be regarded as a part of a geometry of space in which at least the axioms of groups I–III are all fulfilled.

Upon the basis of the axioms of groups I–III, it is well known that the so-called theorem of Desargues may be easily demonstrated. This theorem relates to points of intersection in a plane. Let us assume in particular that the straight line, upon which are situated the points of intersection of the homologous sides of the two triangles, is the straight line which we call the straight line at infinity. We will designate the theorem which arises in this case, together with its converse, as the theorem of Desargues. This theorem is as follows:

.. _grundlagen-en-thm-32:

**Theorem 32.** (Desargues's theorem.) When two triangles are so situated in a plane that their homologous sides are respectively parallel, then the lines joining the homologous vertices pass through one and the same point, or are parallel to one another.

Conversely, if two triangles are so situated in a plane that the straight lines joining the homologous vertices intersect in a common point, or are parallel to one another, and, furthermore, if two pairs of homologous sides are parallel to each other, then the third sides of the two triangles are also parallel to each other.

As we have already mentioned, theorem 32 is a consequence of the axioms I–III. Because of this fact, the validity of Desargues's theorem in the plane is, in any case, a necessary condition that the geometry of this plane may be regarded as a part of a geometry of space in which the axioms of groups I–III are all fulfilled.

Let us assume, as in §§ 13–21, pp. 37–70, that we have a plane geometry in which the axioms I, 1–2 and II–IV all hold and, also, that we have introduced in this geometry an algebra of segments conforming to § 15.

Now, as has already been established in § 17, there may be made to correspond to each point in the plane a pair of segments $(x, y)$ and to each straight line a ratio of three segments $(u:v:w)$, so that the linear equation

$$
ux+vy+w=0
$$

expresses the condition that the point is situated upon the straight line. The system composed of all the segments in our geometry forms, according to § 17, a domain of numbers for which the properties (1–16), enumerated in § 13, are valid. We can, therefore, by means of this domain of numbers, construct a geometry of space in a manner similar to that already employed in § 9 or in § 12, where we made use of the systems of numbers $\Omega$ and $\Omega(t)$, respectively. For this purpose, we assume that a system of three segments $(x, y, z)$ shall represent a point, and that the ratio of four segments $(u:v:w:r)$ shall represent a plane, while a straight line is defined as the intersection of two planes. Hence, the linear equation

$$
ux+vy+wz+r = 0
$$

expresses the fact that the point $(x, y, z)$ lies in the plane $(u: v: w: r)$. Finally, we determine the arrangement of the points upon a straight line, or the points of a plane with respect to a straight line situated in this plane, or the arrangement of the points in space with respect to a plane, by means of inequalities in a manner similar to the method employed for the plane in § 9.

Since we obtain again the original plane geometry by putting $z=0$, we know that our plane geometry can be regarded as a part of geometry of space. Now, the validity of Desargues's theorem is, according to the above considerations, a necessary condition for this result.  Hence, in the assumed plane geometry, it follows that Desargues's theorem must also hold.

It will be seen that the result just stated may also be deduced without difficulty from theorem 23 in the theory of proportion.

.. picture:: /_static/figures/fig_desargues_configuration.svg
   :alt: Theorem 32: triangles ABC and A'B'C' perspective from O with AB ∥ A'B' and BC ∥ B'C' satisfy AC ∥ A'C'.
   :caption: **Affine Desargues Configuration of Perspective Triangles (Theorem 32).** Theorem 32: triangles ABC and A'B'C' perspective from O with AB ∥ A'B' and BC ∥ B'C' satisfy AC ∥ A'C'.


.. _grundlagen-en-s23:

.. folio:: § 23
   :page: 74

§ 23. The Impossibility of Demonstrating Desargues's Theorem for the Plane Without the Help of the Axioms of Congruence
-----------------------------------------------------------------------------------------------------------------------

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


.. _grundlagen-en-s24:

.. folio:: § 24
   :page: 79

§ 24. Introduction of an Algebra of Segments Based Upon Desargues's Theorem and Independent of the Axioms of Congruence
-----------------------------------------------------------------------------------------------------------------------

In order to see fully the significance of Desargues's theorem (theorem 32), let us take as the basis of our consideration a plane geometry where all of the axioms I 1–2, II–III are valid, that is to say, where all of the plane axioms of the first three groups hold, and then introduce into this geometry, in the following manner, a new algebra of segments independent of the axioms of congruence.

Take in the plane two fixed straight lines intersecting in $O$, and consider only such segments as have $O$ for their origin and their other extremity in one of the fixed lines. We will regard the point $O$ itself as a segment and call it the segment $O$. We will indicate this fact by writing

$$
OO = 0,  \text{or}  0 = OO.
$$

Let $E$ and $E'$ be two definite points situated respectively upon the two fixed straight lines through $O$. Then, define the two segments $OE$ and $OE'$ as the segment 1 and write accordingly

$$
OE = OE' = 1  \text{or}  1 = OE = OE'.
$$

We will call the straight line $EE'$, for brevity, the unit-line. If, furthermore, $A$ and $A'$ are points upon

the straight lines $OE$ and $OE'$, respectively, and, if the straight line $AA'$ joining them is parallel to $EE'$, then we will say that the segments OA and OA' are equal to one another, and write

$$
OA=OA'  \text{or}  OA'=OA.
$$

In order now to define the sum of the segments $a=OA$ and $b= OB$, we construct $AA'$ parallel to the unit-line $EE'$ and draw through $A'$ a parallel to $OE$ and through $B$ a parallel to $OE'$. Let these two parallels intersect in $A''$. Finally, draw through $A''$ a straight line parallel to the unit-line $EE'$. Let this parallel cut the two fixed lines $OE$ and $OE'$ in $C$ and $C'$ respectively. Then $c=OC= OC'$ is called the *sum* of the segments $a=OA$ and $b=OB$. We indicate this by writing

$$
c=a+b,  \text{or}  a+b=c.
$$

In order to define the product of a segment $a=OA$ by a segment $b=OB$, we make use of exactly the same construction as employed in § 15, except that, in place of the sides of a right angle, we make use here of the straight lines $OE$ and $OE'$.

The construction is consequently as follows. Determine upon $OE'$ a point $A'$ so that $AA'$ is parallel to the unit-line $EE'$, and join $E$ with $A'$. Then draw through $B$ a straight line parallel to $EA'$. This parallel will intersect the fixed straight line $OE'$ in the point $C'$, and we call $c=OC'$ the product of the segment $a = OA$ by the segment $b = OB$. We indicate this relation by writing

$$
c = ab,  \text{or}  ab = c.
$$

.. _grundlagen-en-s25:

.. folio:: § 25
   :page: 82

§ 25. The Commutative and the Associative Law of Addition for Our New Algebra of Segments
-----------------------------------------------------------------------------------------

In this section, we shall investigate the laws of operation, as enumerated in § 13, in order to see which of these hold for our new algebra of segments, when we base our considerations upon a plane geometry in which axioms I 1–2, II–III are all fulfilled, and, moreover, in which Desargues's theorem also holds.

First of all, we shall show that, for the addition of segments as defined in § 24, the commutative law

$$
a+ b = b+a
$$

holds. Let

$$
\begin{aligned}
 &\; a = OA = OA' \;  \\
 &\; b = OB = OB' \; 
\end{aligned}
$$

Hence, $AA'$ and $BB'$ are, according to our convention, parallel to the unit-line. Construct the points $A''$ and $B''$ by drawing $A'A''$ and $B'B''$ parallel to $OA$ and also $AB''$ and $BA'$ parallel to $OA$. We see at once that the line $A''B''$ is parallel to $AA'$ as the commutative law requires. We shall show the validity of this statement by the aid of Desargues's theorem in the following manner. Denote the point of intersection of $AB''$ and $A'A''$ by $F$ and that of $BA''$ and $B'B''$ by $D$. Then, in the triangles $AA'F$ and $BB'D$, the homologous sides are parallel to each other. By Desargues's theorem, it follows that the three points $O$, $F$, $D$ lie in a straight line. In consequence of this condition, the two triangles $OAA'$ and $DB''A''$ lie in such a way that the lines joining the corresponding vertices pass through the same point $F$, and since the homologous sides $OA$ and $DB''$, as also $OA'$ and $DA''$, are parallel to each other, then, according to the second part of Desargues's theorem (theorem 32), the third sides $AA'$ and $B''A''$ are parallel to each other.

To prove the associative law of addition

$$
a+(b+c)=(a+b)+c,
$$

we shall make use of figure 44. In consequence of the commutative law of addition just demonstrated, the above formula states that the straight line $A''B''$ must be parallel to the unit-line.

The validity of this statement is evident, since the shaded part of figure 44 corresponds exactly with figure 43.

.. picture:: /_static/figures/fig_desargues_segment_algebra.svg
   :alt: Constructing c = a + b and c = ab on fixed axes OX, OY with unit line EE' purely from incidence, parallels, and Desargues's Theorem without Congruence.
   :caption: **Projective-Affine Segment Addition and Skew-Field Multiplication (§§ 24–26).** Constructing c = a + b and c = ab on fixed axes OX, OY with unit line EE' purely from incidence, parallels, and Desargues's Theorem without Congruence.


.. _grundlagen-en-s26:

.. folio:: § 26
   :page: 84

§ 26. The Associative Law of Multiplication and the Two Distributive Laws for the New Algebra of Segments
---------------------------------------------------------------------------------------------------------

The associative law of multiplication

$$
a(bc)=(ab)c
$$

has also a place in our new algebra of segments.

Let there be given upon the first of the two fixed straight lines through $O$ the segments

$$
1 = OA, \quad b = OC, \quad c=OA'
$$

and upon the second of these straight lines, the segments

$$
a=OG,\quad  b=OB.
$$

In order to construct the segments

$$
\begin{aligned}
bc &= OB',\  \text{and} \ bc=OC', \\
ab &= OD, \\
(ab) c &= OD',
\end{aligned}
$$

in accordance with § 24, draw $A'B'$ parallel to $AB$, $B'C'$ parallel to $BC$, $CD$ parallel to $AG$, and $A'D'$ parallel to $AD$. We see at once that the given law amounts to the same as saying that $CD$ must also be parallel to $C'D'$. Denote the point of intersection of the straight lines $A'D'$ and $B'C'$ by $F'$ and that of the straight lines $AD$ and $BC$ by $F$. Then the triangles $ABF$ and $A'B' F'$ have their homologous sides parallel to each other, and, according to Desargues's theorem, the three points $O$, $F$, $F'$ must lie in a straight line. Because of these conditions, we can apply the second part of Desargues's theorem to the two triangle $CDF$ and $C' D'F'$, and hence show that, in fact, $CD$ is parallel to $C'D'$.

Finally, upon the basis of Desargues's theorem, we shall show that the two distributive laws

$$
a (b+c) = ab+ac
$$

and

$$
(a+b)c = ac+bc
$$

hold for our algebra of segments.

In the proof of the first one of these laws, we shall make use of figure 46. [#fn1]_ In this figure, we have

$$
\begin{array}{c}
b = OA', c=OC', \\
ab=OB', ab=OA'', ac=OC'', etc.
\end{array}
$$

In the same figure, $B'' D_2$ is parallel to $C''D_1$ which is parallel to the fixed straight line $OA'$, and $B'D_1$ is parallel to $C'D_2$, which is parallel to the fixed straight line $OA''$. Moreover, we have $A' A''$ parallel to $C'C''$, and $A'B''$ parallel to $B' A''$, parallel to $F'D_2$, parallel to $F''D_1$.

Our proposition amounts to asserting that we must necessarily have also

$F'F''$ parallel to $A'A''$ and to $C'C''$.

We construct the following auxiliary lines:

| $F''J$ parallel to the fixed straight line $OA'$,
| $F'J$ parallel to the fixed straight line $OA''$.

Let us denote the points of intersection of the straight lines $C''D_1$ and $C'D_2$, $C''D_1$ and $F'J$, $C'D_2$ and $F''J$ by $G$, $H_1$, $H_2$, respectively. Finally, we obtain the other auxiliary lines indicated in the figure by joining the points already constructed.

In the two triangles $A' B'' C''$ and $F'D_2G$, the straight lines joining homologous vertices are parallel to each other. According to the second part of Desargues's theorem, it follows, therefore, that

$A'C''$ is parallel to $F' G$.

In the two triangles $A'C''F''$ and $F'GH_2$, the straight lines joining the homologous vertices are also parallel to each other. From the properties already demonstrated, it follows by virtue of the second part of Desargues's theorem that we must have

$A'F''$ parallel to $F'H_2$.

Since in the two horizontally shaded triangles $OA'F'$ and $JH_2F'$ the homologous sides are parallel, Desargues's theorem shows that the three straight lines joining the homologous vertices, viz.:

$$
OJ,\ A'H_2,\ F''F'
$$

all intersect in one and the same point, say in $P$.

In the same way, we have necessarily

$$
A''F'  \text{parallel to}  F''H_1
$$

and since, in the two obliquely shaded triangles $OA''F'$ and $JH_1F''$, the homologous sides are parallel, then, in consequence of Desargues's theorem, the three straight lines joining the homologous vertices, viz.:

$$
OJ, A''H_1, F'F''
$$

all intersect likewise in the same point, namely, in point $P$.

Moreover, in the triangles $OA'A''$ and $JH_2H_1$, the straight lines joining the homologous vertices all pass through this same point $P$, and, consequently, it follows that we have

$$
H_1H_2  \text{parallel to}  A'A'',
$$

and, therefore,

$$
H_1H_2  \text{parallel to}  C'C'',
$$

Finally, let us consider the figure $F''H_2C'C''H_1F'F''$. Since, in this figure, we have

$$
\begin{aligned}
F''H_2  \text{parallel to} &\; C'F', \; \text{parallel to}  C''H_1, \\
GH_2C' \quad \text{" "}\quad &\; F''C'', \; \text{" "}\quad H_1F', \\
C'C''  \quad \text{" "}\quad &\; H_1H_2, \; 
\end{aligned}
$$

we recognize here again figure 43, which we have already made use of in § 25 to prove the commutative law of addition. The conclusions, analogous to those which we reached there, show that we must have

$$
F'F''  \text{parallel to}  H_1H_2
$$

and, consequently, we must have also

$$
F'F''  \text{parallel to}  A'A'',
$$

which result concludes our demonstration.

To prove the second formula of the distributive law, we make use of an entirely different figure,–figure 47. In this figure, we have

$$
1 = OD,\ a = OA,\ a = OB,\ b = OG,\ c = OD',
$$

$$
ac = OA',\ ac = OB',\ BC = OG', \text{etc.} ,
$$

and, furthermore, we have

| $GH$ parallel to $G'H'$, parallel to the fixed line $OA$,
| $GH$ parallel to $A'H'$, parallel to the fixed line $OB$,

We have also

$$
\begin{aligned}
AB &\; \text{parallel to} \; A'B' \\
BD &\; \text{" "} \; B'D' \\
DG &\; \text{" "} \; D'G' \\
HJ &\; \text{" "} \; H'J'.
\end{aligned}
$$

That which we are to prove amounts, then, to demonstrating that

$$
DJ  \text{must be parallel to}  D'J'.
$$

Denote the points in which $BD$ and $GD$ intersect the straight line $AH$ by $C$ and $F$, respectively, and the points in which $B'D'$ and $G'D'$ intersect the straight line $A'H'$ by $C'$ and $F'$, respectively. Finally, draw the auxiliary lines $FJ$ and $F'J'$, indicated in the figure by dotted lines.

In the triangles $ABC$ and $A'B'C'$, the homologous sides are parallel and, consequently, by Desargues's theorem the three points $O$, $C$, $C'$ lie on a straight line. Then, by considering in the same way the triangles $CDF$ and $CD'F'$, it follows that the points $O$, $F$, $F'$ lie upon the same straight line and likewise, from a consideration of the triangles $FGH$ and $F'G'H'$, we find the points $O$, $H$, $H'$ to be situated on a straight line. Now, in the triangles $FHJ$ and $F'H'J'$, the straight lines joining the homologous vertices all pass through the same point $O$, and, hence, as a consequence of the second part of Desargues's theorem, the straight lines $FJ$ and $F'J'$ must also be parallel to each other. Finally, a consideration of the triangles $DFJ$ and $D'F'J'$ shows that the straight lines $DJ$ and $D'J'$ are parallel to each other and with this our proof is completed.

.. _grundlagen-en-s27:

.. folio:: § 27
   :page: 90

§ 27. Equation of the Straight Line, Based Upon the New Algebra of Segments
---------------------------------------------------------------------------

In §§ 24–26, we have introduced into the plane geometry an algebra of segments in which the commutative law of addition and that of multiplication, as well as the two distributive laws, hold. This was done upon the assumption that the axioms cited in § 24, as also the theorem of Desargues, were valid. In this section, we shall show how an analytical representation of the point and straight line in the plane is possible upon the basis of this algebra of segments.

**Definition.** Take the two given fixed straight lines lying in the plane and intersecting in $O$ as the axis of $x$ and of $y$, respectively. Let us suppose any point $P$ of the plane determined by the two segments $x$, $y$ which we obtain upon the $x$-axis and $y$-axis, respectively, by drawing through $P$ parallels to these axes. These segments are called the *co-ordinates* of the point $P$. Upon the basis of this new algebra of segments and by aid of Desargues's theorem, we shall deduce the following proposition.

.. _grundlagen-en-thm-34:

**Theorem 34.** The co-ordinates $x$, $y$ of a point on an arbitrary straight line always satisfy an equation in these segments of the form

$$
ax+by+c = 0.
$$

In this equation, the segments $a$ and $b$ stand necessarily to the left of the co-ordinates $x$ and $y$. The segments $a$ and $b$ are never both zero and $c$ is an arbitrary segment.

Conversely, every equation in these segments and of this form represents always a straight line in the plane geometry under consideration.

**Proof.** Suppose that the straight line $l$ passes through the origin $O$. Furthermore, let $C$ be a definite point upon $l$ different from $O$, and $P$ any arbitrary point of $l$. Let $OA$ and $OB$ be the co-ordinates of $C$ and $x$, $y$ be the co-ordinates of $P$. We will denote the straight line joining the extremities of the segments $x$, $y$ by $g$. Finally, through the extremity of the segment $1$, laid off on the $x$-axis, draw a straight line $h$ parallel to $AB$. This parallel cuts off upon the $y$-axis the segment $e$. From the second part of

Desargues's theorem, it follows that the straight line $g$ is also always parallel to $AB$. Since $g$ is always parallel to $h$, it follows that the co-ordinates $x$, $y$ of the point $P$ must satisfy the equation

$$
ex=g.
$$

Moreover, in figure 49 let $l'$ be any arbitrary straight line in our plane. This straight line will cut off on the $x$-axis the segment $c=OO'$. Now, in the same figure, draw through $O$ the straight line $l$ parallel to $l'$. Let $P'$ be an arbitrary point on the line $l'$. The straight line through $P'$, parallel to the $x$-axis, intersects the straight line $l$ in $P$ and cuts off upon the $y$-axis the segment $y = OB$. Finally, through $P$ and $P'$ let parallels to the $y$-axis cut off on the $x$-axis the segments $x=OA$ and $x'= OA'$.

We shall now undertake to show that the equation

$$
x'=x+c
$$

is fulfilled by the segments in question. For this purpose, draw $O'C$ parallel to the unit-line and likewise $CD$ parallel to the $x$-axis and $AD$ parallel to the $y$-axis.

Then, to prove our proposition amounts to showing that we must have necessarily

$$
A'D  \text{parallel to}  O'C.
$$

Let $D'$ be the point of intersection of the straight lines $CD$ and $A'P'$ and draw $O'C'$ parallel to the $y$-axis.

Since, in the triangles $OCP$ and $O'C'P'$, the straight lines joining the homologous vertices are parallel, it follows, by virtue of the second part of Desargues's theorem, that we must have

$$
CP  \text{parallel to}  C'P'.
$$

In a similar way, a consideration of the triangles $ACP$ and $A'C'P'$ shows that we must have

$$
AC  \text{parallel to}  A'C'.
$$

Since, in the triangles $ACD$ and $C'A'O'$, the homologous sides are parallel to each other, it follows that the straight lines $AC'$, $CA'$ and $DO'$ intersect in a common point. A consideration of the triangles $C'A'D$ and $ACO'$ then shows that $A'D$ and $CO'$ are parallel to each other. From the two equations already obtained, viz.:

$$
ex = y   \text{and}  x' = x + c,
$$

follows at once the equation

$$
ex' = y + ec.
$$

If we denote, finally, by $n$ the segment which added to the segment 1 gives the segment 0, then, from this last equation, we may easily deduce the following

$$
ex' + ny + nec = 0,
$$

and this equation is of the form required by theorem 34.

We can now show that the second part of the theorem is equally true; for, every linear equation

$$
ax + by + c = 0
$$

may evidently be brought into the required form

$$
ex + ny + nec = 0
$$

by a left-sided multiplication by a properly chosen segment.

It must be expressly stated, however, that, by our hypothesis, an equation of segments of the form

$$
xa + yb + c = 0,
$$

where the segments $a$, $b$ stand to the right of the co-ordinates $x$, $y$ does not, in general, represent a straight line.

In Section 30, we shall make an important application of theorem 34.

.. _grundlagen-en-s28:

.. folio:: § 28
   :page: 95

§ 28. The Totality of Segments Regarded as a Complex Number System
------------------------------------------------------------------

We see immediately that, for the new algebra of segments established in Section 24, theorems 1–6 of Section 13 are fulfilled. Moreover, by aid of Desargues's theorem, we have already shown in Sections 25 and 26 that the laws 7–11 of operation, as given in Section 13, are all valid in this algebra of segments. With the single exception of the commutative law of multiplication, therefore, all of the theorems of connection hold.

Finally, in order to make possible an order of magnitude of these segments, we make the following convention. Let $A$ and $B$ be any two distinct points of the straight line $OE$. Suppose then that the four points $O$, $E$, $A$, $B$ stand, in conformity with axiom II, 4, in a certain sequence. If this sequence is one of the following six possible ones, viz.:

$$
ABOE, AOBE, AOEB, OABE, OAEB, OEAB,
$$

then we will call the segment $a = OA$ *smaller* than the segment $b = OB$ and indicate the same by writing

$$
a < b.
$$

On the other hand, if the sequence is one of the six following ones, viz.:

$$
BAOE, BOAE, BOEA, OBAE, OBEA, OEBA,
$$

then we will call the segment $a = OA$ greater than the segment $b = OB$, and we write accordingly

$$
a > b.
$$

This convention remains in force whenever $A$ or $B$ coincides with $O$ or $E$, only then the coinciding points are to be regarded as a single point, and, consequently, we have only to consider the order of three points.

Upon the basis of the axioms of group II, we can easily show also that, in our algebra of segments, the laws 13–16 of operation given in Section 13 are fulfilled. Consequently, the totality of all the different segments forms a complex number system for which the laws 1–11, 13–16 of Section 13 hold; that is to say, all of the usual laws of operation except the commutative law of multiplication and the theorem of Archimedes. We will call such a system, briefly, a *desarguesian number system.*

.. _grundlagen-en-s29:

.. folio:: § 29
   :page: 97

§ 29. Construction of a Geometry of Space by Aid of a Desarguesian Number System
--------------------------------------------------------------------------------

Suppose we have given a desarguesian number system $D$. Such a system makes possible the construction of a geometry of space in which axioms I, II, III are all fulfilled.

In order to show this, let us consider any system of three numbers $(x, y, z)$ of the desarguesian number system $D$ as a point, and the ratio of four such numbers $(u:v:w:r)$, of which the first three are not 0, as a plane. However, the systems $(u:v:w:r)$ and $(au:av:aw:ar)$, where $a$ is any number of $D$ different from 0, represent the same plane. The existence of the equation

$$
ux + vy + wz + r = 0
$$

expresses the condition that the point $(x, y, z)$ shall lie in the plane $(u:v:w:r)$. Finally, we define a straight line by the aid of a system of two planes $(u':v':w':r')$ and $(u'':v'':w'':r'')$, where we impose the condition that it is impossible to find in $D$ two numbers $a'$, $a''$ different from zero, such that we have simultaneously the relations

$$
a'u' = a''u'', a'v' = a''v'', a'w' = a''w'',
$$

A point $(x, y, z)$ is said to be situated upon this straight line $[(u':v':w':r'), (u'':v'':w'':r'')]$, if it is common to the two planes $(u':v':w':r')$ and $(u'':v'':w'':r'')$. Two straight lines which contain the same points are not regarded as being distinct.

By application of the laws 1–11 of § \! 13, which by hypothesis hold for the numbers of $D$, we obtain without difficulty the result that the geometry of space which we have just constructed satisfies all of the axioms of groups I and III.

In order that the axioms (II) of order may also be valid, we adopt the following conventions. Let

$$
(x_1, y_1, z_1), (x_2, y_2, z_2), (x_3, y_3, z_3)
$$

be any three points of a straight line

$$
[(u':v':w':r'), (u'':v'':w'':r'')].
$$

Then, the point $(x_2, y_2, z_2)$ is said to lie between the other two, if we have fulfilled at least one of the six following double inequalities:

$$
\begin{aligned}
 &\; x_1 < x_2 < x_3, \; x_1 > x_2 > x_3, \\
% \tag{1} &\; y_1 < y_2 < y_3, \; y_1 > y_2 > y_3, \\
% \tag{2} &\; z_1 < z_2 < z_3, \; z_1 > z_2 > z_3,
\end{aligned}
$$

If one of the two double inequalities (1) exists, then we can easily conclude that either $y_1 = y_2 = y_3$ or one of the two double inequalities (2) exists, and, consequently, either $z_1 = z_2 = z_3$ or one of the double inequalities (3) must exist. In fact, from the equations

$$
\begin{aligned}
u'x_i +  v'y_i +  w'z_i +  r' & =  0,\\
u''x_i +  v''y_i +  w''z_i +  r'' & =  0,\\
(i = 1,2,3)
\end{aligned}
$$

we may obtain, by a left-sided multiplication of these equations by numbers suitably chosen from $D$ and then adding the resulting equations, a system of equations of the form

$$
u'''x_i + v'''y_i + r''' = 0, (i = 1, 2, 3).
$$

In this system, the coefficient $v'''$ is certainly different from zero, since otherwise the three numbers $x_1$, $x_2$, $x_3$ would be mutually equal.

From

$$
x_1 \lessgtr x_2 \lessgtr x_3,
$$

it follows that

$$
u'''x_1 \lesseqgtr x'''u_2 \lesseqgtr x'''u_3,
$$

and, hence, as a consequence of (4), we have

$$
v'''y_1 + r''' \lesseqgtr v'''y_2 + r''' \lesseqgtr
v'''y_3 + r'''
$$

and, therefore,

$$
v'''y_1 \lesseqgtr v'''y_2 \lesseqgtr v'''y_3.
$$

Since $v'''$ is different from zero, we have

$$
y_1 \lesseqgtr y_2 \lesseqgtr y_3.
$$

In each of these double inequalities, we must take either the upper sign throughout, or the middle sign throughout, or the lower sign throughout.

The preceding considerations show, that, in our geometry, the linear axioms II, 1–4 of order are all valid. However, it remains yet to show that, in this geometry, the plane axiom II, 5 is also valid.

For this purpose let a plane $(u:v:w:r)$ and a straight line $[(u:v:w:r), (u':v':w':r')]$ in this plane be given. Let us assume that all the points $(x, y, z)$ of the plane $(u:v:w:r)$, for which we have the expression $u'x + v'y + w'z + r'$ greater than or less than zero, lie respectively upon the one side or upon the other side of the given straight line. We have then only to show that this convention is in accordance with the preceding statements. This, however, is easily done. We have thus shown that all of the axioms of groups I, II, III are fulfilled in the geometry of space which we have obtained in the above indicated manner from the desarguesian number system *D*. Remembering now that the theorem of Desargues is a consequence of the axioms I, II, III, we see that the proposition just stated is exactly the converse of the result reached in Section 28.

.. _grundlagen-en-s30:

.. folio:: § 30
   :page: 101

§ 30. Significance of Desargues's Theorem
-----------------------------------------

If, in a plane geometry, axioms I, 1–2, II, III are all fulfilled and, moreover, if the theorem of Desargues holds, then, according to §§ 24–28, it is always possible to introduce into this geometry an algebra of segments to which the laws 1–11, 13–16 of § \! 13 are applicable. We will now consider the totality of these segments as a complex number system and construct, upon the basis of this system, a geometry of space, in accordance with § \! 29, in which all of the axioms I, II, III hold.

In this geometry of space, we shall consider only the points $(x, y, 0)$ and those straight lines upon which only such points lie. We have then a plane geometry which must, if we take into account the proposition established in § \! 27, coincide exactly with the plane geometry proposed at the beginning. Hence, we are led to the following proposition, which may be regarded as the objective point of the entire discussion of the present chapter.

.. _grundlagen-en-thm-35:

**Theorem 35.** If, in a plane geometry, axioms I, 1–2, II, III are all fulfilled, then the existence of Desargues's theorem is the necessary and sufficient condition that this plane geometry may be regarded as a part of a geometry of space in which all of the axioms I, II, III are fulfilled.

The theorem of Desargues may be characterized for plane geometry as being, so to speak, the result of the elimination of the space axioms.

The results obtained so far put us now in the position to show that every geometry of space in which axioms I, II, III are all fulfilled may be always regarded as a part of a “geometry of any number of dimensions whatever.” By a geometry of an arbitrary number of dimensions is to be understood the totality of all points, straight lines, planes, and other linear elements, for which the corresponding axioms of connection and of order, as well as the axiom of parallels, are all valid.


----

.. rubric:: Footnotes

.. [#fn1] Figures 46, 47, and 48 were designed by Dr. Von Schaper, as have also the details of the demonstrations relating to these figures.
