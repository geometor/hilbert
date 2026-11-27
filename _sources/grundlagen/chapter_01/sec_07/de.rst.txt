:layout: book
:canonical_id: § 7
:breadcrumb_title: § 7
:order: 7
:folio: § 7
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s7:

.. folio:: § 7
   :page: 12

§ 7: Folgerungen aus den Axiomen der Congruenz
==============================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

**Erklärung.** Es sei die Strecke AB congruent der Strecke A'B'. Da nach Axiom IV 1 auch die Strecke AB congruent AB

ist, so folgt aus Axiom IV 2 A'B' congruent AB ; wir sagen : die beiden Strecken AB und A'B' sind unter einander congruent.

**Erklärung.** Sind :math:`A, B, C, D, \dots, K, L` auf :math:`a` und :math:`A', B', C', D', \dots, K', L'` auf :math:`a'` zwei Reihen von Punkten, so dass die sämtlichen entsprechenden Strecken :math:`AB` und :math:`A'B'`, :math:`AC` und :math:`A'C'`, :math:`BC` und :math:`B'C'`, :math:`\dots`, :math:`KL` und :math:`K'L'` bez. einander congruent sind, so heissen die beiden Reihen von Punkten *unter einander congruent*; :math:`A` und :math:`A'`, :math:`B` und :math:`B'`, :math:`\dots`, :math:`L` und :math:`L'` heissen die *entsprechenden Punkte* der congruenten Punktreihen.

Aus den linearen Axiomen IV 1–3 schliessen wir leicht folgende Sätze:

.. _grundlagen-de-thm-9:

**Satz 9.** Ist von zwei congruenten Punktreihen :math:`A, B, \dots, K, L` und :math:`A', B', \dots, K', L'` die erste so geordnet, dass :math:`B` zwischen :math:`A` einerseits und :math:`C, D, \dots, K, L` andererseits, :math:`C` zwischen :math:`A, B` einerseits und :math:`D, \dots, K, L` andererseits, u. s. w. liegt, so sind die Punkte :math:`A', B', \dots, K', L'` auf die gleiche Weise geordnet, d. h. :math:`B'` liegt zwischen :math:`A'` einerseits und :math:`C', D', \dots, K', L'` andererseits, :math:`C'` zwischen :math:`A', B'` einerseits und :math:`D', \dots, K', L'` andererseits u. s. w.

**Erklärung.** Es sei Winkel :math:`(h, k)` congruent dem Winkel :math:`(h', k')`. Da nach Axiom IV 4 der Winkel :math:`(h, k)` congruent :math:`\angle(h, k)` ist, so folgt aus Axiom IV 5, dass :math:`\angle(h', k')` congruent :math:`\angle(h, k)` ist; wir sagen: die beiden Winkel :math:`(h, k)` und :math:`(h', k')` sind *unter einander congruent*.

**Definition.** Zwei Winkel, die den Scheitel und einen Schenkel gemein haben und deren nicht gemeinsame Schenkel eine gerade Linie bilden, heissen Nebemvinkel. Zwei Winkel mit gemeinsamem Scheitel, deren Schenkel je eine Grerade bilden, heissen Scheitelwinkel. Ein Winkel, welcher einem seiner Nebenwinkel congruent ist, heisst ein rechter Winkel.

**Erklärung.** Zwei Dreiecke :math:`ABC` und :math:`A'B'C'` heissen einander *congruent*, wenn sämtliche Congruenzen

.. math::

   \begin{aligned}
   AB &\equiv A'B', & AC &\equiv A'C', & BC &\equiv B'C', \\
   \angle A &\equiv \angle A', & \angle B &\equiv \angle B', & \angle C &\equiv \angle C'
   \end{aligned}

erfüllt sind.

.. _grundlagen-de-thm-10:

**Satz 10 (Erster Congruenzsatz für Dreiecke).** Wenn für zwei Dreiecke :math:`ABC` und :math:`A'B'C'` die Congruenzen

.. math::

   AB \equiv A'B', \quad AC \equiv A'C', \quad \angle A \equiv \angle A'

gelten, so sind die beiden Dreiecke einander congruent.

**Beweis.** Nach Axiom IV 6 sind die Congruenzen

.. math::

   \angle B \equiv \angle B' \quad \text{und} \quad \angle C \equiv \angle C'

