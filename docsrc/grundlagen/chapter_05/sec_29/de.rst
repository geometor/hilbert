:layout: book
:canonical_id: § 29
:breadcrumb_title: § 29
:order: 29
:folio: § 29
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s29:

.. folio:: § 29
   :page: 67

§ 29: Aufbau einer räumlichen Geometrie mit Hülfe eines Desarguesschen Zahlensystems
====================================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Es sei nun irgend ein Desarguessches Zahlensystem D vorgelegt; dasselbe ermöglicht uns den Aufbau einer räumliehen Geometrie, in der die Axiome I, II, III sämtlich erfüllt sind.

Um dies einzusehen, denken wir uns das System von irgend drei Zahlen :math:`(x, y, z)` des Desarguesschen Zahlensystems :math:`D` als einen Punkt und das System von irgend vier Zahlen :math:`(u : v : w : r)` in :math:`D`, von denen die ersten drei Zahlen nicht zugleich :math:`0` sind, als eine Ebene; doch sollen die Systeme :math:`(u : v : w : r)` und :math:`(au : av : aw : ar)`, wo :math:`a` irgend eine von :math:`0` verschiedene Zahl in :math:`D` bedeutet, die nämliche Ebene darstellen. Das Bestehen der Gleichung

.. math::

   ux + vy + wz + r = 0

möge ausdrücken, dass der Punkt :math:`(x, y, z)` auf der Ebene :math:`(u : v : w : r)` liegt. Die Gerade endlich definiren wir mit Hülfe eines Systems zweier Ebenen :math:`(u' : v' : w' : r')` und :math:`(u'' : v'' : w'' : r'')`, wenn es nicht möglich ist, zwei von :math:`0` verschiedene Zahlen :math:`a', a''` in :math:`D` zu finden, sodass gleichzeitig

.. math::

   a'u' = a''u'', \quad a'v' = a''v'', \quad a'w' = a''w''

wird. Ein Punkt :math:`(x, y, z)` heisst auf dieser Geraden :math:`[(u' : v' : w' : r'), (u'' : v'' : w'' : r'')]` gelegen, wenn er den beiden Ebenen :math:`(u' : v' : w' : r')` und :math:`(u'' : v'' : w'' : r'')` gemeinsam ist. Zwei Gerade, welche dieselben Punkte enthalten, gelten als nicht verschieden.

Indem wir die Rechnungsgesetze 1–11 in § 13 anwenden, die nach Voraussetzung für die Zahlen in :math:`D` gelten sollen, gelangen wir ohne Schwierigkeit zu dem Resultate, dass in der soeben aufgestellten räumlichen Geometrie die Axiome I und III sämtlich erfüllt sind.

Damit auch den Axiomen II der Anordnung Genüge geschehe, treffen wir folgende Festsetzungen. Es seien

.. math::

   (x_1, y_1, z_1), \quad (x_2, y_2, z_2), \quad (x_3, y_3, z_3)

irgend drei Punkte einer Geraden

.. math::

   [(u' : v' : w' : r'), \; (u'' : v'' : w'' : r'')];

dann heisse der Punkt :math:`(x_2, y_2, z_2)` zwischen den beiden anderen gelegen, wenn wenigstens eine der sechs Doppelungleichungen

.. math::

   \begin{aligned}
   (1)\quad x_1 &< x_2 < x_3, & x_1 &> x_2 > x_3, \\
   (2)\quad y_1 &< y_2 < y_3, & y_1 &> y_2 > y_3, \\
   (3)\quad z_1 &< z_2 < z_3, & z_1 &> z_2 > z_3
   \end{aligned}

erfüllt ist. Besteht nun etwa eine der beiden Doppelungleichungen (1), so schliessen wir leicht, dass entweder :math:`y_1 = y_2 = y_3` oder notwendig eine der beiden Doppelungleichungen (2) und ebenso dass entweder :math:`z_1 = z_2 = z_3` oder eine der Doppelungleichungen (3) gelten muss. In der That, aus den Gleichungen

.. math::

   \begin{aligned}
   u'x_i + v'y_i + w'z_i + r' &= 0, \\
   u''x_i + v''y_i + w''z_i + r'' &= 0 \qquad (i = 1, 2, 3)
   \end{aligned}

leiten wir durch linksseitige Multiplikation derselben mit geeigneten Zahlen aus :math:`D` und durch nachherige Addition der entstehenden Gleichungen ein Gleichungssystem von der Gestalt

.. math::

   (4)\quad u'''x_i + v'''y_i + r''' = 0 \qquad (i = 1, 2, 3)

ab. Hierin ist der Coefficient :math:`v'''` sicher nicht :math:`0`, da sonst die Gleichheit der drei Zahlen :math:`x_1, x_2, x_3` folgen würde. Aus

.. math::

   x_1 \lesseqgtr x_2 \lesseqgtr x_3

schliessen wir

.. math::

   u'''x_1 \gtreqless u'''x_2 \gtreqless u'''x_3

und mithin wegen (4)

.. math::

   v'''y_1 + r''' \lesseqgtr v'''y_2 + r''' \lesseqgtr v'''y_3 + r'''

und daher

.. math::

   v'''y_1 \lesseqgtr v'''y_2 \lesseqgtr v'''y_3,

und da :math:`v'''` nicht :math:`0` ist, so haben wir

.. math::

   y_1 \lesseqgtr y_2 \lesseqgtr y_3;

in jeder dieser Doppelungleichungen soll stets entweder durchweg das obere oder durchweg das mittlere oder durchweg das untere Zeichen gelten.

Die angestellten Ueberlegungen lassen erkennen, dass in unserer Geometrie die linearen Axiome II 1–4 der Anordnung zutreffen. Es bleibt noch zu zeigen übrig, dass in unserer Geometrie auch das ebene Axiom II 5 gültig ist.

Zu dem Zwecke sei eine Ebene :math:`(u : v : w : r)` und in ihr eine Gerade :math:`[(u : v : w : r), (u' : v' : w' : r')]` gegeben. Wir setzen fest, dass alle in der Ebene :math:`(u : v : w : r)` gelegenen Punkte :math:`(x, y, z)`, für die der Ausdruck :math:`u'x + v'y + w'z + r'` kleiner oder grösser als :math:`0` ausfällt, auf der einen bez. auf der anderen Seite von jener Geraden gelegen sein sollen, und haben dann zu beweisen, dass diese Festsetzung sich mit der vorigen in Uebereinstimmung befindet, was leicht geschehen kann.

Damit haben wir erkannt, dass die sämtlichen Axiome I, II, III in derjenigen räumlichen Geometrie erfüllt sind, die in der oben geschilderten Weise aus dem Desarguesschen Zahlensystem D entspringt. Bedenken wir, dass der Desarguessche Satz eine Folge der Axiome I, II, III ist, so sehen wir, dass die eben gefundene Thatsache die genaue Umkehrung desjenigen Ergebnisses darstellt, zu dem wir in § 28 gelangt sind.
