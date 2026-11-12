:layout: book

.. _grundlagen-chapter-2-de:

Kapitel II: Die Widerspruchslosigkeit und gegenseitige Unabhängigkeit der Axiome
================================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, B. G. Teubner, Leipzig 1899)

.. contents:: Gliederung
   :local:
   :depth: 2
   :backlinks: none

.. _grundlagen-de-s9:

.. folio:: § 9
   :page: 19

§ 9. Die Widerspruchslosigkeit der Axiome
-----------------------------------------

Die Axiome der fünf in Kapitel I aufgestellten Axiomgruppen stehen mit einander nicht in Widerspruch, d. h. es ist nicht möglich, durch logische Schlüsse aus denselben eine Thatsache abzuleiten, welche einem der aufgestellten Axiome widerspricht. Um

dies einzusehen , genügt es , eine Geometrie anzugeben , in der sämtliche Axiome der fünf Gruppen erfüllt sind.

Man betrachte den Bereich $\Omega$ aller derjenigen algebraischen Zahlen, welche hervorgehen, indem man von der Zahl $1$ ausgeht und eine endliche Anzahl von Malen die vier Rechnungsoperationen: Addition, Subtraktion, Multiplikation, Division und die fünfte Operation $\sqrt{1 + \omega^2}$ anwendet, wobei $\omega$ jedesmal eine Zahl bedeuten kann, die vermöge jener fünf Operationen bereits entstanden ist.

Wir denken uns ein Paar von Zahlen $(x, y)$ des Bereiches $\Omega$ als einen Punkt und die Verhältnisse von irgend drei Zahlen $(u : v : w)$ aus $\Omega$, falls $u, v$ nicht beide Null sind, als eine Gerade; ferner möge das Bestehen der Gleichung

$$
ux + vy + w = 0
$$

ausdrücken, dass der Punkt $(x, y)$ auf der Geraden $(u : v : w)$ liegt; damit sind, wie man leicht sieht, die Axiome I 1–2 und III erfüllt. Die Zahlen des Bereiches $\Omega$ sind sämtlich reell; indem wir berücksichtigen, dass dieselben sich ihrer Grösse nach anordnen lassen, können wir leicht solche Festsetzungen für unsere Punkte und Geraden treffen, dass auch die Axiome II der Anordnung sämtlich gültig sind. In der That, sind $(x_1, y_1), (x_2, y_2), (x_3, y_3), \dots$ irgend welche Punkte auf einer Geraden, so möge dies ihre Reihenfolge auf der Geraden sein, wenn die Zahlen $x_1, x_2, x_3, \dots$ oder $y_1, y_2, y_3, \dots$ in dieser Reihenfolge entweder beständig abnehmen oder wachsen; um ferner die Forderung des Axioms II 5 zu erfüllen, haben wir nur nöthig festzusetzen, dass alle Punkte $(x, y)$, für die $ux + vy + w$ kleiner oder grösser als $0$ ausfällt, auf der einen bez. auf der anderen Seite der Geraden $(u : v : w)$ gelegen sein sollen. Man überzeugt sich leicht, dass diese Festsetzung sich mit der vorigen Festsetzung in Uebereinstimmung befindet, derzufolge ja die Reihenfolge der Punkte auf einer Geraden bereits bestimmt ist.

Das Abtragen von Strecken und Winkeln erfolgt nach den bekannten Methoden der analytischen Geometrie. Eine Transformation von der Gestalt

$$
\begin{aligned}
x' &= x + a, \\
y' &= y + b
\end{aligned}
$$

vermittelt die Parallelverschiebung von Strecken und Winkeln. Wird ferner der Punkt $(0, 0)$ mit $O$, der Punkt $(1, 0)$ mit $E$ und ein beliebiger Punkt $(a, b)$ mit $C$ bezeichnet, so entsteht durch Drehung um den Winkel $\angle COE$, wenn $O$ der feste Drehpunkt ist, aus dem beliebigen Punkte $(x, y)$ der Punkt $(x', y')$, wobei

$$
\begin{aligned}
x' &= \frac{a}{\sqrt{a^2 + b^2}} x - \frac{b}{\sqrt{a^2 + b^2}} y, \\
y' &= \frac{b}{\sqrt{a^2 + b^2}} x + \frac{a}{\sqrt{a^2 + b^2}} y
\end{aligned}
$$

zu setzen ist. Da die Zahl

$$
\sqrt{a^2 + b^2} = a\sqrt{1 + \left(\frac{b}{a}\right)^2}
$$

wiederum dem Bereiche $\Omega$ angehört, so gelten bei unseren Festsetzungen auch die Congruenzaxiome IV und offenbar ist auch das Archimedische Axiom V erfüllt.

