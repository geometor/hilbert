"""Verbatim LaTeX-to-RST parser for E. J. Townsend's 1902 English edition (Gutenberg #17384)."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from geometor.hilbert.chapters_meta import SECTIONS_META, UNITS
from geometor.hilbert.concordance import default_repo_root


def _find_matching_brace(text: str, open_idx: int) -> int:
    """Return the index of the `}` matching `{` at `open_idx`."""
    depth = 0
    i = open_idx
    n = len(text)
    while i < n:
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    raise ValueError(f"Unbalanced brace starting at offset {open_idx}")


def _extract_command_with_arg(
    text: str, cmd_regex: str, transform: Any
) -> str:
    """Repeatedly replace `\\cmd{...}` using balanced-brace extraction."""
    pat = re.compile(cmd_regex)
    while True:
        m = pat.search(text)
        if not m:
            break
        brace_start = m.end() - 1
        brace_end = _extract_matching_or_end(text, brace_start)
        inner = text[brace_start + 1 : brace_end]
        replacement = transform(inner, m)
        text = text[: m.start()] + replacement + text[brace_end + 1 :]
    return text


def _extract_matching_or_end(text: str, brace_start: int) -> int:
    """Find matching closing brace; raise cleanly if malformed."""
    return _find_matching_brace(text, brace_start)


def _extract_brace_group_with_prefix(
    text: str, prefix_regex: str, transform: Any
) -> str:
    """Replace `{\\scshape ...}` or `{\\em ...}` balanced brace groups."""
    pat = re.compile(prefix_regex)
    while True:
        m = pat.search(text)
        if not m:
            break
        brace_start = m.start()
        brace_end = _find_matching_brace(text, brace_start)
        inner = text[m.end() : brace_end]
        replacement = transform(inner, m)
        text = text[: brace_start] + replacement + text[brace_end + 1 :]
    return text


def _normalize_math_inner(expr: str, *, multiline: bool) -> str:
    """Normalize Townsend LaTeX math macros to clean MathJax/KaTeX syntax."""
    lines = [re.sub(r"(?<!\\)%.*$", "", ln) for ln in expr.splitlines()]
    cleaned = "\n".join(lines).strip()
    cleaned = cleaned.replace(r"\begin{split}", r"\begin{aligned}")
    cleaned = cleaned.replace(r"\end{split}", r"\end{aligned}")
    cleaned = re.sub(r"\\mbox\{\s*``\s*``\s*\}", r'\\text{" "}', cleaned)

    def _repl_mbox(inner: str, _m: Any) -> str:
        t = inner.replace(r"\ ", " ").strip()
        if not t:
            return " "
        if t in {",", ".", ";", ":"}:
            return t
        return rf" \text{{{t}}} "

    cleaned = _extract_command_with_arg(cleaned, r"\\mbox\{", _repl_mbox)
    cleaned = cleaned.replace(r"\leqq", r"\le")
    cleaned = cleaned.replace(r"\gtreqqless", r"\gtreqless")
    cleaned = cleaned.replace(r"\lesseqqgtr", r"\lesseqgtr")
    cleaned = cleaned.replace(r"\ast", "*")
    if not multiline:
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def _convert_eqnarray_body(body: str) -> str:
    """Convert LaTeX eqnarray/eqnarray* 3-column rows into `aligned` rows."""
    norm = _normalize_math_inner(body, multiline=True)
    raw_rows = re.split(r"\\\\", norm)
    out_rows: list[str] = []
    for row in raw_rows:
        r = row.strip()
        if not r:
            continue
        parts = [p.strip() for p in r.split("&")]
        if len(parts) == 3:
            lhs, mid, rhs = parts
            if mid:
                out_rows.append(f"{lhs} &{mid} {rhs}" if mid in {"=", r"\equiv", "<", ">", r"\le", r"\ge"} else f"{lhs} &\\; {mid} \\; {rhs}")
            else:
                out_rows.append(f"{lhs} &= {rhs}" if rhs else lhs)
        elif len(parts) == 2:
            out_rows.append(f"{parts[0]} & {parts[1]}")
        else:
            out_rows.append(r)
    if len(out_rows) == 1 and "&" not in out_rows[0]:
        return out_rows[0]
    joined = " \\\\\n".join(out_rows)
    return f"\\begin{{aligned}}\n{joined}\n\\end{{aligned}}"


def _replace_body_tabulars(text: str) -> str:
    """Convert all 9 structural tabular environments in Townsend's body text to clean RST."""
    # TAB 1: Five groups of axioms in § 1
    text = re.sub(
        r"\\begin\{tabular\}\{rcl\}.*?Axioms of \\emph\{connection\}.*?\\end\{tabular\}",
        lambda _m: (
            "\n\n"
            "* **I, 1–7.** Axioms of *connection*.\n"
            "* **II, 1–5.** Axioms of *order*.\n"
            "* **III.** Axiom of *parallels* (Euclid's axiom).\n"
            "* **IV, 1–6.** Axioms of *congruence*.\n"
            "* **V.** Axiom of *continuity* (Archimedes's axiom).\n\n"
        ),
        text,
        flags=re.DOTALL,
    )

    # TAB 2: Four points O, A, B, C in § 11
    text = re.sub(
        r"\\begin\{tabular\}\{cccccc\}\s*\$O\$.*?\\end\{tabular\}",
        lambda _m: (
            "\n\n"
            "| $O$, having the co-ordinates $x = 0$, $y = 0$\n"
            "| $A$, having the co-ordinates $x = 1$, $y = 0$\n"
            "| $B$, having the co-ordinates $x = 0$, $y = 1$\n"
            "| $C$, having the co-ordinates $x = \\frac{1}{2}$, $y = \\frac{1}{2}$\n\n"
        ),
        text,
        flags=re.DOTALL,
    )

    # TAB 3: Algebraic laws 7-12 in § 13 (nested tabular)
    text = re.sub(
        r"\\hspace\*\{-2em\}\s*\\begin\{tabular\}\{lll\}\s*\{\\begin\{tabular\}\{r\}\s*\\textbf\{7\.\}.*?\\end\{array\}\$\s*\\end\{tabular\}",
        lambda _m: (
            "\n\n$$\n\\begin{aligned}\n"
            "\\mathbf{7.}\\quad a + (b + c) &= (a + b) + c \\\\\n"
            "\\mathbf{8.}\\quad a + b &= b + a \\\\\n"
            "\\mathbf{9.}\\quad a(bc) &= (ab)c \\\\\n"
            "\\mathbf{10.}\\quad a(b + c) &= ab + ac \\\\\n"
            "\\mathbf{11.}\\quad (a + b)c &= ac + bc \\\\\n"
            "\\mathbf{12.}\\quad ab &= ba.\n"
            "\\end{aligned}\n$$\n\n"
        ),
        text,
        flags=re.DOTALL,
    )

    # TAB 4: Congruences (1)-(3) in § 14 (nested tabular)
    text = re.sub(
        r"\\begin\{tabular\}\{lll\}\s*\\begin\{tabular\}\{l\}\s*\(1\)\s*\\\\\s*\(2\)\s*\\\\\s*\(3\)\s*\\end\{tabular\}.*?\\end\{array\}\$\s*\\end\{tabular\}(?:\\\\)?",
        lambda _m: (
            "\n\n$$\n\\begin{aligned}\n"
            "(1)\\quad \\lambda b' &\\equiv \\lambda' c, \\\\\n"
            "(2)\\quad \\mu a' &\\equiv \\mu' c, \\\\\n"
            "(3)\\quad \\nu a' &\\equiv \\nu' b.\n"
            "\\end{aligned}\n$$\n\n"
        ),
        text,
        flags=re.DOTALL,
    )

    # TAB 5: Congruences (4)-(5) in § 14 (nested tabular)
    text = re.sub(
        r"\\begin\{tabular\}\{lll\}\s*\\begin\{tabular\}\{l\}\s*\(4\)\s*\\\\\s*\(5\)\s*\\end\{tabular\}.*?\\end\{array\}\$\s*\\end\{tabular\}(?:\\\\)?",
        lambda _m: (
            "\n\n$$\n\\begin{aligned}\n"
            "(4)\\quad \\lambda c' &\\equiv \\lambda' b, \\\\\n"
            "(5)\\quad \\mu c' &\\equiv \\mu' a.\n"
            "\\end{aligned}\n$$\n\n"
        ),
        text,
        flags=re.DOTALL,
    )

    # TAB 6: Congruence (6) in § 14 (nested tabular)
    text = re.sub(
        r"\\begin\{tabular\}\{lll\}\s*\\begin\{tabular\}\{l\}\(6\)\\end\{tabular\}.*?\\end\{array\}\$\s*\\end\{tabular\}(?:\\\\)?",
        lambda _m: "\n\n$$\n(6)\\quad \\nu b' \\equiv \\nu' a.\n$$\n\n",
        text,
        flags=re.DOTALL,
    )

    # TAB 7: Auxiliary parallel lines F''J, F'J in § 26
    text = re.sub(
        r"\\begin\{center\}\s*\\begin\{tabular\}\{cccccccc\}\s*\$F''J\$.*?\\end\{tabular\}\s*\\end\{center\}",
        lambda _m: (
            "\n\n"
            "| $F''J$ parallel to the fixed straight line $OA'$,\n"
            "| $F'J$ parallel to the fixed straight line $OA''$.\n\n"
        ),
        text,
        flags=re.DOTALL,
    )

    # TAB 8: Auxiliary parallel lines GH in § 26
    text = re.sub(
        r"\\begin\{center\}\s*\\begin\{tabular\}\{cccccccccc\}\s*\$GH\$.*?\\end\{tabular\}\s*\\end\{center\}",
        lambda _m: (
            "\n\n"
            "| $GH$ parallel to $G'H'$, parallel to the fixed line $OA$,\n"
            "| $GH$ parallel to $A'H'$, parallel to the fixed line $OB$,\n\n"
        ),
        text,
        flags=re.DOTALL,
    )

    # TAB 9: Max Dehn's 3x3 classification table in Conclusion
    text = re.sub(
        r"\\begin\{tabular\}\{c\|c\|c\|c\}.*?Lobatschewski.*?\\end\{tabular\}",
        lambda _m: (
            "\n\n"
            ".. list-table:: Classification of Plane Geometries (Without Archimedes's Axiom)\n"
            "   :header-rows: 1\n"
            "   :stub-columns: 1\n"
            "   :widths: 22 26 26 26\n\n"
            "   * - The sum of the angles of a triangle is\n"
            "     - Through a given point: **No parallels** to a straight line\n"
            "     - Through a given point: **One parallel** to a straight line\n"
            "     - Through a given point: **An infinity of parallels** to a straight line\n"
            "   * - $> 2$ right angles\n"
            "     - Riemann's (elliptic) geometry\n"
            "     - This case is impossible\n"
            "     - Non-legendrian geometry\n"
            "   * - $< 2$ right angles\n"
            "     - This case is impossible\n"
            "     - Euclidean (parabolic) geometry\n"
            "     - Semi-euclidean geometry\n"
            "   * - $= 2$ right angles\n"
            "     - This case is impossible\n"
            "     - This case is impossible\n"
            "     - Geometry of Lobatschewski (hyperbolic)\n\n"
        ),
        text,
        flags=re.DOTALL,
    )
    return text


