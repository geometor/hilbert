:layout: book

.. _grundlagen-chapter-3-en:

Chapter III: The Theory of Proportion
=====================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-en-s13:

.. folio:: § 13
   :page: 37

§ 13. Complex Number-Systems
----------------------------

At the beginning of this chapter, we shall present briefly certain preliminary ideas concerning complex number systems which will later be of service to us in our discussion.

The real numbers form, in their totality, a system of things having the following properties:

**THEOREMS OF CONNECTION (1–12).**

**1.** From the number $a$ and the number $b$, there is obtained by “addition” a definite number $c$, which we express by writing

$$
a+b= c  \text{or}  c=a+b.
$$

**2.** There exists a definite number, which we call $0$, such that, for every number $a$, we have

$$
a+0= a  \text{and}  0 + a = a.
$$

**3.** If $a$ and $b$ are two given numbers, there exists one and only one number $x$, and also one and only one number $y$, such that we have respectively

$$
a+x = b,\ y+a=b.
$$

**4.** From the number $a$ and the number $b$, there may be obtained in another way, namely, by “multiplication,” a definite number $c$, which we express by writing

$$
ab = c  \text{or}  c = ab.
$$

**5.** There exists a definite number, called $1$, such that, for every number $a$, we have

$$
a\cdot 1 = a  \text{and}  1 \cdot a = a.
$$

**6.** If $a$ and $b$ are any arbitrarily given numbers, where $a$ is different from $0$, then there exists one and only one number $x$ and also one and only one number $y$ such that we have respectively

$$
ax = b,\,ya=b.
$$

If $a$, $b$, $c$ are arbitrary numbers, the following laws of operation always hold: $$
\begin{aligned}
\mathbf{7.}\quad a + (b + c) &= (a + b) + c \\
\mathbf{8.}\quad a + b &= b + a \\
\mathbf{9.}\quad a(bc) &= (ab)c \\
\mathbf{10.}\quad a(b + c) &= ab + ac \\
\mathbf{11.}\quad (a + b)c &= ac + bc \\
\mathbf{12.}\quad ab &= ba.
\end{aligned}
$$

**THEOREMS OF ORDER (13–16).**

**13.** If $a$, $b$ are any two distinct numbers, one of these, say $a$, is always greater ($>$) than the other. The other number is said to be the smaller of the two. We express this relation by writing

$$
a > b  \text{and}  b < a.
$$

**14.** If $a > b$ and $b > c$, then is also $a > c$.

**15.** If $a > b$, then is also $a+c > b+ c$ and $c+a > c+b$.

**16.** If $a > b$ and $c>0$, then is also $ac>bc$ and $ca > cb$.

**THEOREM OF ARCHIMEDES (17).**

**17.** If $a$, $b$ are any two arbitrary numbers, such that $a > 0$ and $b > 0$, it is always possible to add $a$ to itself a sufficient number of times so that the resulting sum shall have the property that

$$
a+a+a+ \cdots + a > b.
$$

A system of things possessing only a portion of the above properties (1–17) is called a *complex number system*, or simply a *number system*. A number system is called *archimedean*, or *non-archimedean*, according as it does, or does not, satisfy condition (17).

Not every one of the properties (1–17) given above is independent of the others. The problem arises to investigate the logical dependence of these properties. Because of their great importance in geometry, we shall, in §§ 32, 33, pp. 101–106, answer two definite questions of this character. We will here merely call attention to the fact that, in any case, the last of these conditions (17) is not a consequence of the remaining properties, since, for example, the complex number system $\Omega(t)$, considered in § 12, possesses all of the properties (1–16), but does not fulfil the law stated in (17).

.. _grundlagen-en-s14:

.. folio:: § 14
   :page: 40

§ 14. Demonstration of Pascal's Theorem
---------------------------------------

In this and the following chapter, we shall take as the basis of our discussion all of the plane axioms with the exception of the axiom of Archimedes; that is to say, the axioms I, 1–2 and II–IV. In the present chapter, we propose, by aid of these axioms, to establish Euclid's theory of proportion; that is, *we shall establish it for the plane and that independently of the axiom of Archimedes*.

