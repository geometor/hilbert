:layout: book
:canonical_id: § 33
:breadcrumb_title: § 33
:order: 33
:folio: § 33
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s33:

.. folio:: § 33
   :page: 107

§ 33: The Commutative Law of Multiplication for a Non-Archimedean Number System
===============================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

.. _grundlagen-en-thm-39:

**Theorem 39.** For a non-archimedean number system, the commutative law of multiplication is not a necessary consequence of the remaining laws of operation; that is to say, there exists a system of numbers possessing the properties 1–11, 13–16 mentioned in § 13, but for which the commutative law (12) of multiplication is not valid. A desarguesian number system, in the sense of § 28, is such a system.

**Proof**. Let :math:`t` be a parameter and :math:`T` any expression containing a finite or infinite number of terms, say of the form

.. math::

   T=r_0t^n + r_1t^{n+1} + r_2t^{n+2} + r_3t^{n+3} + \ldots,

where :math:`r_0(\neq 0), r_1, r_2 \ldots` are arbitrary rational numbers and :math:`n` is an arbitrary integral rational number :math:`\gtreqless 0`. Moreover, let :math:`s` be another parameter and :math:`S` any expression having a finite or infinite number of terms, say of the form

.. math::

   S = s^mT_0 + s^{m+1}T_1 + s^{m+2}T_2 + \ldots ,

where :math:`T_0 (\ne 0), T_1, T_2, \ldots` denote arbitrary expressions of the form :math:`T` and :math:`m` is again an arbitrary integral rational number :math:`\lesseqgtr 0`. We will regard the totality of all the expressions of the form :math:`S` as a complex number system :math:`\Omega(s,\!t)`, for which we will assume the following laws of operation; namely, we will operate with :math:`s` and :math:`t` according to the laws 7–11 of § 13, as with parameters, while in place of rule 12 we will apply the formula

.. math::

   ts = 2st.

If, now, :math:`S'`, :math:`S''` are any two expressions of the form :math:`S`, say

.. math::

   \begin{aligned}
   S' &= s^{m'}T'_0 + s^{m'+1}T'_1 + s^{m'+2}T'_2 + \ldots,\\
   S'' &= s^{m''}T''_0 + s^{m''+1}T''_1 + s^{m''+2}T''_2 + \ldots,
   \end{aligned}

then, by combination, we can evidently form a new expression :math:`S'+S''` which is of the form :math:`S`, and is, moreover, uniquely determined. This expression :math:`S' + S''` is called the sum of the numbers represented by :math:`S'` and :math:`S''`.

By the multiplication of the two expressions :math:`S'` and :math:`S''` term by term, we obtain another expression of the form

.. math::

   \begin{aligned}
   &S'S'' = s^{m'}T'_0 s^{m''} T''_0
   + (s^{m'} T'_0 s^{m''+1} T''_1
   + s^{m'+1} T'_1 s^{m''} T_0'')\\
   &+ (s^{m'} T'_0 s^{m''+2} T''_2
   + s^{m'+1} T'_1 s^{m''+1}T''_1
   + s^{m'+2} T'_2 s^{m''} T''_0) + \ldots
   \end{aligned}

This expression, by the aid of formula (1), is evidently a definite single-valued expression of the form :math:`S` and we will call it the product of the numbers represented by :math:`S'` and :math:`S''`.

This method of calculation shows at once the validity of the laws 1–5 given in Section 13 for calculating with numbers. The validity of law 6 of that section is also not difficult to establish. To this end, let us assume that

.. math::

   S'=s^{m'}T'_0+s^{m'+1}T'_1+s^{m'+2}T'_2+ \cdots

and

.. math::

   S'''=s^{m'''}T'''_0+s^{m'''+1}T'''_1+s^{m'''+2}T'''_2 \cdots

are two expressions of the form :math:`S`, and let us suppose, further, that the coefficient :math:`r'_0` of :math:`T'_0` is different from zero. By equating the like powers of :math:`s` in the two members of the equation

.. math::

   S'S''=S''',

we find, first of all, in a definite manner an integral number :math:`m''` as exponent, and then such a succession of expressions

.. math::

   T''_0 \text{, } T''_1 \text{, } T''_2 \ldots

that, by aid of formula (1), the expression

.. math::

   S''=s^{m''}T''_0+s^{m''+1}T''_1+s^{m''+2}T''_2 \dots

satisfies equation (2). With this our theorem is established.

In order, finally, to render possible an order of sequence of the numbers of our system :math:`\Omega(s, t)`, we make the following conventions. Let a number of this system be called greater or less than 0 according as in the expression :math:`S`, which represents it, the first coefficient :math:`r_0` of :math:`T_0` is greater or less than zero. Given any two numbers :math:`a`, :math:`b` of the complex number system under consideration, we say that :math:`a<b` or :math:`a>b` according as

we have :math:`a-b < 0` or :math:`> 0`. It is seen immediately that, with these conventions, the laws 13–16 of § 13 are valid; that is to say, :math:`\Omega (s, t)` is a desarguesian number system (see § 28).

As equation (1) shows, law 12 of § 13 is not fulfilled by our complex number system and, consequently, the validity of theorem 39 is fully established.

In conformity with theorem 38, Archimedes's theorem (theorem 17, § 13) does not hold for the number system :math:`\Omega (s, t)` which we have just constructed.

We wish also to call attention to the fact that the number system :math:`\Omega (s, t)`, as well as the systems :math:`\Omega` and :math:`\Omega (t)` made use of in § 9 and § 12, respectively, contains only an enumerable set of numbers.

.. toctree::
   :hidden:

   de
   summary
   notes
