"""Generate calibrated, theme-adaptive SVG figures for Hilbert's Grundlagen der Geometrie.

All generated SVGs conform to the `.euclid-graphic` schema used by
`photon-platform/publish`'s `.. picture::` directive, supporting both light and
dark themes seamlessly while remaining standalone-viewable.
"""

from __future__ import annotations

import math
from pathlib import Path

SVG_STYLE = """  <style>
    :root {
      --geom-fg: #18181b;
      --geom-bg: #ffffff;
      --geom-point-stroke: #ffffff;
      --geom-poly-fill: #000000;
      --geom-accent: #c88a1e;
      --geom-assert: #16a34a;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --geom-fg: #d6cfc5;
        --geom-bg: #1e1e20;
        --geom-point-stroke: #1e1e20;
        --geom-poly-fill: #d6cfc5;
        --geom-accent: #e8b85a;
        --geom-assert: #5ec27e;
      }
    }
    .euclid-graphic {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-style: normal;
      font-weight: 700;
      background-color: var(--geom-bg);
    }
    .geom-line {
      stroke: var(--geom-fg);
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-bold {
      stroke: var(--geom-fg);
      stroke-width: 2.3;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-dashed {
      stroke: var(--geom-fg);
      stroke-width: 1.4;
      stroke-dasharray: 5, 3.5;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-accent-line {
      stroke: var(--geom-accent);
      stroke-width: 2.1;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-assert-line {
      stroke: var(--geom-assert);
      stroke-width: 2.2;
      stroke-dasharray: 6, 3;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
    }
    .geom-circle {
      stroke: var(--geom-fg);
      stroke-width: 1.6;
      fill: none;
    }
    .geom-arc {
      stroke: var(--geom-accent);
      stroke-width: 1.9;
      stroke-linecap: round;
      fill: none;
    }
    .geom-ang-arc {
      stroke: var(--geom-assert);
      stroke-width: 2.0;
      stroke-linecap: round;
      fill: none;
    }
    .geom-polygon {
      fill: var(--geom-poly-fill);
      fill-opacity: 0.05;
      stroke: none;
    }
    .geom-polygon-gnomon {
      fill: var(--geom-accent);
      fill-opacity: 0.14;
      stroke: none;
    }
    .geom-point {
      fill: var(--geom-fg);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.1;
    }
    .geom-point-accent {
      fill: var(--geom-accent);
      stroke: var(--geom-point-stroke);
      stroke-width: 1.1;
    }
    .geom-label {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 14px;
      font-weight: 700;
      fill: var(--geom-fg);
      user-select: none;
    }
    .geom-label-sm {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 11.5px;
      font-weight: 700;
      fill: var(--geom-fg);
      opacity: 0.85;
      user-select: none;
    }
  </style>"""


def _svg_wrap(graphic_id: str, section: str, width: int, height: int, body: list[str]) -> str:
    header = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" class="euclid-graphic" '
        f'data-graphic-id="{graphic_id}" data-proposition="{section}">'
    )
    return "\n".join([header, SVG_STYLE, *body, "</svg>", ""])


def _line(x1: float, y1: float, x2: float, y2: float, cls: str = "geom-line") -> str:
    return f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" class="{cls}" />'


def _poly(pts: list[tuple[float, float]], cls: str = "geom-polygon") -> str:
    s = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    return f'  <polygon points="{s}" class="{cls}" />'


def _pt(x: float, y: float, r: float = 3.3, cls: str = "geom-point") -> str:
    return f'  <circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" class="{cls}" />'


def _lbl(x: float, y: float, text: str, cls: str = "geom-label", anchor: str = "middle") -> str:
    return (
        f'  <text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" '
        f'class="{cls}">{text}</text>'
    )


def _ang_arc(
    cx: float, cy: float, r: float, p1: tuple[float, float], p2: tuple[float, float], cls: str = "geom-ang-arc"
) -> str:
    a1 = math.atan2(p1[1] - cy, p1[0] - cx)
    a2 = math.atan2(p2[1] - cy, p2[0] - cx)
    diff = (a2 - a1 + math.pi) % (2 * math.pi) - math.pi
    sweep = 1 if diff >= 0 else 0
    sx, sy = cx + r * math.cos(a1), cy + r * math.sin(a1)
    ex, ey = cx + r * math.cos(a2), cy + r * math.sin(a2)
    return f'  <path d="M {sx:.2f} {sy:.2f} A {r:.2f} {r:.2f} 0 0 {sweep} {ex:.2f} {ey:.2f}" class="{cls}" />'


