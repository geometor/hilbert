:layout: book
:canonical_id: § 11
:breadcrumb_title: § 11
:order: 11
:folio: § 11
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s11:

.. folio:: § 11
   :page: 32

§ 11: Independence of the Axioms of Congruence
==============================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

We shall show the independence of the axioms of congruence by demonstrating that axiom IV, 6, or what amounts to the same thing, that the first theorem of congruence for triangles (theorem 10) cannot be deduced from the remaining axioms I, II, III, IV 1–5, V by any logical process of reasoning.

Select, as the points, straight lines, and planes of our new geometry of space, the points, straight lines, and planes of ordinary geometry, and define the laying off of an angle as in ordinary geometry, for example, as explained in § 9. We will, however, define the laying off of segments in another manner. Let :math:`A_1`, :math:`A_2` be two points which, in ordinary geometry, have the co-ordinates :math:`x_1`, :math:`y_1`, :math:`z_1` and :math:`x_2`, :math:`y_2`, :math:`z_2`, respectively. We will now define the length of the segment :math:`A_1 A_2` as the positive value of the expression

.. math::

   \sqrt{(x_1-x_2+y_1-y_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}

and call the two segments :math:`A_1A_2` and :math:`A'_1A'_2` congruent when they have equal lengths in the sense just defined.

It is at once evident that, in the geometry of space thus defined, the axioms I, II, III, IV 1–2, 4–5, V are all fulfilled.

In order to show that axiom IV, 3 also holds, we select an arbitrary straight line :math:`a` and upon it three points :math:`A_1`, :math:`A_2`, :math:`A_3` so that :math:`A_2` shall lie between :math:`A_1` and :math:`A_3`. Let the points :math:`x`, :math:`y`, :math:`z` of the straight line :math:`a` be given by means of the equations

.. math::

   \begin{aligned}
   x &= \lambda t + \lambda', \\
   y &= \mu t + \mu', \\
   z &= \nu t + \nu',
   \end{aligned}

where :math:`\lambda`, :math:`\lambda'`, :math:`\mu`, :math:`\mu'`, :math:`\nu`, :math:`\nu'` represent certain constants and :math:`T` is a parameter. If :math:`t_1`, :math:`t_2\ (<t_1)`, :math:`t_3\ (<t_2)` are the values of the parameter corresponding to the points :math:`A_1`, :math:`A_2`, :math:`A_3` we have as the lengths of the three segments :math:`A_1A_2` :math:`A_2A_3` and :math:`A_1A_3` respectively, the following values:

.. math::

   (t_1-t_2) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|

.. math::

   (t_2-t_3) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|

.. math::

   (t_1-t_3) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|

Consequently, the length of :math:`A_1A_3` is equal to the sum of the lengths of the segments :math:`A_1A_2` and :math:`A_2A_3`. But this result is equivalent to the existence of axiom IV, 3.

Axiom IV, 6, or rather the first theorem of congruence for triangles, is not always fulfilled in this geometry. Consider, for example, in the plane :math:`z = 0`, the four points

| :math:`O`, having the co-ordinates :math:`x = 0`, :math:`y = 0`
| :math:`A`, having the co-ordinates :math:`x = 1`, :math:`y = 0`
| :math:`B`, having the co-ordinates :math:`x = 0`, :math:`y = 1`
| :math:`C`, having the co-ordinates :math:`x = \frac{1}{2}`, :math:`y = \frac{1}{2}`

Then, in the right triangles :math:`OAC` and :math:`OBC`, the angles at :math:`C` as also the adjacent sides :math:`AC` and :math:`BC` are respectively congruent; for, the side :math:`OC` is common to the two triangles and the sides :math:`AC` and :math:`BC` have the same length, namely, :math:`\frac{1}{2}`. However, the third sides :math:`OA` and :math:`OB` have the lengths :math:`1` and :math:`\sqrt{2}`, respectively, and are not, therefore, congruent.

It is not difficult to find in this geometry two triangles for which axiom IV, 6, itself is not valid.

.. picture:: /_static/figures/fig_non_congruence_model.svg
   :alt: Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).
   :caption: **Anisotropic Countermodel to Congruence Axiom IV 6 (§ 11).** Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).

.. toctree::
   :hidden:

   de
   summary
   notes
