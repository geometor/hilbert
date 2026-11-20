:layout: book
:canonical_id: § 14
:breadcrumb_title: § 14
:order: 14
:folio: § 14
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s14:

.. folio:: § 14
   :page: 28

§ 14: Beweis des Pascalschen Satzes
===================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

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

.. [#fn1] F. Schur hat einen interessanten Beweis des Pascalschen Satzes auf Grund der sämtlichen Axiome I–II, IV in den *Math. Ann.* Bd. 51 veröffentlicht.
