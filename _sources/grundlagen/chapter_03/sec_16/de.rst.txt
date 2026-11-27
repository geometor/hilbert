:layout: book
:canonical_id: § 16
:breadcrumb_title: § 16
:order: 16
:folio: § 16
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s16:

.. folio:: § 16
   :page: 35

§ 16: Die Proportionen und die Aehnlichkeitssätze
=================================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Mit Hülfe der eben dargelegten Streckenrechnung lässt sich Euklids Lehre von den Proportionen einwandsfrei und ohne Archimedisches Axiom in folgender Weise begründen.

**Erklärung.** Sind :math:`a, b, a', b'` irgend vier Strecken, so soll die *Proportion*

.. math::

   a : b = a' : b'

nichts anderes bedeuten als die Streckengleichung

.. math::

   ab' = ba'.

**Definition.** Zwei Dreiecke heissen *ähnlich*, wenn entsprechende Winkel in ihnen congruent sind.

.. _grundlagen-de-thm-22:

**Satz 22.** Wenn :math:`a, b` und :math:`a', b'` entsprechende Seiten in zwei ähnlichen Dreiecken sind, so gilt die Proportion

.. math::

   a : b = a' : b'.

**Beweis.** Wir betrachten zunächst den besonderen Fall, wo die von :math:`a, b` und :math:`a', b'` eingeschlossenen Winkel in beiden Dreiecken Rechte sind, und denken uns die beiden Dreiecke in ein und denselben rechten Winkel eingetragen. Wir tragen sodann vom Scheitel aus auf einem Schenkel die Strecke :math:`1` ab und ziehen durch den Endpunkt dieser Strecke :math:`1` die Parallele zu den beiden Hypotenusen; dieselbe schneide auf dem anderen Schenkel die Strecke :math:`e` ab; dann ist nach unserer Definition des Streckenproduktes

.. math::

   b = ea, \quad b' = ea';

mithin haben wir

.. math::

   ab' = ba',

d. h.

.. math::

   a : b = a' : b'.

Nunmehr kehren wir zu dem allgemeinen Falle zurück. Wir construiren in jedem der beiden ähnlichen Dreiecke den Schnittpunkt :math:`S` bez. :math:`S'` der drei Winkelhalbirenden und fällen von diesem die drei Lote :math:`r` bez. :math:`r'` auf die Dreiecksseiten; die auf diesen entstehenden Abschnitte bezeichnen wir mit

.. math::

   a_b, \; a_c, \; b_c, \; b_a, \; c_a, \; c_b

bez.

.. math::

   a'_b, \; a'_c, \; b'_c, \; b'_a, \; c'_a, \; c'_b.

Der vorhin bewiesene spezielle Fall unseres Satzes liefert dann die Proportionen

.. math::

   \begin{aligned}
   a_b : r &= a'_b : r', & b_c : r &= b'_c : r', \\
   a_c : r &= a'_c : r', & b_a : r &= b'_a : r';
   \end{aligned}

aus diesen schliessen wir mittelst des distributiven Gesetzes

.. math::

   a : r = a' : r', \quad b : r = b' : r'

und folglich mit Rücksicht auf das commutative Gesetz der Multiplikation

.. math::

   a : b = a' : b'.

Aus dem eben bewiesenen Satze 22 entnehmen wir leicht den Fundamentalsatz in der Lehre von den Proportionen, der wie folgt lautet:

.. _grundlagen-de-thm-23:

**Satz 23.** Schneiden zwei Parallele auf den Schenkeln eines beliebigen Winkels die Strecken :math:`a, b` bez. :math:`a', b'` ab, so gilt die Proportion

.. math::

   a : b = a' : b'.

Umgekehrt, wenn vier Strecken :math:`a, b, a', b'` diese Proportion erfüllen und :math:`a, a'` und :math:`b, b'` je auf einem Schenkel eines beliebigen Winkels abgetragen werden, so sind die Verbindungsgeraden der Endpunkte von :math:`a, b` bez. von :math:`a', b'` einander parallel.
