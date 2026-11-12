:layout: book

.. _grundlagen-chapter-6-de:

Kapitel VI: Der Pascalsche Satz
===============================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, B. G. Teubner, Leipzig 1899)

.. contents:: Gliederung
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-de-s31:

.. folio:: § 31
   :page: 71

§ 31. Zwei Sätze über die Beweisbarkeit des Pascalschen Satzes
--------------------------------------------------------------

Der Desarguessche Satz (Satz 32) lässt sich bekanntlich aus den Axiomen I, II, III, d. h. unter wesentlicher Benutzung der räumlichen Axiome beweisen ; in § 23 habe ich gezeigt , dass der Beweis desselben ohne die räumlichen Axiome der Gruppe I und ohne die Congruenzaxiome IV nicht möglich ist, selbst wenn die Benutzung des Archimedischen Axioms gestattet wird.

In § 14 ist der Pascalsche Satz (Satz 21) und damit nach § 22 auch der Desarguessche Satz aus den Axiomen I 1 — 2, II — IV, also mit Ausschluss der räumlichen Axiome und unter wesentlicher Benutzung der Congruenzaxiome abgeleitet worden. Es entsteht die Frage , ob auch der Pascalsche Satz ohne Hinzuziehung der Congruenzaxiome bewiesen werden kann. Unsere Untersuchung wird zeigen, dass in dieser Hinsicht der Pascalsche Satz sich völlig anders als der Desarguessche Satz verhält, indem bei dem Beweise des Pascalschen Satzes die Zulassung oder Ausschliessung des Archimedischen Axioms von entscheidendem Einflüsse für seine Gültigkeit ist. Die wesentlichen Ergebnisse unserer Untersuchung fassen wir in den folgenden zwei Sätzen zusammen:

.. _grundlagen-de-thm-36:

**Satz 36.** Der Pascalsche Satz (Satz 21) ist beweisbar auf Grund der Axiome I, II, III, V, d. h. unter Ausschliessung der Congruenzaxiome mit Zuhülfenahme des Archimedischen Axioms.

.. _grundlagen-de-thm-37:

**Satz 37.** Der Pascalsche Satz (Satz 21) ist *nicht* beweisbar auf Grund der Axiome I, II, III, d. h. unter Ausschliessung der Congruenzaxiome sowie des Archimedischen Axioms.

In der Fassung dieser beiden Sätze können nach dem allgemeinen Satze 35 die räumlichen Axiome I 3–7 auch durch die ebene Forderung ersetzt werden, dass der Desarguessche Satz (Satz 32) gelten soll.

.. _grundlagen-de-s32:

.. folio:: § 32
   :page: 72

§ 32. Das commutative Gesetz der Multiplikation im Archimedischen Zahlensystem
------------------------------------------------------------------------------

Die Beweise der Sätze 36 und 37 beruhen wesentlich auf gewissen gegenseitigen Beziehungen, welche für die Rechnungsregeln und Grundthatsachen der Arithmetik bestehen und deren Kenntnis auch an sich von Interesse erscheint. Wir stellen die folgenden zwei Sätze auf:

.. _grundlagen-de-thm-38:

**Satz 38.** Für ein Archimedisches Zahlensystem ist das commutative Gesetz der Multiplikation eine notwendige Folge der übrigen Rechnungsgesetze ; d. h., wenn ein Zahlensystem die in § 13 aufgezählten Eigenschaften 1 — 11, 13 — 17 besitzt, so folgt notwendig, dass dasselbe auch der Formel 12 genügt.

**Beweis.** Zunächst bemerken wir: wenn $a$ eine beliebige Zahl des Zahlensystems und

$$
n = 1 + 1 + \dots + 1
$$

eine ganze rationale positive Zahl ist, so gilt für $a$ und $n$ stets das commutative Gesetz der Multiplikation; es ist nämlich

$$
\begin{aligned}
an &= a(1 + 1 + \dots + 1) = a \cdot 1 + a \cdot 1 + \dots + a \cdot 1 = a + a + \dots + a
\end{aligned}
$$

