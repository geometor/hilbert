:layout: book

.. _grundlagen-chapter-2-en:

Chapter II: The Compatibility and Mutual Independence of the Axioms
===================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-en-s9:

.. folio:: § 9
   :page: 27

§ 9. Compatibility of the Axioms
--------------------------------

The axioms, which we have discussed in the previous chapter and have divided into five groups, are not contradictory to one another; that is to say, it is not possible to deduce from these axioms, by any logical process of reasoning, a proposition which is contradictory to any of them. To demonstrate this, it is sufficient to construct a geometry where all of the five groups are fulfilled.

To this end, let us consider a domain $\Omega$ consisting of all of those algebraic numbers which may be obtained by beginning with the number one and applying to it a finite number of times the four arithmetical operations (addition, subtraction, multiplication, and division) and the operation $\sqrt{1+\omega^2}$, where $\omega$ represents a number arising from the five operations already given.

Let us regard a pair of numbers $(x, y)$ of the domain $\Omega$ as defining a point and the ratio of three such numbers $(u:v:w)$ of $\Omega$, where $u$, $v$ are not both equal to zero, as defining a straight line. Furthermore, let the existence of the equation

$$
ux+vy+w = 0
$$

express the condition that the point $(x, y)$ lies on the

straight line $(u:v:w)$. Then, as one readily sees, axioms I, 1–2 and III are fulfilled. The numbers of the domain $\Omega$ are all real numbers. If now we take into consideration the fact that these numbers may be arranged according to magnitude, we can easily make such necessary conventions concerning our points and straight lines as will also make the axioms of order (group II) hold. In fact, if $(x_1,y_1)$, $(x_2, y_2)$, $(x_3, y_3)$, $\ldots$ are any points whatever of a straight line, then this may be taken as their sequence on this straight line, providing the numbers $x_1$, $x_2$, $x_3,\ldots,$ or the numbers $y_1$, $y_2$, $y_3, \ldots,$ either all increase or decrease in the order of sequence given here. In order that axiom II, 5 shall be fulfilled, we have merely to assume that all points corresponding to values of $x$ and $y$ which make $ux+vy+w$ less than zero or greater than zero shall fall respectively upon the one side or upon the other side of the straight line $(u:v:w)$. We can easily convince ourselves that this convention is in accordance with those which precede, and by which the sequence of the points on a straight line has already been determined.

The laying off of segments and of angles follows by the known methods of analytical geometry. A transformation of the form

$$
\begin{aligned}
x' &= x + a \\
y' &= y + b
\end{aligned}
$$

produces a translation of segments and of angles.

Furthermore, if, in the accompanying figure, we represent the point $(0, 0)$ by $O$ and the point $(1, 0)$ by $E$, then, corresponding to a rotation of the angle $COE$ about $O$ as a center, any point $(x, y)$ is transformed into another point $(x', y')$ so related that

$$
\begin{aligned}
x' &= \frac{a}{\sqrt{a^2+b^2}} x -  \frac{b}{\sqrt{a^2+b^2}}y , \\
y' &= \frac{b}{\sqrt{a^2+b^2}} x + \frac{a}{\sqrt{a^2+b^2}}y .
\end{aligned}
$$

Since the number

$$
\sqrt{a^2+b^2} = a \sqrt{ 1 + \left( \frac{b}{a} \right)^2 }
$$

belongs to the domain $\Omega$, it follows that, under the conventions which we have made, the axioms of congruence (group IV) are all fulfilled. The same is true of the axiom of Archimedes.

From these considerations, it follows that every contradiction resulting from our system of axioms must also appear in the arithmetic related to the domain $\Omega$.

The corresponding considerations for the geometry of space present no difficulties.

If, in the preceding development, we had selected the domain of all real numbers instead of the domain $\Omega$, we should have obtained likewise a geometry in which all of the axioms of groups I—V are valid. For the purposes of our demonstration, however, it was sufficient to take the domain $\Omega$, containing on an enumerable set of elements.

.. _grundlagen-en-s10:

.. folio:: § 10
   :page: 30

§ 10. Independence of the Axiom of Parallels (Non-Euclidean Geometry)
---------------------------------------------------------------------

Having shown that the axioms of the above system are not contradictory to one another, it is of interest to investigate the question of their mutual independence. In fact, it may be shown that none of them can be deduced from the remaining ones by any logical process of reasoning.

