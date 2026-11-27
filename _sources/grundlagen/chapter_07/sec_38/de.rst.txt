:layout: book
:canonical_id: § 38
:breadcrumb_title: § 38
:order: 38
:folio: § 38
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s38:

.. folio:: § 38
   :page: 82

§ 38: Die Darstellung algebraischer Zahlen und ganzer rationaler Funktionen als Summe von Quadraten
===================================================================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Die Frage nach der Ausführbarkeit geometrischer Konstruktionen mittelst Lineals und Streckenübertragers erfordert zu ihrer weiteren Behandlung einige Sätze zahlentheoretischen und algebraischen Charakters, die, wie mir scheint, auch an sich von Interesse sind.

Nach Fermat ist bekanntlich jede ganze rationale positive Zahl als Summe von vier Quadratzahlen darstellbar. Dieser Fermatsche Satz gestattet eine merkwürdige Verallgemeinerung von folgender Art:

**Definition.** Es sei :math:`k` ein beliebiger Zahlkörper; der Grad dieses Körpers :math:`k` heisse :math:`m`, und die :math:`m - 1` zu :math:`k` konjugirten Zahlkörper mögen mit :math:`k', k'', \dots, k^{(m-1)}` bezeichnet werden. Trifft es sich, dass unter den :math:`m` Körpern :math:`k, k', \dots, k^{(m-1)}` einer oder mehrere aus lauter reellen Zahlen gebildet sind, so nennen wir diese Körper selbst reell; es seien diese Körper etwa :math:`k, k', \dots, k^{(s-1)}`. Eine Zahl :math:`\alpha` des Körpers :math:`k` heisst in diesem Falle *total positiv* in :math:`k`, falls die :math:`s` zu :math:`\alpha` konjugirten bez. in :math:`k, k', \dots, k^{(s-1)}` gelegenen Zahlen sämtlich positiv sind. Kommen dagegen in jedem der :math:`m` Körper :math:`k, k', \dots, k^{(m-1)}` auch imaginäre Zahlen vor, so heisst eine jede Zahl :math:`\alpha` in :math:`k` stets *total positiv*.

.. _grundlagen-de-thm-42:

**Satz 42.** Jede total positive Zahl in :math:`k` lässt sich als Summe von vier Quadraten darstellen, deren Basen ganze oder gebrochene Zahlen des Körpers :math:`k` sind.