und ebenso

$$
\begin{aligned}
na &= (1 + 1 + \dots + 1)a = 1 \cdot a + 1 \cdot a + \dots + 1 \cdot a = a + a + \dots + a.
\end{aligned}
$$

Es seien nun im Gegensatz zu unserer Behauptung $a, b$ solche zwei Zahlen des Zahlensystems, für welche das commutative Gesetz der Multiplikation nicht gültig ist. Wir dürfen dann, wie leicht ersichtlich, die Annahmen

$$
a > 0, \quad b > 0, \quad ab - ba > 0
$$

machen. Wegen der Forderung 6 in § 13 giebt es eine Zahl $c \; (> 0)$, so dass

$$
(a + b + 1)c = ab - ba
$$

ist. Endlich wählen wir eine Zahl $d$, die zugleich den Ungleichungen

$$
d > 0, \quad d < 1, \quad d < c
$$

genügt, und bezeichnen mit $m$ und $n$ zwei solche ganze rationale Zahlen $\ge 0$, für die

$$
md \le a < (m + 1)d \quad \text{bez.} \quad nd \le b < (n + 1)d
$$

wird. Das Vorhandensein solcher Zahlen $m, n$ ist eine unmittelbare Folgerung des Archimedischen Satzes (Satz 17 in § 13). Mit Rücksicht auf die Bemerkung zu Anfang dieses Beweises erhalten wir aus den letzteren Ungleichungen durch Multiplikation

$$
\begin{aligned}
ab &< mnd^2 + (m + n + 1)d^2, \\
ba &\ge mnd^2,
\end{aligned}
$$

also durch Subtraktion

$$
ab - ba < (m + n + 1)d^2.
$$

Nun ist

$$
md \le a, \quad nd \le b, \quad d < 1
$$

und folglich

$$
(m + n + 1)d < a + b + 1,
$$

d. h.

$$
ab - ba < (a + b + 1)d
$$

oder wegen $d < c$

$$
ab - ba < (a + b + 1)c.
$$

Diese Ungleichung widerspricht der Bestimmung der Zahl $c$, und damit ist der Beweis für den Satz 38 erbracht.

.. _grundlagen-de-s33:

.. folio:: § 33
   :page: 73

§ 33. Das commutative Gesetz der Multiplikation im Nicht-Archimedischen Zahlensystem
------------------------------------------------------------------------------------

.. _grundlagen-de-thm-39:

**Satz 39.** Für ein Nicht-Archimedisches Zahlensystem ist das commutative Gesetz der Multiplikation nicht eine notwendige Folge der übrigen Rechnungsgesetze; d. h. es giebt ein Zahlensystem, das die in § 13 aufgezählten Eigenscliaften 1 — 11, 13 — 16 besitzt — ein Desarguessches Zahlensystem nach §28 — , in welchem nicht das commutative Gesetz (12) der Multiplikation besteht.

**Beweis.** Es sei $t$ ein Parameter und $T$ irgend ein Ausdruck mit einer endlichen oder unendlichen Gliederzahl von der Gestalt

$$
T = r_0 t^n + r_1 t^{n+1} + r_2 t^{n+2} + r_3 t^{n+3} + \dots;
$$

darin mögen $r_0 \; (\neq 0), r_1, r_2, \dots$ beliebige rationale Zahlen bedeuten und $n$ sei eine beliebige ganze rationale Zahl $\gtreqless 0$. Ferner sei $s$ ein anderer Parameter und $S$ irgend ein Ausdruck mit einer endlichen oder unendlichen Gliederzahl von der Gestalt

$$
S = s^m T_0 + s^{m+1} T_1 + s^{m+2} T_2 + \dots;
$$