First of all, so far as the particular axioms of groups I, II, and IV are concerned, it is easy to show that the axioms of these groups are each independent of the other of the same group. [#fn1]_

According to our presentation, the axioms of groups I and II form the basis of the remaining axioms. It is sufficient, therefore, to show that each of the groups II, IV, and V is independent of the others.

The first statement of the axiom of parallels can be demonstrated by aid of the axioms of groups I, II, and IV. In order to do this, join the given point $A$ with any arbitrary point $B$ of the straight line $a$. Let $C$ be any other point of the given straight line. At the point $A$ on $AB$, construct the angle $ABC$ so that it shall lie in the same plane $\alpha$ as the point $C$, but upon the opposite side of $AB$ from it. The straight line thus obtained through $A$ does not meet the give straight line $\alpha$; for, if it should cut it, say in the point $D$, and if we suppose $B$ to be situated between $C$ and $D$, we could then find on $\alpha$ a point $D'$ so situated that $B$ would lie between $D$ and $D'$, and, moreover, so that we should have

$$
AD \equiv BD'
$$

Because of the congruence of the two triangles $ABD$ and $BAD'$, we have also

$$
\angle ABD \equiv \angle BAD',
$$

and since the angles $ABD'$ and $ABD$ are supplementary, it follows from theorem 12 that the angles $BAD$ and $BAD'$ are also supplementary. This, however, cannot be true, as, by theorem 1, two straight lines cannot intersect in more than one point, which would be the case if $BAD$ and $BAD'$ were supplementary.

The second statement of the axiom of parallels is independent of all the other axioms. This may be most easily shown in the following well known manner. As the individual elements of a geometry of space, select the points, straight lines, and planes of the ordinary geometry as constructed in § 9, and regard these elements as restricted in extent to the interior of a fixed sphere. Then, define the congruences of this geometry by aid of such linear transformations of the ordinary geometry as transform the fixed sphere into itself. By suitable conventions, we can make this “*non-euclidean geometry*” obey all of the axioms of our system except the axiom of Euclid (group III). Since the possibility of the ordinary geometry has already been established, that of the non-euclidean geometry is now an immediate consequence of the above considerations.

.. _grundlagen-en-s11:

.. folio:: § 11
   :page: 32

§ 11. Independence of the Axioms of Congruence
----------------------------------------------

We shall show the independence of the axioms of congruence by demonstrating that axiom IV, 6, or what amounts to the same thing, that the first theorem of congruence for triangles (theorem 10) cannot be deduced from the remaining axioms I, II, III, IV 1–5, V by any logical process of reasoning.

Select, as the points, straight lines, and planes of our new geometry of space, the points, straight lines, and planes of ordinary geometry, and define the laying off of an angle as in ordinary geometry, for example, as explained in § 9. We will, however, define the laying off of segments in another manner. Let $A_1$, $A_2$ be two points which, in ordinary geometry, have the co-ordinates $x_1$, $y_1$, $z_1$ and $x_2$, $y_2$, $z_2$, respectively. We will now define the length of the segment $A_1 A_2$ as the positive value of the expression

$$
\sqrt{(x_1-x_2+y_1-y_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}
$$

and call the two segments $A_1A_2$ and $A'_1A'_2$ congruent when they have equal lengths in the sense just defined.

It is at once evident that, in the geometry of space thus defined, the axioms I, II, III, IV 1–2, 4–5, V are all fulfilled.

In order to show that axiom IV, 3 also holds, we select an arbitrary straight line $a$ and upon it three points $A_1$, $A_2$, $A_3$ so that $A_2$ shall lie between $A_1$ and $A_3$. Let the points $x$, $y$, $z$ of the straight line $a$ be given by means of the equations

$$
\begin{aligned}
x &= \lambda t + \lambda', \\
y &= \mu t + \mu', \\
z &= \nu t + \nu',
\end{aligned}
$$

where $\lambda$, $\lambda'$, $\mu$, $\mu'$, $\nu$, $\nu'$ represent certain constants and $T$ is a parameter. If $t_1$, $t_2\ (<t_1)$, $t_3\ (<t_2)$ are the values of the parameter corresponding to the points $A_1$, $A_2$, $A_3$ we have as the lengths of the three segments $A_1A_2$ $A_2A_3$ and $A_1A_3$ respectively, the following values:

$$
(t_1-t_2) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|
$$

$$
(t_2-t_3) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|
$$

$$
(t_1-t_3) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|
$$

Consequently, the length of $A_1A_3$ is equal to the sum of the lengths of the segments $A_1A_2$ and $A_2A_3$. But this result is equivalent to the existence of axiom IV, 3.

Axiom IV, 6, or rather the first theorem of congruence for triangles, is not always fulfilled in this geometry. Consider, for example, in the plane $z = 0$, the four points

| $O$, having the co-ordinates $x = 0$, $y = 0$
| $A$, having the co-ordinates $x = 1$, $y = 0$
| $B$, having the co-ordinates $x = 0$, $y = 1$
| $C$, having the co-ordinates $x = \frac{1}{2}$, $y = \frac{1}{2}$

Then, in the right triangles $OAC$ and $OBC$, the angles at $C$ as also the adjacent sides $AC$ and $BC$ are respectively congruent; for, the side $OC$ is common to the two triangles and the sides $AC$ and $BC$ have the same length, namely, $\frac{1}{2}$. However, the third sides $OA$ and $OB$ have the lengths $1$ and $\sqrt{2}$, respectively, and are not, therefore, congruent.

It is not difficult to find in this geometry two triangles for which axiom IV, 6, itself is not valid.

.. picture:: /_static/figures/fig_non_congruence_model.svg
   :alt: Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).
   :caption: **Anisotropic Countermodel to Congruence Axiom IV 6 (§ 11).** Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).


