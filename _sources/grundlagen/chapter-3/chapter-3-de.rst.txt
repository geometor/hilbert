:layout: book

.. _grundlagen-chapter-3-de:

Kapitel III: Die Lehre von den Proportionen
===========================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, B. G. Teubner, Leipzig 1899)

.. contents:: Gliederung
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-de-s13:

.. folio:: § 13
   :page: 26

§ 13. Complexe Zahlensysteme
----------------------------

Am Anfang dieses Kapitels wollen wir einige kurze Auseinandersetzungen über complexe Zahlensysteme vorausschicken, die uns später insbesondere zur Erleichterung der Darstellung nützlich sein werden.

Die reellen Zahlen bilden in ihrer Gesamtheit ein System von Dingen mit folgenden Eigenschaften:

**Sätze der Verknüpfung (1–12):**

**1.** Aus der Zahl $a$ und der Zahl $b$ entsteht durch „Addition“ eine bestimmte Zahl $c$, in Zeichen

$$
a + b = c \quad \text{oder} \quad c = a + b.
$$

**2.** Es giebt eine bestimmte Zahl — sie heisse $0$ —, so dass für jedes $a$ zugleich

$$
a + 0 = a \quad \text{und} \quad 0 + a = a
$$

ist.

**3.** Wenn $a$ und $b$ gegebene Zahlen sind, so existirt stets eine und nur eine Zahl $x$ und auch eine und nur eine Zahl $y$, so dass

$$
a + x = b \quad \text{bez.} \quad y + a = b
$$

wird.

**4.** Aus der Zahl $a$ und der Zahl $b$ entsteht noch auf eine andere Art durch „Multiplikation“ eine bestimmte Zahl $c$, in Zeichen

$$
ab = c \quad \text{oder} \quad c = ab.
$$

**5.** Es giebt eine bestimmte Zahl — sie heisse $1$ —, so dass für jedes $a$ zugleich

$$
a \cdot 1 = a \quad \text{und} \quad 1 \cdot a = a
$$

ist.

**6.** Wenn $a$ und $b$ beliebig gegebene Zahlen sind und $a$ nicht $0$ ist, so existirt stets eine und nur eine Zahl $x$ und auch eine und nur eine Zahl $y$, so dass

$$
ax = b \quad \text{bez.} \quad ya = b
$$

wird.

Wenn $a, b, c$ beliebige Zahlen sind, so gelten stets folgende Rechnungsgesetze:

$$
\begin{aligned}
\mathbf{7.}\quad a + (b + c) &= (a + b) + c \\
\mathbf{8.}\quad a + b &= b + a \\
\mathbf{9.}\quad a(bc) &= (ab)c \\
\mathbf{10.}\quad a(b + c) &= ab + ac \\
\mathbf{11.}\quad (a + b)c &= ac + bc \\
\mathbf{12.}\quad ab &= ba.
\end{aligned}
$$

**Sätze der Anordnung (13–16):**

**13.** Wenn $a, b$ irgend zwei verschiedene Zahlen sind, so ist stets eine bestimmte von ihnen (etwa $a$) grösser ($>$) als die andere; die letztere heisst dann die kleinere, in Zeichen:

$$
a > b \quad \text{und} \quad b < a.
$$

**14.** Wenn $a > b$ und $b > c$, so ist auch $a > c$.

**15.** Wenn $a > b$ ist, so ist auch stets

$$
a + c > b + c \quad \text{und} \quad c + a > c + b.
$$

**16.** Wenn $a > b$ und $c > 0$ ist, so ist auch stets

$$
ac > bc \quad \text{und} \quad ca > cb.
$$

**Archimedischer Satz (17):**

**17.** Wenn $a > 0$ und $b > 0$ zwei beliebige Zahlen sind, so ist es stets möglich, $a$ zu sich selbst so oft zu addiren, dass die entstehende Summe die Eigenschaft hat

$$
a + a + \dots + a > b.
$$

Ein System von Dingen, das nur einen Teil der Eigenschaften 1–17 besitzt, heisse ein *complexes Zahlensystem* oder auch ein *Zahlensystem* schlechthin. Ein Zahlensystem heisse ein *Archimedisches* oder ein *Nicht-Archimedisches*, jenachdem dasselbe der Forderung 17 genügt oder nicht.