def fig_betweenness_pasch() -> str:
    """§ 3 (Figs. 1-2): Linear betweenness A-B-C-D and Pasch's planar axiom II 5."""
    elems: list[str] = []
    # Left panel: linear betweenness A - B - C - D on line g
    elems.append(_lbl(125, 24, "II 1–4: Linear Order", "geom-label-sm"))
    elems.append(_line(24, 95, 226, 95, "geom-line"))
    for x, name in [(48, "A"), (98, "B"), (152, "C"), (200, "D")]:
        elems.append(_pt(x, 95))
        elems.append(_lbl(x, 82, name))
    elems.append(_lbl(220, 112, "g", "geom-label-sm"))

    # Right panel: Pasch's Axiom II 5
    elems.append(_lbl(375, 24, "II 5: Pasch's Axiom", "geom-label-sm"))
    A, B, C = (365.0, 44.0), (285.0, 158.0), (455.0, 158.0)
    elems.append(_poly([A, B, C]))
    elems.append(_line(*A, *B, "geom-bold"))
    elems.append(_line(*B, *C, "geom-bold"))
    elems.append(_line(*C, *A, "geom-bold"))

    # Secant line a piercing AB at P and AC at Q
    L1, L2 = (268.0, 118.0), (476.0, 86.0)
    # Exact intersections with AB and AC:
    def intersect(p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        return px, py

    P = intersect(A, B, L1, L2)
    Q = intersect(A, C, L1, L2)
    elems.append(_line(*L1, *L2, "geom-accent-line"))
    for pt, name, dx, dy in [
        (A, "A", 0, -10),
        (B, "B", -12, 14),
        (C, "C", 12, 14),
    ]:
        elems.append(_pt(*pt))
        elems.append(_lbl(pt[0] + dx, pt[1] + dy, name))
    elems.append(_pt(*P, 3.6, "geom-point-accent"))
    elems.append(_pt(*Q, 3.6, "geom-point-accent"))
    elems.append(_lbl(P[0] - 10, P[1] - 9, "P"))
    elems.append(_lbl(Q[0] + 12, Q[1] - 8, "Q"))
    elems.append(_lbl(478, 102, "a", "geom-label-sm"))
    return _svg_wrap("fig_betweenness_pasch", "S.3", 505, 185, elems)


def fig_sas_supplementary() -> str:
    """§ 7 (Figs. 6-8): Theorem 10 (SAS reductio) and Theorem 12 (Supplementary angles)."""
    elems: list[str] = []
    # Left triangle ABC
    A, B, C = (35.0, 145.0), (165.0, 145.0), (82.0, 48.0)
    elems.append(_poly([A, B, C]))
    elems.append(_line(*A, *B, "geom-bold"))
    elems.append(_line(*B, *C, "geom-bold"))
    elems.append(_line(*C, *A, "geom-bold"))
    elems.append(_ang_arc(*A, 22, B, C))
    elems.append(_ang_arc(*B, 22, C, A))
    for p, n, dx, dy in [(A, "A", -10, 15), (B, "B", 10, 15), (C, "C", 0, -10)]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))

    # Right triangle A'B'C' with auxiliary ray B'C'' (reductio of Theorem 10) and extension D' (Theorem 12)
    Ap, Bp, Cp = (245.0, 145.0), (375.0, 145.0), (292.0, 48.0)
    Cpp = (314.0, 68.0)  # distinct hypothetical intersection on A'C' ray
    # Keep C'' exactly on line A'C' at t=0.72 for clean reductio illustration:
    Cpp = (Ap[0] + 0.74 * (Cp[0] - Ap[0]), Ap[1] + 0.74 * (Cp[1] - Ap[1]))
    Dp = (450.0, 145.0)
    elems.append(_poly([Ap, Bp, Cp]))
    elems.append(_line(*Ap, *Dp, "geom-bold"))
    elems.append(_line(*Bp, *Cp, "geom-bold"))
    elems.append(_line(*Cp, *Ap, "geom-bold"))
    elems.append(_line(*Bp, *Cpp, "geom-dashed"))
    elems.append(_line(*Cp, *Dp, "geom-dashed"))
    elems.append(_ang_arc(*Ap, 22, Bp, Cp))
    elems.append(_ang_arc(*Bp, 22, Cp, Ap))
    elems.append(_ang_arc(*Bp, 27, Dp, Cp, "geom-arc"))
    for p, n, dx, dy in [
        (Ap, "A'", -10, 15),
        (Bp, "B'", 0, 17),
        (Cp, "C'", -4, -10),
        (Cpp, "C''", -16, -2),
        (Dp, "D'", 10, 15),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))
    return _svg_wrap("fig_sas_supplementary", "S.7", 480, 178, elems)