erfüllt und es bedarf somit nur des Nachweises, dass die Seiten :math:`BC` und :math:`B'C'` einander congruent sind. Nehmen wir nun im Gegenteil an, es wäre etwa :math:`BC` nicht congruent :math:`B'C'` und bestimmen auf :math:`B'C'` den Punkt :math:`D'`, so dass :math:`BC \equiv B'D'` wird, so stimmen die beiden Dreiecke :math:`ABC` und :math:`A'B'D'` in zwei Seiten und dem von ihnen eingeschlossenen Winkel überein; nach Axiom IV 6 sind mithin insbesondere die beiden Winkel :math:`\angle BAC` und :math:`\angle B'A'D'` einander congruent. Nach Axiom IV 5 müssten mithin auch die beiden Winkel :math:`\angle B'A'C'` und :math:`\angle B'A'D'` einander congruent ausfallen; dies ist nicht möglich, da nach Axiom IV 4 ein jeder Winkel an einen gegebenen Halbstrahl nach einer gegebenen Seite in einer Ebene nur auf eine Weise abgetragen werden kann. Damit ist der Beweis für Satz 10 vollständig erbracht.

Ebenso leicht beweisen wir die weitere Thatsache:

.. _grundlagen-de-thm-11:

**Satz 11 (Zweiter Congruenzsatz für Dreiecke).** Wenn in zwei Dreiecken je eine Seite und die beiden anliegenden Winkel congruent ausfallen, so sind die Dreiecke stets congruent.

Wir sind nunmehr im Stande, die folgenden wichtigen Thatsachen zu beweisen:

.. _grundlagen-de-thm-12:

**Satz 12.** Wenn zwei Winkel :math:`\angle ABC` und :math:`\angle A'B'C'` einander congruent sind, so sind auch ihre Nebenwinkel :math:`\angle CBD` und :math:`\angle C'B'D'` einander congruent.

**Beweis.** Wir wählen die Punkte :math:`A', C', D'` auf den durch :math:`B'` gehenden Schenkeln derart, dass

.. math::

   A'B' \equiv AB, \quad C'B' \equiv CB, \quad D'B' \equiv DB

wird. In den beiden Dreiecken :math:`ABC` und :math:`A'B'C'` sind dann die Seiten :math:`AB` und :math:`CB` bez. den Seiten :math:`A'B'` und :math:`C'B'` congruent und, da überdies die von diesen Seiten eingeschlossenen Winkel nach Voraussetzung einander congruent sein sollen, so folgt nach Satz 10 die Congruenz jener Dreiecke, d. h. es gelten die Congruenzen

.. math::

   AC \equiv A'C' \quad \text{und} \quad \angle BAC \equiv \angle B'A'C'.

Da andererseits nach Axiom IV 3 die Strecken :math:`AD` und :math:`A'D'` einander congruent sind, so folgt wiederum aus Satz 10 die Congruenz der Dreiecke :math:`CAD` und :math:`C'A'D'`, d. h. es gelten die Congruenzen

.. math::

   CD \equiv C'D' \quad \text{und} \quad \angle ADC \equiv \angle A'D'C'

und hieraus folgt mittels Betrachtung der Dreiecke :math:`BCD` und :math:`B'C'D'` nach Axiom IV 6 die Congruenz der Winkel :math:`\angle CBD` und :math:`\angle C'B'D'`.

Eine unmittelbare Folgerung aus Satz 12 ist der Satz von der Congruenz der Scheitelwinkel.

.. _grundlagen-de-thm-13:

**Satz 13.** Es sei der Winkel :math:`(h, k)` in der Ebene :math:`\alpha` dem Winkel :math:`(h', k')` in der Ebene :math:`\alpha'` congruent und ferner sei :math:`l` ein Halbstrahl der Ebene :math:`\alpha`, der vom Scheitel des Winkels :math:`(h, k)` ausgeht und im Inneren dieses Winkels verläuft: dann giebt es stets einen Halbstrahl :math:`l'` in der Ebene :math:`\alpha'`, der vom Scheitel des Winkels :math:`(h', k')` ausgeht, und im Inneren dieses Winkels :math:`(h', k')` verläuft, so dass

.. math::

   \angle(h, l) \equiv \angle(h', l') \quad \text{und} \quad \angle(k, l) \equiv \angle(k', l')

wird.

**Beweis.** Wir bezeichnen die Scheitel der Winkel :math:`(h, k)` und :math:`(h', k')` bez. mit :math:`O, O'` und bestimmen dann auf den Schenkeln :math:`h, k, h', k'` die Punkte :math:`A, B, A', B'` derart, dass die Congruenzen

.. math::

   OA \equiv O'A' \quad \text{und} \quad OB \equiv O'B'

erfüllt sind. Wegen der Congruenz der Dreiecke :math:`OAB` und :math:`O'A'B'` wird

.. math::

   AB \equiv A'B', \quad \angle OAB \equiv \angle O'A'B', \quad \angle OBA \equiv \angle O'B'A'.