Von den aufgestellten Eigenschaften 1–17 sind einige Folgen der übrigen. Es entsteht die Aufgabe, die logische Abhängigkeit dieser Eigenschaften zu untersuchen. Wir werden in Kapitel VI § 32 und § 33 zwei bestimmte Fragen der angedeuteten Art wegen ihrer geometrischen Bedeutung beantworten und wollen hier nur darauf hinweisen, dass jedenfalls die letzte Forderung 17 keine logische Folge der übrigen Eigenschaften ist, da ja beispielsweise das in § 12 betrachtete complexe Zahlensystem $\Omega(t)$ sämtliche Eigenschaften 1–16 besitzt, aber nicht die Forderung 17 erfüllt.

.. _grundlagen-de-s14:

.. folio:: § 14
   :page: 28

§ 14. Beweis des Pascalschen Satzes
-----------------------------------

In diesem und dem folgenden Kapitel legen wir unserer Untersuchung die ebenen Axiome sämtlicher Gruppen mit Ausnahme des Archimedischen Axioms , d. h. die Axiome I 1 — 2 und II — IV zu Grunde. In dem gegenwärtigen Kapitel III gedenken

wir Euklids Lehre von den Proportionen mittelst der genannten Axiome, d.h. in der Ebene und unabhängig vom Archimedischen Axiom zu begründen.

Zu dem Zwecke beweisen wir zunächst eine Thatsache, die ein besonderer Fall des bekannten Pascalschen Satzes aus der Lehre von den Kegelschnitten ist und die ich künftig kurz als den Pascalschen Satz bezeichnen will. Dieser Satz lautet :

.. _grundlagen-de-thm-21:

**Satz 21** [#fn1]_ **(Pascalscher Satz).** Es seien $A, B, C$ bez. $A', B', C'$ je drei Punkte auf zwei sich schneidenden Geraden, die vom Schnittpunkte der Geraden verschieden sind; ist dann $CB'$ parallel $BC'$ und $CA'$ parallel $AC'$, so ist auch $BA'$ parallel $AB'$.

Um den Beweis für diesen Satz zu erbringen, führen wir zunächst folgende Bezeichnungsweise ein. In einem rechtwinkligen Dreiecke ist offenbar die Kathete $a$ durch die Hypotenuse $c$ und den von $a$ und $c$ eingeschlossenen Basiswinkel $\alpha$ eindeutig bestimmt: wir setzen kurz

$$
a = \alpha c,
$$

sodass das Symbol $\alpha c$ stets eine bestimmte Strecke bedeutet, sobald $c$ eine beliebig gegebene Strecke und $\alpha$ ein beliebig gegebener spitzer Winkel ist.

Nunmehr möge $c$ eine beliebige Strecke und $\alpha, \beta$ mögen zwei beliebige spitze Winkel bedeuten; wir behaupten, dass allemal die Streckencongruenz

$$
\alpha\beta c \equiv \beta\alpha c
$$

besteht und somit die Symbole $\alpha, \beta$ stets mit einander vertauschbar sind.

Um diese Behauptung zu beweisen, nehmen wir die Strecke $c = AB$ und tragen an diese Strecke in $A$ zu beiden Seiten die Winkel $\alpha$ und $\beta$ an. Dann fällen wir von $B$ aus auf die anderen Schenkel dieser Winkel die Lote $BC$ und $BD$, verbinden $C$ mit $D$ und fällen schliesslich von $A$ aus das Lot $AE$ auf $CD$.

Da die Winkel $\angle ACB$ und $\angle ADB$ Rechte sind, so liegen die vier Punkte $A, B, C, D$ auf einem Kreise und demnach sind die beiden Winkel $\angle ACD$ und $\angle ABD$ als Peripheriewinkel auf derselben Sehne $AD$ einander congruent. Nun ist einerseits $\angle ACD$ zusammen mit dem $\angle CAE$ und andererseits $\angle ABD$ zusammen mit $\angle BAD$ je ein Rechter und folglich sind auch die Winkel $\angle CAE$ und $\angle BAD$ einander congruent, d. h. es ist

$$
\angle CAE \equiv \beta,
$$

und daher

$$
\angle DAE \equiv \alpha.
$$

Wir gewinnen nun unmittelbar die Streckencongruenzen

$$
\begin{aligned}
\beta c &\equiv AD, & \alpha c &\equiv AC, \\
\alpha\beta c &\equiv \alpha(AD) \equiv AE, & \beta\alpha c &\equiv \beta(AC) \equiv AE,
\end{aligned}
$$

und hieraus folgt die Richtigkeit der vorhin behaupteten Congruenz.

Wir kehren nun zur Figur des Pascalschen Satzes zurück und bezeichnen den Schnittpunkt der beiden Geraden mit $O$ und die Strecken $OA, OB, OC, OA', OB', OC', CB', BC', CA', AC', BA', AB'$ bez. mit $a, b, c, a', b', c', l, l^*, m, m^*, n, n^*$. Sodann fällen wir von $O$ Lote auf $l, m, n$; das Lot auf $l$ schliesse mit den beiden Geraden $OA, OA'$ die spitzen Winkel $\lambda', \lambda$ ein und die Lote auf $m$ bez. $n$ mögen mit den Geraden $OA$ und $OA'$ die spitzen Winkel $\mu', \mu$ bez. $\nu', \nu$ bilden. Drücken wir nun diese drei Lote in der vorhin angegebenen Weise mit Hülfe der Hypotenusen und Basiswinkel in den betreffenden rechtwinkligen Dreiecken auf doppelte Weise aus, so erhalten wir folgende drei Streckencongruenzen

$$
\begin{aligned}
(1)\quad \lambda b' &\equiv \lambda' c, \\
(2)\quad \mu a' &\equiv \mu' c, \\
(3)\quad \nu a' &\equiv \nu' b.
\end{aligned}
$$

Da nach Voraussetzung $l$ parallel $l^*$ und $m$ parallel $m^*$ sein soll, so stimmen die von $O$ auf $l^*$ bez. $m^*$ zu fällenden Lote mit den Loten auf $l$ bez. $m$ überein und wir erhalten somit

$$
\begin{aligned}
(4)\quad \lambda c' &\equiv \lambda' b, \\
(5)\quad \mu c' &\equiv \mu' a.
\end{aligned}
$$

Wenn wir auf die Congruenz (3) links und rechts das Symbol $\lambda'\mu$ anwenden und bedenken, dass nach dem vorhin Bewiesenen die in Rede stehenden Symbole mit einander vertauschbar sind, so finden wir

$$
\nu\lambda'\mu a' \equiv \nu'\mu\lambda' b.
$$

In dieser Congruenz berücksichtigen wir links die Congruenz (2) und rechts (4); dann wird

$$
\nu\lambda'\mu' c \equiv \nu'\mu\lambda c'
$$

oder

$$
\nu\mu'\lambda' c \equiv \nu'\lambda\mu c'.
$$

Hierin berücksichtigen wir links die Congruenz (1) und rechts (5); dann wird

$$
\nu\mu'\lambda b' \equiv \nu'\lambda\mu' a
$$

oder

$$
\lambda\mu'\nu b' \equiv \lambda\mu'\nu' a.
$$

Wegen der Bedeutung unserer Symbole schliessen wir aus der letzten Congruenz sofort

$$
\mu'\nu b' \equiv \mu'\nu' a
$$

und hieraus

$$
(6)\quad \nu b' \equiv \nu' a.
$$

Fassen wir nun das von $O$ auf $n$ gefällte Lot in's Auge und fällen auf dasselbe Lote von $A$ und $B'$ aus, so zeigt die Congruenz (6), dass die Fusspunkte der letzteren beiden Lote zusammenfallen, d. h. die Gerade $n^* = AB'$ steht zu dem Lote auf $n$ senkrecht und ist mithin zu $n$ parallel. Damit ist der Beweis für den Pascalschen Satz erbracht.

Wenn irgend eine Gerade, ein Punkt ausserhalb derselben und irgend ein Winkel gegeben ist, so kann man offenbar durch Abtragen dieses Winkels und Ziehen einer Parallelen eine Gerade finden, die durch den gegebenen Punkt geht und die gegebene Gerade unter dem gegebenen Winkel schneidet. Im Hinblick auf diesen Umstand dürfen wir uns zum Beweise des Pascalschen Satzes auch des folgenden einfachen Schlussverfahrens bedienen, das ich einer Mittheilung von anderer Seite verdanke.

Man ziehe durch $B$ eine Gerade, die $OA'$ im Punkte $D'$ unter dem Winkel $OCA'$ trifft, so dass die Congruenz

$$
(1^*)\quad \angle OCA' \equiv \angle OD'B
$$

gilt; dann ist nach einem bekannten Satze aus der Lehre vom Kreise $CBD'A'$ ein Kreisviereck und mithin gilt nach dem Satze von der Congruenz der Peripheriewinkel auf der nämlichen Sehne die Congruenz

$$
(2^*)\quad \angle OBA' \equiv \angle OD'C.
$$

Da $CA'$ und $AC'$ nach Voraussetzung einander parallel sind, so ist

$$
(3^*)\quad \angle OCA' \equiv \angle OAC';
$$

aus $(1^*)$ und $(3^*)$ folgern wir die Congruenz

$$
\angle OD'B \equiv \angle OAC';
$$

dann aber ist auch $BAD'C'$ ein Kreisviereck und mithin gilt nach dem Satze von den Winkeln im Kreisviereck die Congruenz

$$
(4^*)\quad \angle OAD' \equiv \angle OC'B.
$$

Da ferner nach Voraussetzung $CB'$ parallel $BC'$ ist, so haben wir auch

$$
(5^*)\quad \angle OB'C \equiv \angle OC'B;
$$

aus $(4^*)$ und $(5^*)$ folgern wir die Congruenz

$$
\angle OAD' \equiv \angle OB'C;
$$

diese endlich lehrt, dass $CAD'B'$ ein Kreisviereck ist, und mithin gilt auch die Congruenz

$$
(6^*)\quad \angle OAB' \equiv \angle OD'C.
$$

Aus $(2^*)$ und $(6^*)$ folgt

$$
\angle OBA' \equiv \angle OAB'
$$

und die Congruenz lehrt, dass $BA'$ und $AB'$ einander parallel sind, wie es der Pascalsche Satz verlangt.

Fällt $D'$ mit einem der Punkte $A', B', C'$ zusammen, so wird eine Abänderung dieses Schlussverfahrens nothwendig, die leicht ersichtlich ist.

.. picture:: /_static/figures/fig_pascal_orthogonal.svg
   :alt: Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.
   :caption: **Affine Pascal's (Pappus's) Hexagon Theorem (Theorem 21).** Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.


