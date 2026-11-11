"""Diplomatic-critical RST parser for David Hilbert's 1899 Teubner Festschrift German edition."""

from __future__ import annotations

import re
from pathlib import Path

from geometor.hilbert.chapters_meta import SECTIONS_META, UNITS
from geometor.hilbert.concordance import default_repo_root

# Exact 1-indexed (start_body_line, end_body_line) in ia_grundlagendergeo00hilb_teubner_1899.txt
# Each start_body_line begins immediately AFTER the raw OCR section title lines.
SECTION_RANGES_DE: dict[int, tuple[int, int]] = {
    0: (92, 115),
    1: (126, 157),
    2: (163, 225),
    3: (229, 299),
    4: (303, 435),
    5: (439, 471),
    6: (475, 601),
    7: (605, 941),
    8: (947, 976),
    9: (986, 1117),
    10: (1121, 1181),
    11: (1188, 1284),
    12: (1291, 1373),
    13: (1382, 1498),
    14: (1502, 1772),
    15: (1776, 1943),
    16: (1947, 2060),
    17: (2064, 2197),
    18: (2206, 2281),
    19: (2285, 2374),
    20: (2378, 2536),
    21: (2540, 2678),
    22: (2688, 2782),
    23: (2788, 2954),
    24: (2960, 3033),
    25: (3040, 3113),
    26: (3121, 3351),
    27: (3355, 3499),
    28: (3503, 3551),
    29: (3557, 3691),
    30: (3695, 3737),
    31: (3746, 3783),
    32: (3789, 3874),
    33: (3881, 3995),
    34: (4001, 4039),
    35: (4045, 4110),
    36: (4122, 4244),
    37: (4248, 4339),
    38: (4345, 4535),
    39: (4541, 4705),
    40: (4711, 4765),
}

