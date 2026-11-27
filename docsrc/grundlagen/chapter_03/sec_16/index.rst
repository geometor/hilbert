:layout: book
:canonical_id: § 16
:breadcrumb_title: § 16
:order: 16
:folio: § 16
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s16:

.. folio:: § 16
   :page: 50

§ 16: Proportion and the Theorems of Similitude
===============================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

By aid of the preceding algebra of segments, we can establish Euclid's theory of proportion in a manner free from objections and without making use of the axiom of Archimedes.

If :math:`a,b,a',b'` are any four segments whatever, the proportion

.. math::

   a:b=a':b'

expresses nothing else than the validity of equation

.. math::

   ab'=ba'.

**Definition**. Two triangles are called *similar* when the corresponding angles are congruent.

.. _grundlagen-en-thm-22:

**Theorem 22.** If :math:`a,b` and :math:`a',b'` are homologous sides of two similar triangles, we have the proportion

.. math::

   a:b=a':b'

**Proof.** We shall first consider the special case where the angle included between :math:`a` and :math:`b` and the one included between :math:`a'` and :math:`b'` are right angles.

Moreover, we shall assume that the two triangles are laid off in one and the same right angle. Upon one of the sides of this right angle, we lay off from the vertex :math:`0` the segment :math:`1`, and through the extremity of this segment, we draw a straight line parallel to the hypotenuses of the two triangles.

This parallel determines upon the other side of the right angle a segment :math:`e`. Then, according to our definition of the product of two segments, we have

.. math::

   b = ea,\ b' = ea',

from which we obtain

.. math::

   ab'=ba',

that is to say,

.. math::

   a:b=a':b'.

Let us now return to the general case. In each of the two similar triangles, find the point of intersection of the bisectors of the three angles. Denote these points by :math:`S` and :math:`S'`. From these points let fall upon the sides of the triangles the perpendiculars :math:`r` and :math:`r'`, respectively. Denote the segments thus determined upon the sides of the triangles by

.. math::

   a_b, a_c, b_c, b_a, c_a, c_b

and

.. math::

   a'_b, a'_c, b'_c, b'_a, c'_a, c'_b,

respectively. The special case of our proposition, demonstrated above, gives us then the following proportions:

.. math::

   \begin{aligned}
   a_b:r = a'_b:r', &\; \ \; b_c:r=b'_c:r', \\
   a_c:r = a'_c:r', &\; \ \; b_a:r=b'_a:r'.
   \end{aligned}

By aid of the distributive law, we obtain from these proportions the following:

.. math::

   a: r = a': r, \quad b: r = b': r'.

Consequently, by virtue of the commutative law of multiplication, we have

.. math::

   a:b=a':b'.

From the theorem just demonstrated, we can easily deduce the fundamental theorem in the theory of proportion. This theorem may be stated as follows:

.. _grundlagen-en-thm-23:

**Theorem 23.** If two parallel lines cut from the sides of an arbitrary angle the segments :math:`a,b` and :math:`a',b'` respectively, then we have always the proportion

.. math::

   a: b = a': b'.

Conversely, if the four segments :math:`a,b,a',b` fulfill this proportion and if :math:`a,a'` and :math:`b,b'` are laid off upon the two sides respectively of an arbitrary angle, then the straight lines joining the extremities of :math:`a` and :math:`b` and of :math:`a'` and :math:`b'` are parallel to each other.

.. toctree::
   :hidden:

   de
   summary
   notes