.. _grundlagen-de-s15:

.. folio:: § 15
   :page: 32

§ 15. Die Streckenrechnung auf Grund des Pascalschen Satzes
-----------------------------------------------------------

Der im vorigen Paragraph bewiesene Pascalsche Satz setzt uns in den Stand, in die Geometrie eine Rechnung mit Strecken einzuführen, in der die Rechnungsregeln für reelle Zahlen sämtlich unverändert gültig sind.

Statt des Wortes „congruent“ und des Zeichens $\equiv$ bedienen wir uns in der Streckenrechnung des Wortes „gleich“ und des Zeichens $=$.

Wenn $A, B, C$ drei Punkte einer Geraden sind und $B$ zwischen $A$ und $C$ liegt, so bezeichnen wir $c = AC$ als die *Summe* der beiden Strecken $a = AB$ und $b = BC$ und setzen

$$
c = a + b.
$$

Die Strecken $a$ und $b$ heissen *kleiner* als $c$, in Zeichen:

$$
a < c, \quad b < c,
$$

und $c$ heisst *grösser* als $a$ und $b$, in Zeichen:

$$
c > a, \quad c > b.
$$

Aus den linearen Congruenzaxiomen IV 1–3 entnehmen wir leicht, dass für die eben definirte Addition der Strecken das associative Gesetz

$$
a + (b + c) = (a + b) + c
$$

sowie das commutative Gesetz

$$
a + b = b + a
$$

gültig ist.

Um das Produkt einer Strecke a in eine Strecke b geometrisch zu definiren, bedienen wir uns folgender Construktion. Wir wählen zunächst eine beliebige Strecke, die für die ganze Betrachtung die nämliche bleibt, und bezeichnen dieselbe mit 1. Nunmehr tragen wir auf dem einen Schenkel eines rechten Winkels vom

Scheitel 0 aus die Strecke 1 und ferner ebenfalls vom Scheitel 0 aus die Strecke b ab ; sodann tragen wir auf dem anderen Schenkel die Strecke a ab. Wir verbinden die Endpunkte der Strecken 1 und a durch eine Gerade und ziehen zu dieser Geraden durch den Endpunkt der Strecke b eine Parallele ; dieselbe möge auf dem anderen Schenkel eine Strecke c abschneiden: dann nennen wir diese Strecke c das Produkt der Strecke a in die Strecke b und bezeichnen sie mit

$$c = ab.$$

