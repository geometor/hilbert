:layout: book

.. _grundlagen-chapter-7-en:

Chapter VII: Geometrical Constructions Based Upon Axioms I–V
============================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-en-s36:

.. folio:: § 36
   :page: 115

§ 36. Geometrical Constructions by Means of a Straight-Edge and a Transferer of Segments
----------------------------------------------------------------------------------------

Suppose we have given a geometry of space, in which all of the axioms I–V are valid. For the sake of simplicity, we shall consider in this chapter a a plane geometry which is contained in this geometry of space and shall investigate the question as to what elementary geometrical constructions may be carried out in such a geometry.

Upon the basis of the axioms of group I, the following constructions are always possible.

**Problem** 1. To join two points with a straight line and to find the intersection of two straight lines, the lines not being parallel.

Axiom III renders possible the following construction:

**Problem** 2. Through a given point to draw a parallel to a given straight line.

By the assistance of the axioms (IV) of congruence, it is possible to lay off segments and angles; that is to say, in the given geometry we may solve the following problems:

**Problem** 3. To lay off from a given point upon a given straight line a given segment.

**Problem** 4. To lay off on a given straight line a given angle; or what is the same thing, to construct a straight line which shall cut a given straight line at a given angle.

It is impossible to make any new constructions by the addition of the axioms of groups II and V. Consequently, when we take into consideration merely the axioms of groups I–V, all of those constructions and only those are possible, which may be reduced to the problems 1–4 given above.

We will add to the fundamental problems 1–4 also the following:

**Problem** 5. To draw a perpendicular to a given straight line.

We see at once that this construction can be made in different ways by means of the problems 1–4.

In order to carry out the construction in problem 1, we need to make use of only a *straight edge*. An instrument which enables us to make the construction in problem 3, we will call a *transferer of segments*. We shall now show that problems 2, 4, and 5 can be reduced to the constructions in problems 1 and 3 and, consequently, all of the problems 1–5 can be completely constructed by means of a straight-edge and a transferer of segments. We arrive, then, at the following result:

.. _grundlagen-en-thm-40:

**Theorem 40.** Those problems in geometrical construction, which may be solved by the assistance of only the axioms I–V, can always be carried out by the use of the straight-edge and the transferer of segments.

**Proof.** In order to reduce problem 2 to the solution of problems 1 and 3, we join the given point $P$ with any point $A$ of the given straight line and produce $PA$ to $C$, making $AC=PA$. Then, join $C$ with any other point $B$ of the given straight line and produce $CB$ to $Q$, making, $BQ=CB$. The straight line $PQ$ is the desired parallel.

We can solve problem 5 in the following manner. Let $A$ be an arbitrary point of the given straight line. Then upon this straight line, lay off in both directions from $A$ the two equal segments $AB$ and $AC$. Determine, upon any two straight lines passing through the point $A$, the points $E$ and $D$ so that the segments $AD$ and $AE$ will equal $AB$ and $AC$.

Suppose the straight lines $BD$ and $CE$ intersect in $F$ and the straight lines $BE$ and $CD$ intersect in $H$. $FH$ is then the desired perpendicular. In fact, the angles $BDC$ and $BEC$, being inscribed in a semicircle having the diameter $BC$, are both right angles, and, hence, according to the theorem relating to the point of intersection of the altitudes of a triangle, the straight lines $FH$ and $BC$ are perpendicular to each other.

Moreover, we can easily solve problem 4 simply by the drawing of straight lines and the laying off of segments. We will employ the following method which requires only the drawing of parallel lines and the erection of perpendiculars. Let $\beta$ be the angle to be laid off and $A$ its vertex. Draw through $A$ a straight line $l$ parallel to the given straight line, upon which we are to lay off the given angle $\beta$. From an arbitrary point $B$ of one side of the angle $\beta$, let fall a perpendicular upon the other side of this angle and also one upon $l$. Denote the feet of these perpendiculars by $D$ and $C$ respectively. The construction of these perpendiculars is accomplished by means of problems 2 and 5. Then, let fall from $A$ a perpendicular upon $CD$, and let its foot be denoted by $E$. According to the demonstration given in Section § 14, the angle $CAE$ equals $\beta$. Consequently, the construction in 4 is made to depend upon that of 1 and 3 and with this our proposition is demonstrated.

