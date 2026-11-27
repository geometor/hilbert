:layout: book
:canonical_id: § 15
:breadcrumb_title: § 15
:order: 15
:folio: § 15
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s15:

.. folio:: § 15
   :page: 32

§ 15: Die Streckenrechnung auf Grund des Pascalschen Satzes
===========================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Der im vorigen Paragraph bewiesene Pascalsche Satz setzt uns in den Stand, in die Geometrie eine Rechnung mit Strecken einzuführen, in der die Rechnungsregeln für reelle Zahlen sämtlich unverändert gültig sind.

Statt des Wortes „congruent“ und des Zeichens :math:`\equiv` bedienen wir uns in der Streckenrechnung des Wortes „gleich“ und des Zeichens :math:`=`.

Wenn :math:`A, B, C` drei Punkte einer Geraden sind und :math:`B` zwischen :math:`A` und :math:`C` liegt, so bezeichnen wir :math:`c = AC` als die *Summe* der beiden Strecken :math:`a = AB` und :math:`b = BC` und setzen

.. math::

   c = a + b.

Die Strecken :math:`a` und :math:`b` heissen *kleiner* als :math:`c`, in Zeichen:

.. math::

   a < c, \quad b < c,

und :math:`c` heisst *grösser* als :math:`a` und :math:`b`, in Zeichen:

.. math::

   c > a, \quad c > b.

Aus den linearen Congruenzaxiomen IV 1–3 entnehmen wir leicht, dass für die eben definirte Addition der Strecken das associative Gesetz

.. math::

   a + (b + c) = (a + b) + c

sowie das commutative Gesetz

.. math::

   a + b = b + a

gültig ist.

Um das Produkt einer Strecke a in eine Strecke b geometrisch zu definiren, bedienen wir uns folgender Construktion. Wir wählen zunächst eine beliebige Strecke, die für die ganze Betrachtung die nämliche bleibt, und bezeichnen dieselbe mit 1. Nunmehr tragen wir auf dem einen Schenkel eines rechten Winkels vom

Scheitel 0 aus die Strecke 1 und ferner ebenfalls vom Scheitel 0 aus die Strecke b ab ; sodann tragen wir auf dem anderen Schenkel die Strecke a ab. Wir verbinden die Endpunkte der Strecken 1 und a durch eine Gerade und ziehen zu dieser Geraden durch den Endpunkt der Strecke b eine Parallele ; dieselbe möge auf dem anderen Schenkel eine Strecke c abschneiden: dann nennen wir diese Strecke c das Produkt der Strecke a in die Strecke b und bezeichnen sie mit

.. math::

   c = ab.

Wir wollen vor Allem beweisen, dass für die eben definirte Multiplikation der Strecken das commutative Gesetz

.. math::

   ab = ba

gültig ist. Zu dem Zwecke construiren wir zuerst auf die oben festgesetzte Weise die Strecke ab. Ferner tragen wir auf dem ersten Schenkel des rechten Winkels die Strecke a und auf dem anderen Schenkel die Strecke b ab, verbinden den Endpunkt der Strecke 1 mit dem Endpunkt von b auf dem anderen Schenkel durch

eine Gerade und ziehen zu dieser Geraden durch den Endpunkt von a auf dem ersten Schenkel eine Parallele: dieselbe schneidet auf dem anderen Schenkel die Strecke ba ab; in der That fällt diese Strecke ba, wie die Figur 22 zeigt, wegen der Parallelität der punktirten Hülfslinien nach dem Pascalschen Satze (Satz 21) mit der vorhin construirten Strecke ab zusammen.

Um für unsere Multiplikation der Strecken das associative Gesetz

.. math::

   a(bc) = (ab)c

zu beweisen, construiren wir erst die Strecke :math:`d = bc`, dann :math:`da`, ferner die Strecke :math:`e = ba` und dann :math:`ec`. Dass die Endpunkte von :math:`da` und :math:`ec` zusammenfallen, ist wiederum auf Grund des Pascalschen Satzes aus der Figur 23 unmittelbar ersichtlich und mit Benutzung des bereits bewiesenen commutativen Gesetzes folgt hieraus die obige Formel für das associative Gesetz der Streckenmultiplikation.

Endlich gilt in unserer Streckenrechnung auch das distributive Gesetz

.. math::

   a(b + c) = ab + ac.

Um dasselbe zu beweisen, construiren wir die Strecken :math:`ab`, :math:`ac` und :math:`a(b + c)` und ziehen dann durch den Endpunkt der Strecke :math:`c` (s. Figur 24) eine Parallele zu dem anderen Schenkel des rechten Winkels. Die Congruenz der beiden rechtwinkligen in der Figur 24 schraffirten Dreiecke und die Anwendung des Satzes von der Gleichheit der Gegenseiten im Parallelogramm liefert dann den gewünschten Nachweis.

Sind :math:`b` und :math:`c` zwei beliebige Strecken, so giebt es stets eine Strecke :math:`a`, sodass :math:`c = ab` wird; diese Strecke :math:`a` wird mit :math:`\frac{c}{b}` bezeichnet und der *Quotient* von :math:`c` durch :math:`b` genannt.

.. picture:: /_static/figures/fig_segment_multiplication.svg
   :alt: Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.
   :caption: **Hilbert's Segment Multiplication c = ab and Commutativity ab = ba (§ 15).** Geometric product c = ab on orthogonal rays and proof of ab = ba via Pappus/Pascal parallels.

.. picture:: /_static/figures/fig_segment_distributive.svg
   :alt: Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.
   :caption: **Geometric Proof of the Distributive Law a(b + c) = ab + ac (§ 15).** Distributivity a(b + c) = ab + ac established via congruent right triangles and parallelogram translation.