# Exact 1-indexed line-span restorations of engraved Teubner mathematical formulas,
# margin-wrapped figure labels, and footnote blocks in ia_grundlagendergeo00hilb_teubner_1899.txt.
LINE_SPAN_PATCHES: list[tuple[int, int, str]] = [
    # Einleitung footnote 1
    (98, 98, "Litteratur @@FN:0_1@@ sich erörtert findet. Die bezeichnete Aufgabe läuft"),
    (110, 113, ""),
    # § 1 list of 5 axiom groups & alpha, beta, gamma
    (131, 131, "$\\alpha, \\beta, \\gamma, \\dots$; die Punkte heissen auch die Elemente der linearen Geo-"),
    (
        147,
        155,
        ("\n* **I 1–7.** Axiome der *Verknüpfung*,\n"
        "* **II 1–5.** Axiome der *Anordnung*,\n"
        "* **III.** Axiom der *Parallelen* (*Euklidisches Axiom*),\n"
        "* **IV 1–6.** Axiome der *Congruenz*,\n"
        "* **V.** Axiom der *Stetigkeit* (*Archimedisches Axiom*).\n"),
    ),
    # § 2 alpha, beta, B != C, I 4, I 1-7
    (180, 181, "bestimmen diese Gerade, d. h. wenn $AB = a$ und $AC = a$, und $B \\neq C$, so ist auch $BC = a$."),
    (183, 199, (
        "**I 3.** Drei nicht auf ein und derselben Geraden liegende Punkte $A, B, C$ bestimmen stets eine Ebene $\\alpha$; wir setzen $ABC = \\alpha$.\n\n"
        "Wir gebrauchen auch die Wendungen: $A, B, C$ „liegen in“ $\\alpha$; $A, B, C$ „sind Punkte von“ $\\alpha$ u. s. w.\n\n"
        "**I 4.** Irgend drei Punkte $A, B, C$ einer Ebene $\\alpha$, die nicht auf ein und derselben Geraden liegen, bestimmen diese Ebene $\\alpha$.\n\n"
        "**I 5.** Wenn zwei Punkte $A, B$ einer Geraden $a$ in einer Ebene $\\alpha$ liegen, so liegt jeder Punkt von $a$ in $\\alpha$.\n\n"
        "In diesem Falle sagen wir: die Gerade $a$ liegt in der Ebene $\\alpha$ u. s. w.\n\n"
        "**I 6.** Wenn zwei Ebenen $\\alpha, \\beta$ einen Punkt $A$ gemein haben, so haben sie wenigstens noch einen weiteren Punkt $B$ gemein."
    )),
    (211, 211, "Von den Sätzen, die aus den Axiomen I 1–7 folgen, erwähne"),
    # § 3 Pasch footnote & wrapped Fig. 1, Fig. 2
    (229, 229, "Die Axiome dieser Gruppe @@FN:3_1@@ definiren den Begriff „zwischen“"),
    (
        237,
        262,
        ("**II 1.** Wenn $A, B, C$ Punkte einer Geraden sind, und $B$ zwischen $A$ und $C$ liegt, so liegt $B$ auch zwischen $C$ und $A$.\n\n"
        "**II 2.** Wenn $A$ und $C$ zwei Punkte einer Geraden sind, so giebt es stets wenigstens einen Punkt $B$, der zwischen $A$ und $C$ liegt und wenigstens einen Punkt $D$, so dass $C$ zwischen $A$ und $D$ liegt.\n\n"
        "**II 3.** Unter irgend drei Punkten einer Geraden giebt es stets einen und nur einen, der zwischen den beiden andern liegt.\n\n"
        "**II 4.** Irgend vier Punkte $A, B, C, D$ einer Geraden können stets so angeordnet werden, dass $B$ zwischen $A$ und $C$ und auch zwischen $A$ und $D$ und ferner $C$ zwischen $A$ und $D$ und auch zwischen $B$ und $D$ liegt."),
    ),
    (270, 272, ""),
    (289, 289, "der Strecke $AC$."),
    # § 4 wrapped Fig. 4, 5, 6, 7
    (
        311,
        322,
        "$A, B, C, D, E, \\dots, K$ anordnen, sodass $B$ zwischen $A$ einerseits und $C, D, E, \\dots, K$ andererseits, ferner $C$ zwischen $A, B$ einerseits und $D, E, \\dots, K$ andererseits, sodann $D$ zwischen $A, B, C$ einerseits und $E, \\dots, K$ andererseits u. s. w. liegt. Ausser dieser Anordnung giebt es nur noch die umgekehrte Anordnung $K, \\dots, E, D, C, B, A$, die von der nämlichen Beschaffenheit ist.",
    ),
    (324, 325, "Satz 5. Jede Gerade $a$, welche in einer Ebene $\\alpha$ liegt, trennt die übrigen Punkte dieser Ebene $\\alpha$ in zwei Gebiete, von folgender"),
    (
        336,
        344,
        "raden $a$ liegt; dagegen bestimmen irgend zwei Punkte $A$ und $A'$ ein und desselben Gebietes eine Strecke $AA'$, welche keinen Punkt von $a$ enthält.",
    ),
    (
        351,
        361,
        "$A, B$ liegen in der Geraden $a$ auf verschiedenen Seiten vom Punkte $O$. Die sämtlichen auf ein und derselben Seite von $O$ gelegenen Punkte der Geraden $a$ heissen auch ein von $O$ ausgehender *Halbstrahl*; somit trennt jeder Punkt einer Geraden diese in zwei Halbstrahlen.",
    ),
    (
        363,
        366,
        "Indem wir die Bezeichnungen des Satzes 5 benutzen, sagen wir: die Punkte $A, A'$ liegen in der Ebene $\\alpha$ auf ein und derselben Seite von der Geraden $a$ und die Punkte $A, B$ liegen in der Ebene $\\alpha$ auf verschiedenen Seiten von der Geraden $a$.",
    ),
    (402, 403, "Punkt des Aeusseren (äusserer Punkt), so hat jeder"),
    (413, 428, (
        "Streckenzüge, die $A$ mit $A'$ und $B$ mit $B'$ verbinden und keinen Punkt mit dem Polygon gemein haben. Es giebt Gerade in $\\alpha$, die ganz im Aeusseren des Polygons verlaufen, dagegen keine solche Gerade, die ganz im Inneren des Polygons verläuft.\n\n"
        "Satz 7. Jede Ebene $\\alpha$ trennt die übrigen Punkte des Raumes in zwei Gebiete von folgender Beschaffenheit: jeder Punkt $A$ des einen Gebietes bestimmt mit jedem Punkt $B$ des andern Gebietes eine Strecke $AB$, innerhalb derer ein Punkt von $\\alpha$ liegt; dagegen bestimmen irgend zwei Punkte $A$ und $A'$ eines und desselben Gebietes stets eine Strecke $AA'$, die keinen Punkt von $\\alpha$ enthält.\n\n"
        "Erklärung. Indem wir die Bezeichnungen dieses Satzes 7 benutzen, sagen wir: die Punkte $A, A'$ liegen im Raume auf ein und derselben Seite von der Ebene $\\alpha$ und die Punkte $A, B$ liegen im Raume auf verschiedenen Seiten von der Ebene $\\alpha$."
    )),
    # § 5 plane alpha
    (446, 453, (
        "**III.** In einer Ebene $\\alpha$ lässt sich durch einen Punkt $A$ ausserhalb einer Geraden $a$ stets eine und nur eine Gerade ziehen, welche jene Gerade $a$ nicht schneidet; dieselbe heisst die Parallele zu $a$ durch den Punkt $A$.\n\n"
        "Diese Fassung des Parallelenaxioms enthält zwei Aussagen; nach der ersteren giebt es in der Ebene $\\alpha$ durch $A$ stets eine Gerade, die $a$ nicht trifft, und zweitens wird ausgesprochen,"
    )),
    # § 6 congruence symbols & Fig. 8
    (
        482,
        493,
        "**IV 1.** Wenn $A, B$ zwei Punkte auf einer Geraden $a$ und ferner $A'$ ein Punkt auf derselben oder einer anderen Geraden $a'$ ist, so kann man auf einer gegebenen Seite der Geraden $a'$ von $A'$ stets einen und nur einen Punkt $B'$ finden, so dass die Strecke $AB$ (oder $BA$) der Strecke $A'B'$ congruent ist, in Zeichen:\n\n$$\nAB \\equiv A'B'.\n$$\n\nJede Strecke ist sich selbst congruent, d. h. es ist stets:\n\n$$\nAB \\equiv AB.\n$$",
    ),
    (
        502,
        522,
        ("**IV 2.** Wenn eine Strecke $AB$ sowohl der Strecke $A'B'$ als auch der Strecke $A''B''$ congruent ist, so ist auch $A'B'$ der Strecke $A''B''$ congruent, d. h.: wenn $AB \\equiv A'B'$ und $AB \\equiv A''B''$, so ist auch $A'B' \\equiv A''B''$.\n\n"
        "**IV 3.** Es seien $AB$ und $BC$ zwei Strecken ohne gemeinsame Punkte auf der Geraden $a$ und ferner $A'B'$ und $B'C'$ zwei Strecken auf derselben oder einer anderen Geraden $a'$ ebenfalls ohne gemeinsame Punkte; wenn dann $AB \\equiv A'B'$ und $BC \\equiv B'C'$ ist, so ist auch stets $AC \\equiv A'C'$."),
    ),
    (523, 530, (
        "Definition. Es sei $\\alpha$ eine beliebige Ebene und $h, k$ seien irgend zwei verschiedene von einem Punkte $O$ ausgehende Halbstrahlen in $\\alpha$, die verschiedenen Geraden angehören. Das System dieser beiden Halbstrahlen $h, k$ nennen wir einen *Winkel* und bezeichnen denselben mit $\\angle(h, k)$ oder $\\angle(k, h)$. Aus den Axiomen II 1–5 kann leicht geschlossen werden, dass die Halbstrahlen $h$ und $k$, zusammengenommen mit dem Punkt $O$ die übrigen Punkte der Ebene $\\alpha$ in zwei Gebiete von folgender Beschaffen-"
    )),
    (
        546,
        590,
        ("**IV 4.** Es sei ein Winkel $\\angle(h, k)$ in einer Ebene $\\alpha$ und eine Gerade $a'$ in einer Ebene $\\alpha'$, sowie eine bestimmte Seite von $a'$ auf $\\alpha'$ gegeben. Es bedeute $h'$ einen Halbstrahl der Geraden $a'$, der vom Punkte $O'$ ausgeht: dann giebt es in der Ebene $\\alpha'$ einen und nur einen Halbstrahl $k'$, so dass der Winkel $(h, k)$ (oder $(k, h)$) congruent dem Winkel $(h', k')$ ist und zugleich alle inneren Punkte des Winkels $(h', k')$ auf der gegebenen Seite von $a'$ liegen, in Zeichen:\n\n$$\n\\angle(h, k) \\equiv \\angle(h', k').\n$$\n\nJeder Winkel ist sich selbst congruent, d. h. es ist stets\n\n$$\n\\angle(h, k) \\equiv \\angle(h, k).\n$$\n\n"
        "Wir sagen auch kurz, dass ein jeder Winkel in einer gegebenen Ebene nach einer gegebenen Seite an einen gegebenen Halbstrahl auf eine eindeutig bestimmte Weise abgetragen werden kann.\n\n"
        "**IV 5.** Wenn ein Winkel $(h, k)$ sowohl dem Winkel $(h', k')$ als auch dem Winkel $(h'', k'')$ congruent ist, so ist auch der Winkel $(h', k')$ dem Winkel $(h'', k'')$ congruent, d. h. wenn $\\angle(h, k) \\equiv \\angle(h', k')$ und $\\angle(h, k) \\equiv \\angle(h'', k'')$ ist, so ist auch stets $\\angle(h', k') \\equiv \\angle(h'', k'')$.\n\n"
        "Erklärung. Es sei ein Dreieck $ABC$ vorgelegt; wir bezeichnen die beiden von $A$ ausgehenden durch $B$ und $C$ laufenden Halbstrahlen mit $h$ bez. $k$. Der Winkel $(h, k)$ heisst dann der von den Seiten $AB$ und $AC$ eingeschlossene oder der der Seite $BC$ gegenüberliegende Winkel des Dreieckes $ABC$; er enthält in seinem Inneren sämtliche innere Punkte des Dreieckes $ABC$ und wird mit $\\angle BAC$ oder $\\angle A$ bezeichnet.\n\n"
        "**IV 6.** Wenn für zwei Dreiecke $ABC$ und $A'B'C'$ die Congruenzen\n\n$$\nAB \\equiv A'B', \\quad AC \\equiv A'C', \\quad \\angle BAC \\equiv \\angle B'A'C'\n$$\n\ngelten, so sind auch stets die Congruenzen\n\n$$\n\\angle ABC \\equiv \\angle A'B'C' \\quad \\text{und} \\quad \\angle ACB \\equiv \\angle A'C'B'\n$$\n\nerfüllt."),
    ),
    # § 7 congruences, Satz 10-18, missing formula L805, Fig. 9-12 noise
    (
        614,
        637,
        ("Erklärung. Sind $A, B, C, D, \\dots, K, L$ auf $a$ und $A', B', C', D', \\dots, K', L'$ auf $a'$ zwei Reihen von Punkten, so dass die sämtlichen entsprechenden Strecken $AB$ und $A'B'$, $AC$ und $A'C'$, $BC$ und $B'C'$, $\\dots$, $KL$ und $K'L'$ bez. einander congruent sind, so heissen die beiden Reihen von Punkten *unter einander congruent*; $A$ und $A'$, $B$ und $B'$, $\\dots$, $L$ und $L'$ heissen die *entsprechenden Punkte* der congruenten Punktreihen.\n\n"
        "Aus den linearen Axiomen IV 1–3 schliessen wir leicht folgende Sätze:\n\n"
        "Satz 9. Ist von zwei congruenten Punktreihen $A, B, \\dots, K, L$ und $A', B', \\dots, K', L'$ die erste so geordnet, dass $B$ zwischen $A$ einerseits und $C, D, \\dots, K, L$ andererseits, $C$ zwischen $A, B$ einerseits und $D, \\dots, K, L$ andererseits, u. s. w. liegt, so sind die Punkte $A', B', \\dots, K', L'$ auf die gleiche Weise geordnet, d. h. $B'$ liegt zwischen $A'$ einerseits und $C', D', \\dots, K', L'$ andererseits, $C'$ zwischen $A', B'$ einerseits und $D', \\dots, K', L'$ andererseits u. s. w.\n\n"
        "Erklärung. Es sei Winkel $(h, k)$ congruent dem Winkel $(h', k')$. Da nach Axiom IV 4 der Winkel $(h, k)$ congruent $\\angle(h, k)$ ist, so folgt aus Axiom IV 5, dass $\\angle(h', k')$ congruent $\\angle(h, k)$ ist; wir sagen: die beiden Winkel $(h, k)$ und $(h', k')$ sind *unter einander congruent*."),
    ),
    (
        646,
        751,
        ("Erklärung. Zwei Dreiecke $ABC$ und $A'B'C'$ heissen einander *congruent*, wenn sämtliche Congruenzen\n\n$$\n\\begin{aligned}\nAB &\\equiv A'B', & AC &\\equiv A'C', & BC &\\equiv B'C', \\\\\n\\angle A &\\equiv \\angle A', & \\angle B &\\equiv \\angle B', & \\angle C &\\equiv \\angle C'\n\\end{aligned}\n$$\n\nerfüllt sind.\n\n"
        "Satz 10 (Erster Congruenzsatz für Dreiecke). Wenn für zwei Dreiecke $ABC$ und $A'B'C'$ die Congruenzen\n\n$$\nAB \\equiv A'B', \\quad AC \\equiv A'C', \\quad \\angle A \\equiv \\angle A'\n$$\n\ngelten, so sind die beiden Dreiecke einander congruent.\n\n"
        "Beweis. Nach Axiom IV 6 sind die Congruenzen\n\n$$\n\\angle B \\equiv \\angle B' \\quad \\text{und} \\quad \\angle C \\equiv \\angle C'\n$$\n\nerfüllt und es bedarf somit nur des Nachweises, dass die Seiten $BC$ und $B'C'$ einander congruent sind. Nehmen wir nun im Gegenteil an, es wäre etwa $BC$ nicht congruent $B'C'$ und bestimmen auf $B'C'$ den Punkt $D'$, so dass $BC \\equiv B'D'$ wird, so stimmen die beiden Dreiecke $ABC$ und $A'B'D'$ in zwei Seiten und dem von ihnen eingeschlossenen Winkel überein; nach Axiom IV 6 sind mithin insbesondere die beiden Winkel $\\angle BAC$ und $\\angle B'A'D'$ einander congruent. Nach Axiom IV 5 müssten mithin auch die beiden Winkel $\\angle B'A'C'$ und $\\angle B'A'D'$ einander congruent ausfallen; dies ist nicht möglich, da nach Axiom IV 4 ein jeder Winkel an einen gegebenen Halbstrahl nach einer gegebenen Seite in einer Ebene nur auf eine Weise abgetragen werden kann. Damit ist der Beweis für Satz 10 vollständig erbracht.\n\n"
        "Ebenso leicht beweisen wir die weitere Thatsache:\n\n"
        "Satz 11 (Zweiter Congruenzsatz für Dreiecke). Wenn in zwei Dreiecken je eine Seite und die beiden anliegenden Winkel congruent ausfallen, so sind die Dreiecke stets congruent.\n\n"
        "Wir sind nunmehr im Stande, die folgenden wichtigen Thatsachen zu beweisen:\n\n"
        "Satz 12. Wenn zwei Winkel $\\angle ABC$ und $\\angle A'B'C'$ einander congruent sind, so sind auch ihre Nebenwinkel $\\angle CBD$ und $\\angle C'B'D'$ einander congruent.\n\n"
        "Beweis. Wir wählen die Punkte $A', C', D'$ auf den durch $B'$ gehenden Schenkeln derart, dass\n\n$$\nA'B' \\equiv AB, \\quad C'B' \\equiv CB, \\quad D'B' \\equiv DB\n$$\n\nwird. In den beiden Dreiecken $ABC$ und $A'B'C'$ sind dann die Seiten $AB$ und $CB$ bez. den Seiten $A'B'$ und $C'B'$ congruent und, da überdies die von diesen Seiten eingeschlossenen Winkel nach Voraussetzung einander congruent sein sollen, so folgt nach Satz 10 die Congruenz jener Dreiecke, d. h. es gelten die Congruenzen\n\n$$\nAC \\equiv A'C' \\quad \\text{und} \\quad \\angle BAC \\equiv \\angle B'A'C'.\n$$\n\nDa andererseits nach Axiom IV 3 die Strecken $AD$ und $A'D'$ einander congruent sind, so folgt wiederum aus Satz 10 die Congruenz der Dreiecke $CAD$ und $C'A'D'$, d. h. es gelten die Congruenzen\n\n$$\nCD \\equiv C'D' \\quad \\text{und} \\quad \\angle ADC \\equiv \\angle A'D'C'\n$$\n\nund hieraus folgt mittels Betrachtung der Dreiecke $BCD$ und $B'C'D'$ nach Axiom IV 6 die Congruenz der Winkel $\\angle CBD$ und $\\angle C'B'D'$."),
    ),
    (
        755,
        858,
        ("Satz 13. Es sei der Winkel $(h, k)$ in der Ebene $\\alpha$ dem Winkel $(h', k')$ in der Ebene $\\alpha'$ congruent und ferner sei $l$ ein Halbstrahl der Ebene $\\alpha$, der vom Scheitel des Winkels $(h, k)$ ausgeht und im Inneren dieses Winkels verläuft: dann giebt es stets einen Halbstrahl $l'$ in der Ebene $\\alpha'$, der vom Scheitel des Winkels $(h', k')$ ausgeht, und im Inneren dieses Winkels $(h', k')$ verläuft, so dass\n\n$$\n\\angle(h, l) \\equiv \\angle(h', l') \\quad \\text{und} \\quad \\angle(k, l) \\equiv \\angle(k', l')\n$$\n\nwird.\n\n"
        "Beweis. Wir bezeichnen die Scheitel der Winkel $(h, k)$ und $(h', k')$ bez. mit $O, O'$ und bestimmen dann auf den Schenkeln $h, k, h', k'$ die Punkte $A, B, A', B'$ derart, dass die Congruenzen\n\n$$\nOA \\equiv O'A' \\quad \\text{und} \\quad OB \\equiv O'B'\n$$\n\nerfüllt sind. Wegen der Congruenz der Dreiecke $OAB$ und $O'A'B'$ wird\n\n$$\nAB \\equiv A'B', \\quad \\angle OAB \\equiv \\angle O'A'B', \\quad \\angle OBA \\equiv \\angle O'B'A'.\n$$\n\nDie Gerade $AB$ schneide $l$ in $C$; bestimmen wir dann auf der Strecke $A'B'$ den Punkt $C'$, so dass $A'C' \\equiv AC$ wird, so ist $O'C'$ der gesuchte Halbstrahl $l'$. In der That, aus $AC \\equiv A'C'$ und $AB \\equiv A'B'$ kann mittelst Axiom IV 3 leicht die Congruenz $BC \\equiv B'C'$ geschlossen werden; nunmehr erweisen sich die Dreiecke $OAC$ und $O'A'C'$, sowie ferner die Dreiecke $OBC$ und $O'B'C'$ unter einander congruent; hieraus ergeben sich die Behauptungen des Satzes 13.\n\n"
        "Auf ähnliche Art gelangen wir zu folgender Thatsache:\n\n"
        "Satz 14. Es seien einerseits $h, k, l$ und andererseits $h', k', l'$ je drei von einem Punkte ausgehende und je in einer Ebene gelegene Halbstrahlen: wenn dann die Congruenzen\n\n$$\n\\angle(h, l) \\equiv \\angle(h', l') \\quad \\text{und} \\quad \\angle(k, l) \\equiv \\angle(k', l')\n$$\n\nerfüllt sind, so ist stets auch\n\n$$\n\\angle(h, k) \\equiv \\angle(h', k').\n$$\n\n"
        "Auf Grund der Sätze 12 und 13 gelingt der Nachweis des folgenden einfachen Satzes, den Euklid — meiner Meinung nach mit Unrecht — unter die Axiome gestellt hat:\n\n"
        "Satz 15. Alle rechten Winkel sind einander congruent.\n\n"
        "Beweis. Der Winkel $BAD$ sei seinem Nebenwinkel $CAD$ congruent und desgleichen sei der Winkel $B'A'D'$ seinem Nebenwinkel $C'A'D'$ congruent; es sind dann $\\angle BAD, \\angle CAD, \\angle B'A'D', \\angle C'A'D'$ sämtlich rechte Winkel. Wir nehmen im Gegensatz zu unserer Behauptung an, es wäre der rechte Winkel $B'A'D'$ nicht congruent dem rechten Winkel $BAD$ und tragen dann $\\angle B'A'D'$ an den Halbstrahl $AB$ an, so dass der entstehende Schenkel $AD''$ entweder in das Innere des Winkels $BAD$ oder des Winkels $CAD$ fällt; es treffe etwa die erstere Möglichkeit zu. Wegen der Congruenz der Winkel $B'A'D'$ und $BAD''$ folgt nach Satz 12, dass auch der Winkel $C'A'D'$ dem Winkel $CAD''$ congruent ist, und da die Winkel $B'A'D'$ und $C'A'D'$ einander congruent sein sollen, so lehrt Axiom IV 5, dass auch der Winkel $BAD''$ dem Winkel $CAD''$ congruent sein muss. Da ferner $\\angle BAD$ congruent $\\angle CAD$ ist, so können wir nach Satz 13 innerhalb des Winkels $CAD$ einen von $A$ ausgehenden Halbstrahl $AD'''$ finden, so dass $\\angle BAD''$ congruent $\\angle CAD'''$ und zugleich $\\angle DAD''$ congruent $\\angle DAD'''$ wird. Nun war aber $\\angle BAD''$ congruent $\\angle CAD''$ und somit müsste nach Axiom IV 5 auch $\\angle CAD''$ congruent $\\angle CAD'''$ sein; das ist nicht möglich, weil nach Axiom IV 4 ein jeder Winkel an einen gegebenen Halbstrahl nach einer gegebenen Seite in einer Ebene nur auf eine Weise abgetragen werden kann; hiermit ist der Beweis für Satz 15 erbracht.\n\n"
        "Wir können jetzt die Bezeichnungen „spitzer Winkel“ und „stumpfer Winkel“ in bekannter Weise einführen.\n\n"
        "Der Satz von der Congruenz der Basiswinkel $\\angle A$ und $\\angle B$"),
    ),
    (
        894,
        908,
        ("Satz 17. Wenn $(A, B, C, \\dots)$ und $(A', B', C', \\dots)$ congruente ebene Figuren sind und $P$ einen Punkt in der Ebene der ersten bedeutet, so lässt sich in der Ebene der zweiten Figur stets ein Punkt $P'$ finden derart, dass $(A, B, C, \\dots, P)$ und $(A', B', C', \\dots, P')$ wieder congruente Figuren sind. Enthalten die beiden Figuren wenigstens drei nicht auf einer Geraden liegende Punkte, so ist die Construction von $P'$ nur auf eine Weise möglich.\n\n"
        "Satz 18. Wenn $(A, B, C, \\dots)$ und $(A', B', C', \\dots)$ congruente Figuren sind und $P$ einen beliebigen Punkt bedeutet, so lässt sich stets ein Punkt $P'$ finden, so dass die Figuren $(A, B, C, \\dots, P)$ und $(A', B', C', \\dots, P')$ congruent sind. Enthält die Figur $(A, B, C, \\dots)$ mindestens vier nicht in einer Ebene liegende Punkte, so ist die Construction von $P'$ nur auf eine Weise möglich."),
    ),
    (928, 928, "Definition. Wenn $M$ ein beliebiger Punkt in einer Ebene $\\alpha$"),
    # § 8 Archimedes subscripts & Fig. 13 noise
    (
        959,
        975,
        "**V.** Es sei $A_1$ ein beliebiger Punkt auf einer Geraden zwischen den beliebig gegebenen Punkten $A$ und $B$; man construire dann die Punkte $A_2, A_3, A_4, \\dots$, so dass $A_1$ zwischen $A$ und $A_2$, ferner $A_2$ zwischen $A_1$ und $A_3$, ferner $A_3$ zwischen $A_2$ und $A_4$ u. s. w. liegt und überdies die Strecken\n\n$$\nAA_1, \\quad A_1A_2, \\quad A_2A_3, \\quad A_3A_4, \\quad \\dots\n$$\n\neinander gleich sind: dann giebt es in der Reihe der Punkte $A_2, A_3, A_4, \\dots$ stets einen solchen Punkt $A_n$, dass $B$ zwischen $A$ und $A_n$ liegt.\n\nDas Archimedische Axiom ist ein lineares Axiom.",
    ),
    # § 9 Omega domain & rotation formulas
    (
        999,
        1116,
        ("Man betrachte den Bereich $\\Omega$ aller derjenigen algebraischen Zahlen, welche hervorgehen, indem man von der Zahl $1$ ausgeht und eine endliche Anzahl von Malen die vier Rechnungsoperationen: Addition, Subtraktion, Multiplikation, Division und die fünfte Operation $\\sqrt{1 + \\omega^2}$ anwendet, wobei $\\omega$ jedesmal eine Zahl bedeuten kann, die vermöge jener fünf Operationen bereits entstanden ist.\n\n"
        "Wir denken uns ein Paar von Zahlen $(x, y)$ des Bereiches $\\Omega$ als einen Punkt und die Verhältnisse von irgend drei Zahlen $(u : v : w)$ aus $\\Omega$, falls $u, v$ nicht beide Null sind, als eine Gerade; ferner möge das Bestehen der Gleichung\n\n$$\nux + vy + w = 0\n$$\n\nausdrücken, dass der Punkt $(x, y)$ auf der Geraden $(u : v : w)$ liegt; damit sind, wie man leicht sieht, die Axiome I 1–2 und III erfüllt. Die Zahlen des Bereiches $\\Omega$ sind sämtlich reell; indem wir berücksichtigen, dass dieselben sich ihrer Grösse nach anordnen lassen, können wir leicht solche Festsetzungen für unsere Punkte und Geraden treffen, dass auch die Axiome II der Anordnung sämtlich gültig sind. In der That, sind $(x_1, y_1), (x_2, y_2), (x_3, y_3), \\dots$ irgend welche Punkte auf einer Geraden, so möge dies ihre Reihenfolge auf der Geraden sein, wenn die Zahlen $x_1, x_2, x_3, \\dots$ oder $y_1, y_2, y_3, \\dots$ in dieser Reihenfolge entweder beständig abnehmen oder wachsen; um ferner die Forderung des Axioms II 5 zu erfüllen, haben wir nur nöthig festzusetzen, dass alle Punkte $(x, y)$, für die $ux + vy + w$ kleiner oder grösser als $0$ ausfällt, auf der einen bez. auf der anderen Seite der Geraden $(u : v : w)$ gelegen sein sollen. Man überzeugt sich leicht, dass diese Festsetzung sich mit der vorigen Festsetzung in Uebereinstimmung befindet, derzufolge ja die Reihenfolge der Punkte auf einer Geraden bereits bestimmt ist.\n\n"
        "Das Abtragen von Strecken und Winkeln erfolgt nach den bekannten Methoden der analytischen Geometrie. Eine Transformation von der Gestalt\n\n$$\n\\begin{aligned}\nx' &= x + a, \\\\\ny' &= y + b\n\\end{aligned}\n$$\n\nvermittelt die Parallelverschiebung von Strecken und Winkeln. Wird ferner der Punkt $(0, 0)$ mit $O$, der Punkt $(1, 0)$ mit $E$ und ein beliebiger Punkt $(a, b)$ mit $C$ bezeichnet, so entsteht durch Drehung um den Winkel $\\angle COE$, wenn $O$ der feste Drehpunkt ist, aus dem beliebigen Punkte $(x, y)$ der Punkt $(x', y')$, wobei\n\n$$\n\\begin{aligned}\nx' &= \\frac{a}{\\sqrt{a^2 + b^2}} x - \\frac{b}{\\sqrt{a^2 + b^2}} y, \\\\\ny' &= \\frac{b}{\\sqrt{a^2 + b^2}} x + \\frac{a}{\\sqrt{a^2 + b^2}} y\n\\end{aligned}\n$$\n\nzu setzen ist. Da die Zahl\n\n$$\n\\sqrt{a^2 + b^2} = a\\sqrt{1 + \\left(\\frac{b}{a}\\right)^2}\n$$\n\nwiederum dem Bereiche $\\Omega$ angehört, so gelten bei unseren Festsetzungen auch die Congruenzaxiome IV und offenbar ist auch das Archimedische Axiom V erfüllt.\n\n"
        "Wir schliessen hieraus, dass jeder Widerspruch in den Folgerungen aus unseren Axiomen auch in der Arithmetik des Bereiches $\\Omega$ erkennbar sein müsste.\n\n"
        "Die entsprechende Betrachtungsweise für die räumliche Geometrie bietet keine Schwierigkeit.\n\n"
        "Wählen wir in der obigen Entwickelung statt des Bereiches $\\Omega$ den Bereich aller reellen Zahlen, so erhalten wir ebenfalls eine Geometrie, in der sämtliche Axiome I–V gültig sind. Für unseren Beweis genügte die Zuhülfenahme des Bereiches $\\Omega$, der nur eine abzählbare Menge von Elementen enthält."),
    ),
    # § 10 footnote 1 & congruences
    (1129, 1133, "Axiome ein und derselben Gruppe je unter sich unabhängig sind @@FN:10_1@@."),
    (
        1147,
        1161,
        "anderer Punkt der Geraden $a$; dann tragen wir $\\angle ABC$ an $AB$ im Punkte $A$ nach derjenigen Seite in der nämlichen Ebene $\\alpha$ an, auf der nicht der Punkt $C$ liegt. Die so erhaltene Gerade durch $A$ trifft die Gerade $a$ nicht. In der That, schnitte sie $a$ im Punkte $D$ und nehmen wir etwa an, dass $B$ zwischen $C$ und $D$ liege, so könnten wir auf $a$ einen Punkt $D'$ finden, so dass $B$ zwischen $D$ und $D'$ liegt und überdies\n\n$$\nAD \\equiv BD'\n$$\n\nausfiele. Wegen der Congruenz der Dreiecke $ABD$ und $BAD'$ würde die Congruenz\n\n$$\n\\angle ABD \\equiv \\angle BAD'\n$$",
    ),
    # § 11 formulas & 4 points O, A, B, C
    (
        1199,
        1278,
        ("andere Art. Die zwei Punkte $A_1, A_2$ mögen in der gewöhnlichen Geometrie die Coordinaten $x_1, y_1, z_1$ bez. $x_2, y_2, z_2$ haben; dann bezeichnen wir den positiven Wert von\n\n$$\n\\sqrt{(x_1 - x_2 + y_1 - y_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}\n$$\n\nals die *Länge* der Strecke $A_1A_2$ und nun sollen zwei beliebige Strecken $A_1A_2$ und $A'_1A'_2$ einander congruent heissen, wenn sie im eben festgesetzten Sinne gleiche Längen haben.\n\n"
        "Es leuchtet unmittelbar ein, dass in der so hergestellten räumlichen Geometrie die Axiome I, II, III, IV 1–2, 4–5, V gültig sind.\n\n"
        "Um zu zeigen, dass auch das Axiom IV 3 erfüllt ist, wählen wir eine beliebige Gerade $a$ und auf ihr drei Punkte $A_1, A_2, A_3$, sodass $A_2$ zwischen $A_1$ und $A_3$ liegt. Die Punkte $x, y, z$ der Geraden $a$ seien durch die Gleichungen\n\n$$\nx = \\lambda t + \\lambda', \\quad y = \\mu t + \\mu', \\quad z = \\nu t + \\nu'\n$$\n\ngegeben, worin $\\lambda, \\lambda', \\mu, \\mu', \\nu, \\nu'$ gewisse Constante und $t$ einen Parameter bedeutet. Sind $t_1, t_2 \\; (< t_1), t_3 \\; (< t_2)$ die Parameterwerte, die den Punkten $A_1, A_2, A_3$ entsprechen, so finden wir für die Längen der drei Strecken $A_1A_2$, $A_2A_3$ und $A_1A_3$ bez. die Ausdrücke:\n\n$$\n(t_1 - t_2)|\\sqrt{(\\lambda + \\mu)^2 + \\mu^2 + \\nu^2}|, \\quad (t_2 - t_3)|\\sqrt{(\\lambda + \\mu)^2 + \\mu^2 + \\nu^2}|, \\quad (t_1 - t_3)|\\sqrt{(\\lambda + \\mu)^2 + \\mu^2 + \\nu^2}|,\n$$\n\nund mithin ist die Summe der Längen der Strecken $A_1A_2$ und $A_2A_3$ gleich der Länge der Strecke $A_1A_3$; dieser Umstand bedingt die Gültigkeit des Axioms IV 3.\n\n"
        "Das Axiom IV 6 oder vielmehr der erste Congruenzsatz für Dreiecke ist in unserer Geometrie nicht immer erfüllt. Betrachten wir nämlich in der Ebene $z = 0$ die vier Punkte\n\n"
        "| $O$ mit den Coordinaten $x = 0, \\quad y = 0$,\n"
        "| $A$ mit den Coordinaten $x = 1, \\quad y = 0$,\n"
        "| $B$ mit den Coordinaten $x = 0, \\quad y = 1$,\n"
        "| $C$ mit den Coordinaten $x = \\frac{1}{2}, \\quad y = \\frac{1}{2}$,\n\n"
        "so sind in den beiden (rechtwinkligen) Dreiecken $OAC$ und $OBC$ die Winkel bei $C$ und die anliegenden Seiten entsprechend congruent, da die Seite $OC$ beiden Dreiecken gemeinsam ist und die Strecken $AC$ und $BC$ die gleiche Länge $\\frac{1}{2}$ besitzen. Dagegen haben die dritten Seiten $OA$ und $OB$ die Länge $1$, bez. $\\sqrt{2}$ und sind daher nicht einander congruent."),
    ),
    # § 12 Omega(t) & footnote 1
    (
        1293,
        1368,
        ("Axiome mit Ausnahme des Archimedischen Axioms erfüllt sind @@FN:12_1@@.\n\n"
        "Zu dem Zwecke construiren wir den Bereich $\\Omega(t)$ aller derjenigen algebraischen Funktionen von $t$, welche aus $t$ durch die vier Rechnungsoperationen der Addition, Subtraktion, Multiplikation, Division und durch die fünfte Operation $\\sqrt{1 + \\omega^2}$ hervorgehen; dabei soll $\\omega$ irgend eine Funktion bedeuten, die vermöge jener fünf Operationen bereits entstanden ist. Die Menge der Elemente von $\\Omega(t)$ ist — ebenso wie von $\\Omega$ — eine abzählbare. Die fünf Operationen sind sämtlich eindeutig und reell ausführbar; der Bereich $\\Omega(t)$ enthält daher nur eindeutige und reelle Funktionen von $t$.\n\n"
        "Es sei $c$ irgend eine Funktion des Bereiches $\\Omega(t)$; da die Funktion $c$ eine algebraische Funktion von $t$ ist, so kann sie jedenfalls nur für eine endliche Anzahl von Werten $t$ verschwinden und es wird daher die Funktion $c$ für genügend grosse positive Werte von $t$ entweder stets positiv oder stets negativ ausfallen.\n\n"
        "Wir sehen jetzt die Funktionen des Bereiches $\\Omega(t)$ als eine Art complexer Zahlen an; offenbar sind in dem so definirten complexen Zahlensystem die gewöhnlichen Rechnungsregeln sämtlich gültig. Ferner möge, wenn $a, b$ irgend zwei verschiedene Zahlen dieses complexen Zahlensystems sind, die Zahl $a$ grösser oder kleiner als $b$, in Zeichen: $a > b$ oder $a < b$, heissen, je nachdem die Differenz $c = a - b$ als Funktion von $t$ für genügend grosse positive Werte von $t$ stets positiv oder stets negativ ausfällt. Bei dieser Festsetzung ist für die Zahlen unseres complexen Zahlensystems eine Anordnung ihrer Grösse nach möglich, die von der gewöhnlichen Art wie bei reellen Zahlen ist; auch gelten, wie man leicht erkennt, für unsere complexen Zahlen die Sätze, wonach Ungleichungen richtig bleiben, wenn man auf beiden Seiten die gleiche Zahl addirt oder beide Seiten mit der gleichen Zahl $> 0$ multiplicirt.\n\n"
        "Bedeutet $n$ eine beliebige positive ganze rationale Zahl, so gilt für die beiden Zahlen $n$ und $t$ des Bereiches $\\Omega(t)$ gewiss die Ungleichung $n < t$, da die Differenz $n - t$, als Funktion von $t$ betrachtet, für genügend grosse positive Werte von $t$ offenbar stets negativ ausfällt. Wir sprechen diese Thatsache in folgender Weise aus: die beiden Zahlen $1$ und $t$ des Bereiches $\\Omega(t)$, die beide $> 0$ sind, besitzen die Eigenschaft, dass ein beliebiges Vielfaches der ersteren stets kleiner als die letztere Zahl bleibt.\n\n"
        "Wir bauen nun aus den complexen Zahlen des Bereiches $\\Omega(t)$ eine Geometrie genau auf dieselbe Art auf, wie dies in § 9 unter Zugrundelegung des Bereiches $\\Omega$ von algebraischen Zahlen geschehen ist: wir denken uns ein System von drei Zahlen $(x, y, z)$ des Bereiches $\\Omega(t)$ als einen Punkt und die Verhältnisse von irgend vier Zahlen $(u : v : w : r)$ aus $\\Omega(t)$, falls $u, v, w$ nicht sämtlich Null sind, als eine Ebene; ferner möge das Bestehen der Gleichung\n\n$$\nux + vy + wz + r = 0\n$$\n\nausdrücken, dass der Punkt $(x, y, z)$ in der Ebene $(u : v : w : r)$ liegt und die Gerade sei die Gesamtheit aller in zwei Ebenen gelegenen Punkte. Treffen wir sodann die entsprechenden Festsetzungen über die Anordnung der Elemente und über Abtragen von Strecken und Winkeln, wie in § 9, so entsteht eine „*Nicht-Archimedische*“ Geometrie, in welcher, wie die zuvor erörterten Eigenschaften des complexen Zahlensystems $\\Omega(t)$ zeigen, sämtliche Axiome mit Ausnahme des Archimedischen Axioms erfüllt sind."),
    ),
    # § 13 complex number systems rules 1-17
    (
        1390,
        1496,
        ("**Sätze der Verknüpfung (1–12):**\n\n"
        "**1.** Aus der Zahl $a$ und der Zahl $b$ entsteht durch „Addition“ eine bestimmte Zahl $c$, in Zeichen\n\n$$\na + b = c \\quad \\text{oder} \\quad c = a + b.\n$$\n\n"
        "**2.** Es giebt eine bestimmte Zahl — sie heisse $0$ —, so dass für jedes $a$ zugleich\n\n$$\na + 0 = a \\quad \\text{und} \\quad 0 + a = a\n$$\n\nist.\n\n"
        "**3.** Wenn $a$ und $b$ gegebene Zahlen sind, so existirt stets eine und nur eine Zahl $x$ und auch eine und nur eine Zahl $y$, so dass\n\n$$\na + x = b \\quad \\text{bez.} \\quad y + a = b\n$$\n\nwird.\n\n"
        "**4.** Aus der Zahl $a$ und der Zahl $b$ entsteht noch auf eine andere Art durch „Multiplikation“ eine bestimmte Zahl $c$, in Zeichen\n\n$$\nab = c \\quad \\text{oder} \\quad c = ab.\n$$\n\n"
        "**5.** Es giebt eine bestimmte Zahl — sie heisse $1$ —, so dass für jedes $a$ zugleich\n\n$$\na \\cdot 1 = a \\quad \\text{und} \\quad 1 \\cdot a = a\n$$\n\nist.\n\n"
        "**6.** Wenn $a$ und $b$ beliebig gegebene Zahlen sind und $a$ nicht $0$ ist, so existirt stets eine und nur eine Zahl $x$ und auch eine und nur eine Zahl $y$, so dass\n\n$$\nax = b \\quad \\text{bez.} \\quad ya = b\n$$\n\nwird.\n\n"
        "Wenn $a, b, c$ beliebige Zahlen sind, so gelten stets folgende Rechnungsgesetze:\n\n"
        "$$\n\\begin{aligned}\n"
        "\\mathbf{7.}\\quad a + (b + c) &= (a + b) + c \\\\\n"
        "\\mathbf{8.}\\quad a + b &= b + a \\\\\n"
        "\\mathbf{9.}\\quad a(bc) &= (ab)c \\\\\n"
        "\\mathbf{10.}\\quad a(b + c) &= ab + ac \\\\\n"
        "\\mathbf{11.}\\quad (a + b)c &= ac + bc \\\\\n"
        "\\mathbf{12.}\\quad ab &= ba.\n"
        "\\end{aligned}\n$$\n\n"
        "**Sätze der Anordnung (13–16):**\n\n"
        "**13.** Wenn $a, b$ irgend zwei verschiedene Zahlen sind, so ist stets eine bestimmte von ihnen (etwa $a$) grösser ($>$) als die andere; die letztere heisst dann die kleinere, in Zeichen:\n\n$$\na > b \\quad \\text{und} \\quad b < a.\n$$\n\n"
        "**14.** Wenn $a > b$ und $b > c$, so ist auch $a > c$.\n\n"
        "**15.** Wenn $a > b$ ist, so ist auch stets\n\n$$\na + c > b + c \\quad \\text{und} \\quad c + a > c + b.\n$$\n\n"
        "**16.** Wenn $a > b$ und $c > 0$ ist, so ist auch stets\n\n$$\nac > bc \\quad \\text{und} \\quad ca > cb.\n$$\n\n"
        "**Archimedischer Satz (17):**\n\n"
        "**17.** Wenn $a > 0$ und $b > 0$ zwei beliebige Zahlen sind, so ist es stets möglich, $a$ zu sich selbst so oft zu addiren, dass die entstehende Summe die Eigenschaft hat\n\n$$\na + a + \\dots + a > b.\n$$\n\n"
        "Ein System von Dingen, das nur einen Teil der Eigenschaften 1–17 besitzt, heisse ein *complexes Zahlensystem* oder auch ein *Zahlensystem* schlechthin. Ein Zahlensystem heisse ein *Archimedisches* oder ein *Nicht-Archimedisches*, jenachdem dasselbe der Forderung 17 genügt oder nicht.\n\n"
        "Von den aufgestellten Eigenschaften 1–17 sind einige Folgen der übrigen. Es entsteht die Aufgabe, die logische Abhängigkeit dieser Eigenschaften zu untersuchen. Wir werden in Kapitel VI § 32 und § 33 zwei bestimmte Fragen der angedeuteten Art wegen ihrer geometrischen Bedeutung beantworten und wollen hier nur darauf hinweisen, dass jedenfalls die letzte Forderung 17 keine logische Folge der übrigen Eigenschaften ist, da ja beispielsweise das in § 12 betrachtete complexe Zahlensystem $\\Omega(t)$ sämtliche Eigenschaften 1–16 besitzt, aber nicht die Forderung 17 erfüllt."),
    ),
    # § 14 Pascal's theorem proof (both proofs, (1)-(6) and (1*)-(6*))
    (
        1516,
        1771,
        ("Satz 21 @@FN:14_1@@ (Pascalscher Satz). Es seien $A, B, C$ bez. $A', B', C'$ je drei Punkte auf zwei sich schneidenden Geraden, die vom Schnittpunkte der Geraden verschieden sind; ist dann $CB'$ parallel $BC'$ und $CA'$ parallel $AC'$, so ist auch $BA'$ parallel $AB'$.\n\n"
        "Um den Beweis für diesen Satz zu erbringen, führen wir zunächst folgende Bezeichnungsweise ein. In einem rechtwinkligen Dreiecke ist offenbar die Kathete $a$ durch die Hypotenuse $c$ und den von $a$ und $c$ eingeschlossenen Basiswinkel $\\alpha$ eindeutig bestimmt: wir setzen kurz\n\n$$\na = \\alpha c,\n$$\n\nsodass das Symbol $\\alpha c$ stets eine bestimmte Strecke bedeutet, sobald $c$ eine beliebig gegebene Strecke und $\\alpha$ ein beliebig gegebener spitzer Winkel ist.\n\n"
        "Nunmehr möge $c$ eine beliebige Strecke und $\\alpha, \\beta$ mögen zwei beliebige spitze Winkel bedeuten; wir behaupten, dass allemal die Streckencongruenz\n\n$$\n\\alpha\\beta c \\equiv \\beta\\alpha c\n$$\n\nbesteht und somit die Symbole $\\alpha, \\beta$ stets mit einander vertauschbar sind.\n\n"
        "Um diese Behauptung zu beweisen, nehmen wir die Strecke $c = AB$ und tragen an diese Strecke in $A$ zu beiden Seiten die Winkel $\\alpha$ und $\\beta$ an. Dann fällen wir von $B$ aus auf die anderen Schenkel dieser Winkel die Lote $BC$ und $BD$, verbinden $C$ mit $D$ und fällen schliesslich von $A$ aus das Lot $AE$ auf $CD$.\n\n"
        "Da die Winkel $\\angle ACB$ und $\\angle ADB$ Rechte sind, so liegen die vier Punkte $A, B, C, D$ auf einem Kreise und demnach sind die beiden Winkel $\\angle ACD$ und $\\angle ABD$ als Peripheriewinkel auf derselben Sehne $AD$ einander congruent. Nun ist einerseits $\\angle ACD$ zusammen mit dem $\\angle CAE$ und andererseits $\\angle ABD$ zusammen mit $\\angle BAD$ je ein Rechter und folglich sind auch die Winkel $\\angle CAE$ und $\\angle BAD$ einander congruent, d. h. es ist\n\n$$\n\\angle CAE \\equiv \\beta,\n$$\n\nund daher\n\n$$\n\\angle DAE \\equiv \\alpha.\n$$\n\n"
        "Wir gewinnen nun unmittelbar die Streckencongruenzen\n\n$$\n\\begin{aligned}\n\\beta c &\\equiv AD, & \\alpha c &\\equiv AC, \\\\\n\\alpha\\beta c &\\equiv \\alpha(AD) \\equiv AE, & \\beta\\alpha c &\\equiv \\beta(AC) \\equiv AE,\n\\end{aligned}\n$$\n\nund hieraus folgt die Richtigkeit der vorhin behaupteten Congruenz.\n\n"
        "Wir kehren nun zur Figur des Pascalschen Satzes zurück und bezeichnen den Schnittpunkt der beiden Geraden mit $O$ und die Strecken $OA, OB, OC, OA', OB', OC', CB', BC', CA', AC', BA', AB'$ bez. mit $a, b, c, a', b', c', l, l^*, m, m^*, n, n^*$. Sodann fällen wir von $O$ Lote auf $l, m, n$; das Lot auf $l$ schliesse mit den beiden Geraden $OA, OA'$ die spitzen Winkel $\\lambda', \\lambda$ ein und die Lote auf $m$ bez. $n$ mögen mit den Geraden $OA$ und $OA'$ die spitzen Winkel $\\mu', \\mu$ bez. $\\nu', \\nu$ bilden. Drücken wir nun diese drei Lote in der vorhin angegebenen Weise mit Hülfe der Hypotenusen und Basiswinkel in den betreffenden rechtwinkligen Dreiecken auf doppelte Weise aus, so erhalten wir folgende drei Streckencongruenzen\n\n$$\n\\begin{aligned}\n(1)\\quad \\lambda b' &\\equiv \\lambda' c, \\\\\n(2)\\quad \\mu a' &\\equiv \\mu' c, \\\\\n(3)\\quad \\nu a' &\\equiv \\nu' b.\n\\end{aligned}\n$$\n\n"
        "Da nach Voraussetzung $l$ parallel $l^*$ und $m$ parallel $m^*$ sein soll, so stimmen die von $O$ auf $l^*$ bez. $m^*$ zu fällenden Lote mit den Loten auf $l$ bez. $m$ überein und wir erhalten somit\n\n$$\n\\begin{aligned}\n(4)\\quad \\lambda c' &\\equiv \\lambda' b, \\\\\n(5)\\quad \\mu c' &\\equiv \\mu' a.\n\\end{aligned}\n$$\n\n"
        "Wenn wir auf die Congruenz (3) links und rechts das Symbol $\\lambda'\\mu$ anwenden und bedenken, dass nach dem vorhin Bewiesenen die in Rede stehenden Symbole mit einander vertauschbar sind, so finden wir\n\n$$\n\\nu\\lambda'\\mu a' \\equiv \\nu'\\mu\\lambda' b.\n$$\n\nIn dieser Congruenz berücksichtigen wir links die Congruenz (2) und rechts (4); dann wird\n\n$$\n\\nu\\lambda'\\mu' c \\equiv \\nu'\\mu\\lambda c'\n$$\n\noder\n\n$$\n\\nu\\mu'\\lambda' c \\equiv \\nu'\\lambda\\mu c'.\n$$\n\nHierin berücksichtigen wir links die Congruenz (1) und rechts (5); dann wird\n\n$$\n\\nu\\mu'\\lambda b' \\equiv \\nu'\\lambda\\mu' a\n$$\n\noder\n\n$$\n\\lambda\\mu'\\nu b' \\equiv \\lambda\\mu'\\nu' a.\n$$\n\nWegen der Bedeutung unserer Symbole schliessen wir aus der letzten Congruenz sofort\n\n$$\n\\mu'\\nu b' \\equiv \\mu'\\nu' a\n$$\n\nund hieraus\n\n$$\n(6)\\quad \\nu b' \\equiv \\nu' a.\n$$\n\n"
        "Fassen wir nun das von $O$ auf $n$ gefällte Lot in's Auge und fällen auf dasselbe Lote von $A$ und $B'$ aus, so zeigt die Congruenz (6), dass die Fusspunkte der letzteren beiden Lote zusammenfallen, d. h. die Gerade $n^* = AB'$ steht zu dem Lote auf $n$ senkrecht und ist mithin zu $n$ parallel. Damit ist der Beweis für den Pascalschen Satz erbracht.\n\n"
        "Wenn irgend eine Gerade, ein Punkt ausserhalb derselben und irgend ein Winkel gegeben ist, so kann man offenbar durch Abtragen dieses Winkels und Ziehen einer Parallelen eine Gerade finden, die durch den gegebenen Punkt geht und die gegebene Gerade unter dem gegebenen Winkel schneidet. Im Hinblick auf diesen Umstand dürfen wir uns zum Beweise des Pascalschen Satzes auch des folgenden einfachen Schlussverfahrens bedienen, das ich einer Mittheilung von anderer Seite verdanke.\n\n"
        "Man ziehe durch $B$ eine Gerade, die $OA'$ im Punkte $D'$ unter dem Winkel $OCA'$ trifft, so dass die Congruenz\n\n$$\n(1^*)\\quad \\angle OCA' \\equiv \\angle OD'B\n$$\n\ngilt; dann ist nach einem bekannten Satze aus der Lehre vom Kreise $CBD'A'$ ein Kreisviereck und mithin gilt nach dem Satze von der Congruenz der Peripheriewinkel auf der nämlichen Sehne die Congruenz\n\n$$\n(2^*)\\quad \\angle OBA' \\equiv \\angle OD'C.\n$$\n\nDa $CA'$ und $AC'$ nach Voraussetzung einander parallel sind, so ist\n\n$$\n(3^*)\\quad \\angle OCA' \\equiv \\angle OAC';\n$$\n\naus $(1^*)$ und $(3^*)$ folgern wir die Congruenz\n\n$$\n\\angle OD'B \\equiv \\angle OAC';\n$$\n\ndann aber ist auch $BAD'C'$ ein Kreisviereck und mithin gilt nach dem Satze von den Winkeln im Kreisviereck die Congruenz\n\n$$\n(4^*)\\quad \\angle OAD' \\equiv \\angle OC'B.\n$$\n\nDa ferner nach Voraussetzung $CB'$ parallel $BC'$ ist, so haben wir auch\n\n$$\n(5^*)\\quad \\angle OB'C \\equiv \\angle OC'B;\n$$\n\naus $(4^*)$ und $(5^*)$ folgern wir die Congruenz\n\n$$\n\\angle OAD' \\equiv \\angle OB'C;\n$$\n\ndiese endlich lehrt, dass $CAD'B'$ ein Kreisviereck ist, und mithin gilt auch die Congruenz\n\n$$\n(6^*)\\quad \\angle OAB' \\equiv \\angle OD'C.\n$$\n\nAus $(2^*)$ und $(6^*)$ folgt\n\n$$\n\\angle OBA' \\equiv \\angle OAB'\n$$\n\nund die Congruenz lehrt, dass $BA'$ und $AB'$ einander parallel sind, wie es der Pascalsche Satz verlangt.\n\n"
        "Fällt $D'$ mit einem der Punkte $A', B', C'$ zusammen, so wird eine Abänderung dieses Schlussverfahrens nothwendig, die leicht ersichtlich ist."),
    ),
    # § 15 segment algebra formulas & figure noise
    (
        1784,
        1816,
        ("Statt des Wortes „congruent“ und des Zeichens $\\equiv$ bedienen wir uns in der Streckenrechnung des Wortes „gleich“ und des Zeichens $=$.\n\n"
        "Wenn $A, B, C$ drei Punkte einer Geraden sind und $B$ zwischen $A$ und $C$ liegt, so bezeichnen wir $c = AC$ als die *Summe* der beiden Strecken $a = AB$ und $b = BC$ und setzen\n\n$$\nc = a + b.\n$$\n\n"
        "Die Strecken $a$ und $b$ heissen *kleiner* als $c$, in Zeichen:\n\n$$\na < c, \\quad b < c,\n$$\n\nund $c$ heisst *grösser* als $a$ und $b$, in Zeichen:\n\n$$\nc > a, \\quad c > b.\n$$\n\n"
        "Aus den linearen Congruenzaxiomen IV 1–3 entnehmen wir leicht, dass für die eben definirte Addition der Strecken das associative Gesetz\n\n$$\na + (b + c) = (a + b) + c\n$$\n\nsowie das commutative Gesetz\n\n$$\na + b = b + a\n$$\n\ngültig ist."),
    ),
    (1838, 1838, "$$c = ab.$$"),
    (1852, 1852, "$$ab = ba$$"),
    (
        1877,
        1941,
        ("$$\na(bc) = (ab)c\n$$\n\nzu beweisen, construiren wir erst die Strecke $d = bc$, dann $da$, ferner die Strecke $e = ba$ und dann $ec$. Dass die Endpunkte von $da$ und $ec$ zusammenfallen, ist wiederum auf Grund des Pascalschen Satzes aus der Figur 23 unmittelbar ersichtlich und mit Benutzung des bereits bewiesenen commutativen Gesetzes folgt hieraus die obige Formel für das associative Gesetz der Streckenmultiplikation.\n\n"
        "Endlich gilt in unserer Streckenrechnung auch das distributive Gesetz\n\n$$\na(b + c) = ab + ac.\n$$\n\nUm dasselbe zu beweisen, construiren wir die Strecken $ab$, $ac$ und $a(b + c)$ und ziehen dann durch den Endpunkt der Strecke $c$ (s. Figur 24) eine Parallele zu dem anderen Schenkel des rechten Winkels. Die Congruenz der beiden rechtwinkligen in der Figur 24 schraffirten Dreiecke und die Anwendung des Satzes von der Gleichheit der Gegenseiten im Parallelogramm liefert dann den gewünschten Nachweis.\n\n"
        "Sind $b$ und $c$ zwei beliebige Strecken, so giebt es stets eine Strecke $a$, sodass $c = ab$ wird; diese Strecke $a$ wird mit $\\frac{c}{b}$ bezeichnet und der *Quotient* von $c$ durch $b$ genannt."),
    ),
    # § 16 proportions & incircle segments
    (
        1951,
        2059,
        ("Erklärung. Sind $a, b, a', b'$ irgend vier Strecken, so soll die *Proportion*\n\n$$\na : b = a' : b'\n$$\n\nnichts anderes bedeuten als die Streckengleichung\n\n$$\nab' = ba'.\n$$\n\n"
        "Definition. Zwei Dreiecke heissen *ähnlich*, wenn entsprechende Winkel in ihnen congruent sind.\n\n"
        "Satz 22. Wenn $a, b$ und $a', b'$ entsprechende Seiten in zwei ähnlichen Dreiecken sind, so gilt die Proportion\n\n$$\na : b = a' : b'.\n$$\n\n"
        "Beweis. Wir betrachten zunächst den besonderen Fall, wo die von $a, b$ und $a', b'$ eingeschlossenen Winkel in beiden Dreiecken Rechte sind, und denken uns die beiden Dreiecke in ein und denselben rechten Winkel eingetragen. Wir tragen sodann vom Scheitel aus auf einem Schenkel die Strecke $1$ ab und ziehen durch den Endpunkt dieser Strecke $1$ die Parallele zu den beiden Hypotenusen; dieselbe schneide auf dem anderen Schenkel die Strecke $e$ ab; dann ist nach unserer Definition des Streckenproduktes\n\n$$\nb = ea, \\quad b' = ea';\n$$\n\nmithin haben wir\n\n$$\nab' = ba',\n$$\n\nd. h.\n\n$$\na : b = a' : b'.\n$$\n\n"
        "Nunmehr kehren wir zu dem allgemeinen Falle zurück. Wir construiren in jedem der beiden ähnlichen Dreiecke den Schnittpunkt $S$ bez. $S'$ der drei Winkelhalbirenden und fällen von diesem die drei Lote $r$ bez. $r'$ auf die Dreiecksseiten; die auf diesen entstehenden Abschnitte bezeichnen wir mit\n\n$$\na_b, \\; a_c, \\; b_c, \\; b_a, \\; c_a, \\; c_b\n$$\n\nbez.\n\n$$\na'_b, \\; a'_c, \\; b'_c, \\; b'_a, \\; c'_a, \\; c'_b.\n$$\n\nDer vorhin bewiesene spezielle Fall unseres Satzes liefert dann die Proportionen\n\n$$\n\\begin{aligned}\na_b : r &= a'_b : r', & b_c : r &= b'_c : r', \\\\\na_c : r &= a'_c : r', & b_a : r &= b'_a : r';\n\\end{aligned}\n$$\n\naus diesen schliessen wir mittelst des distributiven Gesetzes\n\n$$\na : r = a' : r', \\quad b : r = b' : r'\n$$\n\nund folglich mit Rücksicht auf das commutative Gesetz der Multiplikation\n\n$$\na : b = a' : b'.\n$$\n\n"
        "Aus dem eben bewiesenen Satze 22 entnehmen wir leicht den Fundamentalsatz in der Lehre von den Proportionen, der wie folgt lautet:\n\n"
        "Satz 23. Schneiden zwei Parallele auf den Schenkeln eines beliebigen Winkels die Strecken $a, b$ bez. $a', b'$ ab, so gilt die Proportion\n\n$$\na : b = a' : b'.\n$$\n\nUmgekehrt, wenn vier Strecken $a, b, a', b'$ diese Proportion erfüllen und $a, a'$ und $b, b'$ je auf einem Schenkel eines beliebigen Winkels abgetragen werden, so sind die Verbindungsgeraden der Endpunkte von $a, b$ bez. von $a', b'$ einander parallel."),
    ),
    # § 17 line equations & dyadic rationals
    (
        2075,
        2132,
        ("* Es ist stets $a \\cdot 1 = 1 \\cdot a = a$.\n"
        "* Wenn $ab = 0$, so ist entweder $a = 0$ oder $b = 0$.\n"
        "* Wenn $a > b$ und $c > 0$, so folgt stets $ac > bc$.\n\n"
        "Wir nehmen nun in einer Ebene $\\alpha$ durch einen Punkt $O$ zwei zu einander senkrechte Gerade als festes rechtwinkliges Axenkreuz an und tragen dann die beliebigen Strecken $x, y$ von $O$ aus auf den beiden Geraden ab, und zwar nach der einen oder nach der anderen Seite hin, jenachdem die abzutragende Strecke $x$ bez. $y$ positiv oder negativ ist; sodann errichten wir die Lote in den Endpunkten der Strecken $x, y$ und bestimmen den Schnittpunkt $P$ dieser Lote: die Strecken $x, y$ heissen die *Coordinaten* des Punktes $P$; jeder Punkt der Ebene $\\alpha$ ist durch seine Coordinaten $x, y$, die positive oder negative Strecken oder $0$ sein können, eindeutig bestimmt.\n\n"
        "Es sei $l$ irgend eine Gerade in der Ebene $\\alpha$, die durch $O$ und durch einen Punkt $C$ mit den Coordinaten $a, b$ gehe. Sind dann $x, y$ die Coordinaten irgend eines Punktes von $l$, so finden wir leicht aus Satz 22\n\n$$\na : b = x : y \\quad \\text{oder} \\quad bx - ay = 0\n$$\n\nals die Gleichung der Geraden $l$. Ist $l'$ eine zu $l$ parallele Gerade, die auf der $x$-Axe die Strecke $c$ abschneidet, so gelangen wir zu der Gleichung der Geraden $l'$, indem wir in der Gleichung der Geraden $l$ die Strecke $x$ durch die Strecke $x - c$ ersetzen; die gewünschte Gleichung lautet also\n\n$$\nbx - ay - bc = 0.\n$$"),
    ),
    (
        2157,
        2185,
        ("Wir wählen auf der Geraden zwei beliebige Punkte aus und ordnen diesen die Zahlen $0$ und $1$ zu; sodann halbiren wir die durch sie bestimmte Strecke $01$ und bezeichnen den entstehenden Mittelpunkt mit $\\frac{1}{2}$, ferner den Mittelpunkt der Strecke $0\\frac{1}{2}$ mit $\\frac{1}{4}$ u. s. w.; nach $n$-maliger Ausführung dieses Verfahrens gelangen wir zu einem Punkte, dem die Zahl $\\frac{1}{2^n}$ zuzuordnen ist. Nun tragen wir die Strecke $0\\frac{1}{2^n}$ an den Punkt $0$ sowohl nach der Seite des Punktes $1$ als auch nach der anderen Seite hin etwa $m$-mal hintereinander ab und erteilen den so entstehenden Punkten die Zahlenwerte $\\frac{m}{2^n}$ bez. $-\\frac{m}{2^n}$. Aus dem Archimedischen Axiom kann leicht geschlossen werden, dass auf Grund dieser Zuordnung sich jedem beliebigen Punkte der Geraden in eindeutig bestimmter Weise eine reelle Zahl zuordnen lässt und zwar so dass dieser Zuordnung folgende Eigenschaft zukommt: wenn $A, B, C$ irgend drei Punkte der Geraden und bez. $\\alpha, \\beta, \\gamma$ die zugehörigen reellen Zahlen sind und $B$ zwischen $A$ und $C$ liegt, so erfüllen dieselben stets entweder die Ungleichung $\\alpha < \\beta < \\gamma$ oder $\\alpha > \\beta > \\gamma$.\n\n"
        "Aus den Entwicklungen in Kap. II § 9 leuchtet ein, dass dort für jede Zahl, die dem algebraischen Zahlkörper $\\Omega$ angehört, notwendig ein Punkt der Geraden existiren muss, dem sie zugeordnet ist. Ob auch jeder anderen reellen Zahl ein Punkt entspricht, lässt sich im allgemeinen nicht entscheiden, sondern hängt von der vorgelegten Geometrie ab."),
    ),
    # § 18 P_1, P_2, P_3 subscripts
    (2224, 2230, "Erklärung. Verbindet man zwei Punkte eines Polygons $P$ durch irgend einen Streckenzug, der ganz im Inneren des Polygons verläuft, so entstehen zwei neue Polygone $P_1$ und $P_2$, deren innere Punkte alle im Inneren von $P$ liegen; wir sagen: $P$ *zerfällt* in $P_1$ und $P_2$, oder $P_1$ und $P_2$ *setzen* $P$ *zusammen*."),
    (2251, 2272, (
        "Satz 24. Sind zwei Polygone $P_1$ und $P_2$ mit einem dritten Polygon $P_3$ flächengleich, so sind sie auch unter einander flächengleich. Sind zwei Polygone mit einem dritten inhaltsgleich, so sind sie unter einander inhaltsgleich.\n\n"
        "Beweis. Nach Voraussetzung lässt sich sowohl für $P_1$ als auch für $P_2$ eine Zerlegung in Dreiecke angeben, so dass einer jeden dieser beiden Zerlegungen je eine Zerlegung des Polygons $P_3$ in congruente Dreiecke entspricht. Indem wir diese Zerlegungen von $P_3$ gleichzeitig in Betracht ziehen, wird im Allgemeinen jedes Dreieck der einen Zerlegung durch Strecken, welche der anderen Zerlegung angehören, in Polygone zerlegt. Wir fügen nun noch so viele Strecken hinzu, dass jedes dieser Polygone selbst wieder in Dreiecke zerfällt und bringen dann die zwei entsprechenden Zerlegungen in Dreiecke in $P_1$ und in $P_2$ an; dann zerfallen offenbar diese beiden Polygone $P_1$ und $P_2$ in gleich viele paarweise einander congruente Dreiecke und sind somit nach der Definition einander flächengleich."
    )),
    (2279, 2279, "eines Dreiecks."),
    # § 19 Greek Euclid C.N. 5 & L2292 stray 19.
    (2292, 2292, ""),
    (2326, 2326, "chimedischen Axioms nicht möglich ist; in der That lassen sich"),
    (2331, 2331, "gleich sind. Als Beispiel mögen zwei Dreiecke $ABC$ und $ABD$"),
    (
        2364,
        2365,
        "sich jedoch Euklid auf den allgemeinen Grössensatz: „Καὶ τὸ ὅλον τοῦ μέρους μεῖζόν ἐστιν“ — ein Verfahren, welches auf die Ein-",
    ),
    # § 20 triangle area measure F(Delta)
    (
        2378,
        2535,
        ("Definition. Wenn wir in einem Dreieck $ABC$ mit den Seiten $a, b, c$ die beiden Höhen $h_a = AD$, $h_b = BE$ construiren, so folgt aus der Aehnlichkeit der Dreiecke $BCE$ und $ACD$ nach Satz 22 die Proportion\n\n$$\na : h_b = b : h_a, \\quad \\text{d. h.} \\quad ah_a = bh_b;\n$$\n\nmithin ist in jedem Dreiecke das Produkt aus einer Grundlinie und der zu ihr gehörigen Höhe davon unabhängig, welche Seite des Dreiecks man als Grundlinie wählt. Das halbe Produkt aus Grundlinie und Höhe eines Dreiecks $\\Delta$ heisse das *Flächenmass* des Dreiecks $\\Delta$ und werde mit $F(\\Delta)$ bezeichnet.\n\n"
        "Erklärung. Eine Strecke, welche eine Ecke eines Dreiecks mit einem Punkte der gegenüberliegenden Seite verbindet, heisst *Transversale*; dieselbe zerlegt das Dreieck in zwei Dreiecke mit gemeinsamer Höhe, deren Grundlinien in dieselbe Gerade fallen; eine solche Zerlegung heisse eine *transversale Zerlegung* des Dreiecks.\n\n"
        "Satz 29. Wenn ein Dreieck $\\Delta$ durch beliebige Gerade irgendwie in eine gewisse endliche Anzahl von Dreiecken $\\Delta_k$ zerlegt wird, so ist stets das Flächenmass des Dreiecks $\\Delta$ gleich der Summe der Flächenmasse der sämtlichen Dreiecken $\\Delta_k$.\n\n"
        "Beweis. Aus dem distributiven Gesetze in unserer Streckenrechnung folgt unmittelbar, dass das Flächenmass eines beliebigen Dreiecks gleich der Summe der Flächenmasse zweier solcher Dreiecke ist, die durch irgendwelche transversale Zerlegung aus jenem Dreieck hervorgehen. Die wiederholte Anwendung dieser Thatsache zeigt, dass das Flächenmass eines beliebigen Dreiecks auch gleich der Summe der Flächenmasse der sämtlichen Dreiecke ist, die aus dem vorgelegten Dreiecke entstehen, wenn man nach einander beliebig viele transversale Zerlegungen ausführt.\n\n"
        "Um nun den entsprechenden Nachweis für die beliebige Zerlegung des Dreiecks $\\Delta$ in Dreiecke $\\Delta_k$ zu erbringen, ziehen wir von der einen Ecke $A$ des Dreieckes $\\Delta$ durch jeden Teilpunkt der Zerlegung, d. h. durch jeden Eckpunkt der Dreiecke $\\Delta_k$ eine Transversale; durch diese Transversalen zerfällt das Dreieck $\\Delta$ in gewisse Dreiecke $\\Delta_t$. Jedes dieser Dreiecke $\\Delta_t$ zerfällt durch die Teilstrecken der gegebenen Zerlegung in gewisse Dreiecke und Vierecke. Wenn wir in den Vierecken noch je eine Diagonale construiren, so zerfällt jedes Dreieck $\\Delta_t$ in gewisse Dreiecke $\\Delta_{ts}$. Wir wollen nun zeigen, dass die Zerlegung in Dreiecke $\\Delta_{ts}$ sowohl für die Dreiecke $\\Delta_t$ als auch für die Dreiecke $\\Delta_k$ nichts anderes als eine Kette von transversalen Zerlegungen bedeutet.\n\n"
        "In der That, zunächst ist klar, dass jede Zerlegung eines Dreiecks in Teildreiecke stets durch eine Reihe von transversalen Zerlegungen bewirkt werden kann, wenn bei der Zerlegung im Inneren des Dreiecks keine Teilpunkte liegen und überdies wenigstens eine Seite des Dreiecks von Teilpunkten frei bleibt.\n\n"
        "Nun ist für die Dreiecke $\\Delta_t$ unsere Behauptung aus dem Umstande ersichtlich, dass für jedes derselben das Innere sowie eine Seite, nämlich die dem Punkte $A$ gegenüberliegende Seite von weiteren Teilpunkten frei ist.\n\n"
        "Aber auch für jedes $\\Delta_k$ ist die Zerlegung in $\\Delta_{ts}$ auf transversale Zerlegungen zurückführbar. Betrachten wir nämlich ein Dreieck $\\Delta_k$, so wird es unter den von $A$ ausgehenden Transversalen im Dreieck $\\Delta$ eine bestimmte Transversale geben, in welche entweder eine Seite von $\\Delta_k$ hineinfällt oder welche selbst das Dreieck $\\Delta_k$ in zwei Dreiecke zerlegt. Im ersten Fall bleibt die betreffende Seite des Dreiecks $\\Delta_k$ überhaupt frei von weiteren Teilpunkten bei der Zerlegung in Dreiecke $\\Delta_{ts}$; im letzteren Falle ist die im Inneren des Dreiecks $\\Delta_k$ verlaufende Strecke jener Transversale in den beiden entstehenden Dreiecken eine Seite, die bei der Teilung in Dreiecke $\\Delta_{ts}$ von weiteren Teilpunkten gewiss frei bleibt.\n\n"
        "Nach der am Anfang dieses Beweises angestellten Betrachtung ist das Flächenmass $F(\\Delta)$ des Dreiecks $\\Delta$ gleich der Summe aller Flächenmasse $F(\\Delta_t)$ der Dreiecke $\\Delta_t$, und diese Summe ist gleich der Summe aller Flächenmasse $F(\\Delta_{ts})$. Andererseits ist auch die Summe über die Flächenmasse $F(\\Delta_k)$ aller Dreiecke $\\Delta_k$ gleich der Summe aller Flächenmasse $F(\\Delta_{ts})$, und hieraus folgt endlich, dass das Flächenmass $F(\\Delta)$ auch gleich der Summe aller Flächenmasse $F(\\Delta_k)$ ist. Damit ist der Beweis des Satzes 29 vollständig erbracht.\n\n"
        "Definition. Definiren wir das Flächenmass $F(P)$ eines Polygons als die Summe der Flächenmasse aller Dreiecke, in die dasselbe bei einer bestimmten Zerlegung zerfällt, so erkennen wir auf Grund des Satzes 29 durch eine ähnliche Schlussweise, wie wir sie in § 18 beim Beweise des Satzes 24 angewandt haben, dass das Flächenmass eines Polygons von der Art der Zerlegung in Dreiecke unabhängig ist und mithin allein durch das Polygon sich eindeutig bestimmt. Aus dieser Definition entnehmen wir vermittels des Satzes 29 die Thatsache, dass *flächengleiche Polygone gleiches Flächenmass haben*.\n\n"
        "Sind ferner $P$ und $Q$ zwei inhaltsgleiche Polygone, so muss es nach der Definition zwei flächengleiche Polygone $P'$ und $Q'$ geben, so dass das aus $P$ und $P'$ zusammengesetzte Polygon mit dem aus $Q$ und $Q'$ zusammengesetzten Polygon flächengleich ausfällt. Aus den beiden Gleichungen:\n\n$$\nF(P + P') = F(Q + Q'), \\quad F(P') = F(Q')\n$$\n\nschliessen wir leicht\n\n$$\nF(P) = F(Q),\n$$\n\nd. h. *inhaltsgleiche Polygone haben gleiches Flächenmass*.\n\n"
        "Aus der letzteren Thatsache entnehmen wir unmittelbar den Beweis des Satzes 28. Bezeichnen wir nämlich die gleiche Grundlinie der beiden Dreiecke mit $g$, die zugehörigen Höhen mit $h$ und $h'$, so schliessen wir aus der angenommenen Inhaltsgleichheit der beiden Dreiecke, dass dieselben auch gleiches Flächenmass haben müssen, d. h. es folgt:\n\n$$\n\\frac{1}{2}gh = \\frac{1}{2}gh'\n$$\n\nund mithin nach Division durch $\\frac{1}{2}g$\n\n$$\nh = h';\n$$\n\ndies ist die Aussage des Satzes 28."),
    ),
    # § 21 area formulas & 3 footnotes (Schur, Killing, Stolz)
    (
        2558,
        2621,
        ("$$\nF(ABC) = \\frac{1}{2} AB \\cdot AC, \\quad F(AB'C') = \\frac{1}{2} AB' \\cdot AC'\n$$\n\naus. Nehmen wir an, dass diese beiden Flächenmasse einander gleich sind, so folgt:\n\n$$\nAB \\cdot AC = AB' \\cdot AC' \\quad \\text{oder} \\quad AB : AB' = AC' : AC\n$$\n\nund hieraus ergiebt sich nach Satz 23, dass die beiden Geraden $BC$ und $B'C'$ einander parallel sind und sodann erweisen sich nach Satz 27 die beiden Dreiecke $BC'B'$ und $BC'C$ als inhaltsgleich. Durch Hinzufügen des Dreiecks $ABC'$ folgt, dass die beiden Dreiecke $ABC$ und $AB'C'$ einander inhaltsgleich sind. Wir haben damit erkannt, dass zwei rechtwinklige Dreiecke mit gleichem Flächenmass auch stets einander inhaltsgleich sind.\n\n"
        "Nehmen wir jetzt ein beliebiges Dreieck mit der Grundlinie $g$ und der Höhe $h$, so ist dasselbe nach Satz 27 inhaltsgleich einem rechtwinkligen Dreieck mit den beiden Katheten $g$ und $h$; und da das ursprüngliche Dreieck offenbar dasselbe Flächenmass wie das rechtwinklige Dreieck besitzt, so folgt, dass in der letzten Betrachtung die Einschränkung auf rechtwinklige Dreiecke nicht nötig war; damit haben wir erkannt, *dass zwei beliebige Dreiecke mit gleichem Flächenmass auch stets einander inhaltsgleich sind*.\n\n"
        "Es sei nunmehr ein beliebiges Polygon $P$ mit dem Flächenmass $g$ vorgelegt; $P$ zerfalle in $n$ Dreiecke mit den Flächenmassen bez. $g_1, g_2, \\dots, g_n$; dann ist\n\n$$\ng = g_1 + g_2 + \\dots + g_n.\n$$\n\n"
        "Wir construiren nun ein Dreieck $ABC$ mit der Grundlinie $AB = g$ und der Höhe $h = 1$ und markiren auf der Grundlinie die Punkte $A_1, A_2, \\dots, A_{n-1}$, sodass\n\n$$\ng_1 = AA_1, \\quad g_2 = A_1A_2, \\; \\dots, \\; g_{n-1} = A_{n-2}A_{n-1}, \\quad g_n = A_{n-1}B\n$$\n\nausfällt. Da die Dreiecke innerhalb des Polygons $P$ bez. die gleichen Flächenmasse besitzen, wie die Dreiecke $AA_1C, A_1A_2C, \\dots, A_{n-2}A_{n-1}C, A_{n-1}BC$, so sind sie nach dem vorhin Bewiesenen diesen auch inhaltsgleich; folglich ist das Polygon $P$ einem Dreiecke mit der Grundlinie $g$ und der Höhe $h = 1$ inhaltsgleich. Hieraus folgt mit Hülfe von Satz 24, dass zwei Polygone mit gleichem Flächenmass einander stets inhaltsgleich sind."),
    ),
    (2639, 2641, "Dieser Satz 31 ist von F. Schur @@FN:21_1@@ und W. Killing @@FN:21_2@@ mit Hülfe des Archimedischen Axioms bewiesen und von O. Stolz @@FN:21_3@@ als Axiom hingestellt worden."),
    (2664, 2669, ""),
    # § 22 Omega, Omega(t), z coordinates
    (2689, 2696, "der Gruppen II–V sämtlich teils lineare, teils ebene Axiome; die Axiome 3–7 der Gruppe I sind die einzigen räumlichen Axiome. Um die Bedeutung dieser räumlichen Axiome klar zu erkennen, denken wir uns irgend eine ebene Geometrie vorgelegt und untersuchen allgemein die Bedingungen dafür, dass diese ebene Geometrie sich als Teil einer räumlichen Geometrie auffassen lässt, in welcher wenigstens die Axiome der Gruppen I–III sämtlich erfüllt sind."),
    (2742, 2760, "$$\nux + vy + w = 0\n$$\n\ndie Bedingung für die vereinigte Lage von Punkt und Gerade darstellt. Das System aller Strecken in unserer Geometrie bildet nach § 17 einen Zahlenbereich, für welchen die in § 13 aufgezählten Eigenschaften 1–16 bestehen, und wir können daher mittelst dieses Zahlenbereiches, ähnlich wie es in § 9 oder § 12 mittelst des Zahlensystems $\\Omega$ bez. $\\Omega(t)$ geschehen ist, eine räumliche Geometrie construiren: wir setzen zu dem Zwecke fest, dass ein System von drei Strecken $(x, y, z)$ einen Punkt, die Verhältnisse von vier Strecken $(u : v : w : r)$ eine Ebene darstellen möge, während die Geraden als Schnitte zweier Ebenen definirt sind; dabei drückt die lineare Gleichung\n\n$$\nux + vy + wz + r = 0\n$$\n\naus, dass der Punkt $(x, y, z)$ auf der Ebene $(u : v : w : r)$ liegt."),
    # § 23 non-Desarguesian ellipse model
    (2792, 2798, "Satz 33. Es giebt eine ebene Geometrie, in welcher die Axiome I 1–2, II–III, IV 1–5, V, d. h. sämtliche linearen und ebenen Axiome mit Ausnahme des Congruenzaxioms IV 6 erfüllt sind, während der Desarguessche Satz (Satz 32) nicht gilt. Der Desarguessche Satz kann mithin aus den genannten Axiomen allein nicht gefolgert werden: es bedarf zum Beweise desselben notwendig entweder der räumlichen Axiome oder der sämtlichen Congruenzaxiome."),
    (2804, 2806, "systems als Mittelpunkt eine Ellipse mit den Halbaxen $1$ und $\\frac{1}{2}$ construirt; endlich bezeichnen wir mit $F$ den Punkt, welcher in der Entfernung $\\frac{3}{2}$ von $O$ auf der positiven $X$-Axe liegt."),
    (2818, 2820, "ist. Zu dem Zwecke gehen wir von einem beliebigen Kreise aus,"),
    (2829, 2829, "einem anderen Punkte $B$ berührt oder in $A$ mit der Ellipse eine"),
    (2837, 2850, "zur $Y$-Axe symmetrisch. Es seien $a, b$ die Coordinaten irgend eines Punktes der Ellipse: dann lehrt eine leichte Rechnung, dass der in diesem Punkte berührende zur $Y$-Axe symmetrische Kreis auf der positiven $X$-Axe die Strecke\n\n$$\nx = |\\sqrt{1 + 3b^2}|\n$$\n\nabschneidet. Der grösstmögliche Wert dieses Ausdrucks tritt für $b = \\frac{1}{2}$ ein und wird somit gleich $|\\frac{1}{2}\\sqrt{7}|$. Da der vorhin mit $F$ bezeichnete Punkt auf der $X$-Axe die Abscisse $\\frac{3}{2} > |\\frac{1}{2}\\sqrt{7}|$ aufweist, so folgt, *dass unter den die Ellipse viermal treffenden Kreisen sich gewiss keiner befindet, der durch den Punkt $F$ läuft*."),
    (2853, 2857, "gender Weise her. Als Punkte der neuen Geometrie nehmen wir die Punkte der $XY$-Ebene; als Gerade der neuen Geometrie nehmen wir diejenigen Geraden der $XY$-Ebene unverändert, welche die feste Ellipse berühren oder gar nicht treffen; ist dagegen $g$ eine Gerade der $XY$-Ebene, die die Ellipse in zwei Punkten $P$"),
    (2876, 2876, "alle Geraden der $XY$-Ebene die entsprechenden Linienzüge con-"),
    (2887, 2887, "Ferner nennen wir zwei Strecken $AB$ und $A'B'$ in unserer"),
    (2905, 2929, "mögen die Punkte $A, B, C$ in dieser Reihenfolge und die Punkte $A', B', C'$ in dieser Reihenfolge je auf einer Geraden unserer neuen Geometrie liegen; $D$ sei ein Punkt ausserhalb der Geraden $ABC$ und $D'$ ein Punkt ausserhalb der Geraden $A'B'C'$: dann mögen für die Winkel zwischen diesen Geraden in unserer neuen Geometrie die Congruenzen\n\n$$\n\\angle ABD \\equiv \\angle A'B'D' \\quad \\text{und} \\quad \\angle CBD \\equiv \\angle C'B'D'\n$$\n\ngelten, sobald für die natürlichen Winkel zwischen den entsprechenden Linienzügen in der gewöhnlichen Geometrie die Proportion\n\n$$\n\\angle ABD : \\angle CBD = \\angle A'B'D' : \\angle C'B'D'\n$$\n\nerfüllt ist. Bei diesen Festsetzungen sind auch die Axiome IV 1–5 und V gültig.\n\nUm einzusehen, dass in unserer neu hergestellten Geometrie der Desarguessche Satz nicht gilt, betrachten wir folgende drei gewöhnliche gerade Linien in der $XY$-Ebene: die $X$-Axe, die $Y$-Axe und die Gerade, welche die beiden Ellipsenpunkte $x = \\frac{3}{5}, y = \\frac{2}{5}$ und $x = -\\frac{3}{5}, y = -\\frac{2}{5}$ mit einander verbindet. Da"),
    # § 24 & § 25 figure label noise
    (2978, 2978, "$$OO = 0 \\quad \\text{oder} \\quad 0 = OO.$$"),
    (2984, 2984, "$$OE = OE' = 1 \\quad \\text{oder} \\quad 1 = OE = OE'.$$"),
    (2991, 2991, "$$OA = OA' \\quad \\text{oder} \\quad OA' = OA.$$"),
    (3000, 3010, "$OE'$ in $C$ und $C'$: dann heisse $c = OC = OC'$ die *Summe* der Strecke $a = OA$ mit der Strecke $b = OB$, in Zeichen:\n\n$$\nc = a + b \\quad \\text{oder} \\quad a + b = c.\n$$"),
    (3023, 3031, "diese Parallele die feste Gerade $OE'$ im Punkte $C'$, so heisst $c = OC'$ das *Produkt* der Strecke $a = OA$ in die Strecke $b = OB$, in Zeichen:\n\n$$\nc = ab \\quad \\text{oder} \\quad ab = c.\n$$"),
    (3049, 3055, "$$\na + b = b + a\n$$\n\ngilt. Es sei\n\n$$\na = OA = OA', \\quad b = OB = OB',\n$$"),
    (3071, 3108, "Wir bezeichnen den Schnittpunkt von $AB''$ und $A'A''$ mit $F$ und den Schnittpunkt von $BA''$ und $B'B''$ mit $D$; dann sind in den Dreiecken $AA'F$ und $BB'D$ die entsprechenden Seiten einander parallel. Mittelst des Desarguesschen Satzes schliessen wir hieraus, dass die drei Punkte $O, F, D$ in einer Geraden liegen. In Folge dieses Umstandes liegen die beiden Dreiecke $OAA'$ und $DB''A''$ derart, dass die Verbindungslinien entsprechender Ecken durch den nämlichen Punkt $F$ laufen und da überdies zwei Paare entsprechender Seiten, nämlich $OA$ und $DB''$ sowie $OA'$ und $DA''$ einander parallel sind, so laufen nach der zweiten Aussage des Desarguesschen Satzes (Satz 32) auch die dritten Seiten $AA'$ und $B''A''$ einander parallel.\n\nZum Beweise des associativen Gesetzes der Addition\n\n$$\na + (b + c) = (a + b) + c\n$$\n\ndient die Figur 42. Mit Berücksichtigung des eben bewiesenen commutativen Gesetzes der Addition spricht sich die obige Behauptung, wie man sieht, darin aus, dass die Gerade $A''B''$ parallel"),
    # § 26 associative & distributive laws + Dr. von Schaper footnote
    (
        3124,
        3350,
        ("$$\na(bc) = (ab)c.\n$$\n\n"
        "Es seien auf der ersteren der beiden festen Geraden durch $O$ die Strecken\n\n$$\n1 = OA, \\quad b = OC, \\quad c = OA'\n$$\n\nund auf der anderen Geraden die Strecken\n\n$$\na = OG \\quad \\text{und} \\quad b = OB\n$$\n\ngegeben. Um gemäss der Vorschrift in § 24 der Reihe nach die Strecken\n\n$$\nbc = OB' \\; \\text{und} \\; bc = OC', \\quad ab = OD, \\quad (ab)c = OD'\n$$\n\nzu construiren, ziehen wir $A'B'$ parallel $AB$, $B'C'$ parallel $BC$, $CD$ parallel $AG$ sowie $A'D'$ parallel $AD$; wie wir sofort erkennen, läuft dann unsere Behauptung darauf hinaus, dass auch $CD$ parallel $C'D'$ sein muss. Bezeichnen wir nun den Schnittpunkt der Geraden $AD$ und $BC$ mit $F$ und den Schnittpunkt der Geraden $A'D'$ und $B'C'$ mit $F'$, so sind in den Dreiecken $ABF$ und $A'B'F'$ die entsprechenden Seiten einander parallel; nach dem Desarguesschen Satze liegen daher die drei Punkte $O, F, F'$ auf einer Geraden. Wegen dieses Umstandes können wir die zweite Aussage des Desarguesschen Satzes auf die beiden Dreiecke $CDF$ und $C'D'F'$ anwenden und erkennen hieraus, dass in der That $CD$ parallel $C'D'$ ist.\n\n"
        "Wir beweisen endlich in unserer Streckenrechnung auf Grund des Desarguesschen Satzes die beiden distributiven Gesetze:\n\n$$\na(b + c) = ab + ac \\quad \\text{und} \\quad (a + b)c = ac + bc.\n$$\n\n"
        "Zum Beweise des ersteren Gesetzes dient die Figur 44 @@FN:26_1@@. In derselben ist\n\n$$\nb = OA', \\quad c = OC', \\quad ab = OB', \\quad ab = OA'', \\quad ac = OC'' \\; \\text{u. s. f.}\n$$\n\nund es läuft\n\n"
        "| $B''D_2$ parallel $C''D_1$ parallel zur festen Geraden $OA'$,\n"
        "| $B'D_1$ parallel $C'D_2$ parallel zur festen Geraden $OA''$;\n\n"
        "ferner ist $A'A''$ parallel $C'C''$ und\n\n$$\nA'B'' \\; \\text{parallel} \\; B'A'' \\; \\text{parallel} \\; F'D_2 \\; \\text{parallel} \\; F''D_1.\n$$\n\nDie Behauptung läuft darauf hinaus, dass dann auch\n\n$$\nF'F'' \\; \\text{parallel} \\; A'A'' \\; \\text{und} \\; C'C''\n$$\n\nsein muss.\n\n"
        "Wir construiren folgende Hülfslinien:\n\n"
        "| $F''J$ parallel der festen Geraden $OA'$,\n"
        "| $F'J$ parallel der festen Geraden $OA''$;\n\n"
        "die Schnittpunkte der Geraden $C''D_1$ und $C'D_2$, $C''D_1$ und $F'J$, $C'D_2$ und $F''J$ heissen $G, H_1, H_2$; endlich erhalten wir noch die weiteren in der Figur 44 punktirten Hülfslinien durch Verbindung bereits construirter Punkte.\n\n"
        "In den beiden Dreiecken $A'B''C''$ und $F'D_2G$ laufen die Verbindungsgeraden entsprechender Ecken einander parallel; nach der zweiten Aussage des Desarguesschen Satzes folgt daher, dass\n\n$$\nA'C'' \\; \\text{parallel} \\; F'G\n$$\n\nsein muss. In den beiden Dreiecken $A'C''F''$ und $F'GH_2$ laufen ebenfalls die Verbindungsgeraden entsprechender Ecken einander parallel; wegen der vorhin gefundenen Thatsache folgt nach der zweiten Aussage des Desarguesschen Satzes, dass\n\n$$\nA'F'' \\; \\text{parallel} \\; F'H_2\n$$\n\nsein muss. Da somit in den beiden wagerecht schraffirten Dreiecken $OA'F''$ und $JH_2F'$ die entsprechenden Seiten parallel sind, so lehrt der Desarguessche Satz, dass die drei Verbindungsgeraden\n\n$$\nOJ, \\quad A'H_2, \\quad F''F'\n$$\n\nsich in einem und demselben Punkte, etwa in $P$, treffen.\n\n"
        "Auf dieselbe Weise finden wir, dass auch\n\n$$\nA''F' \\; \\text{parallel} \\; F''H_1\n$$\n\nsein muss und da somit in den beiden schräg schraffierten Dreiecken $OA''F'$ und $JH_1F''$ die entsprechenden Seiten parallel laufen, so treffen sich dem Desarguesschen Satze zufolge die drei Verbindungsgeraden\n\n$$\nOJ, \\quad A''H_1, \\quad F'F''\n$$\n\nebenfalls in einem Punkte — dem Punkte $P$.\n\n"
        "Nunmehr laufen für die Dreiecke $OA'A''$ und $JH_2H_1$ die Verbindungsgeraden entsprechender Ecken durch den nämlichen Punkt $P$, und mithin folgt, dass\n\n$$\nH_1H_2 \\; \\text{parallel} \\; A'A''\n$$\n\nsein muss; mithin ist auch\n\n$$\nH_1H_2 \\; \\text{parallel} \\; C'C''.\n$$\n\n"
        "Endlich betrachten wir die Figur $F''H_2C'C''H_1F'F''$. Da in derselben\n\n"
        "| $F''H_2$ parallel $C'F'$ parallel $C''H_1$,\n"
        "| $H_2C'$ parallel $F''C''$ parallel $H_1F'$,\n"
        "| $C'C''$ parallel $H_1H_2$\n\n"
        "ausfällt, so erkennen wir hierin die Figur 41 wieder, die wir in § 25 zum Beweise für das commutative Gesetz der Addition benutzt haben. Die entsprechenden Schlüsse wie dort zeigen dann, dass\n\n$$\nF'F'' \\; \\text{parallel} \\; H_1H_2\n$$\n\nsein muss und da mithin auch\n\n$$\nF'F'' \\; \\text{parallel} \\; A'A''\n$$\n\nausfällt, so ist der Beweis unserer Behauptung vollständig erbracht.\n\n"
        "Zum Beweise der zweiten Formel des distributiven Gesetzes dient die völlig verschiedene Figur 45. In derselben ist\n\n$$\n1 = OD, \\quad a = OA, \\quad a = OB, \\quad b = OG, \\quad c = OD',\n$$\n\n$$\nac = OA', \\quad ac = OB', \\quad bc = OG' \\; \\text{u. s. f.}\n$$\n\nund es läuft\n\n"
        "| $GH$ parallel $G'H'$ parallel zur festen Geraden $OA$,\n"
        "| $AH$ parallel $A'H'$ parallel zur festen Geraden $OB$\n\n"
        "und ferner\n\n"
        "| $AB$ parallel $A'B'$,\n"
        "| $BD$ parallel $B'D'$,\n"
        "| $DG$ parallel $D'G'$,\n"
        "| $HJ$ parallel $H'J'$.\n\n"
        "Die Behauptung läuft darauf hinaus, dass dann auch\n\n$$\nDJ \\; \\text{parallel} \\; D'J'\n$$\n\nsein muss.\n\n"
        "Wir bezeichnen die Punkte, in denen $BD$ und $GD$ die Gerade $AH$ treffen, bez. mit $C$ und $F$ und ferner die Punkte, in denen $B'D'$ und $G'D'$ die Gerade $A'H'$ treffen, bez. mit $C'$ und $F'$; endlich ziehen wir noch die in der Figur 45 punktirten Hülfslinien $FJ$ und $F'J'$.\n\n"
        "In den Dreiecken $ABC$ und $A'B'C'$ laufen die entsprechenden Seiten parallel; mithin liegen nach dem Desarguesschen Satze die drei Punkte $O, C, C'$ auf einer Geraden. Ebenso folgt dann aus der Betrachtung der Dreiecke $CDF$ und $C'D'F'$, dass $O, F, F'$ auf einer Geraden liegen, und die Betrachtung der Dreiecke $FGH$ und $F'G'H'$ lehrt, dass $O, H, H'$ Punkte einer Geraden sind. Nun laufen in den Dreiecken $FHJ$ und $F'H'J'$ die Verbindungsgeraden entsprechender Ecken durch den nämlichen Punkt $O$, und mithin sind zufolge der zweiten Aussage des Desarguesschen Satzes die Geraden $FJ$ und $F'J'$ einander parallel. Endlich zeigt dann die Betrachtung der Dreiecke $DFJ$ und $D'F'J'$, dass die Geraden $DJ$ und $D'J'$ einander parallel sind, und damit ist der Beweis unserer Behauptung vollständig erbracht."),
    ),
    # § 27 & § 28 formulas
    (
        3381,
        3496,
        ("$$\nax + by + c = 0;\n$$\n\nin dieser Gleichung stehen die Strecken $a, b$ notwendig linksseitig von den Coordinaten $x, y$; die Strecken $a, b$ sind niemals beide Null und $c$ ist eine beliebige Strecke.\n\n"
        "Umgekehrt: jede Streckengleichung der beschriebenen Art stellt stets eine Gerade in der zu Grunde gelegten ebenen Geometrie dar.\n\n"
        "Beweis. Wir nehmen zunächst an, die Gerade $l$ gehe durch $O$. Ferner sei $C$ ein bestimmter von $O$ verschiedener Punkt auf $l$ und $P$ ein beliebiger Punkt auf $l$; $C$ habe die Coordinaten $OA, OB$ und $P$ habe die Coordinaten $x, y$; wir bezeichnen die Verbindungsgerade der Endpunkte von $x, y$ mit $g$. Endlich ziehen wir durch den Endpunkt der Strecke $1$ auf der $X$-Axe eine Parallele $h$ zu $AB$: diese Parallele schneide auf der $Y$-Axe die Strecke $e$ ab. Aus der zweiten Aussage des Desarguesschen Satzes folgt leicht, dass die Gerade $g$ stets parallel zu $AB$ läuft. Da somit auch $g$ stets zu $h$ parallel ist, so folgt für die Coordinaten $x, y$ des beliebigen Punktes $P$ auf $l$ die Streckengleichung\n\n$$\nex = y.\n$$\n\n"
        "Nunmehr sei $l'$ eine beliebige Gerade in unserer Ebene; dieselbe schneide auf der $X$-Axe die Strecke $c = OO'$ ab. Wir ziehen ferner die Gerade $l$ durch $O$ parallel zu $l'$. Es sei $P'$ ein beliebiger Punkt auf $l'$; die Parallele durch $P'$ zur $X$-Axe treffe die Gerade $l$ in $P$ und schneide auf der $Y$-Axe die Strecke $y = OB$ ab; ferner mögen die Parallelen durch $P$ und $P'$ zur $Y$-Axe auf der $X$-Axe die Strecken $x = OA$ und $x' = OA'$ abschneiden.\n\n"
        "Wir wollen nun beweisen, dass die Streckengleichung\n\n$$\nx' = x + c\n$$\n\nbesteht. Zu diesem Zwecke ziehen wir $O'C$ parallel zur Einheitsgeraden, ferner $CD$ parallel zur $X$-Axe und $AD$ parallel zur $Y$-Axe; dann läuft unsere Behauptung darauf hinaus, dass\n\n$$\nA'D \\; \\text{parallel} \\; O'C\n$$\n\nsein muss. Wir construiren noch $D'$ als Schnittpunkt der Geraden $CD$ und $A'P'$ und ziehen $O'C'$ parallel zur $Y$-Axe.\n\n"
        "Da in den Dreiecken $OCP$ und $O'C'P'$ die Verbindungsgeraden entsprechender Ecken parallel laufen, so folgt mittelst der zweiten Aussage des Desarguesschen Satzes, dass\n\n$$\nCP \\; \\text{parallel} \\; C'P'\n$$\n\nsein muss; auf gleiche Weise lehrt die Betrachtung der Dreiecke $ACP$ und $A'C'P'$, dass\n\n$$\nAC \\; \\text{parallel} \\; A'C'\n$$\n\nist. Da somit in den Dreiecken $ACD$ und $C'A'O'$ die entsprechenden Seiten einander parallel laufen, so treffen sich die Geraden $AC', C'A, DO'$ in einem Punkte und die Betrachtung der beiden Dreiecke $C'A'D$ und $ACO'$ zeigt dann, dass $A'D$ und $CO'$ einander parallel sind.\n\n"
        "Aus den beiden bisher gefundenen Streckengleichungen\n\n$$\nex = y \\quad \\text{und} \\quad x' = x + c\n$$\n\nfolgt sofort die weitere Gleichung\n\n$$\nex' = y + ec.\n$$\n\nBezeichnen wir schliesslich mit $n$ die Strecke, die zur Strecke $1$ addirt die Strecke $0$ liefert, so folgt, wie man leicht beweist, aus der letzten Gleichung\n\n$$\nex' + ny + nec = 0\n$$\n\nund diese Gleichung ist von der Gestalt, wie der Satz 34 behauptet.\n\n"
        "Die zweite Aussage des Satzes 34 erkennen wir nun ohne Mühe als richtig; denn eine jede vorgelegte Streckengleichung\n\n$$\nax + by + c = 0\n$$\n\nlässt sich offenbar durch linksseitige Multiplikation mit einer geeigneten Strecke in die vorhin gefundene Gestalt\n\n$$\nex + ny + nec = 0\n$$\n\nbringen.\n\n"
        "Es sei noch ausdrücklich bemerkt, dass bei unseren Annahmen eine Streckengleichung von der Gestalt\n\n$$\nxa + yb + c = 0,\n$$\n\nin der die Strecken $a, b$ rechtsseitig von den Coordinaten $x, y$ stehen, im Allgemeinen nicht eine Gerade darstellt."),
    ),
    (
        3520,
        3536,
        "$$\nABOE, \\quad AOBE, \\quad AOEB, \\quad OABE, \\quad OAEB, \\quad OEAB\n$$\n\nmöglich, so nennen wir die Strecke $a = OA$ *kleiner* als die Strecke $b = OB$, in Zeichen:\n\n$$\na < b.\n$$\n\nFindet dagegen eine der sechs Reihenfolgen\n\n$$\nBAOE, \\quad BOAE, \\quad BOEA, \\quad OBAE, \\quad OBEA, \\quad OEBA\n$$\n\nstatt, so nennen wir die Strecke $a = OA$ *grösser* als die Strecke $b = OB$, in Zeichen\n\n$$\na > b.\n$$",
    ),
    # § 29 spatial geometry over Desarguesian number system D
    (
        3568,
        3675,
        ("Um dies einzusehen, denken wir uns das System von irgend drei Zahlen $(x, y, z)$ des Desarguesschen Zahlensystems $D$ als einen Punkt und das System von irgend vier Zahlen $(u : v : w : r)$ in $D$, von denen die ersten drei Zahlen nicht zugleich $0$ sind, als eine Ebene; doch sollen die Systeme $(u : v : w : r)$ und $(au : av : aw : ar)$, wo $a$ irgend eine von $0$ verschiedene Zahl in $D$ bedeutet, die nämliche Ebene darstellen. Das Bestehen der Gleichung\n\n$$\nux + vy + wz + r = 0\n$$\n\nmöge ausdrücken, dass der Punkt $(x, y, z)$ auf der Ebene $(u : v : w : r)$ liegt. Die Gerade endlich definiren wir mit Hülfe eines Systems zweier Ebenen $(u' : v' : w' : r')$ und $(u'' : v'' : w'' : r'')$, wenn es nicht möglich ist, zwei von $0$ verschiedene Zahlen $a', a''$ in $D$ zu finden, sodass gleichzeitig\n\n$$\na'u' = a''u'', \\quad a'v' = a''v'', \\quad a'w' = a''w''\n$$\n\nwird. Ein Punkt $(x, y, z)$ heisst auf dieser Geraden $[(u' : v' : w' : r'), (u'' : v'' : w'' : r'')]$ gelegen, wenn er den beiden Ebenen $(u' : v' : w' : r')$ und $(u'' : v'' : w'' : r'')$ gemeinsam ist. Zwei Gerade, welche dieselben Punkte enthalten, gelten als nicht verschieden.\n\n"
        "Indem wir die Rechnungsgesetze 1–11 in § 13 anwenden, die nach Voraussetzung für die Zahlen in $D$ gelten sollen, gelangen wir ohne Schwierigkeit zu dem Resultate, dass in der soeben aufgestellten räumlichen Geometrie die Axiome I und III sämtlich erfüllt sind.\n\n"
        "Damit auch den Axiomen II der Anordnung Genüge geschehe, treffen wir folgende Festsetzungen. Es seien\n\n$$\n(x_1, y_1, z_1), \\quad (x_2, y_2, z_2), \\quad (x_3, y_3, z_3)\n$$\n\nirgend drei Punkte einer Geraden\n\n$$\n[(u' : v' : w' : r'), \\; (u'' : v'' : w'' : r'')];\n$$\n\ndann heisse der Punkt $(x_2, y_2, z_2)$ zwischen den beiden anderen gelegen, wenn wenigstens eine der sechs Doppelungleichungen\n\n$$\n\\begin{aligned}\n(1)\\quad x_1 &< x_2 < x_3, & x_1 &> x_2 > x_3, \\\\\n(2)\\quad y_1 &< y_2 < y_3, & y_1 &> y_2 > y_3, \\\\\n(3)\\quad z_1 &< z_2 < z_3, & z_1 &> z_2 > z_3\n\\end{aligned}\n$$\n\nerfüllt ist. Besteht nun etwa eine der beiden Doppelungleichungen (1), so schliessen wir leicht, dass entweder $y_1 = y_2 = y_3$ oder notwendig eine der beiden Doppelungleichungen (2) und ebenso dass entweder $z_1 = z_2 = z_3$ oder eine der Doppelungleichungen (3) gelten muss. In der That, aus den Gleichungen\n\n$$\n\\begin{aligned}\nu'x_i + v'y_i + w'z_i + r' &= 0, \\\\\nu''x_i + v''y_i + w''z_i + r'' &= 0 \\qquad (i = 1, 2, 3)\n\\end{aligned}\n$$\n\nleiten wir durch linksseitige Multiplikation derselben mit geeigneten Zahlen aus $D$ und durch nachherige Addition der entstehenden Gleichungen ein Gleichungssystem von der Gestalt\n\n$$\n(4)\\quad u'''x_i + v'''y_i + r''' = 0 \\qquad (i = 1, 2, 3)\n$$\n\nab. Hierin ist der Coefficient $v'''$ sicher nicht $0$, da sonst die Gleichheit der drei Zahlen $x_1, x_2, x_3$ folgen würde. Aus\n\n$$\nx_1 \\lesseqgtr x_2 \\lesseqgtr x_3\n$$\n\nschliessen wir\n\n$$\nu'''x_1 \\gtreqless u'''x_2 \\gtreqless u'''x_3\n$$\n\nund mithin wegen (4)\n\n$$\nv'''y_1 + r''' \\lesseqgtr v'''y_2 + r''' \\lesseqgtr v'''y_3 + r'''\n$$\n\nund daher\n\n$$\nv'''y_1 \\lesseqgtr v'''y_2 \\lesseqgtr v'''y_3,\n$$\n\nund da $v'''$ nicht $0$ ist, so haben wir\n\n$$\ny_1 \\lesseqgtr y_2 \\lesseqgtr y_3;\n$$\n\nin jeder dieser Doppelungleichungen soll stets entweder durchweg das obere oder durchweg das mittlere oder durchweg das untere Zeichen gelten.\n\n"
        "Die angestellten Ueberlegungen lassen erkennen, dass in unserer Geometrie die linearen Axiome II 1–4 der Anordnung zutreffen. Es bleibt noch zu zeigen übrig, dass in unserer Geometrie auch das ebene Axiom II 5 gültig ist.\n\n"
        "Zu dem Zwecke sei eine Ebene $(u : v : w : r)$ und in ihr eine Gerade $[(u : v : w : r), (u' : v' : w' : r')]$ gegeben. Wir setzen fest, dass alle in der Ebene $(u : v : w : r)$ gelegenen Punkte $(x, y, z)$, für die der Ausdruck $u'x + v'y + w'z + r'$ kleiner oder grösser als $0$ ausfällt, auf der einen bez. auf der anderen Seite von jener Geraden gelegen sein sollen, und haben dann zu beweisen, dass diese Fest-"),
    ),
    # § 30 & § 31 minor OCR fixes
    (3714, 3718, "Satz 35. Es seien in einer ebenen Geometrie die Axiome I 1–2, II, III erfüllt: dann ist die Gültigkeit des Desarguesschen Satzes die notwendige und hinreichende Bedingung dafür, dass diese ebene Geometrie sich auffassen lässt als ein Teil einer räumlichen Geometrie, in welcher die sämtlichen Axiome I, II, III erfüllt sind."),
    (3771, 3782, "Satz 37. Der Pascalsche Satz (Satz 21) ist *nicht* beweisbar auf Grund der Axiome I, II, III, d. h. unter Ausschliessung der Congruenzaxiome sowie des Archimedischen Axioms.\n\nIn der Fassung dieser beiden Sätze können nach dem allgemeinen Satze 35 die räumlichen Axiome I 3–7 auch durch die ebene Forderung ersetzt werden, dass der Desarguessche Satz (Satz 32) gelten soll."),
    # § 32 Archimedean commutativity proof formulas
    (
        3801,
        3873,
        ("Beweis. Zunächst bemerken wir: wenn $a$ eine beliebige Zahl des Zahlensystems und\n\n$$\nn = 1 + 1 + \\dots + 1\n$$\n\neine ganze rationale positive Zahl ist, so gilt für $a$ und $n$ stets das commutative Gesetz der Multiplikation; es ist nämlich\n\n$$\n\\begin{aligned}\nan &= a(1 + 1 + \\dots + 1) = a \\cdot 1 + a \\cdot 1 + \\dots + a \\cdot 1 = a + a + \\dots + a\n\\end{aligned}\n$$\n\nund ebenso\n\n$$\n\\begin{aligned}\nna &= (1 + 1 + \\dots + 1)a = 1 \\cdot a + 1 \\cdot a + \\dots + 1 \\cdot a = a + a + \\dots + a.\n\\end{aligned}\n$$\n\n"
        "Es seien nun im Gegensatz zu unserer Behauptung $a, b$ solche zwei Zahlen des Zahlensystems, für welche das commutative Gesetz der Multiplikation nicht gültig ist. Wir dürfen dann, wie leicht ersichtlich, die Annahmen\n\n$$\na > 0, \\quad b > 0, \\quad ab - ba > 0\n$$\n\nmachen. Wegen der Forderung 6 in § 13 giebt es eine Zahl $c \\; (> 0)$, so dass\n\n$$\n(a + b + 1)c = ab - ba\n$$\n\nist. Endlich wählen wir eine Zahl $d$, die zugleich den Ungleichungen\n\n$$\nd > 0, \\quad d < 1, \\quad d < c\n$$\n\ngenügt, und bezeichnen mit $m$ und $n$ zwei solche ganze rationale Zahlen $\\ge 0$, für die\n\n$$\nmd \\le a < (m + 1)d \\quad \\text{bez.} \\quad nd \\le b < (n + 1)d\n$$\n\nwird. Das Vorhandensein solcher Zahlen $m, n$ ist eine unmittelbare Folgerung des Archimedischen Satzes (Satz 17 in § 13). Mit Rücksicht auf die Bemerkung zu Anfang dieses Beweises erhalten wir aus den letzteren Ungleichungen durch Multiplikation\n\n$$\n\\begin{aligned}\nab &< mnd^2 + (m + n + 1)d^2, \\\\\nba &\\ge mnd^2,\n\\end{aligned}\n$$\n\nalso durch Subtraktion\n\n$$\nab - ba < (m + n + 1)d^2.\n$$\n\nNun ist\n\n$$\nmd \\le a, \\quad nd \\le b, \\quad d < 1\n$$\n\nund folglich\n\n$$\n(m + n + 1)d < a + b + 1,\n$$\n\nd. h.\n\n$$\nab - ba < (a + b + 1)d\n$$\n\noder wegen $d < c$\n\n$$\nab - ba < (a + b + 1)c.\n$$\n\nDiese Ungleichung widerspricht der Bestimmung der Zahl $c$, und damit ist der Beweis für den Satz 38 erbracht."),
    ),
    # § 33 Non-Archimedean skew-field Omega(s, t) with ts = 2st
    (
        3888,
        3994,
        ("Beweis. Es sei $t$ ein Parameter und $T$ irgend ein Ausdruck mit einer endlichen oder unendlichen Gliederzahl von der Gestalt\n\n$$\nT = r_0 t^n + r_1 t^{n+1} + r_2 t^{n+2} + r_3 t^{n+3} + \\dots;\n$$\n\ndarin mögen $r_0 \\; (\\neq 0), r_1, r_2, \\dots$ beliebige rationale Zahlen bedeuten und $n$ sei eine beliebige ganze rationale Zahl $\\gtreqless 0$. Ferner sei $s$ ein anderer Parameter und $S$ irgend ein Ausdruck mit einer endlichen oder unendlichen Gliederzahl von der Gestalt\n\n$$\nS = s^m T_0 + s^{m+1} T_1 + s^{m+2} T_2 + \\dots;\n$$\n\ndarin mögen $T_0 \\; (\\neq 0), T_1, T_2, \\dots$ beliebige Ausdrücke von der Gestalt $T$ bezeichnen und $m$ sei wiederum eine beliebige ganze rationale Zahl $\\gtreqless 0$. Die Gesamtheit aller Ausdrücke von der Gestalt $S$ sehen wir als ein complexes Zahlensystem $\\Omega(s, t)$ an, in dem wir folgende Rechnungsregeln festsetzen: man rechne mit $s$ und $t$, wie mit Parametern nach den Regeln 7–11 in § 13, während man an Stelle der Regel 12 stets die Formel\n\n$$\n(1)\\quad ts = 2st\n$$\n\nanwende.\n\n"
        "Sind nun $S', S''$ irgend zwei Ausdrücke von der Gestalt $S$:\n\n$$\n\\begin{aligned}\nS' &= s^{m'} T'_0 + s^{m'+1} T'_1 + s^{m'+2} T'_2 + \\dots, \\\\\nS'' &= s^{m''} T''_0 + s^{m''+1} T''_1 + s^{m''+2} T''_2 + \\dots,\n\\end{aligned}\n$$\n\nso kann man offenbar durch Zusammenfügung einen neuen Ausdruck $S' + S''$ bilden, der wiederum von der Gestalt $S$ und zugleich eindeutig bestimmt ist; dieser Ausdruck $S' + S''$ heisst die *Summe* der durch $S', S''$ dargestellten Zahlen.\n\n"
        "Durch gliedweise Multiplikation der beiden Ausdrücke $S', S''$ gelangen wir zunächst zu einem Ausdrucke von der Gestalt\n\n$$\n\\begin{aligned}\nS'S'' &= s^{m'}T'_0 s^{m''}T''_0 + (s^{m'}T'_0 s^{m''+1}T''_1 + s^{m'+1}T'_1 s^{m''}T''_0) \\\\\n&\\quad + (s^{m'}T'_0 s^{m''+2}T''_2 + s^{m'+1}T'_1 s^{m''+1}T''_1 + s^{m'+2}T'_2 s^{m''}T''_0) + \\dots.\n\\end{aligned}\n$$\n\nDieser Ausdruck wird bei Benutzung der Formel (1) offenbar ein eindeutig bestimmter Ausdruck von der Gestalt $S$; der letztere heisse das *Produkt* der durch $S'$ dargestellten Zahl in die durch $S''$ dargestellte Zahl.\n\n"
        "Bei der so festgesetzten Rechnungsweise leuchtet die Gültigkeit der Rechnungsregeln 1–5 in § 13 unmittelbar ein. Auch die Gültigkeit der Vorschrift 6 in § 13 ist nicht schwer einzusehen. Zu dem Zwecke nehmen wir an, es seien etwa\n\n$$\nS' = s^{m'} T'_0 + s^{m'+1} T'_1 + s^{m'+2} T'_2 + \\dots\n$$\n\nund\n\n$$\nS''' = s^{m'''} T'''_0 + s^{m'''+1} T'''_1 + s^{m'''+2} T'''_2 + \\dots\n$$\n\ngegebene Ausdrücke von der Gestalt $S$, und bedenken, dass unseren Festsetzungen entsprechend der erste Coefficient $r'_0$ aus $T'_0$ von $0$ verschieden sein muss. Indem wir nun die nämlichen Potenzen von $s$ auf beiden Seiten einer Gleichung\n\n$$\n(2)\\quad S'S'' = S'''\n$$\n\nvergleichen, finden wir in eindeutig bestimmter Weise zunächst eine ganze Zahl $m''$ als Exponenten und sodann der Reihe nach gewisse Ausdrücke\n\n$$\nT''_0, \\; T''_1, \\; T''_2, \\; \\dots\n$$\n\nderart, dass der Ausdruck\n\n$$\nS'' = s^{m''} T''_0 + s^{m''+1} T''_1 + s^{m''+2} T''_2 + \\dots\n$$\n\nbei Benutzung der Formel (1) der Gleichung (2) genügt; hiermit ist der gewünschte Nachweis erbracht.\n\n"
        "Um endlich die Anordnung der Zahlen unseres Zahlensystems $\\Omega(s, t)$ zu ermöglichen, treffen wir folgende Festsetzungen. Eine Zahl des Systems heisse $<$ oder $> 0$, jenachdem in dem Ausdrucke $S$, der sie darstellt, der erste Coefficient $r_0$ von $T_0$ $<$ oder $> 0$ ausfällt. Sind irgend zwei Zahlen $a$ und $b$ des complexen Zahlensystems vorgelegt, so heisse $a < b$ bez. $a > b$, jenachdem $a - b < 0$ oder $> 0$ wird. Es leuchtet unmittelbar ein, dass bei diesen Festsetzungen die Regeln 13–16 in § 13 gültig sind, d. h. $\\Omega(s, t)$ ist ein Desarguessches Zahlensystem (vgl. § 28).\n\n"
        "Die Vorschrift 12 in § 13 ist, wie Gleichung (1) zeigt, für unser complexes Zahlensystem $\\Omega(s, t)$ nicht erfüllt und damit ist die Richtigkeit des Satzes 39 vollständig erkannt.\n\n"
        "In Uebereinstimmung mit Satz 38 gilt der Archimedische Satz (Satz 17 in § 13) für das soeben aufgestellte Zahlensystem $\\Omega(s, t)$ nicht.\n\n"
        "Es werde noch hervorgehoben, dass das Zahlensystem $\\Omega(s, t)$ — ebenso wie die in § 9 und § 12 benutzten Zahlensysteme $\\Omega$ und $\\Omega(t)$ — nur eine abzählbare Menge von Zahlen enthält."),
    ),
    # § 34 & § 35 Omega(s, t), Omega, A(p_1, ..., p_r)
    (4022, 4030, "stellte Desarguessche Zahlensystem $\\Omega(s, t)$ ins Auge und construiren mit Hülfe desselben auf die in § 29 beschriebene Art eine räumliche Geometrie, in der die sämtlichen Axiome I, II, III erfüllt sind. Trotzdem gilt der Pascalsche Satz in dieser Geometrie nicht, da das commutative Gesetz der Multiplikation in dem Desarguesschen Zahlensystem $\\Omega(s, t)$ nicht besteht. Die so aufgebaute „*Nicht-Pascalsche*“ Geometrie ist in Uebereinstimmung mit dem vorhin bewiesenen Satz 36 notwendig zugleich auch eine „*Nicht-Archimedische*“ Geometrie."),
    (4055, 4100, (
        "Axiome I 1–2, II–V gültig sind; nach Kap. III § 17 können wir dann vermittelst eines rechtwinkligen Axenkreuzes jedem Punkte ein Zahlenpaar $(x, y)$ und jeder Geraden ein Verhältnis von drei Zahlen $(u : v : w)$ entsprechen lassen; hierbei sind $x, y, u, v, w$ jedenfalls reelle Zahlen, von denen $u, v$ nicht beide verschwinden, und die Bedingung für die vereinigte Lage von Punkt und Geraden\n\n$$\nux + vy + w = 0\n$$\n\nbedeutet eine Gleichung im gewöhnlichen Sinne. Umgekehrt dürfen wir, falls $x, y, u, v, w$ Zahlen des in § 9 construirten algebraischen Bereiches $\\Omega$ sind und $u, v$ nicht beide verschwinden, gewiss annehmen, dass das Zahlenpaar $(x, y)$ und das Zahlentripel $(u : v : w)$ einen Punkt bez. eine Gerade in der vorgelegten Geometrie liefert.\n\n"
        "Führen wir für alle Punkte und Geraden, die in einem beliebigen ebenen Schnittpunktsatze auftreten, die betreffenden Zahlenpaare und Zahlentripel ein, so wird dieser Schnittpunktsatz aussagen, dass ein bestimmter, von gewissen Parametern $p_1, \\dots, p_r$ rational abhängiger Ausdruck $A(p_1, \\dots, p_r)$ mit reellen Coefficienten stets verschwindet, sobald wir für jene Parameter irgend welche Zahlen des in § 9 betrachteten Bereiches $\\Omega$ einsetzen. Wir schliessen hieraus, dass der Ausdruck $A(p_1, \\dots, p_r)$ auch identisch auf Grund der Rechnungsgesetze 7–12 in § 13 verschwinden muss.\n\n"
        "Da in der vorgelegten Geometrie nach § 22 der Desarguessche Satz gilt, so können wir gewiss auch die in § 24 eingeführte Streckenrechnung benutzen, und wegen der Gültigkeit des Pascalschen Satzes trifft für diese Streckenrechnung auch das commutative Gesetz der Multiplikation zu, sodass in dieser Streckenrechnung sämtliche Rechnungsgesetze 7–12 in § 13 gültig sind.\n\n"
        "Indem wir die Axen des bisher benutzten Axenkreuzes auch als Axen dieser neuen Streckenrechnung gewählt und die Einheitspunkte $E$ und $E'$ geeignet festgesetzt denken, erkennen wir die Uebereinstimmung der neuen Streckenrechnung mit der früheren Coordinatenrechnung.\n\n"
        "Um in der neuen Streckenrechnung das identische Verschwinden des Ausdruckes $A(p_1, \\dots, p_r)$ nachzuweisen, genügt die Anwendung des Desarguesschen und Pascalschen Satzes und damit erkennen"
    )),
    # § 36 & § 37 Omega(R), Omega, radicals
    (4146, 4146, "Aufgabe 3. Eine gegebene Strecke auf einer gegebenen"),
    (4212, 4215, "$CD$ in $H$ schneiden: dann ist $FH$ die gesuchte Senkrechte. In der That: die Winkel $\\angle BDC$ und $\\angle BEC$ sind als Winkel im Halbkreise über $BC$ Rechte und daher steht nach dem Satze vom"),
    (4221, 4239, "von Parallelen und Fällen von Loten erfordert. Es sei $\\beta$ der abzutragende Winkel und $A$ der Scheitel dieses Winkels. Wir ziehen die Gerade $l$ durch $A$ parallel zu der gegebenen Geraden, an welche der gegebene Winkel $\\beta$ angetragen werden soll. Von einem beliebigen Punkte $B$ eines Schenkels von $\\beta$ fällen wir Lote auf den anderen Schenkel des Winkels $\\beta$ und auf $l$. Die Fusspunkte dieser Lote seien $D$ und $C$. Das Fällen von Loten geschieht vermöge der Aufgaben 2 und 5. Sodann fällen wir von $A$ eine Senkrechte auf $CD$, ihr Fusspunkt sei $E$. Nach dem in § 14 ausgeführten Beweise ist $\\angle CAE \\equiv \\beta$; die Aufgabe 4 ist somit ebenfalls auf die Aufgaben 1 und 3 zurückgeführt und damit der Satz 40 vollständig bewiesen."),
    (4264, 4291, "Es sei ein System von bestimmten Punkten gegeben; wir setzen aus den Coordinaten dieser Punkte einen Bereich $R$ zusammen; derselbe enthält gewisse reelle Zahlen und gewisse willkürliche Parameter $p$. Nunmehr denken wir uns die Gesamtheit aller derjenigen Punkte, die durch Ziehen von Geraden und Abtragen von Strecken aus dem vorgelegten System von Punkten konstruirbar sind. Der Bereich, der von den Coordinaten dieser Punkte gebildet wird, heisse $\\Omega(R)$; derselbe enthält gewisse reelle Zahlen und Funktionen der willkürlichen Parameter $p$.\n\nUnsere Betrachtungen in § 17 zeigen, dass das Ziehen von Geraden und Parallelen analytisch auf die Anwendung der Addition, Multiplikation, Subtraktion, Division von Strecken hinausläuft; ferner lehrt die bekannte in § 9 aufgestellte Formel für die Drehung, dass das Abtragen von Strecken auf einer beliebigen Geraden keine andere analytische Operation erfordert, als die Quadratwurzel zu ziehen aus einer Summe von zwei Quadraten, deren Basen man bereits konstruirt hat. Umgekehrt kann man zufolge des Pythagoräischen Lehrsatzes vermöge eines rechtwinkligen Dreiecks die Quadratwurzel aus der Summe zweier Streckenquadrate durch Abtragen von Strecken stets konstruiren.\n\nAus diesen Betrachtungen geht hervor, dass der Bereich $\\Omega(R)$ alle diejenigen und nur solche reellen Zahlen und Funktionen der Parameter $p$ enthält, die aus den Zahlen und Parametern in $R$ vermöge einer endlichen Anzahl von Anwendungen von fünf Rechnungsoperationen, nämlich der vier elementaren Rechnungsoperationen hervorgehen, wenn man noch das Ziehen der Quadratwurzel"),
    (4314, 4337, "legen wir diejenige Geometrie zu Grunde, die in § 9 mit Hilfe des algebraischen Zahlenbereichs $\\Omega$ aufgebaut worden ist; in dieser Geometrie giebt es lediglich solche Strecken, die mittelst Lineals und Streckenübertragers konstruirbar sind, nämlich die durch Zahlen des Bereichs $\\Omega$ bestimmten Strecken.\n\nIst nun $\\omega$ irgend eine Zahl in $\\Omega$, so erkennen wir aus der Definition des Bereichs $\\Omega$ leicht, dass auch jede zu $\\omega$ conjugirte algebraische Zahl in $\\Omega$ liegen muss, und da die Zahlen des Bereichs $\\Omega$ offenbar sämtlich reell sind, so folgt hieraus, dass der Bereich $\\Omega$ nur solche reelle algebraische Zahlen enthalten kann, deren Conjugirte ebenfalls reell sind.\n\nWir stellen jetzt die Aufgabe, ein rechtwinkliges Dreieck mit der Hypotenuse $1$ und einer Kathete $|\\sqrt{2}| - 1$ zu konstruiren. Nun kommt die algebraische Zahl $\\sqrt{2|\\sqrt{2}| - 2}$, die den Zahlenwert der anderen Kathete ausdrückt, im Zahlenbereich $\\Omega$ nicht vor, da die zu ihr konjugirte Zahl $\\sqrt{-2|\\sqrt{2}| - 2}$ imaginär ausfällt. Die gestellte Aufgabe ist mithin in der zu Grunde gelegten Geometrie nicht lösbar, und kann daher überhaupt nicht mittelst Lineals und Streckenübertragers lösbar sein, obwohl die Konstruktion mittelst des Zirkels sofort ausführbar ist."),
    # § 38 Sums of squares, Satz 42 & 43, footnotes
    (
        4356,
        4534,
        ("Definition. Es sei $k$ ein beliebiger Zahlkörper; der Grad dieses Körpers $k$ heisse $m$, und die $m - 1$ zu $k$ konjugirten Zahlkörper mögen mit $k', k'', \\dots, k^{(m-1)}$ bezeichnet werden. Trifft es sich, dass unter den $m$ Körpern $k, k', \\dots, k^{(m-1)}$ einer oder mehrere aus lauter reellen Zahlen gebildet sind, so nennen wir diese Körper selbst reell; es seien diese Körper etwa $k, k', \\dots, k^{(s-1)}$. Eine Zahl $\\alpha$ des Körpers $k$ heisst in diesem Falle *total positiv* in $k$, falls die $s$ zu $\\alpha$ konjugirten bez. in $k, k', \\dots, k^{(s-1)}$ gelegenen Zahlen sämtlich positiv sind. Kommen dagegen in jedem der $m$ Körper $k, k', \\dots, k^{(m-1)}$ auch imaginäre Zahlen vor, so heisst eine jede Zahl $\\alpha$ in $k$ stets *total positiv*.\n\n"
        "Satz 42. Jede total positive Zahl in $k$ lässt sich als Summe von vier Quadraten darstellen, deren Basen ganze oder gebrochene Zahlen des Körpers $k$ sind.\n\n"
        "Der Beweis dieses Satzes bietet erhebliche Schwierigkeiten dar; er beruht wesentlich auf der Theorie der relativquadratischen Zahlkörper, die ich unlängst in mehreren Arbeiten @@FN:38_1@@ entwickelt habe. Es sei hier nur auf denjenigen Satz aus dieser Theorie hingewiesen, der die Bedingungen für die Lösbarkeit einer ternären Diophantischen Gleichung von der Gestalt\n\n$$\n\\alpha\\xi^2 + \\beta\\eta^2 + \\gamma\\zeta^2 = 0\n$$\n\nangiebt, worin die Coefficienten $\\alpha, \\beta, \\gamma$ gegebene Zahlen in $k$ und $\\xi, \\eta, \\zeta$ gesuchte Zahlen in $k$ bedeuten. Der Beweis des Satzes 42 wird durch wiederholte Anwendung des eben genannten Satzes erbracht.\n\n"
        "Aus dem Satze 42 folgen eine Reihe von Sätzen über die Darstellung solcher rationaler Funktionen einer Veränderlichen mit rationalen Coefficienten, die niemals negative Werte haben; ich hebe nur den folgenden Satz hervor, der uns im nächsten Paragraphen von Nutzen sein wird.\n\n"
        "Satz 43. Es bedeute $f(x)$ eine solche ganze rationale Funktion von $x$ mit rationalen Zahlencoefficienten, die niemals negative Werte annimmt, wenn man für $x$ beliebige reelle Werte einsetzt: dann lässt sich $f(x)$ stets als Quotient zweier Summen von Quadraten darstellen, so dass die sämtlichen Basen dieser Quadrate ganze rationale Funktionen von $x$ mit rationalen Coefficienten sind.\n\n"
        "Beweis. Den Grad der vorgelegten Funktion $f(x)$ wollen wir mit $m$ bezeichnen; offenbar muss derselbe jedenfalls gerade sein. Für den Fall $m = 0$, d. h. wenn $f(x)$ eine rationale Zahl ist, folgt die Richtigkeit des Satzes 43 unmittelbar aus dem Fermatschen Satze von der Darstellung einer positiven Zahl als Summe von vier Quadratzahlen. Wir nehmen nun an, der Satz sei bereits für die Funktionen vom Grade $2, 4, 6, \\dots, m - 2$ bewiesen, und zeigen dann seine Richtigkeit für den vorliegenden Fall einer Funktion $m$-ten Grades auf folgende Weise.\n\n"
        "Zunächst behandeln wir kurz die Annahme, dass $f(x)$ in das Produkt von zwei oder mehreren ganzen Funktionen von $x$ mit rationalen Coefficienten zerfällt. Ist $p(x)$ eine solche in $f(x)$ aufgehende Funktion, die selbst nicht mehr in ein Produkt von ganzen Funktionen mit rationalen Coefficienten zerlegt werden kann, so folgt aus dem vorausgesetzten definiten Charakter der Funktion $f(x)$ leicht, dass der Faktor $p(x)$ entweder in $f(x)$ zu einer geraden Potenz erhoben vorkommen muss oder dass $p(x)$ selbst definit, d. h. eine solche Funktion ist, die für reelle Werthe von $x$ niemals negativ ausfällt. Im ersteren Falle ist der Quotient $\\frac{f(x)}{\\{p(x)\\}^2}$, im letzteren Falle sind sowohl $p(x)$ als auch $\\frac{f(x)}{p(x)}$ wiederum definite Funktionen und diese Funktionen besitzen einen geraden Grad $< m$. Zufolge unserer Annahme sind daher im ersteren Falle $\\frac{f(x)}{\\{p(x)\\}^2}$, im letzteren Falle sowohl $p(x)$ wie auch $\\frac{f(x)}{p(x)}$ als Quotienten von Quadratsummen von der im Satze 43 angegebenen Art darstellbar, und daher gestattet notwendig in beiden Fällen auch die Funktion $f(x)$ die verlangte Darstellung.\n\n"
        "Wir behandeln nunmehr die Annahme, dass $f(x)$ nicht in das Produkt von zwei ganzen Funktionen mit rationalen Coefficienten zerlegt werden kann. Die Gleichung $f(\\vartheta) = 0$ definirt dann einen algebraischen Zahlkörper $k(\\vartheta)$ vom $m$-ten Grade, der nebst seinen sämtlichen conjugirten Körpern imaginär ausfällt. Da somit nach der Definition, die wir dem Satze 42 vorangestellt haben, jede in $k(\\vartheta)$ gelegene Zahl, also auch insbesondere die Zahl $-1$ total positiv in $k(\\vartheta)$ ist, so giebt es nach diesem Satz 42 eine Darstellung der Zahl $-1$ als Summe von $4$ Quadraten gewisser Zahlen in $k(\\vartheta)$; es sei\n\n$$\n(1)\\quad -1 = \\alpha^2 + \\beta^2 + \\gamma^2 + \\delta^2,\n$$\n\nwobei $\\alpha, \\beta, \\gamma, \\delta$ ganze oder gebrochene Zahlen in $k(\\vartheta)$ sind. Wir setzen\n\n$$\n\\begin{aligned}\n\\alpha &= a_1 \\vartheta^{m-1} + a_2 \\vartheta^{m-2} + \\dots + a_m = \\varphi(\\vartheta), \\\\\n\\beta &= b_1 \\vartheta^{m-1} + b_2 \\vartheta^{m-2} + \\dots + b_m = \\psi(\\vartheta), \\\\\n\\gamma &= c_1 \\vartheta^{m-1} + c_2 \\vartheta^{m-2} + \\dots + c_m = \\chi(\\vartheta), \\\\\n\\delta &= d_1 \\vartheta^{m-1} + d_2 \\vartheta^{m-2} + \\dots + d_m = \\rho(\\vartheta);\n\\end{aligned}\n$$\n\nhierin bedeuten $a_1, a_2, \\dots, a_m, \\dots, d_1, d_2, \\dots, d_m$ rationale Zahlencoefficienten und $\\varphi(\\vartheta), \\psi(\\vartheta), \\chi(\\vartheta), \\rho(\\vartheta)$ die betreffenden ganzen rationalen Funktionen vom $(m - 1)$-ten Grade in $\\vartheta$.\n\n"
        "Wegen (1) ist\n\n$$\n1 + \\{\\varphi(\\vartheta)\\}^2 + \\{\\psi(\\vartheta)\\}^2 + \\{\\chi(\\vartheta)\\}^2 + \\{\\rho(\\vartheta)\\}^2 = 0,\n$$\n\nund mit Rücksicht auf die Irreducibilität der Gleichung $f(x) = 0$ stellt daher der Ausdruck\n\n$$\nF(x) = 1 + \\{\\varphi(x)\\}^2 + \\{\\psi(x)\\}^2 + \\{\\chi(x)\\}^2 + \\{\\rho(x)\\}^2\n$$\n\nnotwendig eine solche ganze rationale Funktion von $x$ dar, die durch $f(x)$ teilbar ist. $F(x)$ ist offenbar eine definite Funktion vom $(2m - 2)$-ten oder von niederem Grade und daher wird der Quotient $\\frac{F(x)}{f(x)}$ eine definite Funktion vom $(m - 2)$-ten oder von niederem Grade in $x$ mit rationalen Coefficienten. Infolgedessen lässt sich im Hinblick auf unsere Annahme $\\frac{F(x)}{f(x)}$ als Quotient zweier Summen von Quadraten von der im Satze 43 angegebenen Art darstellen, und da $F(x)$ selbst eine solche Summe von Quadraten ist, so folgt, dass auch $f(x)$ ein Quotient zweier Summen von Quadraten von der im Satze 43 angegebenen Art sein muss. Damit ist der Beweis des Satzes 43 vollständig erbracht.\n\n"
        "Es dürfte sehr schwierig sein, die entsprechenden Thatsachen für ganze rationale Funktionen von zwei oder mehr Veränderlichen aufzustellen und zu beweisen, doch sei hier darauf hingewiesen, dass die Darstellbarkeit einer beliebigen definiten ganzen rationalen Funktion zweier Veränderlicher als Quotient von Quadratsummen ganzer Funktionen auf einem völlig anderen Wege von mir bewiesen worden ist — unter der Voraussetzung, dass für die darstellenden Funktionen nicht blos rationale, sondern beliebige reelle Coefficienten zulässig sind @@FN:38_2@@."),
    ),
    # § 39 Criterion for constructibility (Satz 44) & footnote block L4546
    (
        4541,
        4684,
        ("Es sei eine geometrische Konstruktionsaufgabe vorgelegt, die mittelst des Zirkels ausführbar ist; wir wollen dann ein Kriterium aufzustellen versuchen, welches unmittelbar aus der analytischen Natur der Aufgabe und ihrer Lösungen beurteilen lässt, ob die Konstruktion auch allein mittelst Lineals und Streckenübertragers ausführbar ist. Wir werden bei dieser Untersuchung auf den folgenden Satz geführt:\n\n"
        "Satz 44. Es sei eine geometrische Konstruktionsaufgabe vorgelegt von der Art, dass man bei analytischer Behandlung derselben die Coordinaten der gesuchten Punkte aus den Coordinaten der gegebenen Punkte lediglich durch rationale Operationen und durch Ziehen von Quadratwurzeln finden kann; es sei $n$ die kleinste Anzahl der Quadratwurzeln, die hierbei zur Berechnung der Coordinaten der Punkte ausreichen: soll dann die vorgelegte Konstruktionsaufgabe sich auch allein durch Ziehen von Geraden und Abtragen von Strecken ausführen lassen, so ist dafür notwendig und hinreichend, dass die geometrische Aufgabe genau $2^n$ reelle Lösungen besitzt und zwar für alle Lagen der gegebenen Punkte, d. h. für alle Werte der in den Coordinaten der gegebenen Punkte auftretenden willkürlichen Parameter.\n\n"
        "Beweis. Wir beweisen diesen Satz 44 ausschliesslich für den Fall, dass die Coordinaten der gegebenen Punkte rationale Funktionen eines Parameters $p$ mit rationalen Coefficienten sind.\n\n"
        "Die Notwendigkeit des aufgestellten Kriteriums leuchtet ein. Um zu zeigen, dass dasselbe auch hinreicht, setzen wir dieses Kriterium als erfüllt voraus und betrachten zunächst eine solche von jenen $n$ Quadratwurzeln, die bei der Berechnung der Coordinaten der gesuchten Punkte zuerst zu ziehen ist. Der Ausdruck unter dieser Quadratwurzel ist eine rationale Funktion $f_1(p)$ des Parameters $p$ mit rationalen Coefficienten; diese rationale Funktion darf für beliebige reelle Parameterwerte $p$ niemals negative Werte annehmen, da sonst entgegen der Voraussetzung die vorgelegte Aufgabe für gewisse Werte $p$ imaginäre Lösungen haben müsste. Aus Satz 43 schliessen wir daher, dass $f_1(p)$ als Quotient von Summen von Quadraten ganzer rationaler Funktionen darstellbar ist.\n\n"
        "Nunmehr zeigen die Formeln\n\n$$\n\\begin{aligned}\n\\sqrt{a^2 + b^2 + c^2} &= \\sqrt{(\\sqrt{a^2 + b^2})^2 + c^2}, \\\\\n\\sqrt{a^2 + b^2 + c^2 + d^2} &= \\sqrt{(\\sqrt{a^2 + b^2 + c^2})^2 + d^2}, \\\\\n&\\;\\;\\vdots\n\\end{aligned}\n$$\n\ndass allgemein das Ziehen der Quadratwurzel aus einer Summe von beliebig vielen Quadraten sich stets zurückführen lässt auf wiederholtes Ziehen der Quadratwurzel aus der Summe zweier Quadrate.\n\n"
        "Nehmen wir diese Bemerkung mit dem vorigen Ergebnisse zusammen, so erkennen wir, dass der Ausdruck $\\sqrt{f_1(p)}$ gewiss mittelst Lineals und Streckenübertragers construirt werden kann.\n\n"
        "Wir betrachten ferner eine solche von den $n$ Quadratwurzeln, die bei der Berechnung der Coordinaten der gesuchten Punkte an zweiter Stelle zu ziehen ist. Der Ausdruck unter dieser Quadratwurzel ist eine rationale Funktion $f_2(p, \\sqrt{f_1})$ des Parameters $p$ und der zuerst betrachteten Quadratwurzel; auch diese Funktion $f_2$ ist bei beliebigen reellen Parameterwerten $p$ und für jedes Vorzeichen von $\\sqrt{f_1}$ niemals negativer Werte fähig, da sonst entgegen der Voraussetzung die vorgelegte Aufgabe unter ihren $2^n$ Lösungen für gewisse Werte $p$ auch imaginäre Lösungen haben müsste. Aus diesem Umstande folgt, dass $f_2$ einer quadratischen Gleichung von der Gestalt\n\n$$\nf_2^2 - \\varphi_1(p)f_2 + \\psi_1(p) = 0\n$$\n\ngenügen muss, worin $\\varphi_1(p)$ und $\\psi_1(p)$ notwendig solche rationale Funktionen von $p$ mit rationalen Coefficienten sind, die für reelle Werte von $p$ niemals negative Werte besitzen. Aus der letzteren quadratischen Gleichung entnehmen wir\n\n$$\nf_2 = \\frac{f_2^2 + \\psi_1(p)}{\\varphi_1(p)}.\n$$\n\n"
        "Nun müssen wiederum nach Satz 43 die Funktionen $\\varphi_1(p)$ und $\\psi_1(p)$ Quotienten von Summen von Quadraten rationaler Funktionen sein und andererseits ist nach dem Vorigen der Ausdruck $f_2$ mittelst Lineals und Streckenübertragers construirbar; der gefundene Ausdruck für $f_2$ zeigt somit, dass $f_2$ ein Quotient von Summen von Quadraten construirbarer Funktionen ist. Also lässt sich auch der Ausdruck $\\sqrt{f_2}$ mittelst Lineals und Streckenübertragers construiren.\n\n"
        "Ebenso wie der Ausdruck $f_2$ erweist sich auch jede andere rationale Funktion $\\varphi_2(p, \\sqrt{f_1})$ von $p$ und $\\sqrt{f_1}$ als Quotient zweier Summen von Quadraten construirbarer Funktionen, sobald diese rationale Funktion $\\varphi_2$ die Eigenschaft besitzt, niemals negative Werte anzunehmen bei reellem Parameter $p$ und für beiderlei Vorzeichen von $\\sqrt{f_1}$.\n\n"
        "Diese Bemerkung gestattet uns, das eben begonnene Schlussverfahren in folgender Weise fortzusetzen.\n\n"
        "Es sei $f_3(p, \\sqrt{f_1}, \\sqrt{f_2})$ ein solcher Ausdruck, der von den drei Argumenten $p, \\sqrt{f_1}, \\sqrt{f_2}$ in rationaler Weise abhängt und aus dem bei der analytischen Berechnung der Coordinaten der gesuchten Punkte an dritter Stelle die Quadratwurzel zu ziehen ist. Wie vorhin schliessen wir, dass $f_3$ bei beliebigen reellen Werten $p$ und für beiderlei Vorzeichen von $\\sqrt{f_1}$ und $\\sqrt{f_2}$ niemals negative Werte annehmen darf; dieser Umstand wiederum zeigt, dass $f_3$ einer quadratischen Gleichung von der Gestalt\n\n$$\nf_3^2 - \\varphi_2(p, \\sqrt{f_1})f_3 + \\psi_2(p, \\sqrt{f_1}) = 0\n$$\n\ngenügen muss, worin $\\varphi_2$ und $\\psi_2$ solche rationale Funktionen von $p$ und $\\sqrt{f_1}$ bedeuten, die für reelle Werte $p$ und beiderlei Vorzeichen von $\\sqrt{f_1}$ negativer Werte nicht fähig sind. Da mithin $\\varphi_2$ und $\\psi_2$ nach der vorigen Bemerkung Quotienten zweier Summen von Quadraten construirbarer Ausdrücke sind, so folgt das gleiche auch für den Ausdruck\n\n$$\nf_3 = \\frac{f_3^2 + \\psi_2(p, \\sqrt{f_1})}{\\varphi_2(p, \\sqrt{f_1})}\n$$\n\nund mithin ist auch $\\sqrt{f_3}$ mittelst Lineals und Streckenübertragers construirbar.\n\n"
        "Die Fortsetzung dieser Schlussweise führt zum Beweise des Satzes 44 in dem betrachteten Falle eines Parameters $p$."),
    ),
    # Schlusswort e and pi, Lindemann's, Abel's
    (4730, 4735, "fruchtbarer Forschungsgebiete. Wir erinnern nur an *Abel*'s Beweis für die Unmöglichkeit der Auflösung der Gleichungen fünften Grades durch Wurzelziehen, ferner an die Erkenntnis der Unbeweisbarkeit des Parallelenaxioms und an *Hermite*'s und *Lindemann*'s Sätze von der Unmöglichkeit, die Zahlen $e$ und $\\pi$ auf algebraischem Wege zu construiren."),
]