def _wrap_emphasis(inner: str, marker: str = "*") -> str:
    """Wrap `inner` in RST `*...*` or `**...**` safely without nested markers or edge spaces."""
    lead = " " if inner[:1].isspace() else ""
    trail = " " if inner[-1:].isspace() else ""
    core = re.sub(r"\s+", " ", inner).strip()
    if not core:
        return lead + trail
    if marker == "*":
        core = core.replace("*", "")
    return f"{lead}{marker}{core}{marker}{trail}"


def _convert_tex_fragment(raw: str, footnotes: list[str] | None = None) -> str:
    """Convert a verbatim Townsend LaTeX fragment into valid RST with MathJax `$...$`/`$$...$$`."""
    text = raw

    # 1. Strip scan comments, PNG figure floats, and pure layout spacing commands
    text = re.sub(r"%%-----File:\s*\d+\.png-----%%\n?", "", text)
    text = re.sub(r"\\begin\{(?:wrap)?figure\}(?:\[[^\]]*\])?(?:\{[^}]*\}\{[^}]*\})?.*?\\end\{(?:wrap)?figure\}", "", text, flags=re.DOTALL)
    text = _replace_body_tabulars(text)

    # 2. Convert § 14 starred congruence lines `(1$\ast$)\hspace*{10em} $...$\\` to display math
    text = re.sub(
        r"\\\\\s*\n\((\d+)\$\\ast\$\)\\hspace\*?\{[^}]+\}\s*\$([^$\n]+)\$([\.,;]?)(?:\\\\)?",
        lambda m: f"\n\n$$\n({m.group(1)}^*)\\quad {_normalize_math_inner(m.group(2), multiline=False)}{m.group(3)}\n$$\n\n",
        text,
    )
    text = re.sub(
        r"\((\d+)\$\\ast\$\)\\hspace\*?\{[^}]+\}\s*\$([^$\n]+)\$([\.,;]?)(?:\\\\)?",
        lambda m: f"\n\n$$\n({m.group(1)}^*)\\quad {_normalize_math_inner(m.group(2), multiline=False)}{m.group(3)}\n$$\n\n",
        text,
    )
    # Inline `(1$\ast$)` or `(4\ast)` -> `$(1^*)$`
    text = re.sub(r"\((\d+)\$\\ast\$\)", r"$(\1^*)$", text)
    text = re.sub(r"\$\((\d+)\s*\\ast\s*\)\$", r"$(\1^*)$", text)

    # 3. Extract `\footnote{...}` before math protection so footnotes get recursively converted
    if footnotes is not None:
        def _repl_fn(inner: str, _m: Any) -> str:
            fn_rst = _convert_tex_fragment(inner, footnotes=None).strip()
            fn_rst = re.sub(r"\s+", " ", fn_rst)
            footnotes.append(fn_rst)
            return f" [#fn{len(footnotes)}]_"

        text = _extract_command_with_arg(text, r"\\footnote\{", _repl_fn)

    # 4. Protect display math and inline math with placeholders
    math_store: dict[str, str] = {}
    m_counter = 0

    def _stash_math(rendered: str) -> str:
        nonlocal m_counter
        m_counter += 1
        tok = f"@@HILBERTMATH{m_counter:05d}@@"
        math_store[tok] = rendered
        return tok

    # Already-converted `$$ ... $$` from tabulars / starred congruences
    text = re.sub(
        r"\$\$\s*(.*?)\s*\$\$",
        lambda m: "\n\n" + _stash_math(f"$$\n{m.group(1).strip()}\n$$") + "\n\n",
        text,
        flags=re.DOTALL,
    )
    # `\[ ... \]`
    text = re.sub(
        r"\\\[(.*?)\\\]",
        lambda m: "\n\n" + _stash_math(f"$$\n{_normalize_math_inner(m.group(1), multiline=True)}\n$$") + "\n\n",
        text,
        flags=re.DOTALL,
    )
    # `equation` and `equation*`
    text = re.sub(
        r"\\begin\{equation\*?\}(.*?)\\end\{equation\*?\}",
        lambda m: "\n\n" + _stash_math(f"$$\n{_normalize_math_inner(m.group(1), multiline=True)}\n$$") + "\n\n",
        text,
        flags=re.DOTALL,
    )
    # `align*`
    text = re.sub(
        r"\\begin\{align\*\}(.*?)\\end\{align\*\}",
        lambda m: (
            "\n\n"
            + _stash_math(
                "$$\n\\begin{aligned}\n"
                + _normalize_math_inner(m.group(1), multiline=True)
                + "\n\\end{aligned}\n$$"
            )
            + "\n\n"
        ),
        text,
        flags=re.DOTALL,
    )
    # `eqnarray` and `eqnarray*`
    text = re.sub(
        r"\\begin\{eqnarray\*?\}(.*?)\\end\{eqnarray\*?\}",
        lambda m: "\n\n" + _stash_math(f"$$\n{_convert_eqnarray_body(m.group(1))}\n$$") + "\n\n",
        text,
        flags=re.DOTALL,
    )
    # Inline `$ ... $`
    text = re.sub(
        r"\$([^$]+)\$",
        lambda m: _stash_math(f"${_normalize_math_inner(m.group(1), multiline=False)}$"),
        text,
    )

    # 5. Strip LaTeX labels, pagination, spacing, and resolve `\pageref{folioN}`
    text = re.sub(r"\\pageref\{folio(\d+)\}", r"\1", text)
    text = re.sub(r"\\label\{[^}]+\}", "", text)
    text = re.sub(r"\\(?:newpage|clearpage|bigskip|medskip|noindent)\b", "\n\n", text)
    text = re.sub(r"\\(?:vspace|hspace)\*?\{[^}]*\}", "", text)
    text = re.sub(r"\\thispagestyle\{[^}]*\}", "", text)
    text = re.sub(r"\\pagestyle\{[^}]*\}", "", text)
    text = re.sub(r"\\pagenumbering\{[^}]*\}", "", text)
    text = re.sub(r"\\setcounter\{[^}]*\}\{[^}]*\}", "", text)

    # 6. Accents, special symbols, quotes, dashes
    text = text.replace(r"\@.", ".")
    text = text.replace(r"\@", "")
    accent_map = {
        r'\"o': "ö",
        r'\"{o}': "ö",
        r'\"u': "ü",
        r'\"{u}': "ü",
        r'\"a': "ä",
        r'\"{a}': "ä",
        r'\"O': "Ö",
        r'\"{O}': "Ö",
        r'\"U': "Ü",
        r'\"{U}': "Ü",
        r'\"A': "Ä",
        r'\"{A}': "Ä",
        r"\'e": "é",
        r"\'{e}": "é",
        r"\`e": "è",
        r"\`{e}": "è",
        r"\^o": "ô",
        r"{\ae}": "æ",
        r"\ae ": "æ ",
        r"\ae": "æ",
    }
    for src_acc, dst_acc in accent_map.items():
        text = text.replace(src_acc, dst_acc)

    text = re.sub(r"\\S\\!~", "§ ", text)
    text = re.sub(r"\\S\\S~", "§§ ", text)
    text = re.sub(r"\\S\\S\s*", "§§ ", text)
    text = re.sub(r"\\S~", "§ ", text)
    text = re.sub(r"\\S\b\s*", "§ ", text)
    text = text.replace("~", " ")
    text = re.sub(r"\\ldots\b\s*", "...", text)
    text = re.sub(r"\\dots\b\s*", "...", text)
    text = text.replace("``", "“").replace("''", "”")
    text = text.replace("---", "—").replace("--", "–")
    text = re.sub(r"\\\\\s*$", "", text, flags=re.MULTILINE)

    # 7. Structural environments: description, itemize, quote, center, small, scshape, flushright
    def _repl_description(m: re.Match[str]) -> str:
        body = m.group(1)
        items = re.split(r"\\item\[([^\]]*)\]", body)
        out: list[str] = []
        for idx in range(1, len(items), 2):
            label = items[idx].strip()
            content = items[idx + 1].strip()
            out.append(f"**{label}** {content}" if label else f"* {content}")
        return "\n\n" + "\n\n".join(out) + "\n\n"

    text = re.sub(r"\\begin\{description\}(.*?)\\end\{description\}", _repl_description, text, flags=re.DOTALL)

    def _repl_itemize(m: re.Match[str]) -> str:
        body = m.group(1)
        parts = re.split(r"\\item\s*\[\s*\]", body)
        out: list[str] = []
        for p in parts:
            cleaned = p.strip()
            if cleaned:
                out.append(cleaned)
        return "\n\n" + "\n\n".join(out) + "\n\n"

    text = re.sub(r"\\begin\{itemize\}(.*?)\\end\{itemize\}", _repl_itemize, text, flags=re.DOTALL)
    text = re.sub(r"\\begin\{quote\}(.*?)\\end\{quote\}", lambda m: "\n\n" + m.group(1).strip() + "\n\n", text, flags=re.DOTALL)

    def _repl_center(m: re.Match[str]) -> str:
        inner = m.group(1).strip()
        if not inner:
            return ""
        if inner.isupper() or inner.startswith("THEOREM"):
            return f"\n\n**{inner}**\n\n"
        return f"\n\n{inner}\n\n"

    text = re.sub(r"\\begin\{center\}(.*?)\\end\{center\}", _repl_center, text, flags=re.DOTALL)
    while re.search(r"\\begin\{(small|scshape|flushright)\}.*?\\end\{\1\}", text, flags=re.DOTALL):
        text = re.sub(
            r"\\begin\{(small|scshape|flushright)\}(.*?)\\end\{\1\}",
            lambda m: "\n\n" + m.group(2).strip() + "\n\n",
            text,
            flags=re.DOTALL,
        )

    # 8. Inline brace groups & formatting commands
    text = _extract_brace_group_with_prefix(
        text,
        r"\{\\scshape\b\s*",
        lambda inner, _m: _wrap_emphasis(inner, "**"),
    )
    text = _extract_brace_group_with_prefix(
        text,
        r"\{\\(?:em|itshape|textit)\b\s*",
        lambda inner, _m: _wrap_emphasis(inner, "*"),
    )
    text = _extract_brace_group_with_prefix(
        text,
        r"\{\\(?:small|large|Large|Huge|footnotesize|tiny|normalsize)\b\s*",
        lambda inner, _m: inner.strip(),
    )
    text = _extract_command_with_arg(
        text,
        r"\\(?:emph|textit)\{",
        lambda inner, _m: _wrap_emphasis(inner, "*"),
    )
    text = _extract_command_with_arg(
        text,
        r"\\textbf\{",
        lambda inner, _m: _wrap_emphasis(inner, "**"),
    )
    text = text.replace(r"\rfb", "")

    # Strip any stray unescaped braces wrapping plain text
    text = re.sub(r"\{([^{}\\]*)\}", r"\1", text)

    # Normalize `**Theorem** 6.` -> `**Theorem 6.**`
    text = re.sub(r"\*\*Theorem\*\*\s+(\d+)\.", r"**Theorem \1.**", text)

    # 9. Emit anchors for `**Theorem N.**`
    def _inject_thm_anchor(m: re.Match[str]) -> str:
        tnum = m.group(1)
        return f"\n\n.. _grundlagen-en-thm-{tnum}:\n\n**Theorem {tnum}.**"

    text = re.sub(r"(?:^|\n\n)\s*\*\*Theorem\s+(\d+)\.\*\*", _inject_thm_anchor, text)

    # Ensure `[#fnN]_` has a leading space when preceded by non-whitespace and escape trailing word chars
    text = re.sub(r"(\S)\s*(\[#fn\d+\]_)", r"\1 \2", text)

    # Normalize paragraph spacing before restoring math
    paragraphs: list[str] = []
    for block in re.split(r"\n\s*\n", text):
        if not block.strip():
            continue
        raw_trimmed = block.strip("\n")
        b = block.strip()
        if raw_trimmed.startswith("   * -"):
            paragraphs.append(raw_trimmed)
        elif b.startswith((".. ", "| ", "* -", "   ", "* **", "* ")):
            paragraphs.append(b)
        else:
            collapsed = " ".join(ln.strip() for ln in b.splitlines() if ln.strip())
            # Guard against `*italic*word` or `word*italic*`
            collapsed = re.sub(r"([A-Za-z0-9])(\*[A-Za-z])", r"\1 \2", collapsed)
            paragraphs.append(collapsed)

    joined = "\n\n".join(paragraphs)

    # 10. Restore math placeholders
    for tok, math_val in math_store.items():
        joined = joined.replace(tok, math_val)

    # Clean up excessive blank lines around display math
    joined = re.sub(r"\n{3,}", "\n\n", joined).strip()
    return joined