Wir wollen vor Allem beweisen, dass für die eben definirte Multiplikation der Strecken das commutative Gesetz

$$ab = ba$$

gültig ist. Zu dem Zwecke construiren wir zuerst auf die oben festgesetzte Weise die Strecke ab. Ferner tragen wir auf dem ersten Schenkel des rechten Winkels die Strecke a und auf dem anderen Schenkel die Strecke b ab, verbinden den Endpunkt der Strecke 1 mit dem Endpunkt von b auf dem anderen Schenkel durch

eine Gerade und ziehen zu dieser Geraden durch den Endpunkt von a auf dem ersten Schenkel eine Parallele: dieselbe schneidet auf dem anderen Schenkel die Strecke ba ab; in der That fällt diese Strecke ba, wie die Figur 22 zeigt, wegen der Parallelität der punktirten Hülfslinien nach dem Pascalschen Satze (Satz 21) mit der vorhin construirten Strecke ab zusammen.

Um für unsere Multiplikation der Strecken das associative Gesetz

$$
a(bc) = (ab)c
$$

zu beweisen, construiren wir erst die Strecke $d = bc$, dann $da$, ferner die Strecke $e = ba$ und dann $ec$. Dass die Endpunkte von $da$ und $ec$ zusammenfallen, ist wiederum auf Grund des Pascalschen Satzes aus der Figur 23 unmittelbar ersichtlich und mit Benutzung des bereits bewiesenen commutativen Gesetzes folgt hieraus die obige Formel für das associative Gesetz der Streckenmultiplikation.

Endlich gilt in unserer Streckenrechnung auch das distributive Gesetz

$$
a(b + c) = ab + ac.
$$

Um dasselbe zu beweisen, construiren wir die Strecken $ab$, $ac$ und $a(b + c)$ und ziehen dann durch den Endpunkt der Strecke $c$ (s. Figur 24) eine Parallele zu dem anderen Schenkel des rechten Winkels. Die Congruenz der beiden rechtwinkligen in der Figur 24 schraffirten Dreiecke und die Anwendung des Satzes von der Gleichheit der Gegenseiten im Parallelogramm liefert dann den gewünschten Nachweis.

Sind $b$ und $c$ zwei beliebige Strecken, so giebt es stets eine Strecke $a$, sodass $c = ab$ wird; diese Strecke $a$ wird mit $\frac{c}{b}$ bezeichnet und der *Quotient* von $c$ durch $b$ genannt.

.. picture:: /_static/figures/fig_segment_multiplication.svg
   :alt: Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.
   :caption: **Hilbert's Segment Multiplication c = ab and Commutativity ab = ba (§ 15).** Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.


.. picture:: /_static/figures/fig_segment_distributive.svg
   :alt: Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.
   :caption: **Geometric Proof of the Distributive Law a(b + c) = ab + ac (§ 15).** Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.


.. _grundlagen-de-s16:

.. folio:: § 16
   :page: 35

§ 16. Die Proportionen und die Aehnlichkeitssätze
-------------------------------------------------

Mit Hülfe der eben dargelegten Streckenrechnung lässt sich Euklids Lehre von den Proportionen einwandsfrei und ohne Archimedisches Axiom in folgender Weise begründen.

**Erklärung.** Sind $a, b, a', b'$ irgend vier Strecken, so soll die *Proportion*

$$
a : b = a' : b'
$$

nichts anderes bedeuten als die Streckengleichung

$$
ab' = ba'.
$$

**Definition.** Zwei Dreiecke heissen *ähnlich*, wenn entsprechende Winkel in ihnen congruent sind.

.. _grundlagen-de-thm-22:

**Satz 22.** Wenn $a, b$ und $a', b'$ entsprechende Seiten in zwei ähnlichen Dreiecken sind, so gilt die Proportion

$$
a : b = a' : b'.
$$

**Beweis.** Wir betrachten zunächst den besonderen Fall, wo die von $a, b$ und $a', b'$ eingeschlossenen Winkel in beiden Dreiecken Rechte sind, und denken uns die beiden Dreiecke in ein und denselben rechten Winkel eingetragen. Wir tragen sodann vom Scheitel aus auf einem Schenkel die Strecke $1$ ab und ziehen durch den Endpunkt dieser Strecke $1$ die Parallele zu den beiden Hypotenusen; dieselbe schneide auf dem anderen Schenkel die Strecke $e$ ab; dann ist nach unserer Definition des Streckenproduktes