darin mögen $T_0 \; (\neq 0), T_1, T_2, \dots$ beliebige Ausdrücke von der Gestalt $T$ bezeichnen und $m$ sei wiederum eine beliebige ganze rationale Zahl $\gtreqless 0$. Die Gesamtheit aller Ausdrücke von der Gestalt $S$ sehen wir als ein complexes Zahlensystem $\Omega(s, t)$ an, in dem wir folgende Rechnungsregeln festsetzen: man rechne mit $s$ und $t$, wie mit Parametern nach den Regeln 7–11 in § 13, während man an Stelle der Regel 12 stets die Formel

$$
(1)\quad ts = 2st
$$

anwende.

Sind nun $S', S''$ irgend zwei Ausdrücke von der Gestalt $S$:

$$
\begin{aligned}
S' &= s^{m'} T'_0 + s^{m'+1} T'_1 + s^{m'+2} T'_2 + \dots, \\
S'' &= s^{m''} T''_0 + s^{m''+1} T''_1 + s^{m''+2} T''_2 + \dots,
\end{aligned}
$$

so kann man offenbar durch Zusammenfügung einen neuen Ausdruck $S' + S''$ bilden, der wiederum von der Gestalt $S$ und zugleich eindeutig bestimmt ist; dieser Ausdruck $S' + S''$ heisst die *Summe* der durch $S', S''$ dargestellten Zahlen.

Durch gliedweise Multiplikation der beiden Ausdrücke $S', S''$ gelangen wir zunächst zu einem Ausdrucke von der Gestalt

$$
\begin{aligned}
S'S'' &= s^{m'}T'_0 s^{m''}T''_0 + (s^{m'}T'_0 s^{m''+1}T''_1 + s^{m'+1}T'_1 s^{m''}T''_0) \\
&\quad + (s^{m'}T'_0 s^{m''+2}T''_2 + s^{m'+1}T'_1 s^{m''+1}T''_1 + s^{m'+2}T'_2 s^{m''}T''_0) + \dots.
\end{aligned}
$$

Dieser Ausdruck wird bei Benutzung der Formel (1) offenbar ein eindeutig bestimmter Ausdruck von der Gestalt $S$; der letztere heisse das *Produkt* der durch $S'$ dargestellten Zahl in die durch $S''$ dargestellte Zahl.

Bei der so festgesetzten Rechnungsweise leuchtet die Gültigkeit der Rechnungsregeln 1–5 in § 13 unmittelbar ein. Auch die Gültigkeit der Vorschrift 6 in § 13 ist nicht schwer einzusehen. Zu dem Zwecke nehmen wir an, es seien etwa

$$
S' = s^{m'} T'_0 + s^{m'+1} T'_1 + s^{m'+2} T'_2 + \dots
$$

und

$$
S''' = s^{m'''} T'''_0 + s^{m'''+1} T'''_1 + s^{m'''+2} T'''_2 + \dots
$$

gegebene Ausdrücke von der Gestalt $S$, und bedenken, dass unseren Festsetzungen entsprechend der erste Coefficient $r'_0$ aus $T'_0$ von $0$ verschieden sein muss. Indem wir nun die nämlichen Potenzen von $s$ auf beiden Seiten einer Gleichung

$$
(2)\quad S'S'' = S'''
$$

vergleichen, finden wir in eindeutig bestimmter Weise zunächst eine ganze Zahl $m''$ als Exponenten und sodann der Reihe nach gewisse Ausdrücke

$$
T''_0, \; T''_1, \; T''_2, \; \dots
$$

derart, dass der Ausdruck

$$
S'' = s^{m''} T''_0 + s^{m''+1} T''_1 + s^{m''+2} T''_2 + \dots
$$

bei Benutzung der Formel (1) der Gleichung (2) genügt; hiermit ist der gewünschte Nachweis erbracht.

