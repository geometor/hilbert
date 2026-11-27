:layout: book
:canonical_id: § 11
:breadcrumb_title: § 11
:order: 11
:folio: § 11
:tracks: English: index | German: de | Summary: summary | Notes: notes

.. _grundlagen-de-s11:

.. folio:: § 11
   :page: 23

§ 11: Die Unabhängigkeit der Congruenzaxiome
============================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

Wir werden die Unabhängigkeit der Congruenzaxiome erkennen, indem wir den Nachweis führen, dass das Axiom IV 6 oder, was auf das nämliche hinausläuft, der erste Congruenzsatz für Dreiecke, d. i. Satz 10 durch logische Schlüsse nicht aus den übrigen Axiomen I, II, III, IV 1—5, V abgeleitet werden kann.

Wir wählen die Punkte, Geraden, Ebenen der gewöhnlichen Geometrie auch als Elemente der neuen räumlichen Geometrie und definiren das Abtragen der Winkel ebenfalls wie in der gewöhnlichen Geometrie, etwa in der Weise, wie in § 9 auseinandergesetzt worden ist ; dagegen definiren wir das Abtragen der Strecken auf andere Art. Die zwei Punkte :math:`A_1, A_2` mögen in der gewöhnlichen Geometrie die Coordinaten :math:`x_1, y_1, z_1` bez. :math:`x_2, y_2, z_2` haben; dann bezeichnen wir den positiven Wert von

.. math::

   \sqrt{(x_1 - x_2 + y_1 - y_2)^2 + (y_1 - y_2)^2 + (z_1 - z_2)^2}

als die *Länge* der Strecke :math:`A_1A_2` und nun sollen zwei beliebige Strecken :math:`A_1A_2` und :math:`A'_1A'_2` einander congruent heissen, wenn sie im eben festgesetzten Sinne gleiche Längen haben.

Es leuchtet unmittelbar ein, dass in der so hergestellten räumlichen Geometrie die Axiome I, II, III, IV 1–2, 4–5, V gültig sind.

Um zu zeigen, dass auch das Axiom IV 3 erfüllt ist, wählen wir eine beliebige Gerade :math:`a` und auf ihr drei Punkte :math:`A_1, A_2, A_3`, sodass :math:`A_2` zwischen :math:`A_1` und :math:`A_3` liegt. Die Punkte :math:`x, y, z` der Geraden :math:`a` seien durch die Gleichungen

.. math::

   x = \lambda t + \lambda', \quad y = \mu t + \mu', \quad z = \nu t + \nu'

gegeben, worin :math:`\lambda, \lambda', \mu, \mu', \nu, \nu'` gewisse Constante und :math:`t` einen Parameter bedeutet. Sind :math:`t_1, t_2 \; (< t_1), t_3 \; (< t_2)` die Parameterwerte, die den Punkten :math:`A_1, A_2, A_3` entsprechen, so finden wir für die Längen der drei Strecken :math:`A_1A_2`, :math:`A_2A_3` und :math:`A_1A_3` bez. die Ausdrücke:

.. math::

   (t_1 - t_2)|\sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2}|, \quad (t_2 - t_3)|\sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2}|, \quad (t_1 - t_3)|\sqrt{(\lambda + \mu)^2 + \mu^2 + \nu^2}|,

und mithin ist die Summe der Längen der Strecken :math:`A_1A_2` und :math:`A_2A_3` gleich der Länge der Strecke :math:`A_1A_3`; dieser Umstand bedingt die Gültigkeit des Axioms IV 3.

Das Axiom IV 6 oder vielmehr der erste Congruenzsatz für Dreiecke ist in unserer Geometrie nicht immer erfüllt. Betrachten wir nämlich in der Ebene :math:`z = 0` die vier Punkte

| :math:`O` mit den Coordinaten :math:`x = 0, \quad y = 0`,
| :math:`A` mit den Coordinaten :math:`x = 1, \quad y = 0`,
| :math:`B` mit den Coordinaten :math:`x = 0, \quad y = 1`,
| :math:`C` mit den Coordinaten :math:`x = \frac{1}{2}, \quad y = \frac{1}{2}`,

so sind in den beiden (rechtwinkligen) Dreiecken :math:`OAC` und :math:`OBC` die Winkel bei :math:`C` und die anliegenden Seiten entsprechend congruent, da die Seite :math:`OC` beiden Dreiecken gemeinsam ist und die Strecken :math:`AC` und :math:`BC` die gleiche Länge :math:`\frac{1}{2}` besitzen. Dagegen haben die dritten Seiten :math:`OA` und :math:`OB` die Länge :math:`1`, bez. :math:`\sqrt{2}` und sind daher nicht einander congruent.

Es ist auch nicht schwer, in dieser Geometrie zwei Dreiecke zu finden, für welche das Axiom IV 6 selbst nicht erfüllt ist.

.. picture:: /_static/figures/fig_non_congruence_model.svg
   :alt: Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).
   :caption: **Anisotropic Countermodel to Congruence Axiom IV 6 (§ 11).** Hilbert's § 11 analytic geometry where segment congruence obeys IV 1–5 yet fails SAS (IV 6).
