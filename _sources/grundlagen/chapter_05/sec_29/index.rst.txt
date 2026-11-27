:layout: book
:canonical_id: § 29
:breadcrumb_title: § 29
:order: 29
:folio: § 29
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s29:

.. folio:: § 29
   :page: 97

§ 29: Construction of a Geometry of Space by Aid of a Desarguesian Number System
================================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

Suppose we have given a desarguesian number system :math:`D`. Such a system makes possible the construction of a geometry of space in which axioms I, II, III are all fulfilled.

In order to show this, let us consider any system of three numbers :math:`(x, y, z)` of the desarguesian number system :math:`D` as a point, and the ratio of four such numbers :math:`(u:v:w:r)`, of which the first three are not 0, as a plane. However, the systems :math:`(u:v:w:r)` and :math:`(au:av:aw:ar)`, where :math:`a` is any number of :math:`D` different from 0, represent the same plane. The existence of the equation

.. math::

   ux + vy + wz + r = 0

expresses the condition that the point :math:`(x, y, z)` shall lie in the plane :math:`(u:v:w:r)`. Finally, we define a straight line by the aid of a system of two planes :math:`(u':v':w':r')` and :math:`(u'':v'':w'':r'')`, where we impose the condition that it is impossible to find in :math:`D` two numbers :math:`a'`, :math:`a''` different from zero, such that we have simultaneously the relations

.. math::

   a'u' = a''u'', a'v' = a''v'', a'w' = a''w'',

A point :math:`(x, y, z)` is said to be situated upon this straight line :math:`[(u':v':w':r'), (u'':v'':w'':r'')]`, if it is common to the two planes :math:`(u':v':w':r')` and :math:`(u'':v'':w'':r'')`. Two straight lines which contain the same points are not regarded as being distinct.

By application of the laws 1–11 of § 13, which by hypothesis hold for the numbers of :math:`D`, we obtain without difficulty the result that the geometry of space which we have just constructed satisfies all of the axioms of groups I and III.

In order that the axioms (II) of order may also be valid, we adopt the following conventions. Let

.. math::

   (x_1, y_1, z_1), (x_2, y_2, z_2), (x_3, y_3, z_3)

be any three points of a straight line

.. math::

   [(u':v':w':r'), (u'':v'':w'':r'')].

Then, the point :math:`(x_2, y_2, z_2)` is said to lie between the other two, if we have fulfilled at least one of the six following double inequalities:

.. math::

   \begin{aligned}
   &\; x_1 < x_2 < x_3, \; x_1 > x_2 > x_3, \\
   % \tag{1} &\; y_1 < y_2 < y_3, \; y_1 > y_2 > y_3, \\
   % \tag{2} &\; z_1 < z_2 < z_3, \; z_1 > z_2 > z_3,
   \end{aligned}

If one of the two double inequalities (1) exists, then we can easily conclude that either :math:`y_1 = y_2 = y_3` or one of the two double inequalities (2) exists, and, consequently, either :math:`z_1 = z_2 = z_3` or one of the double inequalities (3) must exist. In fact, from the equations

.. math::

   \begin{aligned}
   u'x_i + v'y_i + w'z_i + r' & = 0,\\
   u''x_i + v''y_i + w''z_i + r'' & = 0,\\
   (i = 1,2,3)
   \end{aligned}

we may obtain, by a left-sided multiplication of these equations by numbers suitably chosen from :math:`D` and then adding the resulting equations, a system of equations of the form

.. math::

   u'''x_i + v'''y_i + r''' = 0, (i = 1, 2, 3).

In this system, the coefficient :math:`v'''` is certainly different from zero, since otherwise the three numbers :math:`x_1`, :math:`x_2`, :math:`x_3` would be mutually equal.

From

.. math::

   x_1 \lessgtr x_2 \lessgtr x_3,

it follows that

.. math::

   u'''x_1 \lesseqgtr x'''u_2 \lesseqgtr x'''u_3,

and, hence, as a consequence of (4), we have

.. math::

   v'''y_1 + r''' \lesseqgtr v'''y_2 + r''' \lesseqgtr
   v'''y_3 + r'''

and, therefore,

.. math::

   v'''y_1 \lesseqgtr v'''y_2 \lesseqgtr v'''y_3.

Since :math:`v'''` is different from zero, we have

.. math::

   y_1 \lesseqgtr y_2 \lesseqgtr y_3.

In each of these double inequalities, we must take either the upper sign throughout, or the middle sign throughout, or the lower sign throughout.

The preceding considerations show, that, in our geometry, the linear axioms II, 1–4 of order are all valid. However, it remains yet to show that, in this geometry, the plane axiom II, 5 is also valid.

For this purpose let a plane :math:`(u:v:w:r)` and a straight line :math:`[(u:v:w:r), (u':v':w':r')]` in this plane be given. Let us assume that all the points :math:`(x, y, z)` of the plane :math:`(u:v:w:r)`, for which we have the expression :math:`u'x + v'y + w'z + r'` greater than or less than zero, lie respectively upon the one side or upon the other side of the given straight line. We have then only to show that this convention is in accordance with the preceding statements. This, however, is easily done. We have thus shown that all of the axioms of groups I, II, III are fulfilled in the geometry of space which we have obtained in the above indicated manner from the desarguesian number system *D*. Remembering now that the theorem of Desargues is a consequence of the axioms I, II, III, we see that the proposition just stated is exactly the converse of the result reached in Section 28.

.. toctree::
   :hidden:

   de
   summary
   notes