Um endlich die Anordnung der Zahlen unseres Zahlensystems $\Omega(s, t)$ zu ermöglichen, treffen wir folgende Festsetzungen. Eine Zahl des Systems heisse $<$ oder $> 0$, jenachdem in dem Ausdrucke $S$, der sie darstellt, der erste Coefficient $r_0$ von $T_0$ $<$ oder $> 0$ ausfällt. Sind irgend zwei Zahlen $a$ und $b$ des complexen Zahlensystems vorgelegt, so heisse $a < b$ bez. $a > b$, jenachdem $a - b < 0$ oder $> 0$ wird. Es leuchtet unmittelbar ein, dass bei diesen Festsetzungen die Regeln 13–16 in § 13 gültig sind, d. h. $\Omega(s, t)$ ist ein Desarguessches Zahlensystem (vgl. § 28).

Die Vorschrift 12 in § 13 ist, wie Gleichung (1) zeigt, für unser complexes Zahlensystem $\Omega(s, t)$ nicht erfüllt und damit ist die Richtigkeit des Satzes 39 vollständig erkannt.

In Uebereinstimmung mit Satz 38 gilt der Archimedische Satz (Satz 17 in § 13) für das soeben aufgestellte Zahlensystem $\Omega(s, t)$ nicht.

Es werde noch hervorgehoben, dass das Zahlensystem $\Omega(s, t)$ — ebenso wie die in § 9 und § 12 benutzten Zahlensysteme $\Omega$ und $\Omega(t)$ — nur eine abzählbare Menge von Zahlen enthält.

.. _grundlagen-de-s34:

.. folio:: § 34
   :page: 75

§ 34. Beweis der beiden Sätze über den Pascalschen Satz (Nicht-Pascalsche Geometrie)
------------------------------------------------------------------------------------

Wenn in einer räumlichen Geometrie die sämtlichen Axiome I, II, III erfüllt sind, so gilt auch der Desarguessche Satz (Satz 32) und mithin ist nach Kapitel V § 24 bis § 26 in dieser Geometrie die Einführung einer Streckenrechnung möglich, für welche die Vorschriften 1 — 11, 13 — 16 in § 13 gültig sind. Setzen wir nun das Archimedische Axiom V in unserer Geometrie voraus, so gilt

offenbar für die Streckenrechnung der Archimedische Satz (Satz 17 in § 13) und mithin nach Satz 38 auch das commutative Gesetz der Multiplikation. Da aber die hier in Rede stehende in § 24 (Fig. 40) eingeführte Definition des Streckenproduktes mit der in § 15 (Fig. 21) angewandten Definition übereinstimmt, so bedeutet gemäss der in § 15 ausgeführten Construktion das commutative Gesetz der Multiplikation zweier Strecken auch hier nichts anderes als den Pascalschen Satz. Damit ist die Richtigkeit des Satzes 36 erkannt.

Um den Satz 37 zu beweisen, fassen wir das in § 33 aufgestellte Desarguessche Zahlensystem $\Omega(s, t)$ ins Auge und construiren mit Hülfe desselben auf die in § 29 beschriebene Art eine räumliche Geometrie, in der die sämtlichen Axiome I, II, III erfüllt sind. Trotzdem gilt der Pascalsche Satz in dieser Geometrie nicht, da das commutative Gesetz der Multiplikation in dem Desarguesschen Zahlensystem $\Omega(s, t)$ nicht besteht. Die so aufgebaute „*Nicht-Pascalsche*“ Geometrie ist in Uebereinstimmung mit dem vorhin bewiesenen Satz 36 notwendig zugleich auch eine „*Nicht-Archimedische*“ Geometrie.

Es ist offenbar, dass der Pascalsche Satz sich bei unseren Annahmen auch dann nicht beweisen lässt, wenn man die räumliche Geometrie als einen Teil einer Geometrie von beliebig vielen Dimensionen auffasst, in welcher neben den Punkten, Geraden und Ebenen noch weitere lineare Elemente vorhanden sind und für diese ein entsprechendes System von Axiomen der Verknüpfung und Anordnung, sowie das Parallelenaxiom zu Grunde gelegt wird.

.. _grundlagen-de-s35:

.. folio:: § 35
   :page: 76