.. picture:: /_static/figures/fig_gauge_constructions.svg
   :alt: Dropping a perpendicular from P to line AB using only a straightedge and Streckenübertrager (Eichmass) via Thales's semicircle right angles at C and D and orthocenter H.
   :caption: **Orthocenter Perpendicular Construction with Straightedge and Segment-Transferer (§ 36).** Dropping a perpendicular from P to line AB using only a straightedge and Streckenübertrager (Eichmass) via Thales's semicircle right angles at C and D and orthocenter H.


.. _grundlagen-en-s37:

.. folio:: § 37
   :page: 119

§ 37. Analytical Representation of the Co-ordinates of Points Which Can Be So Constructed
-----------------------------------------------------------------------------------------

Besides the elementary geometrical problems considered in § 36, there exists a long series of other problems whose solution is possible by the drawing of straight lines and the laying off of segments. In order to get a general survey of the scope of the problems which may be solved in this manner, let us take as the basis of our consideration a system of axes in rectangular co-ordinates and suppose that the co-ordinates of the points are, as usual, represented by real numbers or by functions of certain arbitrary parameters. In order to answer the question in respect to all the points capable of such a construction, we employ the following considerations.

Let a system of definite points be given. Combine the co-ordinates of these points into a domain $R$. This domain contains, then, certain real numbers and certain arbitrary parameters $p$. Consider, now, the totality of points capable of construction by the drawing of straight lines and the laying off of definite segments, making use of the system of points in question. We will call the domain formed from the co-ordinates of these points $\Omega(R)$, which will then contain real numbers and functions of the arbitrary parameters $p$.

The discussion in § 17 shows that the drawing of straight lines and of parallels amounts, analytically, to the addition, subtraction, multiplication, and division of segments. Furthermore, the well known formula given in § 9 for a rotation shows that the laying off of segments upon a straight line does not necessitate any other analytical operation than the extraction of the square root of the sum of the squares of two segments whose bases have been previously constructed. Conversely, in consequence of the pythagorean theorem, we can always construct, by the aid of a right triangle, the square root of the sum of the squares of two segments by the mere laying off of segments.

From these considerations, it follows that the domain $\Omega(R)$ contains all of those and only those real numbers and functions of the parameters $p$, which arise from the numbers and parameters in $R$ by means of a finite number of applications of the five operations; viz., the four elementary operations of arithmetic and, in addition, the fifth operation of extracting the square root of the sum of two squares. We may express this result as follows:

.. _grundlagen-en-thm-41:

**Theorem 41.** A problem in geometrical construction is, then, possible of solution by the drawing of straight lines and the laying off of segments, that is to say, by the use of the straight-edge and a transferer of segments, when and only when, by the analytical solution of the problem, the co-ordinates of the desired points are such functions of the co-ordinates of the given points as may be determined by the rational operations and, in addition, the extraction of the square root of the sum of two squares.

From this proposition, we can at once show that not every problem which can be solved by the use of a compass can also be solved by the aid of a transferer of segments and a straight-edge. For the purpose of showing this, let us consider again that geometry which was constructed in § 9 by the help of the domain $\Omega$ of algebraic numbers. In this geometry, there exist only such segments as can be constructed by means of a straight-edge and a transferer of segments, namely, the segments determined by the numbers of the domain $\Omega$.

Now, if $\omega$ is a number of the domain $\Omega$, we easily see from the definition of $\Omega$ that every algebraic number conjugate to $\omega$ must also lie in $\Omega$. Since the numbers of the domain $\Omega$ are evidently all real, it follows that it can contain only such real algebraic numbers as have their conjugates also real.

