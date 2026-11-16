:layout: book
:canonical_id: § 21
:breadcrumb_title: § 21
:order: 21
:folio: S. 46
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _grundlagen-de-s21:

.. folio:: § 21
   :page: 46

§ 21: Die Inhaltsgleichheit und das Flächenmass
===============================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

In § 20 haben wir gefunden, dass inhaltsgleiche Polygone

stets gleiches Flächenmass haben. Diese Aussage lässt sich auch umkehren.

Um diese Umkehrung zu beweisen , betrachten wir zunächst zwei Dreiecke ABC und AJB'C mit gemeinsamem rechten Winkel bei A. Die Flächenmasse dieser beiden Dreiecke drücken sich durch

die Formeln

$$
F(ABC) = \frac{1}{2} AB \cdot AC, \quad F(AB'C') = \frac{1}{2} AB' \cdot AC'
$$

aus. Nehmen wir an, dass diese beiden Flächenmasse einander gleich sind, so folgt:

$$
AB \cdot AC = AB' \cdot AC' \quad \text{oder} \quad AB : AB' = AC' : AC
$$

und hieraus ergiebt sich nach Satz 23, dass die beiden Geraden $BC$ und $B'C'$ einander parallel sind und sodann erweisen sich nach Satz 27 die beiden Dreiecke $BC'B'$ und $BC'C$ als inhaltsgleich. Durch Hinzufügen des Dreiecks $ABC'$ folgt, dass die beiden Dreiecke $ABC$ und $AB'C'$ einander inhaltsgleich sind. Wir haben damit erkannt, dass zwei rechtwinklige Dreiecke mit gleichem Flächenmass auch stets einander inhaltsgleich sind.

Nehmen wir jetzt ein beliebiges Dreieck mit der Grundlinie $g$ und der Höhe $h$, so ist dasselbe nach Satz 27 inhaltsgleich einem rechtwinkligen Dreieck mit den beiden Katheten $g$ und $h$; und da das ursprüngliche Dreieck offenbar dasselbe Flächenmass wie das rechtwinklige Dreieck besitzt, so folgt, dass in der letzten Betrachtung die Einschränkung auf rechtwinklige Dreiecke nicht nötig war; damit haben wir erkannt, *dass zwei beliebige Dreiecke mit gleichem Flächenmass auch stets einander inhaltsgleich sind*.

Es sei nunmehr ein beliebiges Polygon $P$ mit dem Flächenmass $g$ vorgelegt; $P$ zerfalle in $n$ Dreiecke mit den Flächenmassen bez. $g_1, g_2, \dots, g_n$; dann ist

$$
g = g_1 + g_2 + \dots + g_n.
$$

Wir construiren nun ein Dreieck $ABC$ mit der Grundlinie $AB = g$ und der Höhe $h = 1$ und markiren auf der Grundlinie die Punkte $A_1, A_2, \dots, A_{n-1}$, sodass

$$
g_1 = AA_1, \quad g_2 = A_1A_2, \; \dots, \; g_{n-1} = A_{n-2}A_{n-1}, \quad g_n = A_{n-1}B
$$

ausfällt. Da die Dreiecke innerhalb des Polygons $P$ bez. die gleichen Flächenmasse besitzen, wie die Dreiecke $AA_1C, A_1A_2C, \dots, A_{n-2}A_{n-1}C, A_{n-1}BC$, so sind sie nach dem vorhin Bewiesenen diesen auch inhaltsgleich; folglich ist das Polygon $P$ einem Dreiecke mit der Grundlinie $g$ und der Höhe $h = 1$ inhaltsgleich. Hieraus folgt mit Hülfe von Satz 24, dass zwei Polygone mit gleichem Flächenmass einander stets inhaltsgleich sind.

Die beiden in diesem und dem vorigen Paragraph gefundenen Thatsachen fassen wir in den folgenden Satz zusammen:

.. _grundlagen-de-thm-30:

**Satz 30.** Zwei inhaltsgleiche Polygone haben stets das gleiche Flächenmass ; und umgekehrt : Zwei Polygone mit gleichem Flächenmass sind stets einander inhaltsgleich.

Insbesondere müssen zwei inhaltsgleiche Rechtecke mit einer gemeinsamen Seite auch in den anderen Seiten übereinstimmen. Auch folgt der Satz:

.. _grundlagen-de-thm-31:

**Satz 31.** Zerlegt man ein Rechteck durch Gerade in mehrere Dreiecke und lässt auch nur eines dieser Dreiecke fort, so kann man mit den übrigen Dreiecken das Rechteck nicht mehr ausfüllen.

Dieser Satz 31 ist von F. Schur [#fn1]_ und W. Killing [#fn2]_ mit Hülfe des Archimedischen Axioms bewiesen und von O. Stolz [#fn3]_ als Axiom hingestellt worden.

völlig unabhängig von dem Archimedischen Axiom gilt. Der Satz 31 reicht übrigens zur Begründung des Euklidischen Satzes von der Gleichheit der Höhen in inhaltsgleichen Dreiecken auf gleicher Grundlinie (Satz 28) an sich nicht aus , wenn man von der Anwendung des Archimedischen Axioms absieht.

Zum Beweise der Sätze 28, 29, 30 haben wir wesentlich die in Kapitel III § 15 eingeführte Streckenrechnung benutzt, und da diese im Wesentlichen auf dem Pascalschen Satze (Satz 21) beruht, so erweist sich für die Lehre von den Flächeninhalten der

Pascalsche Satz als der wichtigste Baustein. Wir erkennen leicht, dass auch umgekehrt aus den Sätzen 27 und 28 der Pascalsche Satz wieder gewonnen werden kann.

Von zwei Polygonen P und Q nennen wir P inhaltskleiner bez. inhaltsgrösser als Q, je nachdem das Flächenmass F(P) kleiner oder grösser als F(Q) ausfällt. Es ist nach dem Vorstehenden klar, dass die Begriffe inhaltsgleich, inhaltskleiner und inhaltsgrösser sich gegenseitig ausschliessen. Ferner erkennen wir leicht,

Kapitel V. Der Dcsarguesscke Satz. § 22. 49

dass ein Polygon, welches ganz im Inneren eines anderen Polygons liegt, stets inhaltskleiner als dieses sein muss.

Hiermit haben wir die wesentlichen Sätze der Lehre von den Flächeninhalten begründet.


----

.. rubric:: Fussnoten

.. [#fn1] *Sitzungsberichte der Dorpater Naturf. Ges.* 1892.

.. [#fn2] *Grundlagen der Geometrie*, Bd. 2, Absch. 5, § 5, 1898.

.. [#fn3] *Monatshefte für Math. und Phys.*, Jahrgang 5, 1894.