Wir schliessen hieraus, dass jeder Widerspruch in den Folgerungen aus unseren Axiomen auch in der Arithmetik des Bereiches $\Omega$ erkennbar sein müsste.

Die entsprechende Betrachtungsweise für die räumliche Geometrie bietet keine Schwierigkeit.

Wählen wir in der obigen Entwickelung statt des Bereiches $\Omega$ den Bereich aller reellen Zahlen, so erhalten wir ebenfalls eine Geometrie, in der sämtliche Axiome I–V gültig sind. Für unseren Beweis genügte die Zuhülfenahme des Bereiches $\Omega$, der nur eine abzählbare Menge von Elementen enthält.

.. _grundlagen-de-s10:

.. folio:: § 10
   :page: 21

§ 10. Die Unabhängigkeit des Parallelenaxioms (Nicht-Euklidische Geometrie)
---------------------------------------------------------------------------

Nachdem wir die Widerspruchslosigkeit der Axiome erkannt haben, ist es von Interesse zu untersuchen, ob sie sämtlich von einander unabhängig sind. In der That zeigt sich , dass keines der Axiome durch logische Schlüsse aus den übrigen abgeleitet werden kann.

Was zunächst die einzelnen Axiome der Gruppen I, II und IV betrifft, so ist der Nachweis dafür leicht zu führen, dass die Axiome ein und derselben Gruppe je unter sich unabhängig sind [#fn1]_.

Die Axiome der Gruppen I und II liegen bei unserer Darstellung den übrigen Axiomen zu Grunde, so dass es sich nur noch darum handelt, für jede der Gruppen III, IV und V die Unabhängigkeit von den übrigen nachzuweisen.

Die e r s t e r e Aussage des Parallelenaxioms kann aus den Axiomen der Gruppen I, II, IV bewiesen werden. Um dies einzusehen, verbinden wir den gegebenen Punkt A mit einem beliebigen Punkte B der Geraden a. Es sei ferner C irgend ein anderer Punkt der Geraden $a$; dann tragen wir $\angle ABC$ an $AB$ im Punkte $A$ nach derjenigen Seite in der nämlichen Ebene $\alpha$ an, auf der nicht der Punkt $C$ liegt. Die so erhaltene Gerade durch $A$ trifft die Gerade $a$ nicht. In der That, schnitte sie $a$ im Punkte $D$ und nehmen wir etwa an, dass $B$ zwischen $C$ und $D$ liege, so könnten wir auf $a$ einen Punkt $D'$ finden, so dass $B$ zwischen $D$ und $D'$ liegt und überdies

$$
AD \equiv BD'
$$

ausfiele. Wegen der Congruenz der Dreiecke $ABD$ und $BAD'$ würde die Congruenz

$$
\angle ABD \equiv \angle BAD'
$$

folgen und da die Winkel ABD' und ABD Nebenwinkel sind, so müssten sich dann mit Rücksicht auf Satz 12 auch die Winkel BAD und BAD' als Nebenwinkel erweisen; dies ist aber wegen Satz 1 nicht der Fall.

Die zweite Aussage des Parallelenaxioms III ist von den übrigen Axiomen unabhängig ; dies zeigt man in bekannter Weise am einfachsten wie folgt. Man wähle die Punkte, Geraden und Ebenen der gewöhnlichen in § 9 construirten Geometrie, so weit sie innerhalb einer festen Kugel Verlaufen , für sich allein als Elemente einer räumlichen Geometrie und vermittle die Congruenzen dieser Geometrie durch solche lineare Transformationen der gewöhnlichen Geometrie, welche die feste Kugel in sich überführen. Bei geeigneten Festsetzungen erkennt man, dass in dieser „Nicht- Euklidischen" Geometrie sämtliche Axiome ausser dem Euklidischen Axiom III gültig sind und da die Möglichkeit der gewöhnlichen Geometrie in § 9 nachgewiesen worden ist, so folgt nunmehr auch die Möglichkeit der Nicht-Euklidischen Geometrie.

.. _grundlagen-de-s11:

.. folio:: § 11
   :page: 23

§ 11. Die Unabhängigkeit der Congruenzaxiome
--------------------------------------------

Wir werden die Unabhängigkeit der Congruenzaxiome erkennen, indem wir den Nachweis führen, dass das Axiom IV 6 oder, was auf das nämliche hinausläuft, der erste Congruenzsatz für Dreiecke, d. i. Satz 10 durch logische Schlüsse nicht aus den übrigen Axiomen I, II, III, IV 1—5, V abgeleitet werden kann.

Wir wählen die Punkte, Geraden, Ebenen der gewöhnlichen Geometrie auch als Elemente der neuen räumlichen Geometrie und definiren das Abtragen der Winkel ebenfalls wie in der gewöhnlichen Geometrie, etwa in der Weise, wie in § 9 auseinandergesetzt worden ist ; dagegen definiren wir das Abtragen der Strecken auf andere Art. Die zwei Punkte $A_1, A_2$ mögen in der gewöhnlichen Geometrie die Coordinaten $x_1, y_1, z_1$ bez. $x_2, y_2, z_2$ haben; dann bezeichnen wir den positiven Wert von

$$
\sqrt{(x_1 - x_2 + y_1 - y_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}
$$

als die *Länge* der Strecke $A_1A_2$ und nun sollen zwei beliebige Strecken $A_1A_2$ und $A'_1A'_2$ einander congruent heissen, wenn sie im eben festgesetzten Sinne gleiche Längen haben.

Es leuchtet unmittelbar ein, dass in der so hergestellten räumlichen Geometrie die Axiome I, II, III, IV 1–2, 4–5, V gültig sind.

Um zu zeigen, dass auch das Axiom IV 3 erfüllt ist, wählen wir eine beliebige Gerade $a$ und auf ihr drei Punkte $A_1, A_2, A_3$, sodass $A_2$ zwischen $A_1$ und $A_3$ liegt. Die Punkte $x, y, z$ der Geraden $a$ seien durch die Gleichungen

$$
x = \lambda t + \lambda', \quad y = \mu t + \mu', \quad z = \nu t + \nu'
$$

gegeben, worin $\lambda, \lambda', \mu, \mu', \nu, \nu'$ gewisse Constante und $t$ einen Parameter bedeutet. Sind $t_1, t_2 \; (< t_1), t_3 \; (< t_2)$ die Parameterwerte, die den Punkten $A_1, A_2, A_3$ entsprechen, so finden wir für die Längen der drei Strecken $A_1A_2$, $A_2A_3$ und $A_1A_3$ bez. die Ausdrücke:

$$
(t_1 - t_2)|\sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2}|, \quad (t_2 - t_3)|\sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2}|, \quad (t_1 - t_3)|\sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2}|,
$$

