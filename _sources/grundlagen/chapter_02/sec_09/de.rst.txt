:layout: book
:canonical_id: § 9
:breadcrumb_title: § 9
:order: 9
:folio: § 9
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s9:

.. folio:: § 9
   :page: 19

§ 9: Die Widerspruchslosigkeit der Axiome
=========================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Die Axiome der fünf in Kapitel I aufgestellten Axiomgruppen stehen mit einander nicht in Widerspruch, d. h. es ist nicht möglich, durch logische Schlüsse aus denselben eine Thatsache abzuleiten, welche einem der aufgestellten Axiome widerspricht. Um

dies einzusehen , genügt es , eine Geometrie anzugeben , in der sämtliche Axiome der fünf Gruppen erfüllt sind.

Man betrachte den Bereich :math:`\Omega` aller derjenigen algebraischen Zahlen, welche hervorgehen, indem man von der Zahl :math:`1` ausgeht und eine endliche Anzahl von Malen die vier Rechnungsoperationen: Addition, Subtraktion, Multiplikation, Division und die fünfte Operation :math:`\sqrt{1 + \omega^2}` anwendet, wobei :math:`\omega` jedesmal eine Zahl bedeuten kann, die vermöge jener fünf Operationen bereits entstanden ist.

Wir denken uns ein Paar von Zahlen :math:`(x, y)` des Bereiches :math:`\Omega` als einen Punkt und die Verhältnisse von irgend drei Zahlen :math:`(u : v : w)` aus :math:`\Omega`, falls :math:`u, v` nicht beide Null sind, als eine Gerade; ferner möge das Bestehen der Gleichung

.. math::

   ux + vy + w = 0

ausdrücken, dass der Punkt :math:`(x, y)` auf der Geraden :math:`(u : v : w)` liegt; damit sind, wie man leicht sieht, die Axiome I 1–2 und III erfüllt. Die Zahlen des Bereiches :math:`\Omega` sind sämtlich reell; indem wir berücksichtigen, dass dieselben sich ihrer Grösse nach anordnen lassen, können wir leicht solche Festsetzungen für unsere Punkte und Geraden treffen, dass auch die Axiome II der Anordnung sämtlich gültig sind. In der That, sind :math:`(x_1, y_1), (x_2, y_2), (x_3, y_3), \dots` irgend welche Punkte auf einer Geraden, so möge dies ihre Reihenfolge auf der Geraden sein, wenn die Zahlen :math:`x_1, x_2, x_3, \dots` oder :math:`y_1, y_2, y_3, \dots` in dieser Reihenfolge entweder beständig abnehmen oder wachsen; um ferner die Forderung des Axioms II 5 zu erfüllen, haben wir nur nöthig festzusetzen, dass alle Punkte :math:`(x, y)`, für die :math:`ux + vy + w` kleiner oder grösser als :math:`0` ausfällt, auf der einen bez. auf der anderen Seite der Geraden :math:`(u : v : w)` gelegen sein sollen. Man überzeugt sich leicht, dass diese Festsetzung sich mit der vorigen Festsetzung in Uebereinstimmung befindet, derzufolge ja die Reihenfolge der Punkte auf einer Geraden bereits bestimmt ist.

Das Abtragen von Strecken und Winkeln erfolgt nach den bekannten Methoden der analytischen Geometrie. Eine Transformation von der Gestalt

.. math::

   \begin{aligned}
   x' &= x + a, \\
   y' &= y + b
   \end{aligned}

vermittelt die Parallelverschiebung von Strecken und Winkeln. Wird ferner der Punkt :math:`(0, 0)` mit :math:`O`, der Punkt :math:`(1, 0)` mit :math:`E` und ein beliebiger Punkt :math:`(a, b)` mit :math:`C` bezeichnet, so entsteht durch Drehung um den Winkel :math:`\angle COE`, wenn :math:`O` der feste Drehpunkt ist, aus dem beliebigen Punkte :math:`(x, y)` der Punkt :math:`(x', y')`, wobei

.. math::

   \begin{aligned}
   x' &= \frac{a}{\sqrt{a^2 + b^2}} x - \frac{b}{\sqrt{a^2 + b^2}} y, \\
   y' &= \frac{b}{\sqrt{a^2 + b^2}} x + \frac{a}{\sqrt{a^2 + b^2}} y
   \end{aligned}

zu setzen ist. Da die Zahl

.. math::

   \sqrt{a^2 + b^2} = a\sqrt{1 + \left(\frac{b}{a}\right)^2}

wiederum dem Bereiche :math:`\Omega` angehört, so gelten bei unseren Festsetzungen auch die Congruenzaxiome IV und offenbar ist auch das Archimedische Axiom V erfüllt.

Wir schliessen hieraus, dass jeder Widerspruch in den Folgerungen aus unseren Axiomen auch in der Arithmetik des Bereiches :math:`\Omega` erkennbar sein müsste.

Die entsprechende Betrachtungsweise für die räumliche Geometrie bietet keine Schwierigkeit.

Wählen wir in der obigen Entwickelung statt des Bereiches :math:`\Omega` den Bereich aller reellen Zahlen, so erhalten wir ebenfalls eine Geometrie, in der sämtliche Axiome I–V gültig sind. Für unseren Beweis genügte die Zuhülfenahme des Bereiches :math:`\Omega`, der nur eine abzählbare Menge von Elementen enthält.
