:layout: book

.. _grundlagen-chapter-6-en:

Chapter VI: Pascal's Theorem
============================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-en-s31:

.. folio:: § 31
   :page: 103

§ 31. Two Theorems Concerning the Possibility of Proving Pascal's Theorem
-------------------------------------------------------------------------

As is well known, Desargues's theorem (theorem 32) may be demonstrated by the aid of axioms I, II, III; that is to say, by the use, essentially, of the axioms of space. In § \! 23, we have shown that the demonstration of this theorem without the aid of the space axioms of group I and without the axioms of congruence (group IV) is impossible, even if we make use of the axiom of Archimedes.

Upon the basis of axioms I, 1–2, II, III, IV and, hence, by the exclusion of the axioms of space but with the assistance, essentially, of the axioms of congruence, we have, in § \! 14, deduced Pascal's theorem and, consequently, according to § \! 22, also Desargues's theorem. The question arises as to whether Pascal's theorem can be demonstrated without the assistance of the axioms of congruence. Our investigation will show that in this respect Pascal's theorem is very different from Desargues's theorem; for, in the demonstration of Pascal's theorem, the admission or exclusion of the axiom of Archimedes is of decided influence. We may combine the essential results of our investigation in the two following theorems.

.. _grundlagen-en-thm-36:

**Theorem 36.** Pascal's theorem (theorem 21) may be demonstrated by means of the axioms I, II,

III, V; that is to say, without the assistance of the axioms of congruence and with the aid of the axiom of Archimedes.

.. _grundlagen-en-thm-37:

**Theorem 37.** Pascal's theorem (theorem 21) cannot be demonstrated by means of the axioms I, II, III alone; that is to say, by exclusion of the axioms of congruence and also the axiom of Archimedes.

In the statement of these two theorems, we may, by virtue of the general theorem 35, replace the space axioms I, 3–7 by the plane condition that Desargues's theorem (theorem 32) shall be valid.

.. _grundlagen-en-s32:

.. folio:: § 32
   :page: 105

§ 32. The Commutative Law of Multiplication for an Archimedean Number System
----------------------------------------------------------------------------

The demonstration of theorems 36 and 37 rests essentially upon certain mutual relations concerning the laws of operation and the fundamental propositions of arithmetic, a knowledge of which is of itself of interest. We will state the two following theorems.

.. _grundlagen-en-thm-38:

**Theorem 38.** For an archimedean number system, the commutative law of multiplication is a necessary consequence of the remaining laws of operation; that is to say, if a number system possesses the properties 1–11, 13–17 given in § \! 13, it follows necessarily that this system satisfies also formula 12.

**Proof**. Let us observe first of all that, if $a$ is an arbitrary number of the system, and, if

$$
n = 1+1+\cdots+1
$$

is a positive integral rational number, then for $n$ and $a$ the commutative law of multiplication always holds. In fact, we have

$$
\begin{aligned}
an &= a(1+ 1 + \cdots +1) \\
    &= a \cdot 1 + a\cdot 1 +\cdots +a\cdot 1\\
    &= a + a +\cdots +a
\end{aligned}
$$

and likewise

$$
\begin{aligned}
na &= (1+ 1 + \cdots +1)a \\
    &= 1 \cdot a + 1\cdot a + \cdots + 1\cdot a\\
    &= a + a +\cdots +a.
\end{aligned}
$$

Suppose now, in contradiction to our hypothesis, $a, b$ to be numbers of this system, for which the commutative law of multiplication does not hold. It is then at once evident that we may make the assumption that we have

$$
a> 0 \text{, }  b > 0 \text{, }  ab-ba > 0.
$$

By virtue of condition 6 of § \! 13, there exists a number $c(> 0)$, such that

$$
(a+b+1) c = ab-ba.
$$

Finally, if we select a number $d$, satisfying simultaneously the inequalities

$$
d> 0 \text{, } d < 1 \text{, }  d<c,
$$

and denote by $m$ and $n$ two such integral rational numbers $\ge 0$ that we have respectively

$$
md < a \le (m+1) d
$$

and

$$
nd < b \le (n+1) d
$$

then the existence of the numbers $m$ and $n$ is an immediate consequence of the theorem of Archimedes (theorem 17, § \! 13). Recalling now the remark made at the beginning of this proof, we have by the multiplication of the last inequalities

$$
\begin{aligned}
ab &\le mnd^2 + (m+n+1)d^2\\
 ba &> mnd^2,
\end{aligned}
$$

and, hence, by subtraction

$$
ab-ba \le (m+n+1)d^2.
$$

We have, however,

$$
md<a \text{, } nd<b, \text{, } d<1
$$

and, consequently,

$$
(m+n+1)d<a+b+1;
$$

i.e.,

$$
ab-ba<(a+b+1)d,
$$

or, since $d<c$, we have

$$
ab-ba<(a+b+1)c.
$$

This inequality stands in contradiction to the definition of the number $c$, and, hence, the validity of the theorem 38 follows.

.. _grundlagen-en-s33:

.. folio:: § 33
   :page: 107

§ 33. The Commutative Law of Multiplication for a Non-Archimedean Number System
-------------------------------------------------------------------------------

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