def fig_non_congruence_model() -> str:
    """§ 11 (Fig. 15): Analytic countermodel to Axiom IV 6 (anisotropic segment length)."""
    elems: list[str] = []
    O = (210.0, 115.0)
    # Axes X and Y
    elems.append(_line(40, 115, 390, 115, "geom-line"))
    elems.append(_line(210, 20, 210, 195, "geom-line"))
    # Under Hilbert's § 11 distance d = sqrt((dx + dy)^2 + dy^2),
    # unit circle around O satisfies (x+y)^2 + y^2 = 1 -> tilted ellipse!
    pts: list[tuple[float, float]] = []
    R = 85.0
    for k in range(121):
        th = 2 * math.pi * k / 120.0
        # Let u = x + y = cos(th), y = sin(th) => x = cos(th) - sin(th), y = sin(th)
        x = math.cos(th) - math.sin(th)
        y = math.sin(th)
        pts.append((O[0] + R * x * 0.72, O[1] - R * y * 0.72))
    path_d = "M " + " L ".join(f"{px:.2f} {py:.2f}" for px, py in pts) + " Z"
    elems.append(f'  <path d="{path_d}" class="geom-dashed" />')

    # Points on positive X, negative X, and positive Y with equal § 11 "length" t from O:
    # Along y=0: d((0,0),(x,0)) = |x| -> P1=(t,0), P2=(-t,0)
    # Along x=0: d((0,0),(0,y)) = sqrt(y^2+y^2) = sqrt(2)|y| -> Q=(0, t/sqrt(2))
    t = R * 0.72
    P1 = (O[0] + t, O[1])
    P2 = (O[0] - t, O[1])
    Q = (O[0], O[1] - t / math.sqrt(2.0))
    elems.append(_poly([O, P1, Q], "geom-polygon"))
    elems.append(_poly([O, P2, Q], "geom-polygon-gnomon"))
    elems.append(_line(*P1, *Q, "geom-bold"))
    elems.append(_line(*P2, *Q, "geom-accent-line"))
    elems.append(_ang_arc(*O, 18, P1, Q))
    elems.append(_ang_arc(*O, 22, Q, P2))
    for p, n, dx, dy in [
        (O, "O", -10, 16),
        (P1, "A", 10, 16),
        (P2, "A'", -12, 16),
        (Q, "B", 12, -6),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))
    elems.append(_lbl(382, 105, "X", "geom-label-sm"))
    elems.append(_lbl(223, 28, "Y", "geom-label-sm"))
    elems.append(_lbl(215, 186, "OA = OA', ∠AOB = ∠A'OB, yet AB ≠ A'B", "geom-label-sm"))
    return _svg_wrap("fig_non_congruence_model", "S.11", 420, 202, elems)


def fig_pascal_orthogonal() -> str:
    """§ 14 (Fig. 16): Hilbert's affine Pascal's (Pappus's) Hexagon Theorem (Theorem 21)."""
    elems: list[str] = []
    O = (42.0, 175.0)
    # Ray 1 along angle -5 deg, Ray 2 along angle -36 deg
    a1 = math.radians(-6.0)
    a2 = math.radians(-37.0)
    u1 = (math.cos(a1), math.sin(a1))
    u2 = (math.cos(a2), math.sin(a2))

    # Distances from O: on ray 1: rA, rB, rC; on ray 2: rAp, rBp, rCp
    # Condition CB' || BC' <=> rC / rBp = rB / rCp => rCp = rB * rBp / rC
    # Condition CA' || AC' <=> rC / rAp = rA / rCp => rAp = rC * rCp / rA = rB * rBp / rA
    # Then automatically rB / rAp = rA / rBp => BA' || AB'!
    rA, rB, rC = 115.0, 225.0, 355.0
    rBp = 195.0
    rCp = rB * rBp / rC
    rAp = rB * rBp / rA  # wait: let's keep rAp < 390; pick rA=140, rB=235, rC=365, rBp=175
    rA, rB, rC = 145.0, 245.0, 375.0
    rBp = 175.0
    rCp = rB * rBp / rC  # 114.33
    rAp = rB * rBp / rA  # 295.69 — all three well-spaced and inside viewBox!

    def ray_pt(u, r):
        return (O[0] + r * u[0], O[1] + r * u[1])

    A, B, C = ray_pt(u1, rA), ray_pt(u1, rB), ray_pt(u1, rC)
    Cp, Bp, Ap = ray_pt(u2, rCp), ray_pt(u2, rBp), ray_pt(u2, rAp)

    elems.append(_line(*O, *ray_pt(u1, 415), "geom-line"))
    elems.append(_line(*O, *ray_pt(u2, 345), "geom-line"))

    # Pair 1: CB' || BC' (solid bold)
    elems.append(_line(*C, *Bp, "geom-bold"))
    elems.append(_line(*B, *Cp, "geom-bold"))
    # Pair 2: CA' || AC' (dashed)
    elems.append(_line(*C, *Ap, "geom-dashed"))
    elems.append(_line(*A, *Cp, "geom-dashed"))
    # Conclusion Pair 3: BA' || AB' (assert green/accent)
    elems.append(_line(*B, *Ap, "geom-assert-line"))
    elems.append(_line(*A, *Bp, "geom-assert-line"))

    elems.append(_pt(*O))
    elems.append(_lbl(O[0] - 12, O[1] + 5, "O"))
    for p, n in [(A, "A"), (B, "B"), (C, "C")]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0], p[1] + 17, n))
    for p, n in [(Cp, "C'"), (Bp, "B'"), (Ap, "A'")]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] - 8, p[1] - 9, n))
    return _svg_wrap("fig_pascal_orthogonal", "S.14", 480, 205, elems)