.. _grundlagen-en-s12:

.. folio:: § 12
   :page: 34

§ 12. Independence of the Axiom of Continuity (Non-Archimedean Geometry)
------------------------------------------------------------------------

In order to demonstrate the independence of the axiom of Archimedes, we must produce a geometry in which all of the axioms are fulfilled with the exception of the one in question. [#fn2]_

For this purpose, we construct a domain $\Omega(t)$ of all those algebraic functions of $t$ which may be obtained from $t$ by means of the four arithmetical operations of addition, subtraction, multiplication, division, and the fifth operation $\sqrt{1+\omega^2}$, where $\omega$ represents any function arising from the application of these five operations. The elements of $\Omega(t)$—just as was previously the case for $\Omega$—constitute an enumerable set. These five operations may all be performed without introducing imaginaries, and that in only one way. The domain $\Omega(t)$ contains, therefore, only real, single-valued functions of $t$.

Let $c$ be any function of the domain $\Omega(t)$. Since this function $c$ is an algebraic function of $t$, it can in no case vanish for more than a finite number of values of $t$, and, hence, for sufficiently large positive values of $t$, it must remain always positive or always negative.

Let us now regard the functions of the domain $\Omega(t)$ as a kind of complex numbers. In the system of complex numbers thus defined, all of the ordinary rules of operation evidently hold. Moreover, if $a$, $b$ are any two distinct numbers of this system, then $a$ is said to be greater than, or less than, $b$ (written $a>b$ or $a<b$) according as the difference $c = a-b$ is always positive or always negative for sufficiently large values of $t$. By the adoption of this convention for the numbers of our system, it is possible to arrange them according to their magnitude in a manner analogous to that employed for real numbers. We readily see also that, for this system of complex numbers, the validity of an inequality is not destroyed by adding the same or equal numbers to both members, or by multiplying both members by the same number, providing it is greater than zero.

If $n$ is any arbitrary positive integral rational number, then, for the two numbers $n$ and $t$ of the domain $\Omega (t)$, the inequality $n<t$ certainly holds; for, the difference $n-t$, considered as a function of $t$, is always negative for sufficiently large values of $t$. We express this fact in the following manner: The two numbers $l$ and $t$ of the domain $\Omega (t)$, each of which is greater than zero, possess the property that any multiple whatever of the first always remains smaller than the second.

From the complex numbers of the domain $\Omega (t)$, we now proceed to construct a geometry in exactly the same manner as in § 9, where we took as the basis of our consideration the algebraic numbers of the domain $\Omega$. We will regard a system of three numbers $(x,y,z)$ of the domain $\Omega (t)$ as defining a point, and the ratio of any four such numbers $(u:v:w:r)$, where $u$, $v$, $w$ are not all zero, as defining a plane. Finally, the existence of the equation

$$
xu + yv + zw + r = 0
$$

shall express the condition that the point $(x, y, z)$ lies in the plane $(u:v:w:r)$. Let the straight line be defined in our geometry as the totality of all the points lying simultaneously in the same two planes. If now we adopt conventions corresponding to those of § 9 concerning the arrangement of elements and the laying off of angles and of segments, we shall obtain a *“non-archimedean” geometry* where, as the properties of the complex number system already investigated show, all of the axioms, with the exception of that of Archimedes, are fulfilled. In fact, we can lay off successively the segment 1 upon the segment $t$ an arbitrary number of times without reaching the end point of the segment $t$, which is a contradiction to the axiom of Archimedes.

THE THEORY OF PROPORTION. [#fn3]_


----

.. rubric:: Footnotes

.. [#fn1] See my lectures upon Euclidean Geometry, winter semester of 1898–1899, which were reported by Dr. Von Schaper and manifolded for the members of the class.

.. [#fn2] In his very scholarly book,—*Grundzüge der Geometrie*, German translation by A. Schepp, Leipzig, 1894,—G. Veronese has also attempted the construction of a geometry independent of the axiom of Archimedes.

.. [#fn3] See also Schur, *Math. Annalen*, Vol. 55, p. 265.—*Tr.*
