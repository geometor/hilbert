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

**Satz 21** [#fn1]_ **(Pascalscher Satz).** Es seien :math:`A, B, C` bez. :math:`A', B', C'` je drei Punkte auf zwei sich schneidenden Geraden, die vom Schnittpunkte der Geraden verschieden sind; ist dann :math:`CB'` parallel :math:`BC'` und :math:`CA'` parallel :math:`AC'`, so ist auch :math:`BA'` parallel :math:`AB'`.

Um den Beweis für diesen Satz zu erbringen, führen wir zunächst folgende Bezeichnungsweise ein. In einem rechtwinkligen Dreiecke ist offenbar die Kathete :math:`a` durch die Hypotenuse :math:`c` und den von :math:`a` und :math:`c` eingeschlossenen Basiswinkel :math:`\alpha` eindeutig bestimmt: wir setzen kurz

.. math::

   a = \alpha c,

sodass das Symbol :math:`\alpha c` stets eine bestimmte Strecke bedeutet, sobald :math:`c` eine beliebig gegebene Strecke und :math:`\alpha` ein beliebig gegebener spitzer Winkel ist.

Nunmehr möge :math:`c` eine beliebige Strecke und :math:`\alpha, \beta` mögen zwei beliebige spitze Winkel bedeuten; wir behaupten, dass allemal die Streckencongruenz

.. math::

   \alpha\beta c \equiv \beta\alpha c

besteht und somit die Symbole :math:`\alpha, \beta` stets mit einander vertauschbar sind.

Um diese Behauptung zu beweisen, nehmen wir die Strecke :math:`c = AB` und tragen an diese Strecke in :math:`A` zu beiden Seiten die Winkel :math:`\alpha` und :math:`\beta` an. Dann fällen wir von :math:`B` aus auf die anderen Schenkel dieser Winkel die Lote :math:`BC` und :math:`BD`, verbinden :math:`C` mit :math:`D` und fällen schliesslich von :math:`A` aus das Lot :math:`AE` auf :math:`CD`.

Da die Winkel :math:`\angle ACB` und :math:`\angle ADB` Rechte sind, so liegen die vier Punkte :math:`A, B, C, D` auf einem Kreise und demnach sind die beiden Winkel :math:`\angle ACD` und :math:`\angle ABD` als Peripheriewinkel auf derselben Sehne :math:`AD` einander congruent. Nun ist einerseits :math:`\angle ACD` zusammen mit dem :math:`\angle CAE` und andererseits :math:`\angle ABD` zusammen mit :math:`\angle BAD` je ein Rechter und folglich sind auch die Winkel :math:`\angle CAE` und :math:`\angle BAD` einander congruent, d. h. es ist

.. math::

   \angle CAE \equiv \beta,

und daher

.. math::

   \angle DAE \equiv \alpha.

Wir gewinnen nun unmittelbar die Streckencongruenzen

.. math::

   \begin{aligned}
   \beta c &\equiv AD, & \alpha c &\equiv AC, \\
   \alpha\beta c &\equiv \alpha(AD) \equiv AE, & \beta\alpha c &\equiv \beta(AC) \equiv AE,
   \end{aligned}

und hieraus folgt die Richtigkeit der vorhin behaupteten Congruenz.

Wir kehren nun zur Figur des Pascalschen Satzes zurück und bezeichnen den Schnittpunkt der beiden Geraden mit :math:`O` und die Strecken :math:`OA, OB, OC, OA', OB', OC', CB', BC', CA', AC', BA', AB'` bez. mit :math:`a, b, c, a', b', c', l, l^*, m, m^*, n, n^*`. Sodann fällen wir von :math:`O` Lote auf :math:`l, m, n`; das Lot auf :math:`l` schliesse mit den beiden Geraden :math:`OA, OA'` die spitzen Winkel :math:`\lambda', \lambda` ein und die Lote auf :math:`m` bez. :math:`n` mögen mit den Geraden :math:`OA` und :math:`OA'` die spitzen Winkel :math:`\mu', \mu` bez. :math:`\nu', \nu` bilden. Drücken wir nun diese drei Lote in der vorhin angegebenen Weise mit Hülfe der Hypotenusen und Basiswinkel in den betreffenden rechtwinkligen Dreiecken auf doppelte Weise aus, so erhalten wir folgende drei Streckencongruenzen

.. math::

   \begin{aligned}
   (1)\quad \lambda b' &\equiv \lambda' c, \\
   (2)\quad \mu a' &\equiv \mu' c, \\
   (3)\quad \nu a' &\equiv \nu' b.
   \end{aligned}

Da nach Voraussetzung :math:`l` parallel :math:`l^*` und :math:`m` parallel :math:`m^*` sein soll, so stimmen die von :math:`O` auf :math:`l^*` bez. :math:`m^*` zu fällenden Lote mit den Loten auf :math:`l` bez. :math:`m` überein und wir erhalten somit

.. math::

   \begin{aligned}
   (4)\quad \lambda c' &\equiv \lambda' b, \\
   (5)\quad \mu c' &\equiv \mu' a.
   \end{aligned}

Wenn wir auf die Congruenz (3) links und rechts das Symbol :math:`\lambda'\mu` anwenden und bedenken, dass nach dem vorhin Bewiesenen die in Rede stehenden Symbole mit einander vertauschbar sind, so finden wir

.. math::

   \nu\lambda'\mu a' \equiv \nu'\mu\lambda' b.

In dieser Congruenz berücksichtigen wir links die Congruenz (2) und rechts (4); dann wird

.. math::

   \nu\lambda'\mu' c \equiv \nu'\mu\lambda c'

oder

.. math::

   \nu\mu'\lambda' c \equiv \nu'\lambda\mu c'.

Hierin berücksichtigen wir links die Congruenz (1) und rechts (5); dann wird

.. math::

   \nu\mu'\lambda b' \equiv \nu'\lambda\mu' a

oder

.. math::

   \lambda\mu'\nu b' \equiv \lambda\mu'\nu' a.

Wegen der Bedeutung unserer Symbole schliessen wir aus der letzten Congruenz sofort

.. math::

   \mu'\nu b' \equiv \mu'\nu' a

und hieraus

.. math::

   (6)\quad \nu b' \equiv \nu' a.

Fassen wir nun das von :math:`O` auf :math:`n` gefällte Lot in's Auge und fällen auf dasselbe Lote von :math:`A` und :math:`B'` aus, so zeigt die Congruenz (6), dass die Fusspunkte der letzteren beiden Lote zusammenfallen, d. h. die Gerade :math:`n^* = AB'` steht zu dem Lote auf :math:`n` senkrecht und ist mithin zu :math:`n` parallel. Damit ist der Beweis für den Pascalschen Satz erbracht.

Wenn irgend eine Gerade, ein Punkt ausserhalb derselben und irgend ein Winkel gegeben ist, so kann man offenbar durch Abtragen dieses Winkels und Ziehen einer Parallelen eine Gerade finden, die durch den gegebenen Punkt geht und die gegebene Gerade unter dem gegebenen Winkel schneidet. Im Hinblick auf diesen Umstand dürfen wir uns zum Beweise des Pascalschen Satzes auch des folgenden einfachen Schlussverfahrens bedienen, das ich einer Mittheilung von anderer Seite verdanke.

Man ziehe durch :math:`B` eine Gerade, die :math:`OA'` im Punkte :math:`D'` unter dem Winkel :math:`OCA'` trifft, so dass die Congruenz

.. math::

   (1^*)\quad \angle OCA' \equiv \angle OD'B

gilt; dann ist nach einem bekannten Satze aus der Lehre vom Kreise :math:`CBD'A'` ein Kreisviereck und mithin gilt nach dem Satze von der Congruenz der Peripheriewinkel auf der nämlichen Sehne die Congruenz

.. math::

   (2^*)\quad \angle OBA' \equiv \angle OD'C.

Da :math:`CA'` und :math:`AC'` nach Voraussetzung einander parallel sind, so ist

.. math::

   (3^*)\quad \angle OCA' \equiv \angle OAC';

aus :math:`(1^*)` und :math:`(3^*)` folgern wir die Congruenz

.. math::

   \angle OD'B \equiv \angle OAC';

dann aber ist auch :math:`BAD'C'` ein Kreisviereck und mithin gilt nach dem Satze von den Winkeln im Kreisviereck die Congruenz

.. math::

   (4^*)\quad \angle OAD' \equiv \angle OC'B.

Da ferner nach Voraussetzung :math:`CB'` parallel :math:`BC'` ist, so haben wir auch

.. math::

   (5^*)\quad \angle OB'C \equiv \angle OC'B;

aus :math:`(4^*)` und :math:`(5^*)` folgern wir die Congruenz

.. math::

   \angle OAD' \equiv \angle OB'C;

diese endlich lehrt, dass :math:`CAD'B'` ein Kreisviereck ist, und mithin gilt auch die Congruenz

.. math::

   (6^*)\quad \angle OAB' \equiv \angle OD'C.

Aus :math:`(2^*)` und :math:`(6^*)` folgt

.. math::

   \angle OBA' \equiv \angle OAB'

und die Congruenz lehrt, dass :math:`BA'` und :math:`AB'` einander parallel sind, wie es der Pascalsche Satz verlangt.

Fällt :math:`D'` mit einem der Punkte :math:`A', B', C'` zusammen, so wird eine Abänderung dieses Schlussverfahrens nothwendig, die leicht ersichtlich ist.

.. picture:: /_static/figures/fig_pascal_orthogonal.svg
   :alt: Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.
   :caption: **Affine Pascal's (Pappus's) Hexagon Theorem (Theorem 21).** Theorem 21 (Pappus's Hexagon Theorem on two intersecting lines): CB' ∥ BC' and CA' ∥ AC' imply BA' ∥ AB' without Archimedes's Axiom.

.. [#fn1] F. Schur hat einen interessanten Beweis des Pascalschen Satzes auf Grund der sämtlichen Axiome I–II, IV in den *Math. Ann.* Bd. 51 veröffentlicht.
