:layout: book
:canonical_id: § 17
:breadcrumb_title: § 17
:order: 17
:folio: p. 53
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _grundlagen-en-s17:

.. folio:: § 17
   :page: 53

§ 17: Equations of Straight Lines and of Planes
===============================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

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

.. toctree::
   :hidden:

   de
   summary
   notes