# Verbatim 1899 Teubner footnotes mapped to @@FN:<id>@@ markers
FOOTNOTES_DE: dict[str, str] = {
    "0_1": "Man vergleiche die zusammenfassenden und erläuternden Berichte von G. Veronese, „*Grundzüge der Geometrie*“, deutsch von A. Schepp, Leipzig 1894 (Anhang), und F. Klein, „Zur ersten Verteilung des Lobatschefskij-Preises“, *Math. Ann.* Bd. 50.",
    "3_1": "Diese Axiome hat zuerst M. Pasch in seinen *Vorlesungen über neuere Geometrie*, Leipzig 1882, ausführlich untersucht. Insbesondere rührt das Axiom II 5 von M. Pasch her.",
    "10_1": "Vergl. meine Vorlesung über Euklidische Geometrie (Wintersemester 1898/99), die nach einer Ausarbeitung des Herrn Dr. von Schaper für meine Zuhörer autographirt worden ist.",
    "12_1": "G. Veronese hat in seinem tiefsinnigen Werke, *Grundzüge der Geometrie*, deutsch von A. Schepp, Leipzig 1894 ebenfalls den Versuch gemacht, eine Geometrie aufzubauen, die von dem Archimedischen Axiom unabhängig ist.",
    "14_1": "F. Schur hat einen interessanten Beweis des Pascalschen Satzes auf Grund der sämtlichen Axiome I–II, IV in den *Math. Ann.* Bd. 51 veröffentlicht.",
    "21_1": "*Sitzungsberichte der Dorpater Naturf. Ges.* 1892.",
    "21_2": "*Grundlagen der Geometrie*, Bd. 2, Absch. 5, § 5, 1898.",
    "21_3": "*Monatshefte für Math. und Phys.*, Jahrgang 5, 1894.",
    "26_1": "Die Figuren 44, 45 und 47 hat Herr Dr. von Schaper entworfen und auch die zugehörigen Beweise ausgeführt.",
    "38_1": "„Ueber die Theorie der relativquadratischen Zahlkörper“, *Jahresber. d. Deutschen Math.-Vereinigung* Bd. 6, 1899 und *Math. Ann.* Bd. 51; ferner: „Ueber die Theorie der relativ-Abelschen Zahlkörper“, *Nachr. d. K. Ges. d. Wiss. zu Göttingen* 1898.",
    "38_2": "„Ueber ternäre definite Formen“, *Acta Mathematica* Bd. 17.",
}