§ 35. Beweis eines beliebigen Schnittpunktsatzes mittelst des Desarguesschen und des Pascalschen Satzes
-------------------------------------------------------------------------------------------------------

Ein jeder ebener Schnittpunktsatz hat notwendig diese Form: Man wähle zunächst ein System von Punkten und Geraden willkürlich, bez. mit der Bedingung, dass für gewisse von diesen Punkten und Geraden die vereinigte Lage vorgeschrieben ist ; wenn man dann in bekannter Weise Verbindungsgerade und Schnittpunkte construirt, so gelangt man schliesslich zu einem bestimmten System von drei Geraden, von denen der Satz aussagt, dass sie durch den nämlichen Punkt hindurchlaufen.

Es sei nun eine ebene Geometrie vorgelegt, in der sämtliche Axiome I 1–2, II–V gültig sind; nach Kap. III § 17 können wir dann vermittelst eines rechtwinkligen Axenkreuzes jedem Punkte ein Zahlenpaar $(x, y)$ und jeder Geraden ein Verhältnis von drei Zahlen $(u : v : w)$ entsprechen lassen; hierbei sind $x, y, u, v, w$ jedenfalls reelle Zahlen, von denen $u, v$ nicht beide verschwinden, und die Bedingung für die vereinigte Lage von Punkt und Geraden

$$
ux + vy + w = 0
$$

bedeutet eine Gleichung im gewöhnlichen Sinne. Umgekehrt dürfen wir, falls $x, y, u, v, w$ Zahlen des in § 9 construirten algebraischen Bereiches $\Omega$ sind und $u, v$ nicht beide verschwinden, gewiss annehmen, dass das Zahlenpaar $(x, y)$ und das Zahlentripel $(u : v : w)$ einen Punkt bez. eine Gerade in der vorgelegten Geometrie liefert.

Führen wir für alle Punkte und Geraden, die in einem beliebigen ebenen Schnittpunktsatze auftreten, die betreffenden Zahlenpaare und Zahlentripel ein, so wird dieser Schnittpunktsatz aussagen, dass ein bestimmter, von gewissen Parametern $p_1, \dots, p_r$ rational abhängiger Ausdruck $A(p_1, \dots, p_r)$ mit reellen Coefficienten stets verschwindet, sobald wir für jene Parameter irgend welche Zahlen des in § 9 betrachteten Bereiches $\Omega$ einsetzen. Wir schliessen hieraus, dass der Ausdruck $A(p_1, \dots, p_r)$ auch identisch auf Grund der Rechnungsgesetze 7–12 in § 13 verschwinden muss.

Da in der vorgelegten Geometrie nach § 22 der Desarguessche Satz gilt, so können wir gewiss auch die in § 24 eingeführte Streckenrechnung benutzen, und wegen der Gültigkeit des Pascalschen Satzes trifft für diese Streckenrechnung auch das commutative Gesetz der Multiplikation zu, sodass in dieser Streckenrechnung sämtliche Rechnungsgesetze 7–12 in § 13 gültig sind.

Indem wir die Axen des bisher benutzten Axenkreuzes auch als Axen dieser neuen Streckenrechnung gewählt und die Einheitspunkte $E$ und $E'$ geeignet festgesetzt denken, erkennen wir die Uebereinstimmung der neuen Streckenrechnung mit der früheren Coordinatenrechnung.

Um in der neuen Streckenrechnung das identische Verschwinden des Ausdruckes $A(p_1, \dots, p_r)$ nachzuweisen, genügt die Anwendung des Desarguesschen und Pascalschen Satzes und damit erkennen

wir, dass jeder in der vorgelegten Geometrie geltende Schnittpunktsatz durch Konstruktion geeigneter Hülfspunkte und Hülfsgeraden sich stets als eine Kombination des Desarguesschen und Pascalschen Satzes herausstellen muss. Zum Nachweise der Richtigkeit des Schnittpunktsatzes brauchen wir also nicht auf die Congruenzsätze zurückzugreifen.