Der Beweis dieses Satzes bietet erhebliche Schwierigkeiten dar; er beruht wesentlich auf der Theorie der relativquadratischen Zahlkörper, die ich unlängst in mehreren Arbeiten [#fn1]_ entwickelt habe. Es sei hier nur auf denjenigen Satz aus dieser Theorie hingewiesen, der die Bedingungen für die Lösbarkeit einer ternären Diophantischen Gleichung von der Gestalt

.. math::

   \alpha\xi^2 + \beta\eta^2 + \gamma\zeta^2 = 0

angiebt, worin die Coefficienten :math:`\alpha, \beta, \gamma` gegebene Zahlen in :math:`k` und :math:`\xi, \eta, \zeta` gesuchte Zahlen in :math:`k` bedeuten. Der Beweis des Satzes 42 wird durch wiederholte Anwendung des eben genannten Satzes erbracht.

Aus dem Satze 42 folgen eine Reihe von Sätzen über die Darstellung solcher rationaler Funktionen einer Veränderlichen mit rationalen Coefficienten, die niemals negative Werte haben; ich hebe nur den folgenden Satz hervor, der uns im nächsten Paragraphen von Nutzen sein wird.

.. _grundlagen-de-thm-43:

**Satz 43.** Es bedeute :math:`f(x)` eine solche ganze rationale Funktion von :math:`x` mit rationalen Zahlencoefficienten, die niemals negative Werte annimmt, wenn man für :math:`x` beliebige reelle Werte einsetzt: dann lässt sich :math:`f(x)` stets als Quotient zweier Summen von Quadraten darstellen, so dass die sämtlichen Basen dieser Quadrate ganze rationale Funktionen von :math:`x` mit rationalen Coefficienten sind.

**Beweis.** Den Grad der vorgelegten Funktion :math:`f(x)` wollen wir mit :math:`m` bezeichnen; offenbar muss derselbe jedenfalls gerade sein. Für den Fall :math:`m = 0`, d. h. wenn :math:`f(x)` eine rationale Zahl ist, folgt die Richtigkeit des Satzes 43 unmittelbar aus dem Fermatschen Satze von der Darstellung einer positiven Zahl als Summe von vier Quadratzahlen. Wir nehmen nun an, der Satz sei bereits für die Funktionen vom Grade :math:`2, 4, 6, \dots, m - 2` bewiesen, und zeigen dann seine Richtigkeit für den vorliegenden Fall einer Funktion :math:`m`-ten Grades auf folgende Weise.

Zunächst behandeln wir kurz die Annahme, dass :math:`f(x)` in das Produkt von zwei oder mehreren ganzen Funktionen von :math:`x` mit rationalen Coefficienten zerfällt. Ist :math:`p(x)` eine solche in :math:`f(x)` aufgehende Funktion, die selbst nicht mehr in ein Produkt von ganzen Funktionen mit rationalen Coefficienten zerlegt werden kann, so folgt aus dem vorausgesetzten definiten Charakter der Funktion :math:`f(x)` leicht, dass der Faktor :math:`p(x)` entweder in :math:`f(x)` zu einer geraden Potenz erhoben vorkommen muss oder dass :math:`p(x)` selbst definit, d. h. eine solche Funktion ist, die für reelle Werthe von :math:`x` niemals negativ ausfällt. Im ersteren Falle ist der Quotient :math:`\frac{f(x)}{\{p(x)\}^2}`, im letzteren Falle sind sowohl :math:`p(x)` als auch :math:`\frac{f(x)}{p(x)}` wiederum definite Funktionen und diese Funktionen besitzen einen geraden Grad :math:`< m`. Zufolge unserer Annahme sind daher im ersteren Falle :math:`\frac{f(x)}{\{p(x)\}^2}`, im letzteren Falle sowohl :math:`p(x)` wie auch :math:`\frac{f(x)}{p(x)}` als Quotienten von Quadratsummen von der im Satze 43 angegebenen Art darstellbar, und daher gestattet notwendig in beiden Fällen auch die Funktion :math:`f(x)` die verlangte Darstellung.

Wir behandeln nunmehr die Annahme, dass :math:`f(x)` nicht in das Produkt von zwei ganzen Funktionen mit rationalen Coefficienten zerlegt werden kann. Die Gleichung :math:`f(\vartheta) = 0` definirt dann einen algebraischen Zahlkörper :math:`k(\vartheta)` vom :math:`m`-ten Grade, der nebst seinen sämtlichen conjugirten Körpern imaginär ausfällt. Da somit nach der Definition, die wir dem Satze 42 vorangestellt haben, jede in :math:`k(\vartheta)` gelegene Zahl, also auch insbesondere die Zahl :math:`-1` total positiv in :math:`k(\vartheta)` ist, so giebt es nach diesem Satz 42 eine Darstellung der Zahl :math:`-1` als Summe von :math:`4` Quadraten gewisser Zahlen in :math:`k(\vartheta)`; es sei

.. math::

   (1)\quad -1 = \alpha^2 + \beta^2 + \gamma^2 + \delta^2,

wobei :math:`\alpha, \beta, \gamma, \delta` ganze oder gebrochene Zahlen in :math:`k(\vartheta)` sind. Wir setzen

.. math::

   \begin{aligned}
   \alpha &= a_1 \vartheta^{m-1} + a_2 \vartheta^{m-2} + \dots + a_m = \varphi(\vartheta), \\
   \beta &= b_1 \vartheta^{m-1} + b_2 \vartheta^{m-2} + \dots + b_m = \psi(\vartheta), \\
   \gamma &= c_1 \vartheta^{m-1} + c_2 \vartheta^{m-2} + \dots + c_m = \chi(\vartheta), \\
   \delta &= d_1 \vartheta^{m-1} + d_2 \vartheta^{m-2} + \dots + d_m = \rho(\vartheta);
   \end{aligned}

hierin bedeuten :math:`a_1, a_2, \dots, a_m, \dots, d_1, d_2, \dots, d_m` rationale Zahlencoefficienten und :math:`\varphi(\vartheta), \psi(\vartheta), \chi(\vartheta), \rho(\vartheta)` die betreffenden ganzen rationalen Funktionen vom :math:`(m - 1)`-ten Grade in :math:`\vartheta`.

Wegen (1) ist

.. math::

   1 + \{\varphi(\vartheta)\}^2 + \{\psi(\vartheta)\}^2 + \{\chi(\vartheta)\}^2 + \{\rho(\vartheta)\}^2 = 0,

und mit Rücksicht auf die Irreducibilität der Gleichung :math:`f(x) = 0` stellt daher der Ausdruck

.. math::

   F(x) = 1 + \{\varphi(x)\}^2 + \{\psi(x)\}^2 + \{\chi(x)\}^2 + \{\rho(x)\}^2

notwendig eine solche ganze rationale Funktion von :math:`x` dar, die durch :math:`f(x)` teilbar ist. :math:`F(x)` ist offenbar eine definite Funktion vom :math:`(2m - 2)`-ten oder von niederem Grade und daher wird der Quotient :math:`\frac{F(x)}{f(x)}` eine definite Funktion vom :math:`(m - 2)`-ten oder von niederem Grade in :math:`x` mit rationalen Coefficienten. Infolgedessen lässt sich im Hinblick auf unsere Annahme :math:`\frac{F(x)}{f(x)}` als Quotient zweier Summen von Quadraten von der im Satze 43 angegebenen Art darstellen, und da :math:`F(x)` selbst eine solche Summe von Quadraten ist, so folgt, dass auch :math:`f(x)` ein Quotient zweier Summen von Quadraten von der im Satze 43 angegebenen Art sein muss. Damit ist der Beweis des Satzes 43 vollständig erbracht.

Es dürfte sehr schwierig sein, die entsprechenden Thatsachen für ganze rationale Funktionen von zwei oder mehr Veränderlichen aufzustellen und zu beweisen, doch sei hier darauf hingewiesen, dass die Darstellbarkeit einer beliebigen definiten ganzen rationalen Funktion zweier Veränderlicher als Quotient von Quadratsummen ganzer Funktionen auf einem völlig anderen Wege von mir bewiesen worden ist — unter der Voraussetzung, dass für die darstellenden Funktionen nicht blos rationale, sondern beliebige reelle Coefficienten zulässig sind [#fn2]_.

.. [#fn1] „Ueber die Theorie der relativquadratischen Zahlkörper“, *Jahresber. d. Deutschen Math.-Vereinigung* Bd. 6, 1899 und *Math. Ann.* Bd. 51; ferner: „Ueber die Theorie der relativ-Abelschen Zahlkörper“, *Nachr. d. K. Ges. d. Wiss. zu Göttingen* 1898.

.. [#fn2] „Ueber ternäre definite Formen“, *Acta Mathematica* Bd. 17.
