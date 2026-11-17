:layout: book
:canonical_id: § 39
:breadcrumb_title: § 39
:order: 39
:folio: S. 85
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s39:

.. folio:: § 39
   :page: 85

§ 39: Kriterium für die Ausführbarkeit geometrischer Konstruktionen mittelst Lineals und Streckenübertragers
============================================================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Es sei eine geometrische Konstruktionsaufgabe vorgelegt, die mittelst des Zirkels ausführbar ist; wir wollen dann ein Kriterium aufzustellen versuchen, welches unmittelbar aus der analytischen Natur der Aufgabe und ihrer Lösungen beurteilen lässt, ob die Konstruktion auch allein mittelst Lineals und Streckenübertragers ausführbar ist. Wir werden bei dieser Untersuchung auf den folgenden Satz geführt:

.. _grundlagen-de-thm-44:

**Satz 44.** Es sei eine geometrische Konstruktionsaufgabe vorgelegt von der Art, dass man bei analytischer Behandlung derselben die Coordinaten der gesuchten Punkte aus den Coordinaten der gegebenen Punkte lediglich durch rationale Operationen und durch Ziehen von Quadratwurzeln finden kann; es sei $n$ die kleinste Anzahl der Quadratwurzeln, die hierbei zur Berechnung der Coordinaten der Punkte ausreichen: soll dann die vorgelegte Konstruktionsaufgabe sich auch allein durch Ziehen von Geraden und Abtragen von Strecken ausführen lassen, so ist dafür notwendig und hinreichend, dass die geometrische Aufgabe genau $2^n$ reelle Lösungen besitzt und zwar für alle Lagen der gegebenen Punkte, d. h. für alle Werte der in den Coordinaten der gegebenen Punkte auftretenden willkürlichen Parameter.

**Beweis.** Wir beweisen diesen Satz 44 ausschliesslich für den Fall, dass die Coordinaten der gegebenen Punkte rationale Funktionen eines Parameters $p$ mit rationalen Coefficienten sind.

Die Notwendigkeit des aufgestellten Kriteriums leuchtet ein. Um zu zeigen, dass dasselbe auch hinreicht, setzen wir dieses Kriterium als erfüllt voraus und betrachten zunächst eine solche von jenen $n$ Quadratwurzeln, die bei der Berechnung der Coordinaten der gesuchten Punkte zuerst zu ziehen ist. Der Ausdruck unter dieser Quadratwurzel ist eine rationale Funktion $f_1(p)$ des Parameters $p$ mit rationalen Coefficienten; diese rationale Funktion darf für beliebige reelle Parameterwerte $p$ niemals negative Werte annehmen, da sonst entgegen der Voraussetzung die vorgelegte Aufgabe für gewisse Werte $p$ imaginäre Lösungen haben müsste. Aus Satz 43 schliessen wir daher, dass $f_1(p)$ als Quotient von Summen von Quadraten ganzer rationaler Funktionen darstellbar ist.

Nunmehr zeigen die Formeln

$$
\begin{aligned}
\sqrt{a^2 + b^2 + c^2} &= \sqrt{(\sqrt{a^2 + b^2})^2 + c^2}, \\
\sqrt{a^2 + b^2 + c^2 + d^2} &= \sqrt{(\sqrt{a^2 + b^2 + c^2})^2 + d^2}, \\
&\;\;\vdots
\end{aligned}
$$

dass allgemein das Ziehen der Quadratwurzel aus einer Summe von beliebig vielen Quadraten sich stets zurückführen lässt auf wiederholtes Ziehen der Quadratwurzel aus der Summe zweier Quadrate.

Nehmen wir diese Bemerkung mit dem vorigen Ergebnisse zusammen, so erkennen wir, dass der Ausdruck $\sqrt{f_1(p)}$ gewiss mittelst Lineals und Streckenübertragers construirt werden kann.

Wir betrachten ferner eine solche von den $n$ Quadratwurzeln, die bei der Berechnung der Coordinaten der gesuchten Punkte an zweiter Stelle zu ziehen ist. Der Ausdruck unter dieser Quadratwurzel ist eine rationale Funktion $f_2(p, \sqrt{f_1})$ des Parameters $p$ und der zuerst betrachteten Quadratwurzel; auch diese Funktion $f_2$ ist bei beliebigen reellen Parameterwerten $p$ und für jedes Vorzeichen von $\sqrt{f_1}$ niemals negativer Werte fähig, da sonst entgegen der Voraussetzung die vorgelegte Aufgabe unter ihren $2^n$ Lösungen für gewisse Werte $p$ auch imaginäre Lösungen haben müsste. Aus diesem Umstande folgt, dass $f_2$ einer quadratischen Gleichung von der Gestalt

