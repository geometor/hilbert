:layout: book
:canonical_id: § 39
:breadcrumb_title: § 39
:order: 39
:folio: § 39
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s39:

.. folio:: § 39
   :page: 126

§ 39: Criterion for the Possibility of a Geometrical Construction by Means of a Straight-Edge and a Transferer of Segments
==========================================================================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

Suppose we have given a problem in geometrical construction which can be affected by means of a compass. We shall attempt to find a criterion which will enable us to decide, from the analytical nature of the problem and its solutions, whether or not the construction can be carried out by means of only a straight-edge and a transferer of segments. Our investigation will lead us to the following proposition.

.. _grundlagen-en-thm-44:

**Theorem 44.** Suppose we have given a problem in geometrical construction, which is of such a character that the analytical treatment of it enables us to determine uniquely the co-ordinates of the desired points from the co-ordinates of the given points by means of the rational operations and the extraction of the square root. Let :math:`n` be the smallest number of square roots which suffice to calculate the co-ordinates of the points. Then, in order that the required construction shall be possible by the drawing of straight lines and the laying off of segments, it is necessary and sufficient that the given geometrical problem shall have exactly :math:`2^n` real solutions for every position of the given points; that is to say, for all values of the arbitrary parameter expressed in terms of the co-ordinates of the given points.

**Proof**. We shall demonstrate this proposition merely for the case where the co-ordinates of the given points are rational functions, having rational coefficients, of a single parameter :math:`p`.

It is at once evident that the proposition gives a necessary condition. In order to show that it is also sufficient, let us assume that it is fulfilled and then, among the :math:`n` square roots, consider that one which, in the calculation of the co-ordinates of the desired points, is first to be extracted. The expression under this radical is a rational function :math:`f_1(p)`, having rational coefficients, of the parameter :math:`p`. This rational function cannot have a negative value for any real value of the parameter :math:`p`; for, otherwise the problem must have imaginary solutions for certain values of :math:`p`, which is contrary to the given hypothesis. Hence, from theorem 43, we conclude that :math:`f_1(p)` can be represented as a quotient of the sums of squares of integral rational functions.

Moreover, the formulæ

.. math::

   \begin{aligned}
   \sqrt{a^2 + b^2 + c^2} &= \sqrt{(\sqrt{a^2 + b^2})^2 + c^2} \\
   \sqrt{a^2 + b^2 + c^2 + d^2} &= \sqrt{(\sqrt{a^2 + b^2 + c^2})^2 + d^2}
   \end{aligned}

.. math::

   \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad
   \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad
   \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot

show that, in general, the extraction of the square root of a sum of any number of squares may always be reduced to the repeated extraction of the square root of the sum of two squares.

If now we combine this conclusion with the preceding results, it follows that the expression :math:`\sqrt{f_1(p)}` can certainly be constructed by means of a straight-edge and a transferer of segments. Among the :math:`n` square roots, consider now the second one to be extracted in the process of calculating the co-ordinates of the required points. The expression under this radical is a rational function :math:`f_2(p, \sqrt{f_1})` of the parameter :math:`p` and the square root first considered. This function :math:`f_2` can never be negative for any real arbitrary value of the parameter :math:`p` and for either sign of :math:`\sqrt{f_1}`; for, otherwise among the :math:`2^n` solutions of our problem, there would exist for certain values of :math:`p` also imaginary solutions, which is contrary to our hypothesis. It follows, therefore, that :math:`f_2` must satisfy a quadratic equation of the form

.. math::

   f_2^2 - \phi_2(p)f_2 + \psi_1(p) = 0,

where :math:`\phi_1(p)` and :math:`\psi_1(p)` are, necessarily, such rational functions of :math:`p` as have rational coefficients and for real values of :math:`p` never become negative. From this equation, we have

.. math::

   f_2 = \frac{f_2^2 + \psi_1(p)}{\phi_1(p)}.

Now, according to theorem 43, the functions :math:`\phi_1(p)` and :math:`\psi_1(p)` must again be the quotient of the sums of squares of rational functions, and, on the other hand, the expression :math:`f_2` may be, from the above considerations, constructed by means of a straight-edge and a transferer of segments. The expression found for :math:`f_2` shows, therefore, that :math:`f_2` is a quotient of the sum of squares of functions which may be constructed in the same way. Hence, the expression :math:`\sqrt{f_2}` can also be constructed by means of a straight-edge and a transferer of segments.

Just as with the expression :math:`f_2`, any other rational function :math:`\phi_2(p, \sqrt{f_1})` of :math:`p` and :math:`\sqrt{f_1}` may be shown to be the quotient of two sums of squares of functions which may be constructed, provided this rational function :math:`\phi_2` possesses the property that for real values of the parameter :math:`p` and for either sign of :math:`\sqrt{f_1}`, it never becomes negative.

This remark permits us to extend the above method of reasoning in the following manner.

Let :math:`f_3(p, \sqrt{f_1}, \sqrt{f_2})` be such an expression as depends in a rational manner upon the three arguments :math:`p, \sqrt{f_1}, \sqrt{f_2}` and of which, in the analytical calculation of the co-ordinates of the desired points, the square root is the third to be extracted. As before, it follows that :math:`f_3` can never have negative values for real values of :math:`p` and for either sign of :math:`\sqrt{f_1}` and :math:`\sqrt{f_2}`. This condition of affairs shows again that :math:`f_3` must satisfy a quadratic equation of the form

.. math::

   f_3^2 - \phi_2(p, \sqrt{f_1}) f_3 - \psi_2(p, \sqrt{f_1}) = 0,

where :math:`\phi_2` and :math:`\psi_2` are such rational functions of :math:`p` and :math:`\sqrt{f_1}` as never become negative for any real value of :math:`p` and either sign of :math:`\sqrt{f_1}`. But, according to the preceding remark, the functions :math:`\phi_2` and :math:`\psi_2` are the quotients of two sums of squares of functions which may be constructed and, hence, it follows that the expression

.. math::

   f_3 = \frac{f_3^2 + \psi_2(p, \sqrt{f_1})}{\phi_2(p, \sqrt{f_1})}

is likewise possible of construction by aid of a straight-edge and a transferer of segments.

The continuation of this method of reasoning leads to the demonstration of theorem 44 for the case of a single parameter :math:`p`.

The truth of theorem 44 for the general case depends upon whether or not theorem 43 can be generalized in a similar manner to cover the case of two or more variables.

As an example of the application of theorem 44, we may consider the regular polygons which may be constructed by means of a compass. In this case, the arbitrary parameter, :math:`p` does not occur, and the expressions to be constructed all represent algebraic numbers. We easily see that the criterion of theorem 44 is fulfilled, and, consequently, it follows that the above-mentioned regular polygons can be constructed by the drawing of straight lines and the laying off of segments. We might deduce this result also directly from the theory of the division of the circle (*Kreisteilung*).

Concerning the other known problems of construction in the elementary geometry, we will here only mention that the problem of Malfatti may be constructed by means of a straight-edge and a transferer of segments. This is, however, not the case with the contact problems of Appolonius.

----

.. rubric:: Footnotes

.. toctree::
   :hidden:

   de
   summary
   notes