und mithin ist die Summe der Längen der Strecken $A_1A_2$ und $A_2A_3$ gleich der Länge der Strecke $A_1A_3$; dieser Umstand bedingt die Gültigkeit des Axioms IV 3.

Das Axiom IV 6 oder vielmehr der erste Congruenzsatz für Dreiecke ist in unserer Geometrie nicht immer erfüllt. Betrachten wir nämlich in der Ebene $z = 0$ die vier Punkte

| $O$ mit den Coordinaten $x = 0, \quad y = 0$,
| $A$ mit den Coordinaten $x = 1, \quad y = 0$,
| $B$ mit den Coordinaten $x = 0, \quad y = 1$,
| $C$ mit den Coordinaten $x = \frac{1}{2}, \quad y = \frac{1}{2}$,

so sind in den beiden (rechtwinkligen) Dreiecken $OAC$ und $OBC$ die Winkel bei $C$ und die anliegenden Seiten entsprechend congruent, da die Seite $OC$ beiden Dreiecken gemeinsam ist und die Strecken $AC$ und $BC$ die gleiche Länge $\frac{1}{2}$ besitzen. Dagegen haben die dritten Seiten $OA$ und $OB$ die Länge $1$, bez. $\sqrt{2}$ und sind daher nicht einander congruent.

Es ist auch nicht schwer, in dieser Geometrie zwei Dreiecke zu finden, für welche das Axiom IV 6 selbst nicht erfüllt ist.

.. picture:: /_static/figures/fig_non_congruence_model.svg
   :alt: Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).
   :caption: **Anisotropic Countermodel to Congruence Axiom IV 6 (§ 11).** Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).


.. _grundlagen-de-s12:

.. folio:: § 12
   :page: 24

§ 12. Die Unabhängigkeit des Stetigkeitsaxioms V (Nicht-Archimedische Geometrie)
--------------------------------------------------------------------------------