$$
b = ea, \quad b' = ea';
$$

mithin haben wir

$$
ab' = ba',
$$

d. h.

$$
a : b = a' : b'.
$$

Nunmehr kehren wir zu dem allgemeinen Falle zurück. Wir construiren in jedem der beiden ähnlichen Dreiecke den Schnittpunkt $S$ bez. $S'$ der drei Winkelhalbirenden und fällen von diesem die drei Lote $r$ bez. $r'$ auf die Dreiecksseiten; die auf diesen entstehenden Abschnitte bezeichnen wir mit

$$
a_b, \; a_c, \; b_c, \; b_a, \; c_a, \; c_b
$$

bez.

$$
a'_b, \; a'_c, \; b'_c, \; b'_a, \; c'_a, \; c'_b.
$$

Der vorhin bewiesene spezielle Fall unseres Satzes liefert dann die Proportionen

$$
\begin{aligned}
a_b : r &= a'_b : r', & b_c : r &= b'_c : r', \\
a_c : r &= a'_c : r', & b_a : r &= b'_a : r';
\end{aligned}
$$

aus diesen schliessen wir mittelst des distributiven Gesetzes

$$
a : r = a' : r', \quad b : r = b' : r'
$$

und folglich mit Rücksicht auf das commutative Gesetz der Multiplikation

$$
a : b = a' : b'.
$$

Aus dem eben bewiesenen Satze 22 entnehmen wir leicht den Fundamentalsatz in der Lehre von den Proportionen, der wie folgt lautet:

.. _grundlagen-de-thm-23:

**Satz 23.** Schneiden zwei Parallele auf den Schenkeln eines beliebigen Winkels die Strecken $a, b$ bez. $a', b'$ ab, so gilt die Proportion

$$
a : b = a' : b'.
$$

Umgekehrt, wenn vier Strecken $a, b, a', b'$ diese Proportion erfüllen und $a, a'$ und $b, b'$ je auf einem Schenkel eines beliebigen Winkels abgetragen werden, so sind die Verbindungsgeraden der Endpunkte von $a, b$ bez. von $a', b'$ einander parallel.

.. _grundlagen-de-s17:

.. folio:: § 17
   :page: 37

§ 17. Die Gleichungen der Geraden und Ebenen
--------------------------------------------

Zu dem bisherigen System von Strecken fügen wir noch ein zweites ebensolches System von Strecken hinzu; die Strecken des neuen Systems denken wir uns durch ein Merkzeichen kenntlich gemacht und nennen sie dann „negative“ Strecken zum Unterschiede von den bisher betrachteten „positiven“ Strecken. Führen wir noch die durch einen einzigen Punkt bestimmte Strecke 0 ein, so gelten bei gehörigen Festsetzungen in dieser erweiterten Streckenrechnung sämtliche Rechnungsregeln für reelle Zahlen, die in § 13 zusammengestellt worden sind. Wir heben folgende specielle Thatsachen hervor:

* Es ist stets $a \cdot 1 = 1 \cdot a = a$.
* Wenn $ab = 0$, so ist entweder $a = 0$ oder $b = 0$.
* Wenn $a > b$ und $c > 0$, so folgt stets $ac > bc$.

Wir nehmen nun in einer Ebene $\alpha$ durch einen Punkt $O$ zwei zu einander senkrechte Gerade als festes rechtwinkliges Axenkreuz an und tragen dann die beliebigen Strecken $x, y$ von $O$ aus auf den beiden Geraden ab, und zwar nach der einen oder nach der anderen Seite hin, jenachdem die abzutragende Strecke $x$ bez. $y$ positiv oder negativ ist; sodann errichten wir die Lote in den Endpunkten der Strecken $x, y$ und bestimmen den Schnittpunkt $P$ dieser Lote: die Strecken $x, y$ heissen die *Coordinaten* des Punktes $P$; jeder Punkt der Ebene $\alpha$ ist durch seine Coordinaten $x, y$, die positive oder negative Strecken oder $0$ sein können, eindeutig bestimmt.

Es sei $l$ irgend eine Gerade in der Ebene $\alpha$, die durch $O$ und durch einen Punkt $C$ mit den Coordinaten $a, b$ gehe. Sind dann $x, y$ die Coordinaten irgend eines Punktes von $l$, so finden wir leicht aus Satz 22