$$
f_2^2 - \varphi_1(p)f_2 + \psi_1(p) = 0
$$

genügen muss, worin $\varphi_1(p)$ und $\psi_1(p)$ notwendig solche rationale Funktionen von $p$ mit rationalen Coefficienten sind, die für reelle Werte von $p$ niemals negative Werte besitzen. Aus der letzteren quadratischen Gleichung entnehmen wir

$$
f_2 = \frac{f_2^2 + \psi_1(p)}{\varphi_1(p)}.
$$

Nun müssen wiederum nach Satz 43 die Funktionen $\varphi_1(p)$ und $\psi_1(p)$ Quotienten von Summen von Quadraten rationaler Funktionen sein und andererseits ist nach dem Vorigen der Ausdruck $f_2$ mittelst Lineals und Streckenübertragers construirbar; der gefundene Ausdruck für $f_2$ zeigt somit, dass $f_2$ ein Quotient von Summen von Quadraten construirbarer Funktionen ist. Also lässt sich auch der Ausdruck $\sqrt{f_2}$ mittelst Lineals und Streckenübertragers construiren.

Ebenso wie der Ausdruck $f_2$ erweist sich auch jede andere rationale Funktion $\varphi_2(p, \sqrt{f_1})$ von $p$ und $\sqrt{f_1}$ als Quotient zweier Summen von Quadraten construirbarer Funktionen, sobald diese rationale Funktion $\varphi_2$ die Eigenschaft besitzt, niemals negative Werte anzunehmen bei reellem Parameter $p$ und für beiderlei Vorzeichen von $\sqrt{f_1}$.

Diese Bemerkung gestattet uns, das eben begonnene Schlussverfahren in folgender Weise fortzusetzen.

Es sei $f_3(p, \sqrt{f_1}, \sqrt{f_2})$ ein solcher Ausdruck, der von den drei Argumenten $p, \sqrt{f_1}, \sqrt{f_2}$ in rationaler Weise abhängt und aus dem bei der analytischen Berechnung der Coordinaten der gesuchten Punkte an dritter Stelle die Quadratwurzel zu ziehen ist. Wie vorhin schliessen wir, dass $f_3$ bei beliebigen reellen Werten $p$ und für beiderlei Vorzeichen von $\sqrt{f_1}$ und $\sqrt{f_2}$ niemals negative Werte annehmen darf; dieser Umstand wiederum zeigt, dass $f_3$ einer quadratischen Gleichung von der Gestalt

$$
f_3^2 - \varphi_2(p, \sqrt{f_1})f_3 + \psi_2(p, \sqrt{f_1}) = 0
$$

genügen muss, worin $\varphi_2$ und $\psi_2$ solche rationale Funktionen von $p$ und $\sqrt{f_1}$ bedeuten, die für reelle Werte $p$ und beiderlei Vorzeichen von $\sqrt{f_1}$ negativer Werte nicht fähig sind. Da mithin $\varphi_2$ und $\psi_2$ nach der vorigen Bemerkung Quotienten zweier Summen von Quadraten construirbarer Ausdrücke sind, so folgt das gleiche auch für den Ausdruck

$$
f_3 = \frac{f_3^2 + \psi_2(p, \sqrt{f_1})}{\varphi_2(p, \sqrt{f_1})}
$$

und mithin ist auch $\sqrt{f_3}$ mittelst Lineals und Streckenübertragers construirbar.

Die Fortsetzung dieser Schlussweise führt zum Beweise des Satzes 44 in dem betrachteten Falle eines Parameters $p$.

Die allgemeine Richtigkeit des Satzes 44 hängt davon ab, ob der Satz 43 in entsprechender Weise sich auf den Fall mehrerer Veränderlicher verallgemeinern lässt.

Als Beispiel für die Anwendung des Satzes 44 mögen die regulären mittelst Zirkels construirbaren Polygone dienen ; in diesem Falle kommt ein willkürlicher Parameter p nicht vor, sondern die zu construirenden Ausdrücke stellen sämtlich algebraische Zahlen dar. Man sieht leicht, dass das Kriterium des Satzes 44 erfüllt ist, und somit ergiebt sich, dass man jene regulären Polygone auch allein mittelst Ziehens von Geraden und Abtragens von Strecken construiren kann — ein Resultat, welches sich auch aus der Theorie der Kreisteilung direkt entnehmen lässt.

Was weitere aus der Elementargeometrie bekannte Konstruktionsaufgaben anbetrifft, so sei hier nur erwähnt, dass das Malfattische Problem, nicht aber die Apollonische Berührungsaufgabe allein mittelst Lineals und Streckenübertragers gelöst werden kann.


----

.. rubric:: Fussnoten