def fig_segment_multiplication() -> str:
    """§ 15 (Figs. 21-22): Segment product c = ab and commutativity ab = ba via Pappus/Pascal."""
    elems: list[str] = []
    O = (65.0, 195.0)
    # Orthogonal rays OX (right) and OY (up)
    elems.append(_line(O[0], O[1], 425, O[1], "geom-line"))
    elems.append(_line(O[0], O[1], O[0], 18, "geom-line"))
    # Right-angle square mark at O
    elems.append(_line(O[0] + 11, O[1], O[0] + 11, O[1] - 11, "geom-dashed"))
    elems.append(_line(O[0], O[1] - 11, O[0] + 11, O[1] - 11, "geom-dashed"))

    u = 68.0  # unit 1
    a = 1.65 * u
    b = 2.35 * u
    ab = (a * b) / u  # 3.8775 * u = 263.7 px

    U_x = (O[0] + u, O[1])
    A_x = (O[0] + a, O[1])
    B_x = (O[0] + b, O[1])
    U_y = (O[0], O[1] - u)
    A_y = (O[0], O[1] - a)
    B_y = (O[0], O[1] - b)
    AB_x = (O[0] + ab, O[1])

    # Construction 1: 1_y to A_x, parallel through B_y meets OX at ab:
    # Wait: slope from (a,0) to (0,1) -> parallel from (0,b) hits OX at (ab, 0)!
    elems.append(_line(*U_y, *A_x, "geom-bold"))
    elems.append(_line(*B_y, *AB_x, "geom-bold"))
    # Construction 2 (commutativity ba): 1_y to B_x, parallel through A_y hits OX at SAME (ba, 0)!
    elems.append(_line(*U_y, *B_x, "geom-dashed"))
    elems.append(_line(*A_y, *AB_x, "geom-dashed"))
    # Auxiliary Pappus symmetry chord A_x B_y and B_x A_y? Wait: in Pappus on OX, OY:
    # Points on OX: A_x(a,0), B_x(b,0), AB_x(ab,0); on OY: U_y(0,1), A_y(0,a), B_y(0,b).
    # Note A_x A_y || B_x B_y (both slope -1)! Let's draw them in accent!
    elems.append(_line(*A_x, *A_y, "geom-accent-line"))
    elems.append(_line(*B_x, *B_y, "geom-accent-line"))

    for p, n, dx, dy in [
        (O, "O", -12, 14),
        (U_x, "1", 0, 17),
        (A_x, "a", 0, 17),
        (B_x, "b", 0, 17),
        (AB_x, "ab = ba", 0, 17),
        (U_y, "1", -14, 4),
        (A_y, "a", -14, 4),
        (B_y, "b", -14, 4),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))
    return _svg_wrap("fig_segment_multiplication", "S.15", 445, 224, elems)