.. _grundlagen-en-s34:

.. folio:: § 34
   :page: 110

§ 34. Proof of the Two Propositions Concerning Pascal's Theorem (Non-Pascalian Geometry)
----------------------------------------------------------------------------------------

If, in a geometry of space, all of the axioms I, II, III are fulfilled, then Desargues's theorem (theorem 32) is also valid, and, consequently, according to §§ 24–26, pp. 79–89, it is possible to introduce into this geometry an algebra of segments for which the rules 1–11, 13–16 of § \! 13 are all valid. If we assume now that the axiom (V) of Archimedes is valid for our geometry, then evidently Archimedes's theorem (theorem 17 of § \! 13) also holds for our algebra of segments, and, consequently, by virtue of theorem 38, the commutative law of multiplication is valid. Since, however, the definition of the product of two segments, as introduced in § \! 24 (figure 42) and which is the definition here also under discussion, agrees with the definition in § \! 15 (figure 22), it follows from the construction made in § \! 15 that the commutative law of multiplication is here nothing else than Pascal's theorem. Consequently, the validity of theorem 36 is established.

In order to demonstrate theorem 37, let us consider again the desarguesian number system $\Omega(s, t)$ introduced in $\S$ 33, and construct, in the manner described in $\S$ 29, a geometry of space for which all of the axioms I, II, III are fulfilled. However, Pascal's theorem will not hold for this geometry; for, the commutative law of multiplication is not valid in the desarguesian number system $\Omega(s, t)$. According to theorem 36, the non-pascalian geometry is then necessarily also a non-archimedean geometry.

By adopting the hypothesis we have, it is evident that we cannot demonstrate Pascal's theorem, providing we regard our geometry of space as a part of a geometry of an arbitrary number of dimensions in which, besides the points, straight lines, and planes, still other linear elements are present, and providing there exists for these elements a corresponding system of axioms of connection and of order, as well as the axiom of parallels.

.. _grundlagen-en-s35:

.. folio:: § 35
   :page: 112

§ 35. The Demonstration, by Means of the Theorems of Pascal and Desargues, of Any Theorem Relating to Points of Intersection
----------------------------------------------------------------------------------------------------------------------------

Every proposition relating to points of intersection in a plane has necessarily The form: Select, first of all, an arbitrary system of points and straight lines satisfying respectively the condition that certain ones of these points are situated on certain ones of the straight lines. If, in some known manner, we construct the straight lines joining the given points and determine the points of intersection of the given lines, we shall obtain finally a definite system of three straight lines, of which our proposition asserts that they all pass through the same point.

Suppose we now have a plane geometry in which all of the axioms I 1–2, II ..., V are valid. According to $\S$ 17, pp. 53–56, we may now find, by making use of a rectangular pair of axes, for each point a corresponding pair of numbers $(x,y)$ and for each straight line a ratio of three definite numbers $(u:v:w)$. Here, the numbers $x,\ y,\ u,\ v,\ w$ are all *real* numbers, of which $u,\ v$ cannot both be zero. The condition showing that the given point is situated upon the given straight line, viz.:

$$
ux+vy+w=0
$$

is an equation in the ordinary sense of the word. Conversely, in case $x,\ y,\ u,\ v,\ w$ are numbers of the algebraic domain $\Omega$ of $\S$ 9, and $u,\ v$ are not both zero, we may certainly assume that each pair of numbers $(x,y)$ gives a point and that each ratio of three numbers $(u:v:w)$ gives a straight line in the geometry in question.

If, for all the points and straight lines which occur in connection with any theorem relating to intersections in a plane, we introduce the corresponding pairs and triples of numbers, then such a theorem asserts that a definite expression $A(p_1,p_2,\ldots,p_r)$ with real coefficients and depending rationally upon certain parameters $p_1,p_2,\ldots,p_r$ always vanishes as soon as we put for each of these parameters a number of the main $\Omega$ considered in $\S$ 9. We conclude from this that the expression $A(p_1,p_2,\dots,p_r)$ must also vanish identically in accordance with the laws 7–12 of $\S$ 13.

Since, according to $\S$ 32, Desargues's theorem holds for the geometry in question, it follows that we certainly can make use of the algebra of segments introduced in $\S$ 24, and because Pascal's theorem is equally valid in this case, the commutative law of multiplication is also. Hence, for this algebra of segments, all of the laws 7–12 of $\S$ 13 are valid.

If we take as our axes in this new algebra of segments the co-ordinate axes already used and consider the unit points $E$, $E'$ as suitably established, we see that the new algebra of segments is nothing else than the system of co-ordinates previously employed.

In order to show that, for the new algebra of segments, the expression $A(p_1,\ p_2,\ \ldots,\ p_r)$ vanishes identically, it is sufficient to apply the theorems of Pascal and Desargues. Consequently we see that:

*Every proposition relative to points of intersection in the geometry in question must always, by the aid of suitably constructed auxiliary points and straight lines, turn out to be a combination of the theorems of Pascal and Desargues. Hence for the proof of the validity of a theorem relating to points of intersection, we need not have resource to the theorems of congruence.*
