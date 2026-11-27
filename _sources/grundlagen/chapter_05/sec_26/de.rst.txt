:layout: book
:canonical_id: § 26
:breadcrumb_title: § 26
:order: 26
:folio: § 26
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s26:

.. folio:: § 26
   :page: 59

§ 26: Das associative Gesetz der Multiplikation und die beiden distributiven Gesetze in der neuen Streckenrechnung
==================================================================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Bei unseren Annahmen gilt auch für die Multiplikation der Strecken das associative Gesetz:

.. math::

   a(bc) = (ab)c.

Es seien auf der ersteren der beiden festen Geraden durch :math:`O` die Strecken

.. math::

   1 = OA, \quad b = OC, \quad c = OA'

und auf der anderen Geraden die Strecken

.. math::

   a = OG \quad \text{und} \quad b = OB

gegeben. Um gemäss der Vorschrift in § 24 der Reihe nach die Strecken

.. math::

   bc = OB' \; \text{und} \quad bc = OC', \quad ab = OD, \quad (ab)c = OD'

zu construiren, ziehen wir :math:`A'B'` parallel :math:`AB`, :math:`B'C'` parallel :math:`BC`, :math:`CD` parallel :math:`AG` sowie :math:`A'D'` parallel :math:`AD`; wie wir sofort erkennen, läuft dann unsere Behauptung darauf hinaus, dass auch :math:`CD` parallel :math:`C'D'` sein muss. Bezeichnen wir nun den Schnittpunkt der Geraden :math:`AD` und :math:`BC` mit :math:`F` und den Schnittpunkt der Geraden :math:`A'D'` und :math:`B'C'` mit :math:`F'`, so sind in den Dreiecken :math:`ABF` und :math:`A'B'F'` die entsprechenden Seiten einander parallel; nach dem Desarguesschen Satze liegen daher die drei Punkte :math:`O, F, F'` auf einer Geraden. Wegen dieses Umstandes können wir die zweite Aussage des Desarguesschen Satzes auf die beiden Dreiecke :math:`CDF` und :math:`C'D'F'` anwenden und erkennen hieraus, dass in der That :math:`CD` parallel :math:`C'D'` ist.

Wir beweisen endlich in unserer Streckenrechnung auf Grund des Desarguesschen Satzes die beiden distributiven Gesetze:

.. math::

   a(b + c) = ab + ac \quad \text{und} \quad (a + b)c = ac + bc.

