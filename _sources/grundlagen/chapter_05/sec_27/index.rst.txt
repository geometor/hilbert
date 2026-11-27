:layout: book
:canonical_id: § 27
:breadcrumb_title: § 27
:order: 27
:folio: § 27
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s27:

.. folio:: § 27
   :page: 90

§ 27: Equation of the Straight Line, Based Upon the New Algebra of Segments
===========================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

In §§ 24–26, we have introduced into the plane geometry an algebra of segments in which the commutative law of addition and that of multiplication, as well as the two distributive laws, hold. This was done upon the assumption that the axioms cited in § 24, as also the theorem of Desargues, were valid. In this section, we shall show how an analytical representation of the point and straight line in the plane is possible upon the basis of this algebra of segments.

**Definition.** Take the two given fixed straight lines lying in the plane and intersecting in :math:`O` as the axis of :math:`x` and of :math:`y`, respectively. Let us suppose any point :math:`P` of the plane determined by the two segments :math:`x`, :math:`y` which we obtain upon the :math:`x`-axis and :math:`y`-axis, respectively, by drawing through :math:`P` parallels to these axes. These segments are called the *co-ordinates* of the point :math:`P`. Upon the basis of this new algebra of segments and by aid of Desargues's theorem, we shall deduce the following proposition.

.. _grundlagen-en-thm-34:

**Theorem 34.** The co-ordinates :math:`x`, :math:`y` of a point on an arbitrary straight line always satisfy an equation in these segments of the form

.. math::

   ax+by+c = 0.

In this equation, the segments :math:`a` and :math:`b` stand necessarily to the left of the co-ordinates :math:`x` and :math:`y`. The segments :math:`a` and :math:`b` are never both zero and :math:`c` is an arbitrary segment.

Conversely, every equation in these segments and of this form represents always a straight line in the plane geometry under consideration.

**Proof.** Suppose that the straight line :math:`l` passes through the origin :math:`O`. Furthermore, let :math:`C` be a definite point upon :math:`l` different from :math:`O`, and :math:`P` any arbitrary point of :math:`l`. Let :math:`OA` and :math:`OB` be the co-ordinates of :math:`C` and :math:`x`, :math:`y` be the co-ordinates of :math:`P`. We will denote the straight line joining the extremities of the segments :math:`x`, :math:`y` by :math:`g`. Finally, through the extremity of the segment :math:`1`, laid off on the :math:`x`-axis, draw a straight line :math:`h` parallel to :math:`AB`. This parallel cuts off upon the :math:`y`-axis the segment :math:`e`. From the second part of

Desargues's theorem, it follows that the straight line :math:`g` is also always parallel to :math:`AB`. Since :math:`g` is always parallel to :math:`h`, it follows that the co-ordinates :math:`x`, :math:`y` of the point :math:`P` must satisfy the equation

.. math::

   ex=g.

Moreover, in figure 49 let :math:`l'` be any arbitrary straight line in our plane. This straight line will cut off on the :math:`x`-axis the segment :math:`c=OO'`. Now, in the same figure, draw through :math:`O` the straight line :math:`l` parallel to :math:`l'`. Let :math:`P'` be an arbitrary point on the line :math:`l'`. The straight line through :math:`P'`, parallel to the :math:`x`-axis, intersects the straight line :math:`l` in :math:`P` and cuts off upon the :math:`y`-axis the segment :math:`y = OB`. Finally, through :math:`P` and :math:`P'` let parallels to the :math:`y`-axis cut off on the :math:`x`-axis the segments :math:`x=OA` and :math:`x'= OA'`.

We shall now undertake to show that the equation

.. math::

   x'=x+c

is fulfilled by the segments in question. For this purpose, draw :math:`O'C` parallel to the unit-line and likewise :math:`CD` parallel to the :math:`x`-axis and :math:`AD` parallel to the :math:`y`-axis.

Then, to prove our proposition amounts to showing that we must have necessarily

.. math::

   A'D \; \text{parallel to} \; O'C.

Let :math:`D'` be the point of intersection of the straight lines :math:`CD` and :math:`A'P'` and draw :math:`O'C'` parallel to the :math:`y`-axis.

Since, in the triangles :math:`OCP` and :math:`O'C'P'`, the straight lines joining the homologous vertices are parallel, it follows, by virtue of the second part of Desargues's theorem, that we must have

.. math::

   CP \; \text{parallel to} \; C'P'.

In a similar way, a consideration of the triangles :math:`ACP` and :math:`A'C'P'` shows that we must have

.. math::

   AC \; \text{parallel to} \; A'C'.

Since, in the triangles :math:`ACD` and :math:`C'A'O'`, the homologous sides are parallel to each other, it follows that the straight lines :math:`AC'`, :math:`CA'` and :math:`DO'` intersect in a common point. A consideration of the triangles :math:`C'A'D` and :math:`ACO'` then shows that :math:`A'D` and :math:`CO'` are parallel to each other. From the two equations already obtained, viz.:

.. math::

   ex = y \quad \text{and} \quad x' = x + c,

follows at once the equation

.. math::

   ex' = y + ec.

If we denote, finally, by :math:`n` the segment which added to the segment 1 gives the segment 0, then, from this last equation, we may easily deduce the following

.. math::

   ex' + ny + nec = 0,

and this equation is of the form required by theorem 34.

We can now show that the second part of the theorem is equally true; for, every linear equation

.. math::

   ax + by + c = 0

may evidently be brought into the required form

.. math::

   ex + ny + nec = 0

by a left-sided multiplication by a properly chosen segment.

It must be expressly stated, however, that, by our hypothesis, an equation of segments of the form

.. math::

   xa + yb + c = 0,

where the segments :math:`a`, :math:`b` stand to the right of the co-ordinates :math:`x`, :math:`y` does not, in general, represent a straight line.

In Section 30, we shall make an important application of theorem 34.

.. toctree::
   :hidden:

   de
   summary
   notes