def fig_segment_distributive() -> str:
    """§ 15 (Fig. 24): Geometric proof of distributive law a(b + c) = ab + ac."""
    elems: list[str] = []
    O = (55.0, 192.0)
    elems.append(_line(O[0], O[1], 435, O[1], "geom-line"))
    elems.append(_line(O[0], O[1], O[0], 22, "geom-line"))

    u = 64.0
    a = 1.75 * u
    b = 1.45 * u
    c = 1.15 * u
    ab = a * b / u
    ac = a * c / u
    abc = ab + ac

    Uy = (O[0], O[1] - u)
    By = (O[0], O[1] - b)
    BCy = (O[0], O[1] - (b + c))
    Ax = (O[0] + a, O[1])
    ABx = (O[0] + ab, O[1])
    ABCx = (O[0] + abc, O[1])
    # Parallelogram completion point D = (ab, -c) in screen coords relative to O:
    D = (O[0] + ab, O[1] - c)

    elems.append(_poly([O, ABx, By], "geom-polygon"))
    elems.append(_poly([By, D, ABCx, BCy], "geom-polygon-gnomon"))
    elems.append(_line(*Uy, *Ax, "geom-dashed"))
    elems.append(_line(*By, *ABx, "geom-bold"))
    elems.append(_line(*BCy, *ABCx, "geom-bold"))
    elems.append(_line(*By, *D, "geom-accent-line"))
    elems.append(_line(*ABx, *D, "geom-accent-line"))

    for p, n, dx, dy in [
        (O, "O", -12, 14),
        (Uy, "1", -14, 4),
        (By, "b", -14, 4),
        (BCy, "b+c", -22, 4),
        (Ax, "a", 0, 17),
        (ABx, "ab", 0, 17),
        (ABCx, "a(b+c) = ab+ac", -10, 17),
        (D, "D", 12, -4),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))
    return _svg_wrap("fig_segment_distributive", "S.15b", 460, 222, elems)


def fig_polygon_equivalence() -> str:
    """§ 19 (Fig. 29): Equicomplementability (inhaltsgleich) of parallelograms on same base."""
    elems: list[str] = []
    # Base AD on bottom line; top parallel line carrying B, C and B', C'
    A, D = (70.0, 160.0), (225.0, 160.0)
    B, C = (115.0, 52.0), (270.0, 52.0)
    Bp, Cp = (295.0, 52.0), (450.0, 52.0)

    elems.append(_line(40, 160, 465, 160, "geom-dashed"))
    elems.append(_line(40, 52, 470, 52, "geom-dashed"))
    elems.append(_poly([A, B, C, D], "geom-polygon"))
    elems.append(_poly([A, Bp, Cp, D], "geom-polygon-gnomon"))

    elems.append(_line(*A, *D, "geom-bold"))
    elems.append(_line(*A, *B, "geom-bold"))
    elems.append(_line(*B, *C, "geom-bold"))
    elems.append(_line(*C, *D, "geom-bold"))

    elems.append(_line(*A, *Bp, "geom-accent-line"))
    elems.append(_line(*Bp, *Cp, "geom-accent-line"))
    elems.append(_line(*Cp, *D, "geom-accent-line"))

    # Intersection E of CD and AB'
    def intersect(p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        return px, py

    E = intersect(C, D, A, Bp)
    elems.append(_pt(*E, 3.2, "geom-point-accent"))
    elems.append(_lbl(E[0] + 2, E[1] + 18, "E"))

    for p, n, dx, dy in [
        (A, "A", -8, 17),
        (D, "D", 8, 17),
        (B, "B", -6, -10),
        (C, "C", 0, -10),
        (Bp, "B'", 0, -10),
        (Cp, "C'", 8, -10),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))
    return _svg_wrap("fig_polygon_equivalence", "S.19", 490, 192, elems)


def fig_desargues_configuration() -> str:
    """§ 22 (Fig. 35): Affine Desargues's Theorem (Theorem 32)."""
    elems: list[str] = []
    O = (42.0, 112.0)
    angles = [math.radians(-23.0), math.radians(3.0), math.radians(24.0)]
    dirs = [(math.cos(a), math.sin(a)) for a in angles]

    # Triangle ABC at r1,r2,r3 and homothetic triangle A'B'C' at k * r_i (k = 1.92)
    radii = [145.0, 195.0, 160.0]
    k = 1.98
    tri1 = [(O[0] + r * u[0], O[1] + r * u[1]) for r, u in zip(radii, dirs)]
    tri2 = [(O[0] + k * r * u[0], O[1] + k * r * u[1]) for r, u in zip(radii, dirs)]
    A, B, C = tri1
    Ap, Bp, Cp = tri2

    for u in dirs:
        elems.append(_line(O[0], O[1], O[0] + 425 * u[0], O[1] + 425 * u[1], "geom-line"))

    elems.append(_poly([A, B, C], "geom-polygon"))
    elems.append(_poly([Ap, Bp, Cp], "geom-polygon-gnomon"))

    elems.append(_line(*A, *B, "geom-bold"))
    elems.append(_line(*B, *C, "geom-bold"))
    elems.append(_line(*Ap, *Bp, "geom-bold"))
    elems.append(_line(*Bp, *Cp, "geom-bold"))

    # Third pair of parallel sides AC || A'C'
    elems.append(_line(*A, *C, "geom-assert-line"))
    elems.append(_line(*Ap, *Cp, "geom-assert-line"))

    elems.append(_pt(*O))
    elems.append(_lbl(O[0] - 14, O[1] + 5, "O"))
    for p, n, dx, dy in [
        (A, "A", -4, -10),
        (B, "B", 6, -9),
        (C, "C", -4, 17),
        (Ap, "A'", 0, -10),
        (Bp, "B'", 10, -8),
        (Cp, "C'", 2, 18),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))
    return _svg_wrap("fig_desargues_configuration", "S.22", 485, 220, elems)