Zum Beweise des ersteren Gesetzes dient die Figur 44 [#fn1]_. In derselben ist

.. math::

   b = OA', \quad c = OC', \quad ab = OB', \quad ab = OA'', \quad ac = OC'' \; \text{u. s. f.}

und es läuft

| :math:`B''D_2` parallel :math:`C''D_1` parallel zur festen Geraden :math:`OA'`,
| :math:`B'D_1` parallel :math:`C'D_2` parallel zur festen Geraden :math:`OA''`;

ferner ist :math:`A'A''` parallel :math:`C'C''` und

.. math::

   A'B'' \; \text{parallel} \; B'A'' \; \text{parallel} \; F'D_2 \; \text{parallel} \; F''D_1.

Die Behauptung läuft darauf hinaus, dass dann auch

.. math::

   F'F'' \; \text{parallel} \; A'A'' \; \text{und} \quad C'C''

sein muss.

Wir construiren folgende Hülfslinien:

| :math:`F''J` parallel der festen Geraden :math:`OA'`,
| :math:`F'J` parallel der festen Geraden :math:`OA''`;

die Schnittpunkte der Geraden :math:`C''D_1` und :math:`C'D_2`, :math:`C''D_1` und :math:`F'J`, :math:`C'D_2` und :math:`F''J` heissen :math:`G, H_1, H_2`; endlich erhalten wir noch die weiteren in der Figur 44 punktirten Hülfslinien durch Verbindung bereits construirter Punkte.

In den beiden Dreiecken :math:`A'B''C''` und :math:`F'D_2G` laufen die Verbindungsgeraden entsprechender Ecken einander parallel; nach der zweiten Aussage des Desarguesschen Satzes folgt daher, dass

.. math::

   A'C'' \; \text{parallel} \; F'G

sein muss. In den beiden Dreiecken :math:`A'C''F''` und :math:`F'GH_2` laufen ebenfalls die Verbindungsgeraden entsprechender Ecken einander parallel; wegen der vorhin gefundenen Thatsache folgt nach der zweiten Aussage des Desarguesschen Satzes, dass

.. math::

   A'F'' \; \text{parallel} \; F'H_2

sein muss. Da somit in den beiden wagerecht schraffirten Dreiecken :math:`OA'F''` und :math:`JH_2F'` die entsprechenden Seiten parallel sind, so lehrt der Desarguessche Satz, dass die drei Verbindungsgeraden

.. math::

   OJ, \quad A'H_2, \quad F''F'

sich in einem und demselben Punkte, etwa in :math:`P`, treffen.

Auf dieselbe Weise finden wir, dass auch

.. math::

   A''F' \; \text{parallel} \; F''H_1

sein muss und da somit in den beiden schräg schraffierten Dreiecken :math:`OA''F'` und :math:`JH_1F''` die entsprechenden Seiten parallel laufen, so treffen sich dem Desarguesschen Satze zufolge die drei Verbindungsgeraden

.. math::

   OJ, \quad A''H_1, \quad F'F''

ebenfalls in einem Punkte — dem Punkte :math:`P`.

Nunmehr laufen für die Dreiecke :math:`OA'A''` und :math:`JH_2H_1` die Verbindungsgeraden entsprechender Ecken durch den nämlichen Punkt :math:`P`, und mithin folgt, dass

.. math::

   H_1H_2 \; \text{parallel} \; A'A''

sein muss; mithin ist auch

.. math::

   H_1H_2 \; \text{parallel} \; C'C''.

Endlich betrachten wir die Figur :math:`F''H_2C'C''H_1F'F''`. Da in derselben

| :math:`F''H_2` parallel :math:`C'F'` parallel :math:`C''H_1`,
| :math:`H_2C'` parallel :math:`F''C''` parallel :math:`H_1F'`,
| :math:`C'C''` parallel :math:`H_1H_2`

ausfällt, so erkennen wir hierin die Figur 41 wieder, die wir in § 25 zum Beweise für das commutative Gesetz der Addition benutzt haben. Die entsprechenden Schlüsse wie dort zeigen dann, dass

.. math::

   F'F'' \; \text{parallel} \; H_1H_2

sein muss und da mithin auch

.. math::

   F'F'' \; \text{parallel} \; A'A''

ausfällt, so ist der Beweis unserer Behauptung vollständig erbracht.

Zum Beweise der zweiten Formel des distributiven Gesetzes dient die völlig verschiedene Figur 45. In derselben ist

.. math::

   1 = OD, \quad a = OA, \quad a = OB, \quad b = OG, \quad c = OD',

.. math::

   ac = OA', \quad ac = OB', \quad bc = OG' \; \text{u. s. f.}

und es läuft

| :math:`GH` parallel :math:`G'H'` parallel zur festen Geraden :math:`OA`,
| :math:`AH` parallel :math:`A'H'` parallel zur festen Geraden :math:`OB`

und ferner

| :math:`AB` parallel :math:`A'B'`,
| :math:`BD` parallel :math:`B'D'`,
| :math:`DG` parallel :math:`D'G'`,
| :math:`HJ` parallel :math:`H'J'`.

Die Behauptung läuft darauf hinaus, dass dann auch

.. math::

   DJ \; \text{parallel} \; D'J'

sein muss.

Wir bezeichnen die Punkte, in denen :math:`BD` und :math:`GD` die Gerade :math:`AH` treffen, bez. mit :math:`C` und :math:`F` und ferner die Punkte, in denen :math:`B'D'` und :math:`G'D'` die Gerade :math:`A'H'` treffen, bez. mit :math:`C'` und :math:`F'`; endlich ziehen wir noch die in der Figur 45 punktirten Hülfslinien :math:`FJ` und :math:`F'J'`.

In den Dreiecken :math:`ABC` und :math:`A'B'C'` laufen die entsprechenden Seiten parallel; mithin liegen nach dem Desarguesschen Satze die drei Punkte :math:`O, C, C'` auf einer Geraden. Ebenso folgt dann aus der Betrachtung der Dreiecke :math:`CDF` und :math:`C'D'F'`, dass :math:`O, F, F'` auf einer Geraden liegen, und die Betrachtung der Dreiecke :math:`FGH` und :math:`F'G'H'` lehrt, dass :math:`O, H, H'` Punkte einer Geraden sind. Nun laufen in den Dreiecken :math:`FHJ` und :math:`F'H'J'` die Verbindungsgeraden entsprechender Ecken durch den nämlichen Punkt :math:`O`, und mithin sind zufolge der zweiten Aussage des Desarguesschen Satzes die Geraden :math:`FJ` und :math:`F'J'` einander parallel. Endlich zeigt dann die Betrachtung der Dreiecke :math:`DFJ` und :math:`D'F'J'`, dass die Geraden :math:`DJ` und :math:`D'J'` einander parallel sind, und damit ist der Beweis unserer Behauptung vollständig erbracht.

.. [#fn1] Die Figuren 44, 45 und 47 hat Herr Dr. von Schaper entworfen und auch die zugehörigen Beweise ausgeführt.
