:layout: book
:canonical_id: § 11
:breadcrumb_title: § 11
:order: 11
:folio: p. 32
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s11:

.. folio:: § 11
   :page: 32

§ 11: Independence of the Axioms of Congruence
==============================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

We shall show the independence of the axioms of congruence by demonstrating that axiom IV, 6, or what amounts to the same thing, that the first theorem of congruence for triangles (theorem 10) cannot be deduced from the remaining axioms I, II, III, IV 1–5, V by any logical process of reasoning.

Select, as the points, straight lines, and planes of our new geometry of space, the points, straight lines, and planes of ordinary geometry, and define the laying off of an angle as in ordinary geometry, for example, as explained in § 9. We will, however, define the laying off of segments in another manner. Let $A_1$, $A_2$ be two points which, in ordinary geometry, have the co-ordinates $x_1$, $y_1$, $z_1$ and $x_2$, $y_2$, $z_2$, respectively. We will now define the length of the segment $A_1 A_2$ as the positive value of the expression

$$
\sqrt{(x_1-x_2+y_1-y_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}
$$

and call the two segments $A_1A_2$ and $A'_1A'_2$ congruent when they have equal lengths in the sense just defined.

It is at once evident that, in the geometry of space thus defined, the axioms I, II, III, IV 1–2, 4–5, V are all fulfilled.

In order to show that axiom IV, 3 also holds, we select an arbitrary straight line $a$ and upon it three points $A_1$, $A_2$, $A_3$ so that $A_2$ shall lie between $A_1$ and $A_3$. Let the points $x$, $y$, $z$ of the straight line $a$ be given by means of the equations

$$
\begin{aligned}
x &= \lambda t + \lambda', \\
y &= \mu t + \mu', \\
z &= \nu t + \nu',
\end{aligned}
$$

where $\lambda$, $\lambda'$, $\mu$, $\mu'$, $\nu$, $\nu'$ represent certain constants and $T$ is a parameter. If $t_1$, $t_2\ (<t_1)$, $t_3\ (<t_2)$ are the values of the parameter corresponding to the points $A_1$, $A_2$, $A_3$ we have as the lengths of the three segments $A_1A_2$ $A_2A_3$ and $A_1A_3$ respectively, the following values:

$$
(t_1-t_2) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|
$$

$$
(t_2-t_3) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|
$$

$$
(t_1-t_3) \left| \sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2} \right|
$$

Consequently, the length of $A_1A_3$ is equal to the sum of the lengths of the segments $A_1A_2$ and $A_2A_3$. But this result is equivalent to the existence of axiom IV, 3.

Axiom IV, 6, or rather the first theorem of congruence for triangles, is not always fulfilled in this geometry. Consider, for example, in the plane $z = 0$, the four points

| $O$, having the co-ordinates $x = 0$, $y = 0$
| $A$, having the co-ordinates $x = 1$, $y = 0$
| $B$, having the co-ordinates $x = 0$, $y = 1$
| $C$, having the co-ordinates $x = \frac{1}{2}$, $y = \frac{1}{2}$

Then, in the right triangles $OAC$ and $OBC$, the angles at $C$ as also the adjacent sides $AC$ and $BC$ are respectively congruent; for, the side $OC$ is common to the two triangles and the sides $AC$ and $BC$ have the same length, namely, $\frac{1}{2}$. However, the third sides $OA$ and $OB$ have the lengths $1$ and $\sqrt{2}$, respectively, and are not, therefore, congruent.

It is not difficult to find in this geometry two triangles for which axiom IV, 6, itself is not valid.

.. picture:: /_static/figures/fig_non_congruence_model.svg
   :alt: Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).
   :caption: **Anisotropic Countermodel to Congruence Axiom IV 6 (§ 11).** Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).

.. toctree::
   :hidden:

   de
   summary
   notes
