:layout: book
:canonical_id: § 27
:breadcrumb_title: § 27
:order: 27
:folio: p. 90
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _grundlagen-en-s27:

.. folio:: § 27
   :page: 90

§ 27: Equation of the Straight Line, Based Upon the New Algebra of Segments
===========================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

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

.. toctree::
   :hidden:

   de
   summary
   notes
