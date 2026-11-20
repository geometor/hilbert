:layout: book
:canonical_id: § 20
:breadcrumb_title: § 20
:order: 20
:folio: § 20
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s20:

.. folio:: § 20
   :page: 43

§ 20: Das Flächenmass von Dreiecken und Polygonen
=================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

**Definition.** Wenn wir in einem Dreieck $ABC$ mit den Seiten $a, b, c$ die beiden Höhen $h_a = AD$, $h_b = BE$ construiren, so folgt aus der Aehnlichkeit der Dreiecke $BCE$ und $ACD$ nach Satz 22 die Proportion

$$
a : h_b = b : h_a, \quad \text{d. h.} \quad ah_a = bh_b;
$$

mithin ist in jedem Dreiecke das Produkt aus einer Grundlinie und der zu ihr gehörigen Höhe davon unabhängig, welche Seite des Dreiecks man als Grundlinie wählt. Das halbe Produkt aus Grundlinie und Höhe eines Dreiecks $\Delta$ heisse das *Flächenmass* des Dreiecks $\Delta$ und werde mit $F(\Delta)$ bezeichnet.

**Erklärung.** Eine Strecke, welche eine Ecke eines Dreiecks mit einem Punkte der gegenüberliegenden Seite verbindet, heisst *Transversale*; dieselbe zerlegt das Dreieck in zwei Dreiecke mit gemeinsamer Höhe, deren Grundlinien in dieselbe Gerade fallen; eine solche Zerlegung heisse eine *transversale Zerlegung* des Dreiecks.

.. _grundlagen-de-thm-29:

**Satz 29.** Wenn ein Dreieck $\Delta$ durch beliebige Gerade irgendwie in eine gewisse endliche Anzahl von Dreiecken $\Delta_k$ zerlegt wird, so ist stets das Flächenmass des Dreiecks $\Delta$ gleich der Summe der Flächenmasse der sämtlichen Dreiecken $\Delta_k$.

**Beweis.** Aus dem distributiven Gesetze in unserer Streckenrechnung folgt unmittelbar, dass das Flächenmass eines beliebigen Dreiecks gleich der Summe der Flächenmasse zweier solcher Dreiecke ist, die durch irgendwelche transversale Zerlegung aus jenem Dreieck hervorgehen. Die wiederholte Anwendung dieser Thatsache zeigt, dass das Flächenmass eines beliebigen Dreiecks auch gleich der Summe der Flächenmasse der sämtlichen Dreiecke ist, die aus dem vorgelegten Dreiecke entstehen, wenn man nach einander beliebig viele transversale Zerlegungen ausführt.

Um nun den entsprechenden Nachweis für die beliebige Zerlegung des Dreiecks $\Delta$ in Dreiecke $\Delta_k$ zu erbringen, ziehen wir von der einen Ecke $A$ des Dreieckes $\Delta$ durch jeden Teilpunkt der Zerlegung, d. h. durch jeden Eckpunkt der Dreiecke $\Delta_k$ eine Transversale; durch diese Transversalen zerfällt das Dreieck $\Delta$ in gewisse Dreiecke $\Delta_t$. Jedes dieser Dreiecke $\Delta_t$ zerfällt durch die Teilstrecken der gegebenen Zerlegung in gewisse Dreiecke und Vierecke. Wenn wir in den Vierecken noch je eine Diagonale construiren, so zerfällt jedes Dreieck $\Delta_t$ in gewisse Dreiecke $\Delta_{ts}$. Wir wollen nun zeigen, dass die Zerlegung in Dreiecke $\Delta_{ts}$ sowohl für die Dreiecke $\Delta_t$ als auch für die Dreiecke $\Delta_k$ nichts anderes als eine Kette von transversalen Zerlegungen bedeutet.

In der That, zunächst ist klar, dass jede Zerlegung eines Dreiecks in Teildreiecke stets durch eine Reihe von transversalen Zerlegungen bewirkt werden kann, wenn bei der Zerlegung im Inneren des Dreiecks keine Teilpunkte liegen und überdies wenigstens eine Seite des Dreiecks von Teilpunkten frei bleibt.