def parse_english_source(tex_path: Path | None = None) -> dict[str, Any]:
    """Slice `gutenberg_17384_townsend_1902.tex` into Preface, Epigraph, §§ 0–39, Conclusion, and Appendix."""
    root = default_repo_root()
    path = tex_path or (root / "resources" / "grundlagen" / "sources" / "gutenberg_17384_townsend_1902.tex")
    tex = path.read_text(encoding="utf-8")

    # 1. Preface
    pref_start = tex.index(r"\begin{center}{\Large PREFACE.}\end{center}") + len(
        r"\begin{center}{\Large PREFACE.}\end{center}"
    )
    pref_end = tex.index(r"\clearpage", pref_start)
    raw_preface = tex[pref_start:pref_end]

    # 2. Body from `\label{folio1}` to `*** END OF THE PROJECT GUTENBERG`
    body_start = tex.index(r"\label{folio1}")
    body_end = tex.index("*** END OF THE PROJECT GUTENBERG")
    body = tex[body_start:body_end]
    # Remove trailing `\begin{verbatim}` before Gutenberg footer
    body = re.sub(r"\\small\s*\\pagenumbering\{gobble\}\s*\\begin\{verbatim\}\s*$", "", body.strip())

    # Remove chapter-banner `\begin{center}{\Large ...}\end{center}` lines between sections
    body = re.sub(r"\\begin\{center\}\{\\Large\s+[^}]+\}\\end\{center\}\s*", "", body)

    # Locate markers: p0, p1..p39, pc, and APPENDIX
    markers: list[tuple[str, int, int]] = []
    for m in re.finditer(r"\\rfa\{.*?\}\\label\{(p\d+|pc)\}", body, flags=re.DOTALL):
        markers.append((m.group(1), m.start(), m.end()))
    app_match = re.search(r"\\rfa\{APPENDIX\.(.*?)\}\s*\n", body, flags=re.DOTALL)
    if not app_match:
        raise ValueError("Could not locate APPENDIX header in Townsend TeX source.")
    markers.append(("appendix", app_match.start(), app_match.end()))
    markers.sort(key=lambda item: item[1])

    raw_epigraph_area = body[: markers[0][1]]
    slices: dict[str, str] = {}
    for i, (key, _m_start, m_end) in enumerate(markers):
        next_start = markers[i + 1][1] if i + 1 < len(markers) else len(body)
        chunk = body[m_end:next_start]
        if key == "appendix":
            # Preserve the footnote inside `\rfa{APPENDIX.\footnote{...}}`
            app_header_inner = app_match.group(1).strip()
            chunk = app_header_inner + "\n\n" + chunk
        slices[key] = chunk

    return {
        "raw_preface": raw_preface,
        "raw_epigraph": raw_epigraph_area,
        "slices": slices,
    }