Die Gerade :math:`AB` schneide :math:`l` in :math:`C`; bestimmen wir dann auf der Strecke :math:`A'B'` den Punkt :math:`C'`, so dass :math:`A'C' \equiv AC` wird, so ist :math:`O'C'` der gesuchte Halbstrahl :math:`l'`. In der That, aus :math:`AC \equiv A'C'` und :math:`AB \equiv A'B'` kann mittelst Axiom IV 3 leicht die Congruenz :math:`BC \equiv B'C'` geschlossen werden; nunmehr erweisen sich die Dreiecke :math:`OAC` und :math:`O'A'C'`, sowie ferner die Dreiecke :math:`OBC` und :math:`O'B'C'` unter einander congruent; hieraus ergeben sich die Behauptungen des Satzes 13.

Auf ähnliche Art gelangen wir zu folgender Thatsache:

.. _grundlagen-de-thm-14:

**Satz 14.** Es seien einerseits :math:`h, k, l` und andererseits :math:`h', k', l'` je drei von einem Punkte ausgehende und je in einer Ebene gelegene Halbstrahlen: wenn dann die Congruenzen

.. math::

   \angle(h, l) \equiv \angle(h', l') \quad \text{und} \quad \angle(k, l) \equiv \angle(k', l')

erfüllt sind, so ist stets auch

.. math::

   \angle(h, k) \equiv \angle(h', k').

Auf Grund der Sätze 12 und 13 gelingt der Nachweis des folgenden einfachen Satzes, den Euklid — meiner Meinung nach mit Unrecht — unter die Axiome gestellt hat:

.. _grundlagen-de-thm-15:

**Satz 15.** Alle rechten Winkel sind einander congruent.

**Beweis.** Der Winkel :math:`BAD` sei seinem Nebenwinkel :math:`CAD` congruent und desgleichen sei der Winkel :math:`B'A'D'` seinem Nebenwinkel :math:`C'A'D'` congruent; es sind dann :math:`\angle BAD, \angle CAD, \angle B'A'D', \angle C'A'D'` sämtlich rechte Winkel. Wir nehmen im Gegensatz zu unserer Behauptung an, es wäre der rechte Winkel :math:`B'A'D'` nicht congruent dem rechten Winkel :math:`BAD` und tragen dann :math:`\angle B'A'D'` an den Halbstrahl :math:`AB` an, so dass der entstehende Schenkel :math:`AD''` entweder in das Innere des Winkels :math:`BAD` oder des Winkels :math:`CAD` fällt; es treffe etwa die erstere Möglichkeit zu. Wegen der Congruenz der Winkel :math:`B'A'D'` und :math:`BAD''` folgt nach Satz 12, dass auch der Winkel :math:`C'A'D'` dem Winkel :math:`CAD''` congruent ist, und da die Winkel :math:`B'A'D'` und :math:`C'A'D'` einander congruent sein sollen, so lehrt Axiom IV 5, dass auch der Winkel :math:`BAD''` dem Winkel :math:`CAD''` congruent sein muss. Da ferner :math:`\angle BAD` congruent :math:`\angle CAD` ist, so können wir nach Satz 13 innerhalb des Winkels :math:`CAD` einen von :math:`A` ausgehenden Halbstrahl :math:`AD'''` finden, so dass :math:`\angle BAD''` congruent :math:`\angle CAD'''` und zugleich :math:`\angle DAD''` congruent :math:`\angle DAD'''` wird. Nun war aber :math:`\angle BAD''` congruent :math:`\angle CAD''` und somit müsste nach Axiom IV 5 auch :math:`\angle CAD''` congruent :math:`\angle CAD'''` sein; das ist nicht möglich, weil nach Axiom IV 4 ein jeder Winkel an einen gegebenen Halbstrahl nach einer gegebenen Seite in einer Ebene nur auf eine Weise abgetragen werden kann; hiermit ist der Beweis für Satz 15 erbracht.

Wir können jetzt die Bezeichnungen „spitzer Winkel“ und „stumpfer Winkel“ in bekannter Weise einführen.

Der Satz von der Congruenz der Basiswinkel :math:`\angle A` und :math:`\angle B`

im gleichschenkligen Dreiecke ABC folgt unmittelbar durch Anwendung des Axioms IV 6 auf Dreieck ABC und Dreieck BAC. Mit Hülfe dieses Satzes und unter Hinzuziehung des Satzes 14 beweisen wir dann leicht in bekannter Weise die folgende Thatsache :

.. _grundlagen-de-thm-16:

**Satz 16 (Dritter Congruenzsatz für Dreiecke).** Wenn in zwei Dreiecken die drei Seiten entsprechend congruent ausfallen, so sind die Dreiecke congruent.

