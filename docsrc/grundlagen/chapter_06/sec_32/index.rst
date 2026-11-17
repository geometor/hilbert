:layout: book
:canonical_id: § 32
:breadcrumb_title: § 32
:order: 32
:folio: p. 105
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-en-s32:

.. folio:: § 32
   :page: 105

§ 32: The Commutative Law of Multiplication for an Archimedean Number System
============================================================================

.. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)

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

.. toctree::
   :hidden:

   de
   summary
   notes
