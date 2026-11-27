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

**Definition**. Let :math:`k` be an arbitrary number field and let :math:`m` be its degree. We will denote by :math:`k^{\prime}`, :math:`k^{\prime\prime}`, ..., :math:`k^{(m-1)}` the :math:`m-1` number fields conjugate to :math:`k`. If, among the :math:`m` fields :math:`k`, :math:`k^{\prime}, k^{\prime\prime}, \ldots, k^{(m-1)}` there is one or more formed entirely of real numbers, then we call these fields real. Suppose that the fields :math:`k`, :math:`k^\prime`, ..., :math:`k^{(s-1)}` are such. A number :math:`\alpha` of the field :math:`k` is called in this case *totally positive in* :math:`k`, whenever the :math:`s` numbers conjugate to :math:`\alpha`, contained respectively in :math:`k`, :math:`k^\prime`, :math:`k^{\prime\prime}`, ..., :math:`k^{(s-1)}` are all positive. However, if in each of the :math:`m` fields :math:`k`, :math:`k^\prime`, :math:`k^{\prime\prime}`, ..., :math:`k^{(m-1)}` there are also imaginary numbers present, we call every number :math:`\alpha` in :math:`k` *totally positive*.

We have, then, the following proposition:

.. _grundlagen-en-thm-42:

**Theorem 42.** Every totally positive number in :math:`k` may be represented as the sum of four squares, whose bases are integral or fractional numbers of the field :math:`k`.