Nun ist für die Dreiecke $\Delta_t$ unsere Behauptung aus dem Umstande ersichtlich, dass für jedes derselben das Innere sowie eine Seite, nämlich die dem Punkte $A$ gegenüberliegende Seite von weiteren Teilpunkten frei ist.

Aber auch für jedes $\Delta_k$ ist die Zerlegung in $\Delta_{ts}$ auf transversale Zerlegungen zurückführbar. Betrachten wir nämlich ein Dreieck $\Delta_k$, so wird es unter den von $A$ ausgehenden Transversalen im Dreieck $\Delta$ eine bestimmte Transversale geben, in welche entweder eine Seite von $\Delta_k$ hineinfällt oder welche selbst das Dreieck $\Delta_k$ in zwei Dreiecke zerlegt. Im ersten Fall bleibt die betreffende Seite des Dreiecks $\Delta_k$ überhaupt frei von weiteren Teilpunkten bei der Zerlegung in Dreiecke $\Delta_{ts}$; im letzteren Falle ist die im Inneren des Dreiecks $\Delta_k$ verlaufende Strecke jener Transversale in den beiden entstehenden Dreiecken eine Seite, die bei der Teilung in Dreiecke $\Delta_{ts}$ von weiteren Teilpunkten gewiss frei bleibt.

Nach der am Anfang dieses Beweises angestellten Betrachtung ist das Flächenmass $F(\Delta)$ des Dreiecks $\Delta$ gleich der Summe aller Flächenmasse $F(\Delta_t)$ der Dreiecke $\Delta_t$, und diese Summe ist gleich der Summe aller Flächenmasse $F(\Delta_{ts})$. Andererseits ist auch die Summe über die Flächenmasse $F(\Delta_k)$ aller Dreiecke $\Delta_k$ gleich der Summe aller Flächenmasse $F(\Delta_{ts})$, und hieraus folgt endlich, dass das Flächenmass $F(\Delta)$ auch gleich der Summe aller Flächenmasse $F(\Delta_k)$ ist. Damit ist der Beweis des Satzes 29 vollständig erbracht.

**Definition.** Definiren wir das Flächenmass $F(P)$ eines Polygons als die Summe der Flächenmasse aller Dreiecke, in die dasselbe bei einer bestimmten Zerlegung zerfällt, so erkennen wir auf Grund des Satzes 29 durch eine ähnliche Schlussweise, wie wir sie in § 18 beim Beweise des Satzes 24 angewandt haben, dass das Flächenmass eines Polygons von der Art der Zerlegung in Dreiecke unabhängig ist und mithin allein durch das Polygon sich eindeutig bestimmt. Aus dieser Definition entnehmen wir vermittels des Satzes 29 die Thatsache, dass *flächengleiche Polygone gleiches Flächenmass haben*.

Sind ferner $P$ und $Q$ zwei inhaltsgleiche Polygone, so muss es nach der Definition zwei flächengleiche Polygone $P'$ und $Q'$ geben, so dass das aus $P$ und $P'$ zusammengesetzte Polygon mit dem aus $Q$ und $Q'$ zusammengesetzten Polygon flächengleich ausfällt. Aus den beiden Gleichungen:

$$
F(P + P') = F(Q + Q'), \quad F(P') = F(Q')
$$

schliessen wir leicht

$$
F(P) = F(Q),
$$

d. h. *inhaltsgleiche Polygone haben gleiches Flächenmass*.

Aus der letzteren Thatsache entnehmen wir unmittelbar den Beweis des Satzes 28. Bezeichnen wir nämlich die gleiche Grundlinie der beiden Dreiecke mit $g$, die zugehörigen Höhen mit $h$ und $h'$, so schliessen wir aus der angenommenen Inhaltsgleichheit der beiden Dreiecke, dass dieselben auch gleiches Flächenmass haben müssen, d. h. es folgt:

$$
\frac{1}{2}gh = \frac{1}{2}gh'
$$

und mithin nach Division durch $\frac{1}{2}g$

$$
h = h';
$$

dies ist die Aussage des Satzes 28.