def fig_non_desarguesian_plane() -> str:
    """§ 23 (Fig. 36): Hilbert's 1899 Non-Desarguesian Plane (refracted ellipse model)."""
    elems: list[str] = []
    # In Hilbert § 23, ellipse x^2 + y^2 / (1/4)? In 1899 § 23: x^2 + 4 y^2 = 1 (semi-axes a=1, b=1/2)
    # and fixed point F = (sqrt(3)/2, 0) on positive X-axis? Wait: in 1899 § 23:
    # semi-axes a = 1, b = 1/2 (or a=1, b=1/2 -> F = (3/2, 0) outside or (sqrt(3)/2, 0)).
    # Let's draw the exact ellipse with semi-axes rx=135, ry=78 centered at C=(225, 110),
    # exterior straight ray segments P1-Q1 and Q2-P2, and the unique circular arc Q1-Q2
    # inside the ellipse passing through Q1, Q2 and refracting a Euclidean line!
    cx, cy = 225.0, 112.0
    rx, ry = 135.0, 76.0
    elems.append(_line(30, cy, 450, cy, "geom-dashed"))
    elems.append(_line(cx, 16, cx, 206, "geom-dashed"))
    elems.append(
        f'  <ellipse cx="{cx:.2f}" cy="{cy:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" class="geom-circle" />'
    )

    # Euclidean chord line (dashed) meeting ellipse at P and Q
    ang1, ang2 = math.radians(148.0), math.radians(26.0)
    P = (cx + rx * math.cos(ang1), cy - ry * math.sin(ang1))
    Q = (cx + rx * math.cos(ang2), cy - ry * math.sin(ang2))
    dx, dy = Q[0] - P[0], Q[1] - P[1]
    L_start = (P[0] - 0.36 * dx, P[1] - 0.36 * dy)
    L_end = (Q[0] + 0.36 * dx, Q[1] + 0.36 * dy)

    # Exterior segments of the Hilbert "line":
    elems.append(_line(*L_start, *P, "geom-bold"))
    elems.append(_line(*Q, *L_end, "geom-bold"))
    # Unrefracted Euclidean segment inside (dashed reference):
    elems.append(_line(*P, *Q, "geom-dashed"))
    # Refracted circular arc inside ellipse joining P and Q (Hilbert's deformed line):
    elems.append(
        f'  <path d="M {P[0]:.2f} {P[1]:.2f} A 175 175 0 0 0 {Q[0]:.2f} {Q[1]:.2f}" class="geom-accent-line" />'
    )

    F = (cx + 0.72 * rx, cy)
    elems.append(_pt(*F, 3.3, "geom-point-accent"))
    elems.append(_lbl(F[0], F[1] + 17, "F"))
    elems.append(_pt(*P))
    elems.append(_pt(*Q))
    elems.append(_lbl(P[0] - 12, P[1] - 8, "P"))
    elems.append(_lbl(Q[0] + 12, Q[1] - 8, "Q"))
    elems.append(_lbl(cx - 85, cy + 56, "Ellipse Boundary", "geom-label-sm"))
    elems.append(_lbl(cx + 10, cy + 32, "Hilbert Arc", "geom-label-sm"))
    return _svg_wrap("fig_non_desarguesian_plane", "S.23", 475, 218, elems)


