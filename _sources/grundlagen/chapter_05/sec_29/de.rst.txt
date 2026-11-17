:layout: book
:canonical_id: § 29
:breadcrumb_title: § 29
:order: 29
:folio: S. 67
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s29:

.. folio:: § 29
   :page: 67

§ 29: Aufbau einer räumlichen Geometrie mit Hülfe eines Desarguesschen Zahlensystems
====================================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Es sei nun irgend ein Desarguessches Zahlensystem D vorgelegt; dasselbe ermöglicht uns den Aufbau einer räumliehen Geometrie, in der die Axiome I, II, III sämtlich erfüllt sind.

Um dies einzusehen, denken wir uns das System von irgend drei Zahlen $(x, y, z)$ des Desarguesschen Zahlensystems $D$ als einen Punkt und das System von irgend vier Zahlen $(u : v : w : r)$ in $D$, von denen die ersten drei Zahlen nicht zugleich $0$ sind, als eine Ebene; doch sollen die Systeme $(u : v : w : r)$ und $(au : av : aw : ar)$, wo $a$ irgend eine von $0$ verschiedene Zahl in $D$ bedeutet, die nämliche Ebene darstellen. Das Bestehen der Gleichung

$$
ux + vy + wz + r = 0
$$

möge ausdrücken, dass der Punkt $(x, y, z)$ auf der Ebene $(u : v : w : r)$ liegt. Die Gerade endlich definiren wir mit Hülfe eines Systems zweier Ebenen $(u' : v' : w' : r')$ und $(u'' : v'' : w'' : r'')$, wenn es nicht möglich ist, zwei von $0$ verschiedene Zahlen $a', a''$ in $D$ zu finden, sodass gleichzeitig

$$
a'u' = a''u'', \quad a'v' = a''v'', \quad a'w' = a''w''
$$

wird. Ein Punkt $(x, y, z)$ heisst auf dieser Geraden $[(u' : v' : w' : r'), (u'' : v'' : w'' : r'')]$ gelegen, wenn er den beiden Ebenen $(u' : v' : w' : r')$ und $(u'' : v'' : w'' : r'')$ gemeinsam ist. Zwei Gerade, welche dieselben Punkte enthalten, gelten als nicht verschieden.

Indem wir die Rechnungsgesetze 1–11 in § 13 anwenden, die nach Voraussetzung für die Zahlen in $D$ gelten sollen, gelangen wir ohne Schwierigkeit zu dem Resultate, dass in der soeben aufgestellten räumlichen Geometrie die Axiome I und III sämtlich erfüllt sind.

Damit auch den Axiomen II der Anordnung Genüge geschehe, treffen wir folgende Festsetzungen. Es seien

$$
(x_1, y_1, z_1), \quad (x_2, y_2, z_2), \quad (x_3, y_3, z_3)
$$

irgend drei Punkte einer Geraden

$$
[(u' : v' : w' : r'), \; (u'' : v'' : w'' : r'')];
$$

dann heisse der Punkt $(x_2, y_2, z_2)$ zwischen den beiden anderen gelegen, wenn wenigstens eine der sechs Doppelungleichungen

$$
\begin{aligned}
(1)\quad x_1 &< x_2 < x_3, & x_1 &> x_2 > x_3, \\
(2)\quad y_1 &< y_2 < y_3, & y_1 &> y_2 > y_3, \\
(3)\quad z_1 &< z_2 < z_3, & z_1 &> z_2 > z_3
\end{aligned}
$$

erfüllt ist. Besteht nun etwa eine der beiden Doppelungleichungen (1), so schliessen wir leicht, dass entweder $y_1 = y_2 = y_3$ oder notwendig eine der beiden Doppelungleichungen (2) und ebenso dass entweder $z_1 = z_2 = z_3$ oder eine der Doppelungleichungen (3) gelten muss. In der That, aus den Gleichungen

$$
\begin{aligned}
u'x_i + v'y_i + w'z_i + r' &= 0, \\
u''x_i + v''y_i + w''z_i + r'' &= 0 \qquad (i = 1, 2, 3)
\end{aligned}
$$

leiten wir durch linksseitige Multiplikation derselben mit geeigneten Zahlen aus $D$ und durch nachherige Addition der entstehenden Gleichungen ein Gleichungssystem von der Gestalt

$$
(4)\quad u'''x_i + v'''y_i + r''' = 0 \qquad (i = 1, 2, 3)
$$

ab. Hierin ist der Coefficient $v'''$ sicher nicht $0$, da sonst die Gleichheit der drei Zahlen $x_1, x_2, x_3$ folgen würde. Aus

$$
x_1 \lesseqgtr x_2 \lesseqgtr x_3
$$

schliessen wir

$$
u'''x_1 \gtreqless u'''x_2 \gtreqless u'''x_3
$$

und mithin wegen (4)

$$
v'''y_1 + r''' \lesseqgtr v'''y_2 + r''' \lesseqgtr v'''y_3 + r'''
$$

und daher

$$
v'''y_1 \lesseqgtr v'''y_2 \lesseqgtr v'''y_3,
$$

und da $v'''$ nicht $0$ ist, so haben wir

$$
y_1 \lesseqgtr y_2 \lesseqgtr y_3;
$$

in jeder dieser Doppelungleichungen soll stets entweder durchweg das obere oder durchweg das mittlere oder durchweg das untere Zeichen gelten.

Die angestellten Ueberlegungen lassen erkennen, dass in unserer Geometrie die linearen Axiome II 1–4 der Anordnung zutreffen. Es bleibt noch zu zeigen übrig, dass in unserer Geometrie auch das ebene Axiom II 5 gültig ist.

Zu dem Zwecke sei eine Ebene $(u : v : w : r)$ und in ihr eine Gerade $[(u : v : w : r), (u' : v' : w' : r')]$ gegeben. Wir setzen fest, dass alle in der Ebene $(u : v : w : r)$ gelegenen Punkte $(x, y, z)$, für die der Ausdruck $u'x + v'y + w'z + r'$ kleiner oder grösser als $0$ ausfällt, auf der einen bez. auf der anderen Seite von jener Geraden gelegen sein sollen, und haben dann zu beweisen, dass diese Festsetzung sich mit der vorigen in Uebereinstimmung befindet, was leicht geschehen kann.

Damit haben wir erkannt, dass die sämtlichen Axiome I, II, III in derjenigen räumlichen Geometrie erfüllt sind, die in der oben geschilderten Weise aus dem Desarguesschen Zahlensystem D entspringt. Bedenken wir, dass der Desarguessche Satz eine Folge der Axiome I, II, III ist, so sehen wir, dass die eben gefundene Thatsache die genaue Umkehrung desjenigen Ergebnisses darstellt, zu dem wir in § 28 gelangt sind.
