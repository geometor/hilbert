:layout: book
:canonical_id: § 38
:breadcrumb_title: § 38
:order: 38
:folio: § 38
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s38:

.. folio:: § 38
   :page: 122

§ 38: The Representation of Algebraic Numbers and of Integral Rational Functions as Sums of Squares
===================================================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

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

.. [#fn1] “Ueber die Theorie der relativquadratischen Zahlkörper,” *Jahresbericht der Deutschen Math. Vereinigung*, Vol. 6, 1899, and *Math. Annalen*, Vol. 51. See, also, “Ueber die Theorie der relativ-Abelschen Zahlkörper” *Nachr.\ der K. Ges.\ der Wiss.\ zu Göttingen*, 1898.

.. [#fn2] See “Ueber ternäre definite Formen,” *Acta mathematica*, Vol. 17.

.. toctree::
   :hidden:

   de
   summary
   notes
