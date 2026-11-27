:layout: book
:canonical_id: § 37
:breadcrumb_title: § 37
:order: 37
:folio: § 37
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s37:

.. folio:: § 37
   :page: 119

§ 37: Analytical Representation of the Co-ordinates of Points Which Can Be So Constructed
=========================================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

Besides the elementary geometrical problems considered in § 36, there exists a long series of other problems whose solution is possible by the drawing of straight lines and the laying off of segments. In order to get a general survey of the scope of the problems which may be solved in this manner, let us take as the basis of our consideration a system of axes in rectangular co-ordinates and suppose that the co-ordinates of the points are, as usual, represented by real numbers or by functions of certain arbitrary parameters. In order to answer the question in respect to all the points capable of such a construction, we employ the following considerations.

Let a system of definite points be given. Combine the co-ordinates of these points into a domain :math:`R`. This domain contains, then, certain real numbers and certain arbitrary parameters :math:`p`. Consider, now, the totality of points capable of construction by the drawing of straight lines and the laying off of definite segments, making use of the system of points in question. We will call the domain formed from the co-ordinates of these points :math:`\Omega(R)`, which will then contain real numbers and functions of the arbitrary parameters :math:`p`.

The discussion in § 17 shows that the drawing of straight lines and of parallels amounts, analytically, to the addition, subtraction, multiplication, and division of segments. Furthermore, the well known formula given in § 9 for a rotation shows that the laying off of segments upon a straight line does not necessitate any other analytical operation than the extraction of the square root of the sum of the squares of two segments whose bases have been previously constructed. Conversely, in consequence of the pythagorean theorem, we can always construct, by the aid of a right triangle, the square root of the sum of the squares of two segments by the mere laying off of segments.

From these considerations, it follows that the domain :math:`\Omega(R)` contains all of those and only those real numbers and functions of the parameters :math:`p`, which arise from the numbers and parameters in :math:`R` by means of a finite number of applications of the five operations; viz., the four elementary operations of arithmetic and, in addition, the fifth operation of extracting the square root of the sum of two squares. We may express this result as follows:

.. _grundlagen-en-thm-41:

**Theorem 41.** A problem in geometrical construction is, then, possible of solution by the drawing of straight lines and the laying off of segments, that is to say, by the use of the straight-edge and a transferer of segments, when and only when, by the analytical solution of the problem, the co-ordinates of the desired points are such functions of the co-ordinates of the given points as may be determined by the rational operations and, in addition, the extraction of the square root of the sum of two squares.

From this proposition, we can at once show that not every problem which can be solved by the use of a compass can also be solved by the aid of a transferer of segments and a straight-edge. For the purpose of showing this, let us consider again that geometry which was constructed in § 9 by the help of the domain :math:`\Omega` of algebraic numbers. In this geometry, there exist only such segments as can be constructed by means of a straight-edge and a transferer of segments, namely, the segments determined by the numbers of the domain :math:`\Omega`.

Now, if :math:`\omega` is a number of the domain :math:`\Omega`, we easily see from the definition of :math:`\Omega` that every algebraic number conjugate to :math:`\omega` must also lie in :math:`\Omega`. Since the numbers of the domain :math:`\Omega` are evidently all real, it follows that it can contain only such real algebraic numbers as have their conjugates also real.

Let us now consider the following problem; viz., to construct a right triangle having the hypotenuse 1 and one side :math:`|\sqrt{2}| - 1`. The algebraic number :math:`\sqrt{2|\sqrt{2}| - 2}`, which expresses the numerical value of the other side, does not occur in the domain :math:`\Omega`, since the conjugate number :math:`\sqrt{-2|\sqrt{2}| - 2}` is imaginary. This problem is, therefore, not capable of solution in the geometry in question and, hence, cannot be constructed by means of a straight-edge and a transferer of segments, although the solution by means of a compass is possible.

.. toctree::
   :hidden:

   de
   summary
   notes
