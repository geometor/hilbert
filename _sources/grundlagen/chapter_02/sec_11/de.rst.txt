:layout: book
:canonical_id: § 11
:breadcrumb_title: § 11
:order: 11
:folio: S. 23
:tracks: English: index | Deutsch: de | Summary: summary | Notes: notes

.. _grundlagen-de-s11:

.. folio:: § 11
   :page: 23

§ 11: Die Unabhängigkeit der Congruenzaxiome
============================================

.. rubric:: David Hilbert — *Grundlagen der Geometrie* (Festschrift, Leipzig 1899)

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