# Exact OCR word corrections for Teubner italic/fraktur scan misreads (preserving 1899 spelling)
OCR_WORD_FIXES: dict[str, str] = {
    "ArcJiimedische": "Archimedische",
    "PunJct": "Punkt",
    "PunJcte": "Punkte",
    "Punlcte": "Punkte",
    "Tunide": "Punkte",
    "Jiaben": "haben",
    "nicJit": "nicht",
    "niclit": "nicht",
    "ivenigstens": "wenigstens",
    "tvenigstens": "wenigstens",
    "iveiteren": "weiteren",
    "ivenn": "wenn",
    "ivir": "wir",
    "zivei": "zwei",
    "entiveder": "entweder",
    "notivendig": "notwendig",
    "notivendige": "notwendige",
    "beiveisbar": "beweisbar",
    "gebrocJiene": "gebrochene",
    "inJialtsgleiche": "inhaltsgleiche",
    "inhaltsgleichc": "inhaltsgleiche",
    "räumlicJien": "räumlichen",
    "Konstruläionsaufgaben": "Konstruktionsaufgaben",
    "EuMidischen": "Euklidischen",
    "NicM-": "Nicht-",
    "Pechteck": "Rechteck",
    "Pechtecke": "Rechtecke",
    "Bechteck": "Rechteck",
    "ßaume": "Raume",
    "Räume": "Raume",
    "ßezeichnungsweise": "Bezeichnungsweise",
    "ßeweismethode": "Beweismethode",
    "schrafiirten": "schraffirten",
    "oiTenbar": "offenbar",
    "paraUel": "parallel",
    "entstellt": "entsteht",
    "uud": "und",
    "anch": "auch",
    "lägst": "lässt",
    "aasfällt": "ausfällt",
    "einesParameters": "eines Parameters",
    "fürDreiecke": "für Dreiecke",
    "DesarguesscherSatz": "Desarguesscher Satz",
    "jedemDreiecke": "jedem Dreiecke",
    "mithinist": "mithin ist",
    "Anlas s": "Anlass",
    "d. li,": "d. h.",
    "class dabei": "dass dabei",
    '"Weise': "Weise",
    '"Wir': "Wir",
    '"Wenn': "Wenn",
    '"Wegen': "Wegen",
    '"Winkeln': "Winkeln",
    "Greometrie": "Geometrie",
    "Yerbindungsgeraden": "Verbindungsgeraden",
}