The demonstration of this theorem presents serious difficulty. It depends essentially upon the theory of relatively quadratic number fields, which I have recently developed in several papers. [#fn1]_ We will here call attention only to that proposition in this theory which gives the condition that a ternary diophantine equation of the form

.. math::

   \alpha\xi^2 + \beta\eta^2 + \gamma\zeta^2 = 0

can be solved when the coefficients :math:`\alpha`, :math:`\beta`, :math:`\gamma` are given numbers in :math:`k` and :math:`\xi`, :math:`\eta`, :math:`\zeta` are the required numbers in :math:`k`. The demonstration of theorem 42 is accomplished by the repeated application of the proposition just mentioned.

From theorem 42 follow a series of propositions concerning the representation of such rational functions of a variable, with rational coefficients, as never have negative values. I will mention only the following theorem, which will be of service in the following sections.

.. _grundlagen-en-thm-43:

**Theorem 43.** Let, :math:`f(x)` be an integral rational function of :math:`x` whose coefficients are rational numbers and which never becomes negative for any real value of :math:`x`. Then :math:`f(x)` can always be represented as the quotient of two sums of squares of which the bases are all integral rational functions of :math:`x` with rational coefficients.

**Proof**. We will denote the degree of the function :math:`f(x)` by :math:`m`, which, in any case, must evidently be even. When :math:`m = 0`, that is to say, when :math:`f(x)` is a rational number, the validity of theorem 43 follows immediately from Fermat's theorem concerning the representation of a positive number as the sum of four squares. We will assume that the proposition is already established for functions of degree :math:`2`, :math:`4`, :math:`6`, ..., :math:`m-2`, and show, in the following manner, its validity for the case of a function of the :math:`m^{th}` degree.

Let us, first of all, consider briefly the case where :math:`f(x)` breaks up into the product of two or more integral functions of :math:`x` with rational coefficients. Suppose :math:`p(x)` to be one of those functions contained in :math:`f(x)`, which itself cannot be further decomposed into a product of integral functions having rational coefficients. It then follows at once from the “definite” character which we have given to the function :math:`f(x)`, that the factor :math:`p(x)` must either appear in :math:`f(x)` to an even degree or :math:`p(x)` must be itself “definite”; that is to say, must be a function which never has negative values for any real values of :math:`x`. In the first case, the quotient :math:`\frac{f(x)}{\{p(x)\}^2}` and, in the second case, both :math:`p(x)` and :math:`\frac{f(x)}{p(x)}`, are “definite,” and these functions have an even degree :math:`< m`. Hence, according to our hypothesis, in the first case, :math:`\frac{f(x)}{\{p(x)\}^2}` and, in the last case, :math:`p(x)` and :math:`\frac{f(x)}{p(x)}` may be represented as the quotient of the sum of squares of the character mentioned in theorem 43. Consequently, in both of these cases, the function :math:`f(x)` admits of the required representation.

Let us now consider the case where :math:`f(x)` cannot be broken up into the product of two integral functions having rational coefficients. The equation :math:`f(\theta)=0` defines, then, a field of algebraic numbers :math:`k(\theta)` of the :math:`m^\text{th}` degree, which, together with all their conjugate fields, are imaginary. Since, according to the definition given just before the statement of theorem 42, each number given in :math:`k(\theta)`, and hence also :math:`-1` is totally positive in :math:`k(\theta)`, it follows from theorem 42 that the number :math:`-1` can be represented as a sum of the squares of four definite numbers in :math:`k(\theta)`. Let, for example

.. math::

   \tag{1}
   -1 = \alpha^2 + \beta^2 + \gamma^2 + \delta^2,

where :math:`\alpha`, :math:`\beta`, :math:`\gamma`, :math:`\delta` are integral or fractional numbers in :math:`k(\theta)`. Let us put

.. math::

   \begin{array}{rcccl}
   \alpha & = & a_1 \theta^{m-1} + a_2 \theta^{m-2} + \cdots + a_m & = & \phi(\theta), \\
   \beta & = & b_1 \theta^{m-1} + b_2 \theta^{m-2} + \cdots + b_m & = & \psi(\theta), \\
   \gamma & = & c_1 \theta^{m-1} + c_2 \theta^{m-2} + \cdots + c_m & = & \chi(\theta), \\
   \theta & = & d_1 \theta^{m-1} + d_2 \theta^{m-2} + \cdots + d_m & = & \rho(\theta);
   \end{array}

where :math:`a_1`, :math:`a_2`, ..., :math:`a_m`, ..., :math:`d_1`, :math:`d_2`, ..., :math:`d_m` are the rational numerical coefficients and :math:`\phi(\theta)`, :math:`\psi(\theta)`, :math:`\chi(\theta)`, :math:`\rho(\theta)` the integral rational functions in question, having the degree :math:`(m-1)` in :math:`\theta`.

From (1), we have

.. math::

   1 + \{ \phi(\theta) \}^2 + \{\psi(\theta)\}^2 + \{\chi(\theta)\}^2 + \{\rho(\theta)\}^2 = 0

Because of the irreducibility of the equation :math:`f(x) = 0`, the expression

.. math::

   F(x) = 1 + \{ \phi(\theta) \}^2 + \{\psi(\theta)\}^2 + \{\chi(\theta)\}^2 + \{\rho(\theta)\}^2

represents, necessarily, an integral rational function of :math:`x` which is divisible by :math:`f(x)`. :math:`F(x)` is, then, a “definite” function of the degree :math:`(2m-2)` or lower. Hence, the quotient :math:`\frac{F(x)}{f(x)}` is a “definite” function of the degree :math:`(m-2)` or lower in :math:`x`, having rational coefficients. Consequently, by the hypothesis we have made, :math:`\frac{F(x)}{f(x)}`  can be represented as the quotient of two sums of squares of the kind mentioned in theorem 43 and, since :math:`F(x)` is itself such a sum of squares, it follows that, :math:`f(x)` must also be a quotient of two sums of squares of the required kind. The validity of theorem 43 is accordingly established.

It would be perhaps difficult to formulate and to demonstrate the corresponding proposition for integral functions of two or more variables. However, I will here merely remark that I have demonstrated in an entirely different manner the possibility of representing any “definite” integral rational function of two variables as the quotient of sums of squares of integral functions, upon the hypothesis that the functions represented may have as coefficients not only rational but *any* real numbers. [#fn2]_

.. [#fn1] “Ueber die Theorie der relativquadratischen Zahlkörper,” *Jahresbericht der Deutschen Math. Vereinigung*, Vol. 6, 1899, and *Math. Annalen*, Vol. 51. See, also, “Ueber die Theorie der relativ-Abelschen Zahlkörper” *Nachr.\ der K. Ges.\ der Wiss.\ zu Göttingen*, 1898.

.. [#fn2] See “Ueber ternäre definite Formen,” *Acta mathematica*, Vol. 17.

.. toctree::
   :hidden:

   de
   summary
   notes