Let us now consider the following problem; viz., to construct a right triangle having the hypotenuse 1 and one side $|\sqrt{2}| - 1$. The algebraic number $\sqrt{2|\sqrt{2}| - 2}$, which expresses the numerical value of the other side, does not occur in the domain $\Omega$, since the conjugate number $\sqrt{-2|\sqrt{2}| - 2}$ is imaginary. This problem is, therefore, not capable of solution in the geometry in question and, hence, cannot be constructed by means of a straight-edge and a transferer of segments, although the solution by means of a compass is possible.

.. _grundlagen-en-s38:

.. folio:: § 38
   :page: 122

§ 38. The Representation of Algebraic Numbers and of Integral Rational Functions as Sums of Squares
---------------------------------------------------------------------------------------------------

The question of the possibility of geometrical constructions by the aid of a straight-edge and a transferer of segments necessitates, for its complete treatment, particular theorems of an arithmetical and algebraic character, which, it appears to me, are themselves of interest. Since the time of Fermat, it has been known that every positive integral rational number can be represented as the sum of four squares. This theorem of Fermat permits the following remarkable generalization:

**Definition**. Let $k$ be an arbitrary number field and let $m$ be its degree. We will denote by $k^{\prime}$, $k^{\prime\prime}$, ..., $k^{(m-1)}$ the $m-1$ number fields conjugate to $k$. If, among the $m$ fields $k$, $k^{\prime}, k^{\prime\prime}, \ldots, k^{(m-1)}$ there is one or more formed entirely of real numbers, then we call these fields real. Suppose that the fields $k$, $k^\prime$, ..., $k^{(s-1)}$ are such. A number $\alpha$ of the field $k$ is called in this case *totally positive in $k$*, whenever the $s$ numbers conjugate to $\alpha$, contained respectively in $k$, $k^\prime$, $k^{\prime\prime}$, ..., $k^{(s-1)}$ are all positive. However, if in each of the $m$ fields $k$, $k^\prime$, $k^{\prime\prime}$, ..., $k^{(m-1)}$ there are also imaginary numbers present, we call every number $\alpha$ in $k$ *totally positive*.

We have, then, the following proposition:

.. _grundlagen-en-thm-42:

**Theorem 42.** Every totally positive number in $k$ may be represented as the sum of four squares, whose bases are integral or fractional numbers of the field $k$.

