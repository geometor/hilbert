:layout: book
:canonical_id: § 27
:breadcrumb_title: § 27
:order: 27
:folio: § 27
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s27:

.. folio:: § 27
   :page: 63

§ 27: Die Gleichung der Geraden auf Grund der neuen Streckenrechnung
====================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Wir haben in § 24 bis § 26 mittelst der in § 24 angeführten Axiome und unter Voraussetzung der Gültigkeit des Desarguesschen Satzes in der Ebene eine Streckenrechnung eingeführt , in welcher das commutative Gesetz der Addition, die associativen Gesetze der Addition und Multiplikation, sowie die beiden distributiven Gesetze gültig sind. Wir wollen in diesem Paragraphen

zeigen, in welcher Weise auf Grund dieser Streckenrechnung eine analytische Darstellung der Punkte und Geraden in der Ebene möglich ist.

**Definition.** Wir bezeichnen in der Ebene die beiden angenommenen festen Geraden durch den Punkt 0 als die X- und Y- Axe und denken uns irgend einen Punkt P der Ebene durch die Strecken x, y bestimmt, die man auf der X- bez. Y-Axe erhält, wenn man durch P zu diesen Axen Parallelen zieht. Diese Strecken x, y heissen Coordinaten des Punktes P. Auf Grund der neuen Streckenrechnung und mit Hülfe des Desarguesschen Satzes gelangen wir zu der folgenden Thatsache :

.. _grundlagen-de-thm-34:

**Satz 34.** Die Coordinaten x, y der Punkte auf einer beliebigen Geraden erfüllen stets eine Streckengleichung von der Gestalt:

.. math::

   ax + by + c = 0;

in dieser Gleichung stehen die Strecken :math:`a, b` notwendig linksseitig von den Coordinaten :math:`x, y`; die Strecken :math:`a, b` sind niemals beide Null und :math:`c` ist eine beliebige Strecke.

Umgekehrt: jede Streckengleichung der beschriebenen Art stellt stets eine Gerade in der zu Grunde gelegten ebenen Geometrie dar.

**Beweis.** Wir nehmen zunächst an, die Gerade :math:`l` gehe durch :math:`O`. Ferner sei :math:`C` ein bestimmter von :math:`O` verschiedener Punkt auf :math:`l` und :math:`P` ein beliebiger Punkt auf :math:`l`; :math:`C` habe die Coordinaten :math:`OA, OB` und :math:`P` habe die Coordinaten :math:`x, y`; wir bezeichnen die Verbindungsgerade der Endpunkte von :math:`x, y` mit :math:`g`. Endlich ziehen wir durch den Endpunkt der Strecke :math:`1` auf der :math:`X`-Axe eine Parallele :math:`h` zu :math:`AB`: diese Parallele schneide auf der :math:`Y`-Axe die Strecke :math:`e` ab. Aus der zweiten Aussage des Desarguesschen Satzes folgt leicht, dass die Gerade :math:`g` stets parallel zu :math:`AB` läuft. Da somit auch :math:`g` stets zu :math:`h` parallel ist, so folgt für die Coordinaten :math:`x, y` des beliebigen Punktes :math:`P` auf :math:`l` die Streckengleichung

.. math::

   ex = y.

Nunmehr sei :math:`l'` eine beliebige Gerade in unserer Ebene; dieselbe schneide auf der :math:`X`-Axe die Strecke :math:`c = OO'` ab. Wir ziehen ferner die Gerade :math:`l` durch :math:`O` parallel zu :math:`l'`. Es sei :math:`P'` ein beliebiger Punkt auf :math:`l'`; die Parallele durch :math:`P'` zur :math:`X`-Axe treffe die Gerade :math:`l` in :math:`P` und schneide auf der :math:`Y`-Axe die Strecke :math:`y = OB` ab; ferner mögen die Parallelen durch :math:`P` und :math:`P'` zur :math:`Y`-Axe auf der :math:`X`-Axe die Strecken :math:`x = OA` und :math:`x' = OA'` abschneiden.

Wir wollen nun beweisen, dass die Streckengleichung

.. math::

   x' = x + c

besteht. Zu diesem Zwecke ziehen wir :math:`O'C` parallel zur Einheitsgeraden, ferner :math:`CD` parallel zur :math:`X`-Axe und :math:`AD` parallel zur :math:`Y`-Axe; dann läuft unsere Behauptung darauf hinaus, dass

.. math::

   A'D \; \text{parallel} \; O'C

sein muss. Wir construiren noch :math:`D'` als Schnittpunkt der Geraden :math:`CD` und :math:`A'P'` und ziehen :math:`O'C'` parallel zur :math:`Y`-Axe.

Da in den Dreiecken :math:`OCP` und :math:`O'C'P'` die Verbindungsgeraden entsprechender Ecken parallel laufen, so folgt mittelst der zweiten Aussage des Desarguesschen Satzes, dass

.. math::

   CP \; \text{parallel} \; C'P'

sein muss; auf gleiche Weise lehrt die Betrachtung der Dreiecke :math:`ACP` und :math:`A'C'P'`, dass

.. math::

   AC \; \text{parallel} \; A'C'

ist. Da somit in den Dreiecken :math:`ACD` und :math:`C'A'O'` die entsprechenden Seiten einander parallel laufen, so treffen sich die Geraden :math:`AC', C'A, DO'` in einem Punkte und die Betrachtung der beiden Dreiecke :math:`C'A'D` und :math:`ACO'` zeigt dann, dass :math:`A'D` und :math:`CO'` einander parallel sind.

Aus den beiden bisher gefundenen Streckengleichungen

.. math::

   ex = y \quad \text{und} \quad x' = x + c

folgt sofort die weitere Gleichung

.. math::

   ex' = y + ec.

Bezeichnen wir schliesslich mit :math:`n` die Strecke, die zur Strecke :math:`1` addirt die Strecke :math:`0` liefert, so folgt, wie man leicht beweist, aus der letzten Gleichung

.. math::

   ex' + ny + nec = 0

und diese Gleichung ist von der Gestalt, wie der Satz 34 behauptet.

Die zweite Aussage des Satzes 34 erkennen wir nun ohne Mühe als richtig; denn eine jede vorgelegte Streckengleichung

.. math::

   ax + by + c = 0

lässt sich offenbar durch linksseitige Multiplikation mit einer geeigneten Strecke in die vorhin gefundene Gestalt

.. math::

   ex + ny + nec = 0

bringen.

Es sei noch ausdrücklich bemerkt, dass bei unseren Annahmen eine Streckengleichung von der Gestalt

.. math::

   xa + yb + c = 0,

in der die Strecken :math:`a, b` rechtsseitig von den Coordinaten :math:`x, y` stehen, im Allgemeinen nicht eine Gerade darstellt.

Wir werden in § 30 eine wichtige Anwendung von dem Satze 34 machen.