def fig_desargues_segment_algebra() -> str:
    """§§ 24-26 (Figs. 40-41): Projective/affine segment addition and multiplication without Congruence."""
    elems: list[str] = []
    # Left panel: Segment Addition c = a + b via parallels to fixed unit line EE'
    O1 = (38.0, 185.0)
    ex1 = (225.0, 185.0)
    ey1 = (95.0, 32.0)
    u_ax = ((ex1[0] - O1[0]), (ex1[1] - O1[1]))
    u_ay = ((ey1[0] - O1[0]), (ey1[1] - O1[1]))
    elems.append(_lbl(130, 20, "§ 25: Addition c = a + b", "geom-label-sm"))
    elems.append(_line(*O1, *ex1, "geom-line"))
    elems.append(_line(*O1, *ey1, "geom-line"))

    A = (O1[0] + 0.36 * u_ax[0], O1[1])
    B = (O1[0] + 0.44 * u_ax[0], O1[1])
    # Parallel to OX through A' on OY:
    Ap = (O1[0] + 0.42 * u_ay[0], O1[1] + 0.42 * u_ay[1])
    # Line A A' determines direction; parallel through B meets Ap-horizontal at P, then parallel to A A' gives C = a+b!
    # Wait: in Hilbert § 25 Fig. 40: A->A' parallel to EE', A'->P parallel to OX, B->P parallel to OY, P->C parallel to A A'!
    (Ap[0] - A[0], Ap[1] - A[1])
    # B->P parallel to OY, A'->P parallel to OX => P = B + (Ap - O1)
    P = (B[0] + (Ap[0] - O1[0]), B[1] + (Ap[1] - O1[1]))
    C = (A[0] + (B[0] - O1[0]), O1[1])
    elems.append(_line(*A, *Ap, "geom-dashed"))
    elems.append(_line(*Ap, *P, "geom-dashed"))
    elems.append(_line(*B, *P, "geom-dashed"))
    elems.append(_line(*P, *C, "geom-accent-line"))
    for p, n, dx, dy in [
        (O1, "O", -10, 14),
        (A, "a", 0, 16),
        (B, "b", 0, 16),
        (C, "a+b", 6, 16),
        (Ap, "A'", -14, 2),
        (P, "P", 10, -4),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))

    # Right panel: Skew-field multiplication c = ab (§ 26 Fig. 41)
    O2 = (268.0, 185.0)
    ex2 = (468.0, 185.0)
    ey2 = (325.0, 32.0)
    vx = (ex2[0] - O2[0], 0.0)
    vy = (ey2[0] - O2[0], ey2[1] - O2[1])
    elems.append(_lbl(368, 20, "§ 26: Product c = ab", "geom-label-sm"))
    elems.append(_line(*O2, *ex2, "geom-line"))
    elems.append(_line(*O2, *ey2, "geom-line"))

    t1, ta, tb = 0.26, 0.45, 0.68
    Ex = (O2[0] + t1 * vx[0], O2[1])
    Ey = (O2[0] + t1 * vy[0], O2[1] + t1 * vy[1])
    Ax = (O2[0] + ta * vx[0], O2[1])
    (O2[0] + ta * vy[0], O2[1] + ta * vy[1])
    By = (O2[0] + tb * vy[0], O2[1] + tb * vy[1])
    # 1) A on OX -> A' on OY parallel to EE' (already Ay!)
    # 2) Join Ey to Ax? No: join Ex(1 on OX)? Wait: in § 26, B' on OY (with B->B' || EE'), join Ey(1) to Ax(a),
    # then parallel through By(b) meets OX at C = ab (since ta * tb / t1 = 0.45*0.68/0.26? Wait: keep C < 460 -> pick t1=0.36, ta=0.52, tb=0.62 => tc = 0.52*0.62/0.36 = 0.895!)
    t1, ta, tb = 0.36, 0.52, 0.62
    tc = ta * tb / t1
    Ex = (O2[0] + t1 * vx[0], O2[1])
    Ey = (O2[0] + t1 * vy[0], O2[1] + t1 * vy[1])
    Ax = (O2[0] + ta * vx[0], O2[1])
    Bx = (O2[0] + tb * vx[0], O2[1])
    By = (O2[0] + tb * vy[0], O2[1] + tb * vy[1])
    Cx = (O2[0] + tc * vx[0], O2[1])

    elems.append(_line(*Ex, *Ey, "geom-dashed"))
    elems.append(_line(*Bx, *By, "geom-dashed"))
    elems.append(_line(*Ey, *Ax, "geom-bold"))
    elems.append(_line(*By, *Cx, "geom-accent-line"))
    for p, n, dx, dy in [
        (O2, "O", -10, 14),
        (Ex, "1", 0, 16),
        (Ax, "a", 0, 16),
        (Bx, "b", 0, 16),
        (Cx, "ab", 4, 16),
        (Ey, "1'", -14, 4),
        (By, "b'", -14, 4),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))
    return _svg_wrap("fig_desargues_segment_algebra", "S.24-26", 490, 212, elems)