The demonstration of this theorem presents serious difficulty. It depends essentially upon the theory of relatively quadratic number fields, which I have recently developed in several papers. [#fn1]_ We will here call attention only to that proposition in this theory which gives the condition that a ternary diophantine equation of the form

$$
\alpha\xi^2 + \beta\eta^2 + \gamma\zeta^2 = 0
$$

can be solved when the coefficients $\alpha$, $\beta$, $\gamma$ are given numbers in $k$ and $\xi$, $\eta$, $\zeta$ are the required numbers in $k$. The demonstration of theorem 42 is accomplished by the repeated application of the proposition just mentioned.

From theorem 42 follow a series of propositions concerning the representation of such rational functions of a variable, with rational coefficients, as never have negative values. I will mention only the following theorem, which will be of service in the following sections.

.. _grundlagen-en-thm-43:

**Theorem 43.** Let, $f(x)$ be an integral rational function of $x$ whose coefficients are rational numbers and which never becomes negative for any real value of $x$. Then $f(x)$ can always be represented as the quotient of two sums of squares of which the bases are all integral rational functions of $x$ with rational coefficients.

**Proof**. We will denote the degree of the function $f(x)$ by $m$, which, in any case, must evidently be even. When $m = 0$, that is to say, when $f(x)$ is a rational number, the validity of theorem 43 follows immediately from Fermat's theorem concerning the representation of a positive number as the sum of four squares. We will assume that the proposition is already established for functions of degree $2$, $4$, $6$, ..., $m-2$, and show, in the following manner, its validity for the case of a function of the $m^{th}$ degree.

Let us, first of all, consider briefly the case where $f(x)$ breaks up into the product of two or more integral functions of $x$ with rational coefficients. Suppose $p(x)$ to be one of those functions contained in $f(x)$, which itself cannot be further decomposed into a product of integral functions having rational coefficients. It then follows at once from the “definite” character which we have given to the function $f(x)$, that the factor $p(x)$ must either appear in $f(x)$ to an even degree or $p(x)$ must be itself “definite”; that is to say, must be a function which never has negative values for any real values of $x$. In the first case, the quotient $\frac{f(x)}{\{p(x)\}^2}$ and, in the second case, both $p(x)$ and $\frac{f(x)}{p(x)}$, are “definite,” and these functions have an even degree $< m$. Hence, according to our hypothesis, in the first case, $\frac{f(x)}{\{p(x)\}^2}$ and, in the last case, $p(x)$ and $\frac{f(x)}{p(x)}$ may be represented as the quotient of the sum of squares of the character mentioned in theorem 43. Consequently, in both of these cases, the function $f(x)$ admits of the required representation.

Let us now consider the case where $f(x)$ cannot be broken up into the product of two integral functions having rational coefficients. The equation $f(\theta)=0$ defines, then, a field of algebraic numbers $k(\theta)$ of the $m^\text{th}$ degree, which, together with all their conjugate fields, are imaginary. Since, according to the definition given just before the statement of theorem 42, each number given in $k(\theta)$, and hence also $-1$ is totally positive in $k(\theta)$, it follows from theorem 42 that the number $-1$ can be represented as a sum of the squares of four definite numbers in $k(\theta)$. Let, for example

$$
\tag{1}
-1 = \alpha^2 + \beta^2 + \gamma^2 + \delta^2,
$$

where $\alpha$, $\beta$, $\gamma$, $\delta$ are integral or fractional numbers in $k(\theta)$. Let us put

$$
\begin{array}{rcccl}
\alpha & = & a_1 \theta^{m-1} + a_2 \theta^{m-2} + \cdots + a_m  & = & \phi(\theta), \\
\beta  & = & b_1 \theta^{m-1} + b_2 \theta^{m-2} + \cdots + b_m  & = & \psi(\theta), \\
\gamma & = & c_1 \theta^{m-1} + c_2 \theta^{m-2} + \cdots + c_m  & = & \chi(\theta), \\
\theta & = & d_1 \theta^{m-1} + d_2 \theta^{m-2} + \cdots + d_m  & = & \rho(\theta);
\end{array}
$$

where $a_1$, $a_2$, ..., $a_m$, ..., $d_1$, $d_2$, ..., $d_m$ are the rational numerical coefficients and $\phi(\theta)$, $\psi(\theta)$, $\chi(\theta)$, $\rho(\theta)$ the integral rational functions in question, having the degree $(m-1)$ in $\theta$.

From (1), we have

$$
1 + \{ \phi(\theta) \}^2 + \{\psi(\theta)\}^2 + \{\chi(\theta)\}^2 + \{\rho(\theta)\}^2 = 0
$$

Because of the irreducibility of the equation $f(x) = 0$, the expression

$$
F(x) = 1 + \{ \phi(\theta) \}^2 + \{\psi(\theta)\}^2 + \{\chi(\theta)\}^2 + \{\rho(\theta)\}^2
$$

represents, necessarily, an integral rational function of $x$ which is divisible by $f(x)$. $F(x)$ is, then, a “definite” function of the degree $(2m-2)$ or lower. Hence, the quotient $\frac{F(x)}{f(x)}$ is a “definite” function of the degree $(m-2)$ or lower in $x$, having rational coefficients. Consequently, by the hypothesis we have made, $\frac{F(x)}{f(x)}$  can be represented as the quotient of two sums of squares of the kind mentioned in theorem 43 and, since $F(x)$ is itself such a sum of squares, it follows that, $f(x)$ must also be a quotient of two sums of squares of the required kind. The validity of theorem 43 is accordingly established.

It would be perhaps difficult to formulate and to demonstrate the corresponding proposition for integral functions of two or more variables. However, I will here merely remark that I have demonstrated in an entirely different manner the possibility of representing any “definite” integral rational function of two variables as the quotient of sums of squares of integral functions, upon the hypothesis that the functions represented may have as coefficients not only rational but *any* real numbers. [#fn2]_

.. _grundlagen-en-s39:

.. folio:: § 39
   :page: 126

§ 39. Criterion for the Possibility of a Geometrical Construction by Means of a Straight-Edge and a Transferer of Segments
--------------------------------------------------------------------------------------------------------------------------

Suppose we have given a problem in geometrical construction which can be affected by means of a compass. We shall attempt to find a criterion which will enable us to decide, from the analytical nature of the problem and its solutions, whether or not the construction can be carried out by means of only a straight-edge and a transferer of segments. Our investigation will lead us to the following proposition.

.. _grundlagen-en-thm-44:

**Theorem 44.** Suppose we have given a problem in geometrical construction, which is of such a character that the analytical treatment of it enables us to determine uniquely the co-ordinates of the desired points from the co-ordinates of the given points by means of the rational operations and the extraction of the square root. Let $n$ be the smallest number of square roots which suffice to calculate the co-ordinates of the points. Then, in order that the required construction shall be possible by the drawing of straight lines and the laying off of segments, it is necessary and sufficient that the given geometrical problem shall have exactly $2^n$ real solutions for every position of the given points; that is to say, for all values of the arbitrary parameter expressed in terms of the co-ordinates of the given points.

**Proof**. We shall demonstrate this proposition merely for the case where the co-ordinates of the given points are rational functions, having rational coefficients, of a single parameter $p$.

It is at once evident that the proposition gives a necessary condition. In order to show that it is also sufficient, let us assume that it is fulfilled and then, among the $n$ square roots, consider that one which, in the calculation of the co-ordinates of the desired points, is first to be extracted. The expression under this radical is a rational function $f_1(p)$, having rational coefficients, of the parameter $p$. This rational function cannot have a negative value for any real value of the parameter $p$\,; for, otherwise the problem must have imaginary solutions for certain values of $p$, which is contrary to the given hypothesis. Hence, from theorem 43, we conclude that $f_1(p)$ can be represented as a quotient of the sums of squares of integral rational functions.

Moreover, the formulæ

$$
\begin{aligned}
\sqrt{a^2 + b^2 + c^2} &= \sqrt{(\sqrt{a^2 + b^2})^2 + c^2} \\
\sqrt{a^2 + b^2 + c^2 + d^2} &= \sqrt{(\sqrt{a^2 + b^2 + c^2})^2 + d^2}
\end{aligned}
$$

$$
\cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad
\cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot \quad
\cdot \quad \cdot \quad \cdot \quad \cdot \quad \cdot
$$

show that, in general, the extraction of the square root of a sum of any number of squares may always be reduced to the repeated extraction of the square root of the sum of two squares.

If now we combine this conclusion with the preceding results, it follows that the expression $\sqrt{f_1(p)}$ can certainly be constructed by means of a straight-edge and a transferer of segments. Among the $n$ square roots, consider now the second one to be extracted in the process of calculating the co-ordinates of the required points. The expression under this radical is a rational function $f_2(p, \sqrt{f_1})$ of the parameter $p$ and the square root first considered. This function $f_2$ can never be negative for any real arbitrary value of the parameter $p$ and for either sign of $\sqrt{f_1}$; for, otherwise among the $2^n$ solutions of our problem, there would exist for certain values of $p$ also imaginary solutions, which is contrary to our hypothesis. It follows, therefore, that $f_2$ must satisfy a quadratic equation of the form

$$
f_2^2 - \phi_2(p)f_2 + \psi_1(p) = 0,
$$

where $\phi_1(p)$ and $\psi_1(p)$ are, necessarily, such rational functions of $p$ as have rational coefficients and for real values of $p$ never become negative. From this equation, we have

$$
f_2 = \frac{f_2^2 + \psi_1(p)}{\phi_1(p)}.
$$

Now, according to theorem 43, the functions $\phi_1(p)$ and $\psi_1(p)$ must again be the quotient of the sums of squares of rational functions, and, on the other hand, the expression $f_2$ may be, from the above considerations, constructed by means of a straight-edge and a transferer of segments. The expression found for $f_2$ shows, therefore, that $f_2$ is a quotient of the sum of squares of functions which may be constructed in the same way. Hence, the expression $\sqrt{f_2}$ can also be constructed by means of a straight-edge and a transferer of segments.

Just as with the expression $f_2$, any other rational function $\phi_2(p, \sqrt{f_1})$ of $p$ and $\sqrt{f_1}$ may be shown to be the quotient of two sums of squares of functions which may be constructed, provided this rational function $\phi_2$ possesses the property that for real values of the parameter $p$ and for either sign of $\sqrt{f_1}$, it never becomes negative.

This remark permits us to extend the above method of reasoning in the following manner.

Let $f_3(p, \sqrt{f_1}, \sqrt{f_2})$ be such an expression as depends in a rational manner upon the three arguments $p, \sqrt{f_1}, \sqrt{f_2}$ and of which, in the analytical calculation of the co-ordinates of the desired points, the square root is the third to be extracted. As before, it follows that $f_3$ can never have negative values for real values of $p$ and for either sign of $\sqrt{f_1}$ and $\sqrt{f_2}$. This condition of affairs shows again that $f_3$ must satisfy a quadratic equation of the form

$$
f_3^2 - \phi_2(p, \sqrt{f_1}) f_3 - \psi_2(p, \sqrt{f_1}) = 0,
$$

where $\phi_2$ and $\psi_2$ are such rational functions of $p$ and $\sqrt{f_1}$ as never become negative for any real value of $p$ and either sign of $\sqrt{f_1}$. But, according to the preceding remark, the functions $\phi_2$ and $\psi_2$ are the quotients of two sums of squares of functions which may be constructed and, hence, it follows that the expression

$$
f_3 = \frac{f_3^2 + \psi_2(p, \sqrt{f_1})}{\phi_2(p, \sqrt{f_1})}
$$

is likewise possible of construction by aid of a straight-edge and a transferer of segments.

The continuation of this method of reasoning leads to the demonstration of theorem 44 for the case of a single parameter $p$.

The truth of theorem 44 for the general case depends upon whether or not theorem 43 can be generalized in a similar manner to cover the case of two or more variables.

As an example of the application of theorem 44, we may consider the regular polygons which may be constructed by means of a compass. In this case, the arbitrary parameter, $p$ does not occur, and the expressions to be constructed all represent algebraic numbers. We easily see that the criterion of theorem 44 is fulfilled, and, consequently, it follows that the above-mentioned regular polygons can be constructed by the drawing of straight lines and the laying off of segments. We might deduce this result also directly from the theory of the division of the circle (*Kreisteilung*).

Concerning the other known problems of construction in the elementary geometry, we will here only mention that the problem of Malfatti may be constructed by means of a straight-edge and a transferer of segments. This is, however, not the case with the contact problems of Appolonius.


----

.. rubric:: Footnotes

.. [#fn1] “Ueber die Theorie der relativquadratischen Zahlkörper,” *Jahresbericht der Deutschen Math. Vereinigung*, Vol. 6, 1899, and *Math. Annalen*, Vol. 51. See, also, “Ueber die Theorie der relativ-Abelschen Zahlkörper” *Nachr.\ der K. Ges.\ der Wiss.\ zu Göttingen*, 1898.

.. [#fn2] See “Ueber ternäre definite Formen,” *Acta mathematica*, Vol. 17.
