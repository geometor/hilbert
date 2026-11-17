:layout: book
:canonical_id: § 14
:breadcrumb_title: § 14
:order: 14
:folio: p. 40
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s14:

.. folio:: § 14
   :page: 40

§ 14: Demonstration of Pascal's Theorem
=======================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

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

.. [#fn1] F. Schur has published in the *Math. Ann.*, Vol. 51, a very interesting proof of the theorem of Pascal, based upon the axioms I–II, IV.

.. toctree::
   :hidden:

   de
   summary
   notes