For this purpose, we shall first demonstrate a proposition which is a special case of the well known theorem of Pascal usually considered in the theory of conic sections, and which we shall hereafter, for the sake of brevity, refer to simply as Pascal's theorem. This theorem may be stated as follows:

.. _grundlagen-en-thm-21:

**Theorem 21.** (Pascal's theorem.) Given the two sets of points $A$, $B$, $C$ and $A'$, $B'$, $C'$ so situated respectively upon two intersecting straight lines that none of them fall at the intersection of these lines. If $CB'$ is parallel to $BC'$ and $CA'$ is also parallel to $AC'$, then $BA'$ is parallel to $AB'$. [#fn1]_

In order to demonstrate this theorem, we shall first introduce the following notation. In a right triangle, the base $a$ is uniquely determined by the hypotenuse $c$ and the base angle $\alpha$ included by $a$ and $c$.  We will express this fact briefly by writing

$$
a=\alpha c.
$$

Hence, the symbol $\alpha c$ always represents a definite segment, providing $c$ is any given segment whatever and $\alpha$ is any given acute angle.

Furthermore, if $c$ is any arbitrary segment and $\alpha$, $\beta$ are any two acute angles whatever, then the two segments $\alpha \beta c$ and $\beta \alpha c$ are always congruent; that is, we have

$$
\alpha \beta c = \beta \alpha c,
$$

and, consequently, the symbols $\alpha$ and $\beta$ are interchangeable.

In order to prove this statement, we take the segment $c = AB$, and with $A$ as a vertex lay off upon the one side of this segment the angle $\alpha$ and upon the other the angle $\beta$. Then, from the point $B$, let fall upon the opposite sides of the $\alpha$ and $\beta$ the perpendiculars $BC$ and $BD$, respectively. Finally, join $C$ with $D$ and let fall from $A$ the perpendicular $AE$ upon $CD$.

Since the two angles $ACB$ and $ADB$ are right angles, the four points $A$, $B$, $C$, $D$ are situated upon a circle. Consequently, the angles $ACD$ and $ABD$, being inscribed in the same segment of the circle, are congruent. But the angles $ACD$ and $CAE$, taken together, make a right angle, and the same is true of the two angles $ABD$ and $BAD$. Hence, the two angles $CAE$ and $BAD$ are also congruent; that is to say,

$$
\angle CAE \equiv \beta
$$

and, therefore,

$$
\angle DAE \equiv \alpha.
$$

From these considerations, we have immediately the following congruences of segments:

$$
\begin{array}{rclrcl}
\beta c  & \equiv & AD, & \alpha c & \equiv & AC, \\
\alpha \beta c & \equiv & \alpha(AD) \equiv AE, & \beta \alpha c & \equiv & \beta(AC) \equiv AE. \\
\end{array}
$$

From these, the validity of the congruence in question follows.

Returning now to the figure in connection with Pascal's theorem, denote the intersection of the two given straight lines by $O$ and the segments $OA$, $OB$, $OC$, $OA'$, $OB'$, $OC'$, $CB'$, $BC'$, $CA'$, $AC'$, $BA'$, $AB'$ by $a$, $b$, $c$, $a'$, $b'$, $c'$, $l$, $l^{*}$, $m$, $m^{*}$, $n$, $n^{*}$, respectively.

Let fall from the point $O$ a perpendicular upon each of the segments $l$, $m$, $n$. The perpendicular to $l$ will form with the straight lines $OA$ and $OA'$ acute angles, which we shall denote by $\lambda'$ and $\lambda$, respectively. Likewise, the perpendiculars to $m$ and $n$ form with these same lines $OA$ and $OA'$ acute angles, which we shall denote by $\mu'$, $\mu$ and $\nu'$, $\nu$, respectively. If we now express, as indicated above, each of these perpendiculars in terms of the hypotenuse and base angle, we have the three following congruences of segments: $$
\begin{aligned}
(1)\quad \lambda b' &\equiv \lambda' c, \\
(2)\quad \mu a' &\equiv \mu' c, \\
(3)\quad \nu a' &\equiv \nu' b.
\end{aligned}
$$

But since, according to our hypothesis, $l$ is parallel to $l^{*}$ and $m$ is parallel to $m^{*}$, the perpendiculars from $O$ falling upon $l^{*}$ and $m^{*}$ must coincide with the perpendiculars from the same point falling upon $l$ and $m$, and consequently, we have $$
\begin{aligned}
(4)\quad \lambda c' &\equiv \lambda' b, \\
(5)\quad \mu c' &\equiv \mu' a.
\end{aligned}
$$

Multiplying both members of congruence (3) by the symbol $\lambda' \mu$, and remembering that, as we have already seen, the symbols in question are commutative, we have

$$
\nu \lambda' \mu a' \equiv \nu' \mu \lambda' b.
$$

In this congruence, we may replace $\mu a'$ in the first member by its value given in (2) and $\lambda' b$ in the second member by its value given in (4), thus obtaining as a result

$$
\nu \lambda' \mu' c \equiv \nu' \mu \lambda c',
$$

or

$$
\nu \mu' \lambda' c \equiv \nu' \lambda \mu c'.
$$

Here again in this congruence we can, by aid of (1), replace $\lambda' c$ by $\lambda b'$, and, by aid of (5), we may replace in the second member $\mu c'$ by $\mu' a$. We then have

$$
\nu\mu'\lambda b' \equiv \nu'\lambda\mu' a,
$$

or

$$
\lambda\mu'\nu b' \equiv \lambda\mu'\nu' a.
$$

Because of the significance of our symbols, we can conclude at once from this congruence that

$$
\mu'\nu b' \equiv \mu'\nu' a,
$$

and, consequently, that $$
(6)\quad \nu b' \equiv \nu' a.
$$

If now we consider the perpendicular let fall from $O$ upon $n$ and draw perpendiculars to this same line from the points $A$ and $B'$, then congruence (6) shows that the feet of the last two perpendiculars must coincide; that is to say, the straight line $n^{*} = AB'$ makes a right angle with the perpendicular to $n$ and, consequently, is parallel to $n$. This establishes the truth of Pascal's theorem.

Having given any straight line whatever, together with an arbitrary angle and a point lying outside of the given line, we can, by constructing the given angle and drawing a parallel line, find a straight line passing through the given point and cutting the given straight line at the given angle. By means of this construction, we can demonstrate Pascal's theorem in the following very simple manner, for which, however, I am indebted to another source.

Through the point $B$, draw a straight line cutting $OA'$ in the point $D'$ and making with it the angle $OCA'$, so that the congruence

$$
(1^*)\quad \angle OCA' \equiv \angle OD'B
$$

is fulfilled. Now, according to a well known property of circles, $CBD'A'$ is an inscribed quadrilateral, and, consequently, by aid of the theorem concerning the congruence of angles inscribed in the same segment of a circle, we have the congruence

$$
(2^*)\quad \angle OBA' \equiv \angle OD'C.
$$

Since, by hypothesis, $CA'$ and $AC'$ are parallel, we have

$$
(3^*)\quad \angle OCA' \equiv \angle OAC',
$$

and from $(1^*)$ and $(3^*)$ we obtain the congruence

$$
\angle OD'B \equiv \angle OAC'.
$$

However, $BAD'C'$ is also an inscribed quadrilateral, and, consequently, by virtue of the theorem relating to the angles of such a quadrilateral, we have the congruence

$$
(4^*)\quad \angle OAD' \equiv \angle OC'B.
$$

But as $CB'$ is, by hypothesis, parallel to $BC'$, we have also $$
(5^*)\quad \angle OB'C \equiv \angle OC'B.
$$

From $(4^*)$ and $(5^*)$, we obtain the congruence

$$
\angle OAD' \equiv \angle OB'C,
$$

which shows that $CAD'B'$ is also an inscribed quadrilateral, and, hence, the congruence

$$
(6^*)\quad \angle OAB' \equiv \angle OD'C,
$$

is valid. From $(2^*)$ and $(6^*)$, it follows that

$$
\angle OBA' \equiv \angle OAB',
$$

and this congruence shows that $BA'$ and $AB'$ are parallel as Pascal's theorem demands. In case $D'$ coincides with one of the points $A'$, $B'$, $C'$, it is necessary to make a modification of this method, which evidently is not difficult to do.

.. picture:: /_static/figures/fig_pascal_orthogonal.svg
   :alt: Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.
   :caption: **Affine Pascal's (Pappus's) Hexagon Theorem (Theorem 21).** Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.


.. _grundlagen-en-s15:

.. folio:: § 15
   :page: 46

§ 15. An Algebra of Segments, Based Upon Pascal's Theorem
---------------------------------------------------------

Pascal's theorem, which was demonstrated in the last section, puts us in a position to introduce into geometry a method of calculating with segments, in which all of the rules for calculating with real numbers remain valid without any modification.

Instead of the word “congruent” and the sign $\equiv$, we make use, in the algebra of segments, of the word “equal” and the sign $=$.

If $A, B, C$ are three points of a straight line and if $B$ lies between $A$ and $C$, then we say that $c = AC$ is the *sum* of the two segments $a=AB$ and $b=BC$. We indicate this by writing

$$
c=a+b.
$$

The segments $a$ and $b$ are said to be smaller than c, which fact we indicate by writing

$$
a<c,\ b<c.
$$

On the other hand, $c$ is said to be larger than $a$ and $b$, and we indicate this by writing

$$
c>a,\ c>b.
$$

From the linear axioms of congruence (axioms IV, 1–3), we easily see that, for the above definition of addition of segments, the associative law

$$
a+(b+c)=(a+b)+c,
$$

as well as the commutative law

$$
a+b = b+a
$$

is valid.

In order to define geometrically the product of two segments $a$ and $b$, we shall make use of the following construction. Select any convenient segment, which, having been selected, shall remain constant throughout the discussion, and denote the same by $1$. Upon the one side of a right angle, lay off from the vertex $O$ the segment $1$ and also the segment $b$. Then, from $O$ lay off upon the other side of the right angle the segment $a$. Join the extremities of the segments $1$ and $a$ by a straight line, and from the extremity of $b$ draw a line parallel to this straight line. This parallel will cut off from the other side of the right angle a segment $c$. We call this segment $c$ the *product* of the segments $a$ and $b$, and indicate this relation by writing

$$
c=ab.
$$

% required for correct placement of Figure 23

We shall now demonstrate that, for this definition of the multiplication of segments, the *commutative* law

$$
ab=ba
$$

holds. For this purpose, we construct in the above manner the product $ab$. Furthermore, lay off from $0$ upon the first side (I) of the right angle the segment $a$ and upon the other side (II) the segment $b$. Connect by a straight line the extremity of the segment $1$ with the extremity of $b$, situated on II, and draw through the endpoint of $a$, on I, a line parallel to this straight line. This parallel will determine, by its intersection with the side II, the segment $ba$. But, because the two dotted lines are, by Pascal's theorem, parallel, the segment $ba$ just found coincides with the segment $ab$ previously constructed, and our proposition is established. In order to show that the *associative* law

$$
a(bc)=(ab)c
$$

holds for the multiplication of segments, we construct first of all the segment $d=be$, then $da$, after that the segment $e=ba$, and finally $ec$. By virtue of Pascal's theorem, the extremities of the segments $da$ and $ec$ coincide, as may be clearly seen from figure 24.

If now we apply the commutative law which we have just demonstrated, we obtain the above formula, which expresses the associative law for the multiplication of two segments.

Finally, *the distributive* law

$$
a(b+c) = ab+ac
$$

also holds for our algebra of segments. In order to demonstrate this, we construct the segments, $ab$, $ac$,

and $a(b+c)$, and draw through the extremity of the segment $c$ (Fig. 25) a straight line parallel to the other side of the right angle. From the congruence of the two right-angled triangles which are shaded in the figure and the application of the theorem relating to the equality of the opposite sides of a parallelogram, the desired result follows. If $b$ and $c$ are any two arbitrary segments, there is always a segment $a$ to be found such that $c=ab$. This segment $a$ is denoted by $\frac{c}{b}$ and is called the *quotient* of $c$ by $b$.

.. picture:: /_static/figures/fig_segment_multiplication.svg
   :alt: Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.
   :caption: **Hilbert's Segment Multiplication c = ab and Commutativity ab = ba (§ 15).** Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.


.. picture:: /_static/figures/fig_segment_distributive.svg
   :alt: Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.
   :caption: **Geometric Proof of the Distributive Law a(b + c) = ab + ac (§ 15).** Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.


.. _grundlagen-en-s16:

.. folio:: § 16
   :page: 50

§ 16. Proportion and the Theorems of Similitude
-----------------------------------------------

By aid of the preceding algebra of segments, we can establish Euclid's theory of proportion in a manner free from objections and without making use of the axiom of Archimedes.

If $a,b,a',b'$ are any four segments whatever, the proportion

$$
a:b=a':b'
$$

expresses nothing else than the validity of equation

$$
ab'=ba'.
$$

**Definition**. Two triangles are called *similar* when the corresponding angles are congruent.

.. _grundlagen-en-thm-22:

**Theorem 22.** If $a,b$ and $a',b'$ are homologous sides of two similar triangles, we have the proportion

$$
a:b=a':b'
$$

**Proof.** We shall first consider the special case where the angle included between $a$ and $b$ and the one included between $a'$ and $b'$ are right angles.

Moreover, we shall assume that the two triangles are laid off in one and the same right angle. Upon one of the sides of this right angle, we lay off from the vertex $0$ the segment $1$, and through the extremity of this segment, we draw a straight line parallel to the hypotenuses of the two triangles.

This parallel determines upon the other side of the right angle a segment $e$. Then, according to our definition of the product of two segments, we have

$$
b = ea,\ b' = ea',
$$

from which we obtain

$$
ab'=ba',
$$

that is to say,

$$
a:b=a':b'.
$$

Let us now return to the general case. In each of the two similar triangles, find the point of intersection of the bisectors of the three angles. Denote these points by $S$ and $S'$. From these points let fall upon the sides of the triangles the perpendiculars $r$ and $r'$, respectively. Denote the segments thus determined upon the sides of the triangles by

$$
a_b, a_c, b_c, b_a, c_a, c_b
$$

and

$$
a'_b, a'_c, b'_c, b'_a, c'_a, c'_b,
$$

respectively. The special case of our proposition, demonstrated above, gives us then the following proportions:

$$
\begin{aligned}
a_b:r = a'_b:r', &\; \ \; b_c:r=b'_c:r', \\
a_c:r = a'_c:r', &\; \ \; b_a:r=b'_a:r'.
\end{aligned}
$$

By aid of the distributive law, we obtain from these proportions the following:

$$
a: r = a': r, \quad  b: r = b': r'.
$$

Consequently, by virtue of the commutative law of multiplication, we have

$$
a:b=a':b'.
$$

From the theorem just demonstrated, we can easily deduce the fundamental theorem in the theory of proportion. This theorem may be stated as follows:

.. _grundlagen-en-thm-23:

**Theorem 23.** If two parallel lines cut from the sides of an arbitrary angle the segments $a,b$ and $a',b'$ respectively, then we have always the proportion

$$
a: b = a': b'.
$$

Conversely, if the four segments $a,b,a',b$ fulfill this proportion and if $a,a'$ and $b,b'$ are laid off upon the two sides respectively of an arbitrary angle, then the straight lines joining the extremities of $a$ and $b$ and of $a'$ and $b'$ are parallel to each other.

.. _grundlagen-en-s17:

.. folio:: § 17
   :page: 53

§ 17. Equations of Straight Lines and of Planes
-----------------------------------------------

To the system of segments already discussed, let us now add a second system. We will distinguish the segments of the new system from those of the former one by means of a special sign, and will call them “*negative*” segments in contradistinction to the “*positive*” segments already considered. If we introduce also the segment $O$, which is determined by a single point, and make other appropriate conventions, then all of the rules deduced in § 13 for calculating with real numbers will hold equally well here for calculating with segments. We call special attention to the following particular propositions:

* We have always $a\cdot 1 = 1\cdot a=a$.

* If $a\cdot b=0$, then either $a=0$, or $b=0$.

* If $a>b$ and $c>0$, then $ac>bc$.

In a plane $\alpha$, we now take two straight lines cutting each other in $O$ at right angles as the fixed axes of rectangular co-ordinates, and lay off from $O$ upon these two straight lines the arbitrary segments $x$ and $y$. We lay off these segments upon the one side or upon the other side of $O$, according as they are positive or negative. At the extremities of $x$ and $y$, erect perpendiculars and determine the point $P$ of their intersection. The segments $x$ and $y$ are called the co-ordinates of $P$. Every point of the plane $\alpha$ is uniquely determined by its co-ordinates $x$, $y$, which may be positive, negative, or zero.

Let $l$ be a straight line in the plane $\alpha$, such that it shall pass through $O$ and also through a point $C$ having the co-ordinates $a,b$. If $x,y$ are the co-ordinates

of any point on $l$, it follows at once from theorem 22 that

$$
a: b = x: y,
$$

or

$$
bx-ay = 0,
$$

is the equation of the straight line $l$. If $l'$ is a straight line parallel to $l$ and cutting off from the $x$-axis the segment $c$, then we may obtain the equation of the straight line $l'$ by replacing, in the equation for $l$, the segment $x$ by the segment $x-c$. The desired equation will then be of the form

$$
bx-ay-bc=0.
$$

From these considerations, we may easily conclude, independently of the axiom of Archimedes, that every straight line of a plane is represented by an equation which is linear in the co-ordinates $x$, $y$, and, conversely, every such linear equation represents a straight line when the co-ordinates are segments appertaining to the geometry in question. The corresponding results for the geometry of space may be easily deduced.

The remaining parts of geometry may now be developed by the usual methods of analytic geometry.

So far in this chapter, we have made absolutely no use of the axiom of Archimedes. If now we assume the validity of this axiom, we can arrange a definite correspondence between the points on any straight line in space and the real numbers. This may be accomplished in the following manner.

We first select on a straight line any two points, and assign to these points the numbers $0$ and $1$. Then, bisect the segment $(0,1)$ thus determined and denote the middle point by the number $\frac{1}{2}$. In the same way, we denote the middle of $(0, \frac{1}{2})$ by $\frac{1}{4}$, etc. After applying this process $n$ times, we obtain a point which corresponds to $\frac{1}{2^n}$.  Now, lay off $m$ times in both directions from the point $O$ the segment $(O,\frac{1}{2^n})$. We obtain in this manner a point corresponding to the numbers $\frac{m}{2^n})$ and $-\frac{m}{2^n})$. From the axiom of Archimedes, we now easily see that, upon the basis of this association, to each arbitrary point of a straight line there corresponds a single, definite, real number, and, indeed, such that this correspondence possesses the following property: If $A$, $B$, $C$ are any three points on a straight line and $\alpha$, $\beta$, $\gamma$ are the corresponding real numbers, and, if $B$ lies between $A$ and $C$, then one of the inequalities,

$$
\alpha<\beta<\gamma\  \text{or} \ \alpha>\beta>\gamma,
$$

is always fulfilled.

From the development given in § 9, p. 27, it is evident, that to every number belonging to the field of

algebraic numbers $\Omega$, there must exist a corresponding point upon the straight line. Whether to every real number there corresponds a point cannot in general be established, but depends upon the geometry to which we have reference.

However, it is always possible to generalize the original system of points, straight lines, and planes by the addition of “ideal” or “irrational” elements, so that, upon any straight line of the corresponding geometry, a point corresponds without exception to every system of three real numbers. By the adoption of suitable conventions, it may also be seen that, in this generalized geometry, all of the axioms I–V are valid. This geometry, generalized by the addition of irrational elements, is nothing else than the ordinary analytic geometry of space.


----

.. rubric:: Footnotes

.. [#fn1] F. Schur has published in the *Math. Ann.*, Vol. 51, a very interesting proof of the theorem of Pascal, based upon the axioms I–II, IV.