def fig_gauge_constructions() -> str:
    """§ 36 (Figs. 49-50): Dropping a perpendicular with straightedge and segment-transferer (Eichmass)."""
    elems: list[str] = []
    # Semicircle orthocenter construction for dropping a perpendicular from P to line AB using only
    # straightedge + segment-transferer (laying off equal segments OA = OB = OC = OD from O to get right angles AC ⊥ BC, AD ⊥ BD!)
    O = (225.0, 162.0)
    R = 108.0
    A = (O[0] - R, O[1])
    B = (O[0] + R, O[1])
    # Auxiliary circle reference (dashed, since the instrument only transfers segment R along rays OC, OD!)
    elems.append(
        f'  <path d="M {A[0]:.2f} {A[1]:.2f} A {R:.2f} {R:.2f} 0 0 1 {B[0]:.2f} {B[1]:.2f}" class="geom-dashed" />'
    )
    elems.append(_line(55, O[1], 415, O[1], "geom-bold"))

    # Choose apex P above semicircle; rays PA and PB meet semicircle at D and C!
    P = (255.0, 26.0)

    def circle_secant(pt_base):
        # Intersection of line P - pt_base with circle |X - O|^2 = R^2 other than pt_base
        dx, dy = P[0] - pt_base[0], P[1] - pt_base[1]
        fx, fy = pt_base[0] - O[0], pt_base[1] - O[1]
        # |f + t d|^2 = R^2 => t^2 |d|^2 + 2 t (f.d) = 0 => t = -2 (f.d) / |d|^2
        t = -2.0 * (fx * dx + fy * dy) / (dx * dx + dy * dy)
        return (pt_base[0] + t * dx, pt_base[1] + t * dy)

    C = circle_secant(A)  # lies on AP; angle ACB = 90° so BC is altitude!
    D = circle_secant(B)  # lies on BP; angle ADB = 90° so AD is altitude!

    def intersect(p1, p2, p3, p4):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        x4, y4 = p4
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        return px, py

    H = intersect(B, C, A, D)  # exact orthocenter of triangle PAB!
    F = (P[0], O[1])  # exact foot of perpendicular PH on AB!

    elems.append(_line(*A, *P, "geom-line"))
    elems.append(_line(*B, *P, "geom-line"))
    elems.append(_line(*O, *C, "geom-dashed"))
    elems.append(_line(*O, *D, "geom-dashed"))
    elems.append(_line(*B, *C, "geom-line"))
    elems.append(_line(*A, *D, "geom-line"))
    elems.append(_line(*P, *F, "geom-accent-line"))
    # Right angle square at foot F
    elems.append(_line(F[0] - 10, F[1], F[0] - 10, F[1] - 10, "geom-accent-line"))
    elems.append(_line(F[0] - 10, F[1] - 10, F[0], F[1] - 10, "geom-accent-line"))

    for p, n, dx, dy in [
        (O, "O", 0, 17),
        (A, "A", -10, 17),
        (B, "B", 10, 17),
        (C, "C", -13, -4),
        (D, "D", 13, -4),
        (P, "P", 0, -9),
        (H, "H", 13, 3),
        (F, "F", 0, 17),
    ]:
        elems.append(_pt(*p))
        elems.append(_lbl(p[0] + dx, p[1] + dy, n))
    return _svg_wrap("fig_gauge_constructions", "S.36", 460, 198, elems)


FIGURES = {
    "fig_betweenness_pasch.svg": fig_betweenness_pasch,
    "fig_sas_supplementary.svg": fig_sas_supplementary,
    "fig_non_congruence_model.svg": fig_non_congruence_model,
    "fig_pascal_orthogonal.svg": fig_pascal_orthogonal,
    "fig_segment_multiplication.svg": fig_segment_multiplication,
    "fig_segment_distributive.svg": fig_segment_distributive,
    "fig_polygon_equivalence.svg": fig_polygon_equivalence,
    "fig_desargues_configuration.svg": fig_desargues_configuration,
    "fig_non_desarguesian_plane.svg": fig_non_desarguesian_plane,
    "fig_desargues_segment_algebra.svg": fig_desargues_segment_algebra,
    "fig_gauge_constructions.svg": fig_gauge_constructions,
}


def build_all_figures(out_dir: Path | None = None) -> list[Path]:
    """Render all calibrated SVG figures into `docsrc/_static/figures/`."""
    if out_dir is None:
        repo_root = Path(__file__).resolve().parent.parent
        out_dir = repo_root / "docsrc" / "_static" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for filename, builder in FIGURES.items():
        target = out_dir / filename
        target.write_text(builder(), encoding="utf-8")
        written.append(target)
    return written


if __name__ == "__main__":
    paths = build_all_figures()
    print(f"Generated {len(paths)} calibrated SVG figures in {paths[0].parent}")
