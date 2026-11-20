:layout: book
:canonical_id: § 15
:breadcrumb_title: § 15
:order: 15
:folio: § 15
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s15:

.. folio:: § 15
   :page: 46

§ 15: An Algebra of Segments, Based Upon Pascal's Theorem
=========================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

Pascal's theorem, which was demonstrated in the last section, puts us in a position to introduce into geometry a method of calculating with segments, in which all of the rules for calculating with real numbers remain valid without any modification.

Instead of the word “congruent” and the sign $\equiv$, we make use, in the algebra of segments, of the word “equal” and the sign $=$.

If $A, B, C$ are three points of a straight line and if $B$ lies between $A$ and $C$, then we say that $c = AC$ is the *sum* of the two segments $a=AB$ and $b=BC$. We indicate this by writing

$$
c=a+b.
$$

The segments $a$ and $b$ are said to be smaller than c, which fact we indicate by writing

$$
a<c,\ b<c.
$$

On the other hand, $c$ is said to be larger than $a$ and $b$, and we indicate this by writing

$$
c>a,\ c>b.
$$

From the linear axioms of congruence (axioms IV, 1–3), we easily see that, for the above definition of addition of segments, the associative law

$$
a+(b+c)=(a+b)+c,
$$

as well as the commutative law

$$
a+b = b+a
$$

is valid.

In order to define geometrically the product of two segments $a$ and $b$, we shall make use of the following construction. Select any convenient segment, which, having been selected, shall remain constant throughout the discussion, and denote the same by $1$. Upon the one side of a right angle, lay off from the vertex $O$ the segment $1$ and also the segment $b$. Then, from $O$ lay off upon the other side of the right angle the segment $a$. Join the extremities of the segments $1$ and $a$ by a straight line, and from the extremity of $b$ draw a line parallel to this straight line. This parallel will cut off from the other side of the right angle a segment $c$. We call this segment $c$ the *product* of the segments $a$ and $b$, and indicate this relation by writing

$$
c=ab.
$$

% required for correct placement of Figure 23

We shall now demonstrate that, for this definition of the multiplication of segments, the *commutative* law

$$
ab=ba
$$

holds. For this purpose, we construct in the above manner the product $ab$. Furthermore, lay off from $0$ upon the first side (I) of the right angle the segment $a$ and upon the other side (II) the segment $b$. Connect by a straight line the extremity of the segment $1$ with the extremity of $b$, situated on II, and draw through the endpoint of $a$, on I, a line parallel to this straight line. This parallel will determine, by its intersection with the side II, the segment $ba$. But, because the two dotted lines are, by Pascal's theorem, parallel, the segment $ba$ just found coincides with the segment $ab$ previously constructed, and our proposition is established. In order to show that the *associative* law

$$
a(bc)=(ab)c
$$

holds for the multiplication of segments, we construct first of all the segment $d=be$, then $da$, after that the segment $e=ba$, and finally $ec$. By virtue of Pascal's theorem, the extremities of the segments $da$ and $ec$ coincide, as may be clearly seen from figure 24.

If now we apply the commutative law which we have just demonstrated, we obtain the above formula, which expresses the associative law for the multiplication of two segments.

Finally, *the distributive* law

$$
a(b+c) = ab+ac
$$

also holds for our algebra of segments. In order to demonstrate this, we construct the segments, $ab$, $ac$,

and $a(b+c)$, and draw through the extremity of the segment $c$ (Fig. 25) a straight line parallel to the other side of the right angle. From the congruence of the two right-angled triangles which are shaded in the figure and the application of the theorem relating to the equality of the opposite sides of a parallelogram, the desired result follows. If $b$ and $c$ are any two arbitrary segments, there is always a segment $a$ to be found such that $c=ab$. This segment $a$ is denoted by $\frac{c}{b}$ and is called the *quotient* of $c$ by $b$.

.. picture:: /_static/figures/fig_segment_multiplication.svg
   :alt: Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.
   :caption: **Hilbert's Segment Multiplication c = ab and Commutativity ab = ba (§ 15).** Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.


.. picture:: /_static/figures/fig_segment_distributive.svg
   :alt: Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.
   :caption: **Geometric Proof of the Distributive Law a(b + c) = ab + ac (§ 15).** Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.

.. toctree::
   :hidden:

   de
   summary
   notes
