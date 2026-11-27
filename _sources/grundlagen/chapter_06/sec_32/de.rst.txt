:layout: book
:canonical_id: § 32
:breadcrumb_title: § 32
:order: 32
:folio: § 32
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s32:

.. folio:: § 32
   :page: 72

§ 32: Das commutative Gesetz der Multiplikation im Archimedischen Zahlensystem
==============================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Die Beweise der Sätze 36 und 37 beruhen wesentlich auf gewissen gegenseitigen Beziehungen, welche für die Rechnungsregeln und Grundthatsachen der Arithmetik bestehen und deren Kenntnis auch an sich von Interesse erscheint. Wir stellen die folgenden zwei Sätze auf:

.. _grundlagen-de-thm-38:

**Satz 38.** Für ein Archimedisches Zahlensystem ist das commutative Gesetz der Multiplikation eine notwendige Folge der übrigen Rechnungsgesetze ; d. h., wenn ein Zahlensystem die in § 13 aufgezählten Eigenschaften 1 — 11, 13 — 17 besitzt, so folgt notwendig, dass dasselbe auch der Formel 12 genügt.

**Beweis.** Zunächst bemerken wir: wenn :math:`a` eine beliebige Zahl des Zahlensystems und

.. math::

   n = 1 + 1 + \dots + 1

eine ganze rationale positive Zahl ist, so gilt für :math:`a` und :math:`n` stets das commutative Gesetz der Multiplikation; es ist nämlich

.. math::

   \begin{aligned}
   an &= a(1 + 1 + \dots + 1) = a \cdot 1 + a \cdot 1 + \dots + a \cdot 1 = a + a + \dots + a
   \end{aligned}

und ebenso

.. math::

   \begin{aligned}
   na &= (1 + 1 + \dots + 1)a = 1 \cdot a + 1 \cdot a + \dots + 1 \cdot a = a + a + \dots + a.
   \end{aligned}

Es seien nun im Gegensatz zu unserer Behauptung :math:`a, b` solche zwei Zahlen des Zahlensystems, für welche das commutative Gesetz der Multiplikation nicht gültig ist. Wir dürfen dann, wie leicht ersichtlich, die Annahmen

.. math::

   a > 0, \quad b > 0, \quad ab - ba > 0

machen. Wegen der Forderung 6 in § 13 giebt es eine Zahl :math:`c \; (> 0)`, so dass

.. math::

   (a + b + 1)c = ab - ba

ist. Endlich wählen wir eine Zahl :math:`d`, die zugleich den Ungleichungen

.. math::

   d > 0, \quad d < 1, \quad d < c

genügt, und bezeichnen mit :math:`m` und :math:`n` zwei solche ganze rationale Zahlen :math:`\ge 0`, für die

.. math::

   md \le a < (m + 1)d \quad \text{bez.} \quad nd \le b < (n + 1)d

wird. Das Vorhandensein solcher Zahlen :math:`m, n` ist eine unmittelbare Folgerung des Archimedischen Satzes (Satz 17 in § 13). Mit Rücksicht auf die Bemerkung zu Anfang dieses Beweises erhalten wir aus den letzteren Ungleichungen durch Multiplikation

.. math::

   \begin{aligned}
   ab &< mnd^2 + (m + n + 1)d^2, \\
   ba &\ge mnd^2,
   \end{aligned}

also durch Subtraktion

.. math::

   ab - ba < (m + n + 1)d^2.

Nun ist

.. math::

   md \le a, \quad nd \le b, \quad d < 1

und folglich

.. math::

   (m + n + 1)d < a + b + 1,

d. h.

.. math::

   ab - ba < (a + b + 1)d

oder wegen :math:`d < c`

.. math::

   ab - ba < (a + b + 1)c.

Diese Ungleichung widerspricht der Bestimmung der Zahl :math:`c`, und damit ist der Beweis für den Satz 38 erbracht.