def _is_page_furniture(line: str) -> bool:
    """Return True if `line` is a running page header, sheet signature, or standalone figure/page marker."""
    s = line.strip()
    if not s:
        return False
    if re.match(r"^(?:\d+\s*[•.]?\s*)?Kap(?:itel)?\.\s+[IVXHLTI1l]+\b.*$", s):
        return True
    if re.match(r"^H[iu]l?bert,\s+Grundlagen\s+der\s+Geometrie.*$", s):
        return True
    if re.match(r"^[1-7]\*?$", s):
        return True
    if re.match(r"^\d{1,2}$", s):
        return True
    return bool(re.match(r"^Fig\.\s*\d+\.?$", s))


def _clean_german_chunk(raw_lines: list[str], unit_footnotes: list[str]) -> str:
    """Clean a section slice of 1899 German lines into valid RST with MathJax and footnotes."""
    cleaned_lines: list[str] = []
    for ln in raw_lines:
        if _is_page_furniture(ln):
            continue
        # Strip margin-attached `Fig. N.` at start or end of a prose line
        s = re.sub(r"^\s*Fig\.\s*\d+\.?\s+", "", ln)
        s = re.sub(r"\s+Fig\.\s*\d+\.?\s*$", "", s)
        cleaned_lines.append(s)

    text = "\n".join(cleaned_lines)

    # Protect already-restored math blocks (`$$...$$` and `$...$`) before hyphen/word cleanup
    math_store: dict[str, str] = {}
    m_idx = 0

    def _stash(val: str) -> str:
        nonlocal m_idx
        m_idx += 1
        tok = f"@@DEMATH{m_idx:05d}@@"
        math_store[tok] = val
        return tok

    text = re.sub(r"\$\$.*?\$\$", lambda m: _stash(m.group(0)), text, flags=re.DOTALL)
    text = re.sub(r"\$[^$\n]+\$", lambda m: _stash(m.group(0)), text)

    # Rejoin end-of-line hyphenated lowercase German syllabifications (`Grund-\nthatsachen` -> `Grundthatsachen`)
    text = re.sub(r"([a-zäöüß])-\s*\n\s*([a-zäöüß])", r"\1\2", text)
    # Normalize spaced hyphens like `Nicht - Archimedischen` -> `Nicht-Archimedischen`
    text = re.sub(r"\b(Nicht)\s*-\s*([A-ZÄÖÜ])", r"\1-\2", text)
    text = re.sub(r"\b(elementar)\s*-\s*(geometrischen)\b", r"\1-\2", text)

    # Collapse multi-spaces inside non-directive lines
    norm_lines: list[str] = []
    for ln in text.splitlines():
        st = ln.strip()
        if not st:
            norm_lines.append("")
        elif st.startswith(("* ", "| ", ".. ")):
            norm_lines.append(re.sub(r"  +", " ", st))
        else:
            norm_lines.append(re.sub(r"  +", " ", st))
    text = "\n".join(norm_lines)

    # Apply verified OCR word fixes
    for bad, good in OCR_WORD_FIXES.items():
        text = text.replace(bad, good)

    # Normalize German quotation marks `„..."` -> `„...“`
    text = re.sub(r'„([^"“”\n]+)"-?', r"„\1“", text)

    # Resolve footnote placeholders `@@FN:key@@` into sequential per-unit `[#fnN]_`
    def _repl_fn(m: re.Match[str]) -> str:
        fn_key = m.group(1)
        unit_footnotes.append(FOOTNOTES_DE[fn_key])
        return f"[#fn{len(unit_footnotes)}]_"

    text = re.sub(r"@@FN:([0-9_]+)@@", _repl_fn, text)

    # Merge wrapped prose paragraphs while preserving display math blocks, lists, and line blocks
    blocks: list[str] = []
    for para in re.split(r"\n\s*\n", text):
        p = para.strip()
        if not p:
            continue
        if p.startswith(("* ", "| ", ".. ")) or re.match(r"^@@DEMATH\d+@@$", p):
            blocks.append(p)
        else:
            merged = " ".join(x.strip() for x in p.splitlines() if x.strip())
            # Format structural German lead-ins (`Erklärung.`, `Definition.`, `Beweis.`, `Aufgabe N.`, `Satz N.`)
            merged = re.sub(r"^(Erklärung|Definition|Beweis)\s*[:.]\s+", r"**\1.** ", merged)
            merged = re.sub(r"^Aufgabe\s+(\d+)\.\s+", r"**Aufgabe \1.** ", merged)
            merged = re.sub(r"^(I{1,3}|IV|V)\s*(\d+)\.\s+", r"**\1 \2.** ", merged)
            m_satz = re.match(r"^Satz\s+(\d+)(\s*(?:\[#fn\d+\]_\s*)?(?:\([^)]+\))?\s*\.)\s*(.*)$", merged)
            if not m_satz:
                m_satz = re.match(r"^Satz\s+(\d+)\.\s*(\([^)]+\)\.)\s*(.*)$", merged)
                if m_satz:
                    s_num, paren, rest = m_satz.group(1), m_satz.group(2), m_satz.group(3)
                    merged = f".. _grundlagen-de-thm-{s_num}:\n\n**Satz {s_num}.** *{paren}* {rest}"
            else:
                s_num, tail_head, rest = m_satz.group(1), m_satz.group(2).strip(), m_satz.group(3)
                # Keep `[#fnN]_` outside `**...**` for valid RST!
                fn_in_head = re.search(r"(\[#fn\d+\]_)", tail_head)
                if fn_in_head:
                    fn_tok = fn_in_head.group(1)
                    clean_tail = tail_head.replace(fn_tok, "").strip()
                    merged = f".. _grundlagen-de-thm-{s_num}:\n\n**Satz {s_num}** {fn_tok} **{clean_tail}** {rest}"
                else:
                    merged = f".. _grundlagen-de-thm-{s_num}:\n\n**Satz {s_num}{(' ' + tail_head) if not tail_head.startswith('.') else tail_head}** {rest}"
            blocks.append(merged)

    out = "\n\n".join(blocks)
    for tok, val in math_store.items():
        out = out.replace(tok, val)
    return re.sub(r"\n{3,}", "\n\n", out).strip()