$$
a : b = x : y \quad \text{oder} \quad bx - ay = 0
$$

als die Gleichung der Geraden $l$. Ist $l'$ eine zu $l$ parallele Gerade, die auf der $x$-Axe die Strecke $c$ abschneidet, so gelangen wir zu der Gleichung der Geraden $l'$, indem wir in der Gleichung der Geraden $l$ die Strecke $x$ durch die Strecke $x - c$ ersetzen; die gewünschte Gleichung lautet also

$$
bx - ay - bc = 0.
$$

Aus diesen Entwickelungen schliessen wir leicht auf eine Weise, die von dem Archimedischen Axiom unabhängig ist, dass jede Gerade in einer Ebene durch eine lineare Gleichung in den Coordinaten x, y dargestellt wird und umgekehrt jede solche lineare Gleichung eine Gerade darstellt, wenn die Coefficienten

derselben in der betreffenden Geometrie vorkommende Strecken sind.

Die entsprechenden Resultate beweist man ebenso leicht in der räumlichen Geometrie.

Der weitere Aufbau der Geometrie kann von nun an nach den Methoden geschehen, die man in der analytischen Geometrie gemeinhin anwendet.

Wir haben bisher in diesem Kapitel III das Archimedische Axiom nirgends benutzt ; setzen wir jetzt die Gültigkeit desselben voraus, so können wir den Punkten einer beliebigen Geraden im Raume reelle Zahlen zuordnen und zwar auf folgende Art.

Wir wählen auf der Geraden zwei beliebige Punkte aus und ordnen diesen die Zahlen $0$ und $1$ zu; sodann halbiren wir die durch sie bestimmte Strecke $01$ und bezeichnen den entstehenden Mittelpunkt mit $\frac{1}{2}$, ferner den Mittelpunkt der Strecke $0\frac{1}{2}$ mit $\frac{1}{4}$ u. s. w.; nach $n$-maliger Ausführung dieses Verfahrens gelangen wir zu einem Punkte, dem die Zahl $\frac{1}{2^n}$ zuzuordnen ist. Nun tragen wir die Strecke $0\frac{1}{2^n}$ an den Punkt $0$ sowohl nach der Seite des Punktes $1$ als auch nach der anderen Seite hin etwa $m$-mal hintereinander ab und erteilen den so entstehenden Punkten die Zahlenwerte $\frac{m}{2^n}$ bez. $-\frac{m}{2^n}$. Aus dem Archimedischen Axiom kann leicht geschlossen werden, dass auf Grund dieser Zuordnung sich jedem beliebigen Punkte der Geraden in eindeutig bestimmter Weise eine reelle Zahl zuordnen lässt und zwar so dass dieser Zuordnung folgende Eigenschaft zukommt: wenn $A, B, C$ irgend drei Punkte der Geraden und bez. $\alpha, \beta, \gamma$ die zugehörigen reellen Zahlen sind und $B$ zwischen $A$ und $C$ liegt, so erfüllen dieselben stets entweder die Ungleichung $\alpha < \beta < \gamma$ oder $\alpha > \beta > \gamma$.

Aus den Entwicklungen in Kap. II § 9 leuchtet ein, dass dort für jede Zahl, die dem algebraischen Zahlkörper $\Omega$ angehört, notwendig ein Punkt der Geraden existiren muss, dem sie zugeordnet ist. Ob auch jeder anderen reellen Zahl ein Punkt entspricht, lässt sich im allgemeinen nicht entscheiden, sondern hängt von der vorgelegten Geometrie ab.

Dagegen ist es stets möglich, das ursprüngliche System von Punkten, Geraden und Ebenen so durch „ideale“ oder „irrationale“ Elemente zu erweitern, dass auf irgend einer Geraden der entstehenden Geometrie jedem System von drei reellen Zahlen ohne Ausnahme ein Punkt zugeordnet ist. Durch gehörige Festsetzung kann zugleich erreicht werden, dass in der erweiterten Geometrie sämtliche Axiome I — V gültig sind. Diese (durch Hinzufügung der irrationalen Elemente) erweiterte Geometrie ist keine andere als die gewöhnliche analytische Geometrie des Raumes.


----

.. rubric:: Fussnoten

.. [#fn1] F. Schur hat einen interessanten Beweis des Pascalschen Satzes auf Grund der sämtlichen Axiome I–II, IV in den *Math. Ann.* Bd. 51 veröffentlicht.