def _render_figure_directive(sec_num: int) -> str:
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


def build_english_units(tex_path: Path | None = None) -> dict[str, str]:
    """Generate the complete 9 English unit RST documents (`<unit>-en.rst`)."""
    parsed = parse_english_source(tex_path)
    slices = parsed["slices"]
    units_rst: dict[str, str] = {}

    for unit in UNITS:
        slug = unit["slug"]
        footnotes: list[str] = []
        head_title = f"{unit['num_en']}: {unit['title_en']}" if slug.startswith("chapter-") else unit["title_en"]
        bar = "=" * len(head_title)
        parts: list[str] = [
            ":layout: book",
            "",
            f".. _grundlagen-{slug}-en:",
            "",
            head_title,
            bar,
            "",
            ".. rubric:: David Hilbert — *The Foundations of Geometry* (Authorized Translation by E. J. Townsend, 1902)",
            "",
            ".. contents:: In This Unit",
            "   :local:",
            "   :depth: 2",
            "   :backlinks: none",
            "",
        ]

        if slug == "introduction":
            preface_rst = _convert_tex_fragment(parsed["raw_preface"], footnotes=footnotes)
            # Clean signature spacing at the end of Townsend's Preface
            preface_rst = preface_rst.replace("E. J. Townsend\n\nUniversity of Illinois.", "| **E. J. Townsend**\n| *University of Illinois.*")
            sec0_meta = SECTIONS_META[0]
            sec0_rst = _convert_tex_fragment(slices["p0"], footnotes=footnotes)
            parts.extend(
                [
                    ".. _grundlagen-en-preface:",
                    "",
                    "Translator's Preface (1902)",
                    "---------------------------",
                    "",
                    preface_rst,
                    "",
                    "----",
                    "",
                    ".. epigraph::",
                    "",
                    "   “All human knowledge begins with intuitions, thence passes to concepts and ends with ideas.”",
                    "",
                    "   — Kant, *Kritik der reinen Vernunft*, *Elementariehre*, Part 2, Sec. 2.",
                    "",
                    ".. _grundlagen-en-s0:",
                    "",
                    ".. folio:: Introduction",
                    f"   :page: {sec0_meta['page_en']}",
                    "",
                    "Introduction",
                    "------------",
                    "",
                    sec0_rst,
                ]
            )
        elif slug == "conclusion":
            conc_rst = _convert_tex_fragment(slices["pc"], footnotes=footnotes)
            app_rst = _convert_tex_fragment(slices["appendix"], footnotes=footnotes)
            # Attach the translator's opening footnote cleanly to an introductory notice line if bare
            if app_rst.startswith("[#fn"):
                first_nl = app_rst.find("\n\n")
                fn_tag = app_rst[:first_nl].strip()
                rest_app = app_rst[first_nl:].strip()
                app_rst = f"*(Author's Summary of the 1902 Memoir on Lie Transformation Groups)* {fn_tag}\n\n{rest_app}"
            app_heading = "Appendix: Foundations of Geometry Based Upon Transformation Groups"
            parts.extend(
                [
                    ".. _grundlagen-en-s40:",
                    "",
                    ".. folio:: Conclusion",
                    "   :page: 108",
                    "",
                    "Conclusion",
                    "----------",
                    "",
                    conc_rst,
                    "",
                    ".. _grundlagen-en-appendix:",
                    "",
                    ".. folio:: Appendix",
                    "   :page: 113",
                    "",
                    app_heading,
                    "-" * len(app_heading),
                    "",
                    app_rst,
                ]
            )
        else:
            for sec_num in unit["sections"]:
                smeta = SECTIONS_META[sec_num]
                stitle = smeta["title_en"]
                sbody = _convert_tex_fragment(slices[f"p{sec_num}"], footnotes=footnotes)
                fig_block = _render_figure_directive(sec_num)
                parts.extend(
                    [
                        f".. _grundlagen-en-s{sec_num}:",
                        "",
                        f".. folio:: § {sec_num}",
                        f"   :page: {smeta['page_en']}",
                        "",
                        stitle,
                        "-" * len(stitle),
                        "",
                        sbody + fig_block,
                        "",
                    ]
                )

        if footnotes:
            parts.extend(["", "----", "", ".. rubric:: Footnotes", ""])
            for idx, fn_text in enumerate(footnotes, 1):
                parts.append(f".. [#fn{idx}] {fn_text}")
                parts.append("")

        units_rst[slug] = "\n".join(parts).rstrip() + "\n"

    return units_rst