def _prepare_patched_lines(txt_path: Path | None = None) -> list[str]:
    """Load `ia_grundlagendergeo00hilb_teubner_1899.txt` and apply length-preserving 1-indexed patches."""
    root = default_repo_root()
    path = txt_path or (root / "resources" / "grundlagen" / "sources" / "ia_grundlagendergeo00hilb_teubner_1899.txt")
    lines = path.read_text(encoding="utf-8").splitlines()
    for start_1, end_1, replacement in LINE_SPAN_PATCHES:
        span_len = end_1 - start_1 + 1
        lines[start_1 - 1 : end_1] = [replacement] + [""] * (span_len - 1)
    return lines


def _render_figure_directive_de(sec_num: int) -> str:
    """Emit `.. picture::` directives if `SECTIONS_META[sec_num]` specifies SVG figures."""
    meta = SECTIONS_META.get(sec_num, {})
    blocks: list[str] = []
    for key in ("figure", "figure_extra"):
        fig = meta.get(key)
        if fig:
            svg_name, fig_title, alt_text = fig
            blocks.append(
                f"\n\n.. picture:: /_static/figures/{svg_name}\n"
                f"   :alt: {alt_text}\n"
                f"   :caption: **{fig_title}.** {alt_text}\n"
            )
    return "".join(blocks)