Um die Unabhängigkeit des Archimedischen Axioms V zu beweisen, müssen wir eine Geometrie herstellen, in der sämtliche Axiome mit Ausnahme des Archimedischen Axioms erfüllt sind [#fn2]_.

Zu dem Zwecke construiren wir den Bereich $\Omega(t)$ aller derjenigen algebraischen Funktionen von $t$, welche aus $t$ durch die vier Rechnungsoperationen der Addition, Subtraktion, Multiplikation, Division und durch die fünfte Operation $\sqrt{1 + \omega^2}$ hervorgehen; dabei soll $\omega$ irgend eine Funktion bedeuten, die vermöge jener fünf Operationen bereits entstanden ist. Die Menge der Elemente von $\Omega(t)$ ist — ebenso wie von $\Omega$ — eine abzählbare. Die fünf Operationen sind sämtlich eindeutig und reell ausführbar; der Bereich $\Omega(t)$ enthält daher nur eindeutige und reelle Funktionen von $t$.

Es sei $c$ irgend eine Funktion des Bereiches $\Omega(t)$; da die Funktion $c$ eine algebraische Funktion von $t$ ist, so kann sie jedenfalls nur für eine endliche Anzahl von Werten $t$ verschwinden und es wird daher die Funktion $c$ für genügend grosse positive Werte von $t$ entweder stets positiv oder stets negativ ausfallen.

Wir sehen jetzt die Funktionen des Bereiches $\Omega(t)$ als eine Art complexer Zahlen an; offenbar sind in dem so definirten complexen Zahlensystem die gewöhnlichen Rechnungsregeln sämtlich gültig. Ferner möge, wenn $a, b$ irgend zwei verschiedene Zahlen dieses complexen Zahlensystems sind, die Zahl $a$ grösser oder kleiner als $b$, in Zeichen: $a > b$ oder $a < b$, heissen, je nachdem die Differenz $c = a - b$ als Funktion von $t$ für genügend grosse positive Werte von $t$ stets positiv oder stets negativ ausfällt. Bei dieser Festsetzung ist für die Zahlen unseres complexen Zahlensystems eine Anordnung ihrer Grösse nach möglich, die von der gewöhnlichen Art wie bei reellen Zahlen ist; auch gelten, wie man leicht erkennt, für unsere complexen Zahlen die Sätze, wonach Ungleichungen richtig bleiben, wenn man auf beiden Seiten die gleiche Zahl addirt oder beide Seiten mit der gleichen Zahl $> 0$ multiplicirt.

Bedeutet $n$ eine beliebige positive ganze rationale Zahl, so gilt für die beiden Zahlen $n$ und $t$ des Bereiches $\Omega(t)$ gewiss die Ungleichung $n < t$, da die Differenz $n - t$, als Funktion von $t$ betrachtet, für genügend grosse positive Werte von $t$ offenbar stets negativ ausfällt. Wir sprechen diese Thatsache in folgender Weise aus: die beiden Zahlen $1$ und $t$ des Bereiches $\Omega(t)$, die beide $> 0$ sind, besitzen die Eigenschaft, dass ein beliebiges Vielfaches der ersteren stets kleiner als die letztere Zahl bleibt.

Wir bauen nun aus den complexen Zahlen des Bereiches $\Omega(t)$ eine Geometrie genau auf dieselbe Art auf, wie dies in § 9 unter Zugrundelegung des Bereiches $\Omega$ von algebraischen Zahlen geschehen ist: wir denken uns ein System von drei Zahlen $(x, y, z)$ des Bereiches $\Omega(t)$ als einen Punkt und die Verhältnisse von irgend vier Zahlen $(u : v : w : r)$ aus $\Omega(t)$, falls $u, v, w$ nicht sämtlich Null sind, als eine Ebene; ferner möge das Bestehen der Gleichung

$$
ux + vy + wz + r = 0
$$

ausdrücken, dass der Punkt $(x, y, z)$ in der Ebene $(u : v : w : r)$ liegt und die Gerade sei die Gesamtheit aller in zwei Ebenen gelegenen Punkte. Treffen wir sodann die entsprechenden Festsetzungen über die Anordnung der Elemente und über Abtragen von Strecken und Winkeln, wie in § 9, so entsteht eine „*Nicht-Archimedische*“ Geometrie, in welcher, wie die zuvor erörterten Eigenschaften des complexen Zahlensystems $\Omega(t)$ zeigen, sämtliche Axiome mit Ausnahme des Archimedischen Axioms erfüllt sind.

In der That können wir die Strecke 1 auf der Strecke t beliebig oft hinter einander abtragen, ohne dass der Endpunkt der Strecke t bedeckt wird ; dies widerspricht der Forderung des Archimedischen Axioms.


----

.. rubric:: Fussnoten

.. [#fn1] Vergl. meine Vorlesung über Euklidische Geometrie (Wintersemester 1898/99), die nach einer Ausarbeitung des Herrn Dr. von Schaper für meine Zuhörer autographirt worden ist.

.. [#fn2] G. Veronese hat in seinem tiefsinnigen Werke, *Grundzüge der Geometrie*, deutsch von A. Schepp, Leipzig 1894 ebenfalls den Versuch gemacht, eine Geometrie aufzubauen, die von dem Archimedischen Axiom unabhängig ist.
