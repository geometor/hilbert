:layout: book
:canonical_id: § 33
:breadcrumb_title: § 33
:order: 33
:folio: p. 107
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _grundlagen-en-s33:

.. folio:: § 33
   :page: 107

§ 33: The Commutative Law of Multiplication for a Non-Archimedean Number System
===============================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

.. _grundlagen-en-thm-39:

**Theorem 39.** For a non-archimedean number system, the commutative law of multiplication is not a necessary consequence of the remaining laws of operation; that is to say, there exists a system of numbers possessing the properties 1–11, 13–16 mentioned in § \! 13, but for which the commutative law (12) of multiplication is not valid. A desarguesian number system, in the sense of § \! 28, is such a system.

**Proof**. Let $t$ be a parameter and $T$ any expression containing a finite or infinite number of terms, say of the form

$$
T=r_0t^n + r_1t^{n+1} + r_2t^{n+2} + r_3t^{n+3} + \ldots,
$$

where $r_0(\neq 0), r_1, r_2 \ldots$ are arbitrary rational numbers and $n$ is an arbitrary integral rational number $\gtreqless 0$. Moreover, let $s$ be another parameter and $S$ any expression having a finite or infinite number of terms, say of the form

$$
S = s^mT_0 + s^{m+1}T_1 + s^{m+2}T_2 + \ldots ,
$$

where $T_0 (\ne 0), T_1, T_2, \ldots$ denote arbitrary expressions of the form $T$ and $m$ is again an arbitrary integral rational number $\lesseqgtr 0$. We will regard the totality of all the expressions of the form $S$ as a complex number system $\Omega(s,\!t)$, for which we will assume the following laws of operation; namely, we will operate with $s$ and $t$ according to the laws 7–11 of § \! 13, as with parameters, while in place of rule 12 we will apply the formula

$$
ts = 2st.
$$

If, now, $S'$, $S''$ are any two expressions of the form $S$, say

$$
\begin{aligned}
S' &= s^{m'}T'_0 + s^{m'+1}T'_1 + s^{m'+2}T'_2 + \ldots,\\
 S'' &= s^{m''}T''_0 + s^{m''+1}T''_1 + s^{m''+2}T''_2 + \ldots,
\end{aligned}
$$

then, by combination, we can evidently form a new expression $S'+S''$ which is of the form $S$, and is, moreover, uniquely determined. This expression $S' + S''$ is called the sum of the numbers represented by $S'$ and $S''$.

By the multiplication of the two expressions $S'$ and $S''$ term by term, we obtain another expression of the form

$$
\begin{aligned}
 &S'S'' = s^{m'}T'_0 s^{m''} T''_0
 + (s^{m'} T'_0 s^{m''+1} T''_1
 + s^{m'+1} T'_1 s^{m''} T_0'')\\
 &+ (s^{m'} T'_0 s^{m''+2} T''_2
 + s^{m'+1} T'_1 s^{m''+1}T''_1
 + s^{m'+2} T'_2 s^{m''} T''_0) + \ldots
\end{aligned}
$$

This expression, by the aid of formula (1), is evidently a definite single-valued expression of the form $S$ and we will call it the product of the numbers represented by $S'$ and $S''$.

This method of calculation shows at once the validity of the laws 1–5 given in Section 13 for calculating with numbers. The validity of law 6 of that section is also not difficult to establish. To this end, let us assume that

$$
S'=s^{m'}T'_0+s^{m'+1}T'_1+s^{m'+2}T'_2+ \cdots
$$

and

$$
S'''=s^{m'''}T'''_0+s^{m'''+1}T'''_1+s^{m'''+2}T'''_2 \cdots
$$

are two expressions of the form $S$, and let us suppose, further, that the coefficient $r'_0$ of $T'_0$ is different from zero. By equating the like powers of $s$ in the two members of the equation

$$
S'S''=S''',
$$

we find, first of all, in a definite manner an integral number $m''$ as exponent, and then such a succession of expressions

$$
T''_0 \text{, } T''_1 \text{, } T''_2 \ldots
$$

that, by aid of formula (1), the expression

$$
S''=s^{m''}T''_0+s^{m''+1}T''_1+s^{m''+2}T''_2 \dots
$$

satisfies equation (2). With this our theorem is established.

In order, finally, to render possible an order of sequence of the numbers of our system $\Omega(s, t)$, we make the following conventions. Let a number of this system be called greater or less than 0 according as in the expression $S$, which represents it, the first coefficient $r_0$ of $T_0$ is greater or less than zero. Given any two numbers $a$, $b$ of the complex number system under consideration, we say that $a<b$ or $a>b$ according as

we have $a-b < 0$ or $> 0$. It is seen immediately that, with these conventions, the laws 13–16 of § \! 13 are valid; that is to say, $\Omega (s, t)$ is a desarguesian number system (see § \! 28).

As equation (1) shows, law 12 of § \! 13 is not fulfilled by our complex number system and, consequently, the validity of theorem 39 is fully established.

In conformity with theorem 38, Archimedes's theorem (theorem 17, § \! 13) does not hold for the number system $\Omega (s, t)$ which we have just constructed.

We wish also to call attention to the fact that the number system $\Omega (s, t)$, as well as the systems $\Omega$ and $\Omega (t)$ made use of in § \! 9 and § \! 12, respectively, contains only an enumerable set of numbers.

.. toctree::
   :hidden:

   de
   summary
   notes