VOLLSTAENDIGKEIT_NOTE_DE = """

.. admonition:: [Philologische Editionsnotiz: Das Axiom der Vollständigkeit (1900 / 1902 / 1903)]
   :class: note

   Die vorliegende **Teubner-Festschrift von Juni 1899** (Erste Auflage) enthält in der Axiomgruppe V ausschliesslich das obige **Archimedische Axiom**. Erst in seinem Vortrag *„Über den Zahlbegriff“* (*Jahresbericht der Deutschen Mathematiker-Vereinigung*, Bd. 8, 1900, S. 180–184), in L. Laugels französischer Ausgabe (1900), in E. J. Townsends englischer Übersetzung (:ref:`Chapter I, § 8 <grundlagen-en-s8>`, 1902) sowie ab der zweiten deutschen Auflage (1903) fügte Hilbert als Axiom **V 2** das **Axiom der Vollständigkeit** hinzu:

      **Axiom der Vollständigkeit (V 2).** *Die Elemente (Punkte, Geraden, Ebenen) der Geometrie bilden ein System von Dingen, welches bei Aufrechterhaltung sämtlicher genannten Axiome keiner Erweiterung mehr fähig ist; d. h.: zu dem System der Punkte, Geraden, Ebenen ist es nicht möglich, ein anderes System von Dingen hinzuzufügen, so dass in dem durch Zusammensetzung entstehenden System sämtliche aufgeführten Axiome I–IV, V 1 erfüllt sind.*
"""

