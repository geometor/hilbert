:layout: book
:canonical_id: § 22
:breadcrumb_title: § 22
:order: 22
:folio: p. 71
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s22:

.. folio:: § 22
   :page: 71

§ 22: Desargues's Theorem and Its Demonstration for Plane Geometry by Aid of the Axioms of Congruence
=====================================================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

Of the axioms given in §§ 1–8, pp. 1–26, those of groups II–V are in part linear and in part plane axioms. Axioms 3–7 of group I are the only space axioms. In order to show clearly the significance of these axioms of space, let us assume a plane geometry and investigate, in general, the conditions for which this plane geometry may be regarded as a part of a geometry of space in which at least the axioms of groups I–III are all fulfilled.

Upon the basis of the axioms of groups I–III, it is well known that the so-called theorem of Desargues may be easily demonstrated. This theorem relates to points of intersection in a plane. Let us assume in particular that the straight line, upon which are situated the points of intersection of the homologous sides of the two triangles, is the straight line which we call the straight line at infinity. We will designate the theorem which arises in this case, together with its converse, as the theorem of Desargues. This theorem is as follows:

.. _grundlagen-en-thm-32:

**Theorem 32.** (Desargues's theorem.) When two triangles are so situated in a plane that their homologous sides are respectively parallel, then the lines joining the homologous vertices pass through one and the same point, or are parallel to one another.

Conversely, if two triangles are so situated in a plane that the straight lines joining the homologous vertices intersect in a common point, or are parallel to one another, and, furthermore, if two pairs of homologous sides are parallel to each other, then the third sides of the two triangles are also parallel to each other.

As we have already mentioned, theorem 32 is a consequence of the axioms I–III. Because of this fact, the validity of Desargues's theorem in the plane is, in any case, a necessary condition that the geometry of this plane may be regarded as a part of a geometry of space in which the axioms of groups I–III are all fulfilled.

Let us assume, as in §§ 13–21, pp. 37–70, that we have a plane geometry in which the axioms I, 1–2 and II–IV all hold and, also, that we have introduced in this geometry an algebra of segments conforming to § 15.

Now, as has already been established in § 17, there may be made to correspond to each point in the plane a pair of segments $(x, y)$ and to each straight line a ratio of three segments $(u:v:w)$, so that the linear equation

$$
ux+vy+w=0
$$

expresses the condition that the point is situated upon the straight line. The system composed of all the segments in our geometry forms, according to § 17, a domain of numbers for which the properties (1–16), enumerated in § 13, are valid. We can, therefore, by means of this domain of numbers, construct a geometry of space in a manner similar to that already employed in § 9 or in § 12, where we made use of the systems of numbers $\Omega$ and $\Omega(t)$, respectively. For this purpose, we assume that a system of three segments $(x, y, z)$ shall represent a point, and that the ratio of four segments $(u:v:w:r)$ shall represent a plane, while a straight line is defined as the intersection of two planes. Hence, the linear equation

$$
ux+vy+wz+r = 0
$$

expresses the fact that the point $(x, y, z)$ lies in the plane $(u: v: w: r)$. Finally, we determine the arrangement of the points upon a straight line, or the points of a plane with respect to a straight line situated in this plane, or the arrangement of the points in space with respect to a plane, by means of inequalities in a manner similar to the method employed for the plane in § 9.

Since we obtain again the original plane geometry by putting $z=0$, we know that our plane geometry can be regarded as a part of geometry of space. Now, the validity of Desargues's theorem is, according to the above considerations, a necessary condition for this result.  Hence, in the assumed plane geometry, it follows that Desargues's theorem must also hold.

It will be seen that the result just stated may also be deduced without difficulty from theorem 23 in the theory of proportion.

.. picture:: /_static/figures/fig_desargues_configuration.svg
   :alt: Theorem 32: triangles ABC and A'B'C' perspective from O with AB ∥ A'B' and BC ∥ B'C' satisfy AC ∥ A'C'.
   :caption: **Affine Desargues Configuration of Perspective Triangles (Theorem 32).** Theorem 32: triangles ABC and A'B'C' perspective from O with AB ∥ A'B' and BC ∥ B'C' satisfy AC ∥ A'C'.

.. toctree::
   :hidden:

   de
   summary
   notes
