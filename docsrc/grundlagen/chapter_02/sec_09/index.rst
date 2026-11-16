:layout: book
:canonical_id: § 9
:breadcrumb_title: § 9
:order: 9
:folio: p. 27
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _grundlagen-en-s9:

.. folio:: § 9
   :page: 27

§ 9: Compatibility of the Axioms
================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

The axioms, which we have discussed in the previous chapter and have divided into five groups, are not contradictory to one another; that is to say, it is not possible to deduce from these axioms, by any logical process of reasoning, a proposition which is contradictory to any of them. To demonstrate this, it is sufficient to construct a geometry where all of the five groups are fulfilled.

To this end, let us consider a domain $\Omega$ consisting of all of those algebraic numbers which may be obtained by beginning with the number one and applying to it a finite number of times the four arithmetical operations (addition, subtraction, multiplication, and division) and the operation $\sqrt{1+\omega^2}$, where $\omega$ represents a number arising from the five operations already given.

Let us regard a pair of numbers $(x, y)$ of the domain $\Omega$ as defining a point and the ratio of three such numbers $(u:v:w)$ of $\Omega$, where $u$, $v$ are not both equal to zero, as defining a straight line. Furthermore, let the existence of the equation

$$
ux+vy+w = 0
$$

express the condition that the point $(x, y)$ lies on the

straight line $(u:v:w)$. Then, as one readily sees, axioms I, 1–2 and III are fulfilled. The numbers of the domain $\Omega$ are all real numbers. If now we take into consideration the fact that these numbers may be arranged according to magnitude, we can easily make such necessary conventions concerning our points and straight lines as will also make the axioms of order (group II) hold. In fact, if $(x_1,y_1)$, $(x_2, y_2)$, $(x_3, y_3)$, $\ldots$ are any points whatever of a straight line, then this may be taken as their sequence on this straight line, providing the numbers $x_1$, $x_2$, $x_3,\ldots,$ or the numbers $y_1$, $y_2$, $y_3, \ldots,$ either all increase or decrease in the order of sequence given here. In order that axiom II, 5 shall be fulfilled, we have merely to assume that all points corresponding to values of $x$ and $y$ which make $ux+vy+w$ less than zero or greater than zero shall fall respectively upon the one side or upon the other side of the straight line $(u:v:w)$. We can easily convince ourselves that this convention is in accordance with those which precede, and by which the sequence of the points on a straight line has already been determined.

The laying off of segments and of angles follows by the known methods of analytical geometry. A transformation of the form

$$
\begin{aligned}
x' &= x + a \\
y' &= y + b
\end{aligned}
$$

produces a translation of segments and of angles.

Furthermore, if, in the accompanying figure, we represent the point $(0, 0)$ by $O$ and the point $(1, 0)$ by $E$, then, corresponding to a rotation of the angle $COE$ about $O$ as a center, any point $(x, y)$ is transformed into another point $(x', y')$ so related that

$$
\begin{aligned}
x' &= \frac{a}{\sqrt{a^2+b^2}} x -  \frac{b}{\sqrt{a^2+b^2}}y , \\
y' &= \frac{b}{\sqrt{a^2+b^2}} x + \frac{a}{\sqrt{a^2+b^2}}y .
\end{aligned}
$$

Since the number

$$
\sqrt{a^2+b^2} = a \sqrt{ 1 + \left( \frac{b}{a} \right)^2 }
$$

belongs to the domain $\Omega$, it follows that, under the conventions which we have made, the axioms of congruence (group IV) are all fulfilled. The same is true of the axiom of Archimedes.

From these considerations, it follows that every contradiction resulting from our system of axioms must also appear in the arithmetic related to the domain $\Omega$.

The corresponding considerations for the geometry of space present no difficulties.

If, in the preceding development, we had selected the domain of all real numbers instead of the domain $\Omega$, we should have obtained likewise a geometry in which all of the axioms of groups I—V are valid. For the purposes of our demonstration, however, it was sufficient to take the domain $\Omega$, containing on an enumerable set of elements.

.. toctree::
   :hidden:

   de
   summary
   notes