SCHLUSSWORT_NOTE_DE = """

.. admonition:: [Philologische Editionsnotiz: Erweiterungen des Schlusswortes und Anhang (1900–1902)]
   :class: note

   Das vorstehende **Schlusswort** giebt den vollständigen Originalwortlaut der **Göttinger Festschrift von 1899** wieder (einschliesslich Hilberts Danksagung an Hans von Schaper, Hermann Minkowski und Julius Sommer, die in Townsends englischer Ausgabe entfiel). In der französischen Ausgabe von 1900 und der englischen Ausgabe von 1902 (:ref:`Conclusion & Appendix <grundlagen-conclusion-en>`) erweiterte Hilbert das Schlusswort um die Ergebnisse der Göttinger Dissertation seines Schülers **Max Dehn** (1900) über Nicht-Legendresche und Semi-Euklidische Geometrien ohne Archimedisches Axiom und fügte in der Ausgabe von 1902 einen **Anhang** über die gruppentheoretisch-topologische Begründung der ebenen Geometrie (ohne Differenzierbarkeitsannahmen im Sinne von Sophus Lie) hinzu. Beide Texte sind im englischen Paralleltrack vollständig ediert und in den :ref:`Notes <grundlagen-conclusion-notes>` kommentiert.
"""


def build_german_units(txt_path: Path | None = None) -> dict[str, str]:
    """Generate the complete 9 German unit RST documents (`<unit>-de.rst`) from the 1899 Festschrift."""
    lines = _prepare_patched_lines(txt_path)
    units_rst: dict[str, str] = {}

    for unit in UNITS:
        slug = unit["slug"]
        unit_footnotes: list[str] = []
        head_title = f"{unit['num_de']}: {unit['title_de']}" if slug.startswith("chapter-") else unit["title_de"]
        bar = "=" * len(head_title)
        parts: list[str] = [
            ":layout: book",
            "",
            f".. _grundlagen-{slug}-de:",
            "",
            head_title,
            bar,
            "",
            ".. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, B. G. Teubner, Leipzig 1899)",
            "",
            ".. contents:: Gliederung",
            "   :local:",
            "   :depth: 2",
            "   :backlinks: none",
            "",
        ]

        if slug == "introduction":
            sec0_meta = SECTIONS_META[0]
            start_1, end_1 = SECTION_RANGES_DE[0]
            sec0_rst = _clean_german_chunk(lines[start_1 - 1 : end_1], unit_footnotes)
            parts.extend(
                [
                    ".. epigraph::",
                    "",
                    "   „So fängt denn alle menschliche Erkenntnis mit Anschauungen an, geht von da zu Begriffen und endigt mit Ideen.“",
                    "",
                    "   — Kant, *Kritik der reinen Vernunft*, Elementarlehre 2. T. 2. Abt.",
                    "",
                    ".. _grundlagen-de-s0:",
                    "",
                    ".. folio:: Einleitung",
                    f"   :page: {sec0_meta['page_de']}",
                    "",
                    "Einleitung",
                    "----------",
                    "",
                    sec0_rst,
                ]
            )
        elif slug == "conclusion":
            start_1, end_1 = SECTION_RANGES_DE[40]
            schluss_rst = _clean_german_chunk(lines[start_1 - 1 : end_1], unit_footnotes)
            parts.extend(
                [
                    ".. _grundlagen-de-s40:",
                    "",
                    ".. folio:: Schlusswort",
                    "   :page: 89",
                    "",
                    "Schlusswort",
                    "-----------",
                    "",
                    schluss_rst + SCHLUSSWORT_NOTE_DE,
                ]
            )
        else:
            for sec_num in unit["sections"]:
                smeta = SECTIONS_META[sec_num]
                stitle = smeta["title_de"]
                start_1, end_1 = SECTION_RANGES_DE[sec_num]
                sbody = _clean_german_chunk(lines[start_1 - 1 : end_1], unit_footnotes)
                fig_block = _render_figure_directive_de(sec_num)
                extra_note = VOLLSTAENDIGKEIT_NOTE_DE if sec_num == 8 else ""
                parts.extend(
                    [
                        f".. _grundlagen-de-s{sec_num}:",
                        "",
                        f".. folio:: § {sec_num}",
                        f"   :page: {smeta['page_de']}",
                        "",
                        stitle,
                        "-" * len(stitle),
                        "",
                        sbody + fig_block + extra_note,
                        "",
                    ]
                )

        if unit_footnotes:
            parts.extend(["", "----", "", ".. rubric:: Fussnoten", ""])
            for idx, fn_text in enumerate(unit_footnotes, 1):
                parts.append(f".. [#fn{idx}] {fn_text}")
                parts.append("")

        units_rst[slug] = "\n".join(parts).rstrip() + "\n"

    return units_rst