**Erklärung.** Irgend eine endliche Anzahl von Punkten heisst eine Figur; liegen alle Punkte der Figur in einer Ebene, so heisst sie eine ebene Figur.

Zwei Figuren heissen congruent, wenn ihre Punkte sich paarweise einander so zuordnen lassen, dass die auf diese Weise einander zugeordneten Strecken und Winkel sämtlich einander congruent sind.

Congruente Figuren haben, wie man aus den Sätzen 12 und 9 erkennt, folgende Eigenschaften : Drei Punkte einer Geraden liegen auch in jeder congruenten Figur auf einer Geraden. Die Anordnung der Punkte in entsprechenden Ebenen in Bezug auf entsprechende Gerade ist in congruenten Figuren die nämliche; das Gleiche gilt von der Reihenfolge entsprechender Punkte in entsprechenden Geraden.

Der allgemeinste Congruenzsatz für die Ebene und für den Raum drückt sich, wie folgt, aus :

.. _grundlagen-de-thm-17:

**Satz 17.** Wenn :math:`(A, B, C, \dots)` und :math:`(A', B', C', \dots)` congruente ebene Figuren sind und :math:`P` einen Punkt in der Ebene der ersten bedeutet, so lässt sich in der Ebene der zweiten Figur stets ein Punkt :math:`P'` finden derart, dass :math:`(A, B, C, \dots, P)` und :math:`(A', B', C', \dots, P')` wieder congruente Figuren sind. Enthalten die beiden Figuren wenigstens drei nicht auf einer Geraden liegende Punkte, so ist die Construction von :math:`P'` nur auf eine Weise möglich.

.. _grundlagen-de-thm-18:

**Satz 18.** Wenn :math:`(A, B, C, \dots)` und :math:`(A', B', C', \dots)` congruente Figuren sind und :math:`P` einen beliebigen Punkt bedeutet, so lässt sich stets ein Punkt :math:`P'` finden, so dass die Figuren :math:`(A, B, C, \dots, P)` und :math:`(A', B', C', \dots, P')` congruent sind. Enthält die Figur :math:`(A, B, C, \dots)` mindestens vier nicht in einer Ebene liegende Punkte, so ist die Construction von :math:`P'` nur auf eine Weise möglich.

Dieser Satz enthält das wichtige Resultat, dass die sämtlichen räumlichen Thatsachen der Congruenz, d. h. der Bewegung im Raume — mit Hinzuziehung der Axiomgruppen I und II — lediglich Folgerungen aus den sechs oben aufgestellten linearen und ebenen Axiomen der Congruenz sind, also das Parallelenaxiom zu ihrer Feststellung nicht notwendig ist.

Nehmen wir zu den Congruenzaxiomen noch das Parallelenaxiom III hinzu, so gelangen wir leicht zu den bekannten Thatsachen :

.. _grundlagen-de-thm-19:

**Satz 19.** Wenn zwei Parallelen von einer dritten Geraden geschnitten werden , so sind die Gegenwinkel und Wechselwinkel congruent, und umgekehrt : die Congruenz der Gegen- und Wechselwinkel hat zur Folge, dass die Geraden parallel sind.

.. _grundlagen-de-thm-20:

**Satz 20.** Die Winkel eines Dreiecks machen zusammen zwei Rechte aus.

**Definition.** Wenn :math:`M` ein beliebiger Punkt in einer Ebene :math:`\alpha` ist, so heisst die Gesamtheit aller Punkte A, für welche die

Strecken MA einander congruent sind, ein Kreis; M heisst der Mittelpunkt des Kreises.

Auf Grund dieser Definition folgen mit Hülfe der Axiomgruppen III — IV leicht die bekannten Sätze über den Kreis, insbesondere die Möglichkeit der Konstruktion eines Kreises durch irgend drei nicht in einer Geraden gelegene Punkte sowie der Satz über die Congruenz aller Peripheriewinkel über der nämlichen Sehne und der Satz von den Winkeln im Kreisviereck.

.. picture:: /_static/figures/fig_sas_supplementary.svg
   :alt: Eliminating Euclidean superposition: SAS congruence (Theorem 10) via Axiom IV 6 and supplementary angles (Theorem 12; cf. Heath on Euclid C.N. 4, folios 0243–0244).
   :caption: **Hilbert's SAS Reductio (Theorem 10) and Supplementary Angle Congruence (Theorem 12).** Eliminating Euclidean superposition: SAS congruence (Theorem 10) via Axiom IV 6 and supplementary angles (Theorem 12; cf. Heath on Euclid C.N. 4, folios 0243–0244).
