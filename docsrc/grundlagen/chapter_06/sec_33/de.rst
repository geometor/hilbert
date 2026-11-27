:layout: book
:canonical_id: § 33
:breadcrumb_title: § 33
:order: 33
:folio: § 33
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s33:

.. folio:: § 33
   :page: 73

§ 33: Das commutative Gesetz der Multiplikation im Nicht-Archimedischen Zahlensystem
====================================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

.. _grundlagen-de-thm-39:

**Satz 39.** Für ein Nicht-Archimedisches Zahlensystem ist das commutative Gesetz der Multiplikation nicht eine notwendige Folge der übrigen Rechnungsgesetze; d. h. es giebt ein Zahlensystem, das die in § 13 aufgezählten Eigenscliaften 1 — 11, 13 — 16 besitzt — ein Desarguessches Zahlensystem nach §28 — , in welchem nicht das commutative Gesetz (12) der Multiplikation besteht.

**Beweis.** Es sei :math:`t` ein Parameter und :math:`T` irgend ein Ausdruck mit einer endlichen oder unendlichen Gliederzahl von der Gestalt

.. math::

   T = r_0 t^n + r_1 t^{n+1} + r_2 t^{n+2} + r_3 t^{n+3} + \dots;

darin mögen :math:`r_0 \; (\neq 0), r_1, r_2, \dots` beliebige rationale Zahlen bedeuten und :math:`n` sei eine beliebige ganze rationale Zahl :math:`\gtreqless 0`. Ferner sei :math:`s` ein anderer Parameter und :math:`S` irgend ein Ausdruck mit einer endlichen oder unendlichen Gliederzahl von der Gestalt

.. math::

   S = s^m T_0 + s^{m+1} T_1 + s^{m+2} T_2 + \dots;

darin mögen :math:`T_0 \; (\neq 0), T_1, T_2, \dots` beliebige Ausdrücke von der Gestalt :math:`T` bezeichnen und :math:`m` sei wiederum eine beliebige ganze rationale Zahl :math:`\gtreqless 0`. Die Gesamtheit aller Ausdrücke von der Gestalt :math:`S` sehen wir als ein complexes Zahlensystem :math:`\Omega(s, t)` an, in dem wir folgende Rechnungsregeln festsetzen: man rechne mit :math:`s` und :math:`t`, wie mit Parametern nach den Regeln 7–11 in § 13, während man an Stelle der Regel 12 stets die Formel

.. math::

   (1)\quad ts = 2st

anwende.

Sind nun :math:`S', S''` irgend zwei Ausdrücke von der Gestalt :math:`S`:

.. math::

   \begin{aligned}
   S' &= s^{m'} T'_0 + s^{m'+1} T'_1 + s^{m'+2} T'_2 + \dots, \\
   S'' &= s^{m''} T''_0 + s^{m''+1} T''_1 + s^{m''+2} T''_2 + \dots,
   \end{aligned}

so kann man offenbar durch Zusammenfügung einen neuen Ausdruck :math:`S' + S''` bilden, der wiederum von der Gestalt :math:`S` und zugleich eindeutig bestimmt ist; dieser Ausdruck :math:`S' + S''` heisst die *Summe* der durch :math:`S', S''` dargestellten Zahlen.

Durch gliedweise Multiplikation der beiden Ausdrücke :math:`S', S''` gelangen wir zunächst zu einem Ausdrucke von der Gestalt

.. math::

   \begin{aligned}
   S'S'' &= s^{m'}T'_0 s^{m''}T''_0 + (s^{m'}T'_0 s^{m''+1}T''_1 + s^{m'+1}T'_1 s^{m''}T''_0) \\
   &\quad + (s^{m'}T'_0 s^{m''+2}T''_2 + s^{m'+1}T'_1 s^{m''+1}T''_1 + s^{m'+2}T'_2 s^{m''}T''_0) + \dots.
   \end{aligned}

Dieser Ausdruck wird bei Benutzung der Formel (1) offenbar ein eindeutig bestimmter Ausdruck von der Gestalt :math:`S`; der letztere heisse das *Produkt* der durch :math:`S'` dargestellten Zahl in die durch :math:`S''` dargestellte Zahl.

Bei der so festgesetzten Rechnungsweise leuchtet die Gültigkeit der Rechnungsregeln 1–5 in § 13 unmittelbar ein. Auch die Gültigkeit der Vorschrift 6 in § 13 ist nicht schwer einzusehen. Zu dem Zwecke nehmen wir an, es seien etwa

.. math::

   S' = s^{m'} T'_0 + s^{m'+1} T'_1 + s^{m'+2} T'_2 + \dots

und

.. math::

   S''' = s^{m'''} T'''_0 + s^{m'''+1} T'''_1 + s^{m'''+2} T'''_2 + \dots

gegebene Ausdrücke von der Gestalt :math:`S`, und bedenken, dass unseren Festsetzungen entsprechend der erste Coefficient :math:`r'_0` aus :math:`T'_0` von :math:`0` verschieden sein muss. Indem wir nun die nämlichen Potenzen von :math:`s` auf beiden Seiten einer Gleichung

.. math::

   (2)\quad S'S'' = S'''

vergleichen, finden wir in eindeutig bestimmter Weise zunächst eine ganze Zahl :math:`m''` als Exponenten und sodann der Reihe nach gewisse Ausdrücke

.. math::

   T''_0, \; T''_1, \; T''_2, \; \dots

derart, dass der Ausdruck

.. math::

   S'' = s^{m''} T''_0 + s^{m''+1} T''_1 + s^{m''+2} T''_2 + \dots

bei Benutzung der Formel (1) der Gleichung (2) genügt; hiermit ist der gewünschte Nachweis erbracht.

Um endlich die Anordnung der Zahlen unseres Zahlensystems :math:`\Omega(s, t)` zu ermöglichen, treffen wir folgende Festsetzungen. Eine Zahl des Systems heisse :math:`<` oder :math:`> 0`, jenachdem in dem Ausdrucke :math:`S`, der sie darstellt, der erste Coefficient :math:`r_0` von :math:`T_0` :math:`<` oder :math:`> 0` ausfällt. Sind irgend zwei Zahlen :math:`a` und :math:`b` des complexen Zahlensystems vorgelegt, so heisse :math:`a < b` bez. :math:`a > b`, jenachdem :math:`a - b < 0` oder :math:`> 0` wird. Es leuchtet unmittelbar ein, dass bei diesen Festsetzungen die Regeln 13–16 in § 13 gültig sind, d. h. :math:`\Omega(s, t)` ist ein Desarguessches Zahlensystem (vgl. § 28).

Die Vorschrift 12 in § 13 ist, wie Gleichung (1) zeigt, für unser complexes Zahlensystem :math:`\Omega(s, t)` nicht erfüllt und damit ist die Richtigkeit des Satzes 39 vollständig erkannt.

In Uebereinstimmung mit Satz 38 gilt der Archimedische Satz (Satz 17 in § 13) für das soeben aufgestellte Zahlensystem :math:`\Omega(s, t)` nicht.

Es werde noch hervorgehoben, dass das Zahlensystem :math:`\Omega(s, t)` — ebenso wie die in § 9 und § 12 benutzten Zahlensysteme :math:`\Omega` und :math:`\Omega(t)` — nur eine abzählbare Menge von Zahlen enthält.
