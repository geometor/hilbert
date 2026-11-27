:layout: book
:canonical_id: § 14
:breadcrumb_title: § 14
:order: 14
:folio: § 14
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

**Theorem 21.** (Pascal's theorem.) Given the two sets of points :math:`A`, :math:`B`, :math:`C` and :math:`A'`, :math:`B'`, :math:`C'` so situated respectively upon two intersecting straight lines that none of them fall at the intersection of these lines. If :math:`CB'` is parallel to :math:`BC'` and :math:`CA'` is also parallel to :math:`AC'`, then :math:`BA'` is parallel to :math:`AB'`. [#fn1]_

In order to demonstrate this theorem, we shall first introduce the following notation. In a right triangle, the base :math:`a` is uniquely determined by the hypotenuse :math:`c` and the base angle :math:`\alpha` included by :math:`a` and :math:`c`.  We will express this fact briefly by writing

.. math::

   a=\alpha c.

Hence, the symbol :math:`\alpha c` always represents a definite segment, providing :math:`c` is any given segment whatever and :math:`\alpha` is any given acute angle.

Furthermore, if :math:`c` is any arbitrary segment and :math:`\alpha`, :math:`\beta` are any two acute angles whatever, then the two segments :math:`\alpha \beta c` and :math:`\beta \alpha c` are always congruent; that is, we have

.. math::

   \alpha \beta c = \beta \alpha c,

and, consequently, the symbols :math:`\alpha` and :math:`\beta` are interchangeable.

In order to prove this statement, we take the segment :math:`c = AB`, and with :math:`A` as a vertex lay off upon the one side of this segment the angle :math:`\alpha` and upon the other the angle :math:`\beta`. Then, from the point :math:`B`, let fall upon the opposite sides of the :math:`\alpha` and :math:`\beta` the perpendiculars :math:`BC` and :math:`BD`, respectively. Finally, join :math:`C` with :math:`D` and let fall from :math:`A` the perpendicular :math:`AE` upon :math:`CD`.

Since the two angles :math:`ACB` and :math:`ADB` are right angles, the four points :math:`A`, :math:`B`, :math:`C`, :math:`D` are situated upon a circle. Consequently, the angles :math:`ACD` and :math:`ABD`, being inscribed in the same segment of the circle, are congruent. But the angles :math:`ACD` and :math:`CAE`, taken together, make a right angle, and the same is true of the two angles :math:`ABD` and :math:`BAD`. Hence, the two angles :math:`CAE` and :math:`BAD` are also congruent; that is to say,

.. math::

   \angle CAE \equiv \beta

and, therefore,

.. math::

   \angle DAE \equiv \alpha.

From these considerations, we have immediately the following congruences of segments:

.. math::

   \begin{array}{rclrcl}
   \beta c & \equiv & AD, & \alpha c & \equiv & AC, \\
   \alpha \beta c & \equiv & \alpha(AD) \equiv AE, & \beta \alpha c & \equiv & \beta(AC) \equiv AE. \\
   \end{array}

From these, the validity of the congruence in question follows.

Returning now to the figure in connection with Pascal's theorem, denote the intersection of the two given straight lines by :math:`O` and the segments :math:`OA`, :math:`OB`, :math:`OC`, :math:`OA'`, :math:`OB'`, :math:`OC'`, :math:`CB'`, :math:`BC'`, :math:`CA'`, :math:`AC'`, :math:`BA'`, :math:`AB'` by :math:`a`, :math:`b`, :math:`c`, :math:`a'`, :math:`b'`, :math:`c'`, :math:`l`, :math:`l^{*}`, :math:`m`, :math:`m^{*}`, :math:`n`, :math:`n^{*}`, respectively.

Let fall from the point :math:`O` a perpendicular upon each of the segments :math:`l`, :math:`m`, :math:`n`. The perpendicular to :math:`l` will form with the straight lines :math:`OA` and :math:`OA'` acute angles, which we shall denote by :math:`\lambda'` and :math:`\lambda`, respectively. Likewise, the perpendiculars to :math:`m` and :math:`n` form with these same lines :math:`OA` and :math:`OA'` acute angles, which we shall denote by :math:`\mu'`, :math:`\mu` and :math:`\nu'`, :math:`\nu`, respectively. If we now express, as indicated above, each of these perpendiculars in terms of the hypotenuse and base angle, we have the three following congruences of segments:

.. math::

   \begin{aligned}
   (1)\quad \lambda b' &\equiv \lambda' c, \\
   (2)\quad \mu a' &\equiv \mu' c, \\
   (3)\quad \nu a' &\equiv \nu' b.
   \end{aligned}

But since, according to our hypothesis, :math:`l` is parallel to :math:`l^{*}` and :math:`m` is parallel to :math:`m^{*}`, the perpendiculars from :math:`O` falling upon :math:`l^{*}` and :math:`m^{*}` must coincide with the perpendiculars from the same point falling upon :math:`l` and :math:`m`, and consequently, we have

.. math::

   \begin{aligned}
   (4)\quad \lambda c' &\equiv \lambda' b, \\
   (5)\quad \mu c' &\equiv \mu' a.
   \end{aligned}

Multiplying both members of congruence (3) by the symbol :math:`\lambda' \mu`, and remembering that, as we have already seen, the symbols in question are commutative, we have

.. math::

   \nu \lambda' \mu a' \equiv \nu' \mu \lambda' b.

In this congruence, we may replace :math:`\mu a'` in the first member by its value given in (2) and :math:`\lambda' b` in the second member by its value given in (4), thus obtaining as a result

.. math::

   \nu \lambda' \mu' c \equiv \nu' \mu \lambda c',

or

.. math::

   \nu \mu' \lambda' c \equiv \nu' \lambda \mu c'.

Here again in this congruence we can, by aid of (1), replace :math:`\lambda' c` by :math:`\lambda b'`, and, by aid of (5), we may replace in the second member :math:`\mu c'` by :math:`\mu' a`. We then have

.. math::

   \nu\mu'\lambda b' \equiv \nu'\lambda\mu' a,

or

.. math::

   \lambda\mu'\nu b' \equiv \lambda\mu'\nu' a.

Because of the significance of our symbols, we can conclude at once from this congruence that

.. math::

   \mu'\nu b' \equiv \mu'\nu' a,

and, consequently, that

.. math::

   (6)\quad \nu b' \equiv \nu' a.

If now we consider the perpendicular let fall from :math:`O` upon :math:`n` and draw perpendiculars to this same line from the points :math:`A` and :math:`B'`, then congruence (6) shows that the feet of the last two perpendiculars must coincide; that is to say, the straight line :math:`n^{*} = AB'` makes a right angle with the perpendicular to :math:`n` and, consequently, is parallel to :math:`n`. This establishes the truth of Pascal's theorem.

Having given any straight line whatever, together with an arbitrary angle and a point lying outside of the given line, we can, by constructing the given angle and drawing a parallel line, find a straight line passing through the given point and cutting the given straight line at the given angle. By means of this construction, we can demonstrate Pascal's theorem in the following very simple manner, for which, however, I am indebted to another source.

Through the point :math:`B`, draw a straight line cutting :math:`OA'` in the point :math:`D'` and making with it the angle :math:`OCA'`, so that the congruence

.. math::

   (1^*)\quad \angle OCA' \equiv \angle OD'B

is fulfilled. Now, according to a well known property of circles, :math:`CBD'A'` is an inscribed quadrilateral, and, consequently, by aid of the theorem concerning the congruence of angles inscribed in the same segment of a circle, we have the congruence

.. math::

   (2^*)\quad \angle OBA' \equiv \angle OD'C.

Since, by hypothesis, :math:`CA'` and :math:`AC'` are parallel, we have

.. math::

   (3^*)\quad \angle OCA' \equiv \angle OAC',

and from :math:`(1^*)` and :math:`(3^*)` we obtain the congruence

.. math::

   \angle OD'B \equiv \angle OAC'.

However, :math:`BAD'C'` is also an inscribed quadrilateral, and, consequently, by virtue of the theorem relating to the angles of such a quadrilateral, we have the congruence

.. math::

   (4^*)\quad \angle OAD' \equiv \angle OC'B.

But as :math:`CB'` is, by hypothesis, parallel to :math:`BC'`, we have also

.. math::

   (5^*)\quad \angle OB'C \equiv \angle OC'B.

From :math:`(4^*)` and :math:`(5^*)`, we obtain the congruence

.. math::

   \angle OAD' \equiv \angle OB'C,

which shows that :math:`CAD'B'` is also an inscribed quadrilateral, and, hence, the congruence

.. math::

   (6^*)\quad \angle OAB' \equiv \angle OD'C,

is valid. From :math:`(2^*)` and :math:`(6^*)`, it follows that

.. math::

   \angle OBA' \equiv \angle OAB',

and this congruence shows that :math:`BA'` and :math:`AB'` are parallel as Pascal's theorem demands. In case :math:`D'` coincides with one of the points :math:`A'`, :math:`B'`, :math:`C'`, it is necessary to make a modification of this method, which evidently is not difficult to do.

.. picture:: /_static/figures/fig_pascal_orthogonal.svg
   :alt: Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.
   :caption: **Affine Pascal's (Pappus's) Hexagon Theorem (Theorem 21).** Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.

.. [#fn1] F. Schur has published in the *Math. Ann.*, Vol. 51, a very interesting proof of the theorem of Pascal, based upon the axioms I–II, IV.

.. toctree::
   :hidden:

   de
   summary
   notes
