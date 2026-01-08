# LaTeX Typesetting Skill

## Overview

This skill provides comprehensive methodologies for typesetting mathematical documents using LaTeX. It covers document structure, mathematical notation, theorem environments, equation formatting, bibliography management, and publication-quality standards for academic mathematical writing.

## When to Use

- Writing mathematical papers and articles
- Formatting proofs and theorems
- Creating technical documentation
- Preparing manuscripts for publication
- Typesetting complex equations and formulas
- Managing mathematical bibliographies

---

## Document Structure

### Standard Mathematical Article Template

```latex
MATHEMATICAL ARTICLE STRUCTURE
═══════════════════════════════════════════════════════════════

\documentclass[11pt,a4paper]{article}

% Essential packages
\usepackage{amsmath}      % Enhanced math environments
\usepackage{amssymb}      % Mathematical symbols
\usepackage{amsthm}       % Theorem environments
\usepackage{amsfonts}     % Mathematical fonts
\usepackage{mathtools}    % Extensions to amsmath
\usepackage{thmtools}     % Enhanced theorem tools

% Additional recommended packages
\usepackage{enumitem}     % List customization
\usepackage{hyperref}     % Hyperlinks
\usepackage{cleveref}     % Smart cross-references
\usepackage{tikz}         % Diagrams
\usepackage{pgfplots}     % Plots and graphs
\usepackage{algorithm2e}  % Algorithms
\usepackage{listings}     % Code listings

% Bibliography
\usepackage[numbers,sort&compress]{natbib}

% Document metadata
\title{Title of the Paper}
\author{Author Name\\
  \small Institution\\
  \small \texttt{email@domain.com}}
\date{\today}

\begin{document}

\maketitle
\begin{abstract}
  Brief summary of the paper's contributions.
\end{abstract}

\section{Introduction}
\section{Preliminaries}
\section{Main Results}
\section{Proofs}
\section{Applications}
\section{Conclusion}

\bibliographystyle{plainnat}
\bibliography{references}

\end{document}
```

### Package Selection Guide

```
ESSENTIAL PACKAGES BY PURPOSE
═══════════════════════════════════════════════════════════════

CORE MATHEMATICS
─────────────────────────────────────────
amsmath     : Multi-line equations, alignment, matrices
amssymb     : \mathbb, \mathfrak, additional symbols
amsthm      : Theorem, lemma, proof environments
mathtools   : Fixes and extensions to amsmath
thmtools    : Advanced theorem customization

SYMBOLS AND FONTS
─────────────────────────────────────────
amsfonts    : \mathbb{R}, \mathfrak{g}, etc.
stmaryrd    : \llbracket, \rrbracket (semantic brackets)
wasysym     : Additional symbols
dsfont      : \mathds for double-struck fonts
bm          : Bold math symbols (\bm{x})

DIAGRAMS AND GRAPHICS
─────────────────────────────────────────
tikz        : General-purpose diagrams
tikz-cd     : Commutative diagrams
pgfplots    : Function plots, data visualization
xy          : Alternative for commutative diagrams

ALGORITHMS AND CODE
─────────────────────────────────────────
algorithm2e : Algorithm pseudocode
algorithmicx: Alternative algorithm package
listings    : Source code with syntax highlighting
minted      : Advanced syntax highlighting (requires Python)

REFERENCES AND CITATIONS
─────────────────────────────────────────
hyperref    : Clickable links (load late!)
cleveref    : \cref{eq:main} → "Equation (1)"
natbib      : Flexible citation styles
biblatex    : Modern bibliography (alternative to natbib)

DOCUMENT CLASSES BY VENUE
─────────────────────────────────────────
article     : General mathematical articles
amsart      : AMS journal style
book        : Mathematical textbooks
memoir      : Flexible class for longer works
revtex4     : Physics journals (APS)
elsarticle  : Elsevier journals
llncs       : Springer LNCS proceedings
acmart      : ACM publications
```

---

## Theorem Environments

### Standard Theorem Setup

```latex
THEOREM ENVIRONMENT CONFIGURATION
═══════════════════════════════════════════════════════════════

% Basic setup with amsthm
\theoremstyle{plain}      % Italic body text
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}

\theoremstyle{definition} % Roman body text
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{exercise}[theorem]{Exercise}

\theoremstyle{remark}     % Roman, smaller
\newtheorem*{remark}{Remark}
\newtheorem*{note}{Note}
\newtheorem*{notation}{Notation}

% Numbered equations within theorems
\newtheorem{theoremnum}{Theorem}
\newenvironment{theoremeq}
  {\begin{theoremnum}}
  {\end{theoremnum}\addtocounter{equation}{-1}}

USAGE EXAMPLES
─────────────────────────────────────────

\begin{theorem}[Fundamental Theorem of Calculus]
  \label{thm:ftc}
  If $f$ is continuous on $[a,b]$ and $F'(x) = f(x)$, then
  \[
    \int_a^b f(x)\,dx = F(b) - F(a).
  \]
\end{theorem}

\begin{proof}
  Let $\epsilon > 0$ be given...
  [proof content]
\end{proof}

\begin{definition}[Continuity]
  A function $f: X \to Y$ is \emph{continuous} at $x_0$ if
  for every $\epsilon > 0$ there exists $\delta > 0$ such that
  $d_X(x, x_0) < \delta$ implies $d_Y(f(x), f(x_0)) < \epsilon$.
\end{definition}

\begin{lemma}
  \label{lem:key}
  Every bounded sequence in $\mathbb{R}^n$ has a convergent
  subsequence.
\end{lemma}
```

### Advanced Theorem Styling

```latex
CUSTOM THEOREM STYLES WITH thmtools
═══════════════════════════════════════════════════════════════

\usepackage{thmtools}
\usepackage{mdframed}  % For boxed theorems

% Boxed theorem style
\declaretheoremstyle[
  headfont=\bfseries,
  notefont=\normalfont,
  bodyfont=\normalfont,
  mdframed={
    linewidth=1pt,
    linecolor=black,
    backgroundcolor=gray!10,
    skipabove=12pt,
    skipbelow=12pt,
    innerleftmargin=10pt,
    innerrightmargin=10pt,
  }
]{boxedthm}

\declaretheorem[style=boxedthm,name=Theorem]{boxedtheorem}

% Named theorem (for citing famous theorems)
\declaretheoremstyle[
  headfont=\bfseries,
  notefont=\bfseries,
  notebraces={[}{]},
  bodyfont=\normalfont\itshape,
]{namedthm}

\declaretheorem[style=namedthm,name=Theorem,numbered=no]{namedtheorem}

USAGE:
─────────────────────────────────────────

\begin{boxedtheorem}
  This theorem appears in a box with gray background.
\end{boxedtheorem}

\begin{namedtheorem}[Bolzano-Weierstrass]
  Every bounded sequence in $\mathbb{R}^n$ has a convergent
  subsequence.
\end{namedtheorem}
```

---

## Equation Formatting

### Display Equations

```latex
EQUATION ENVIRONMENTS
═══════════════════════════════════════════════════════════════

SINGLE EQUATIONS
─────────────────────────────────────────

% Unnumbered display equation
\[
  E = mc^2
\]

% Numbered equation
\begin{equation}
  \label{eq:einstein}
  E = mc^2
\end{equation}

% Refer to equation: \eqref{eq:einstein} gives "(1)"

MULTI-LINE EQUATIONS
─────────────────────────────────────────

% Aligned at relation symbols
\begin{align}
  f(x) &= x^2 + 2x + 1 \\
       &= (x+1)^2 \label{eq:factored}
\end{align}

% Aligned, single number
\begin{equation}
\begin{aligned}
  \nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} \\
  \nabla \cdot \mathbf{B} &= 0 \\
  \nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
  \nabla \times \mathbf{B} &= \mu_0 \mathbf{J} +
    \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{aligned}
\end{equation}

% Multiple alignment points
\begin{alignat}{2}
  f(x) &= x^2    &\quad g(x) &= x^3 \\
  f'(x) &= 2x   &\quad g'(x) &= 3x^2
\end{alignat}

% Gathered equations (centered, multiple numbers)
\begin{gather}
  x + y = 1 \\
  x - y = 0
\end{gather}

CASES AND PIECEWISE FUNCTIONS
─────────────────────────────────────────

\begin{equation}
  |x| =
  \begin{cases}
    x  & \text{if } x \geq 0 \\
    -x & \text{if } x < 0
  \end{cases}
\end{equation}

% With array for more control
\begin{equation}
  f(x) = \left\{
  \begin{array}{ll}
    x^2 & x \geq 0 \\
    0   & x < 0
  \end{array}
  \right.
\end{equation}
```

### Matrices and Arrays

```latex
MATRIX ENVIRONMENTS
═══════════════════════════════════════════════════════════════

BASIC MATRICES (from amsmath)
─────────────────────────────────────────

% No delimiters
\begin{matrix}
  a & b \\
  c & d
\end{matrix}

% Parentheses
\begin{pmatrix}
  a & b \\
  c & d
\end{pmatrix}

% Square brackets
\begin{bmatrix}
  a & b \\
  c & d
\end{bmatrix}

% Curly braces
\begin{Bmatrix}
  a & b \\
  c & d
\end{Bmatrix}

% Vertical bars (determinant)
\begin{vmatrix}
  a & b \\
  c & d
\end{vmatrix}

% Double vertical bars (norm)
\begin{Vmatrix}
  a & b \\
  c & d
\end{Vmatrix}

LARGE MATRICES
─────────────────────────────────────────

% With dots
\begin{pmatrix}
  a_{11} & a_{12} & \cdots & a_{1n} \\
  a_{21} & a_{22} & \cdots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}

% Small inline matrix
The matrix $\bigl(\begin{smallmatrix}
  a & b \\ c & d
\end{smallmatrix}\bigr)$ is invertible.

BLOCK MATRICES
─────────────────────────────────────────

\begin{pmatrix}
  A & B \\
  \hline
  C & D
\end{pmatrix}

% Using array for precise control
\left(\begin{array}{c|c}
  A & B \\
  \hline
  C & D
\end{array}\right)
```

### Delimiters and Sizing

```latex
DELIMITER SIZING
═══════════════════════════════════════════════════════════════

AUTOMATIC SIZING
─────────────────────────────────────────
\left( \frac{a}{b} \right)
\left[ \sum_{i=1}^n x_i \right]
\left\{ x \in \mathbb{R} : x > 0 \right\}
\left| \frac{f(x)}{g(x)} \right|
\left\| \mathbf{v} \right\|

% Unmatched delimiters
\left( x + y \right.  % no right delimiter
\left. x + y \right)  % no left delimiter

MANUAL SIZING (when \left/\right fails)
─────────────────────────────────────────
% Size commands: \big, \Big, \bigg, \Bigg
\bigl( x \bigr)       % slightly larger than normal
\Bigl( x \Bigr)       % larger
\biggl( x \biggr)     % even larger
\Biggl( x \Biggr)     % largest

% For relations and operators
\bigl| \Bigl| \biggl| \Biggl|

% Example: nested fractions
\Biggl( \biggl( \Bigl( \bigl( x \bigr) \Bigr) \biggr) \Biggr)

ANGLE BRACKETS
─────────────────────────────────────────
\langle x, y \rangle           % inner product
\left\langle x, y \right\rangle % auto-sized

FLOOR AND CEILING
─────────────────────────────────────────
\lfloor x \rfloor   % floor
\lceil x \rceil     % ceiling
\left\lfloor \frac{n}{2} \right\rfloor

SEMANTIC BRACKETS (stmaryrd)
─────────────────────────────────────────
\llbracket x \rrbracket  % denotational semantics
```

---

## Mathematical Notation

### Common Symbol Reference

```latex
MATHEMATICAL SYMBOLS QUICK REFERENCE
═══════════════════════════════════════════════════════════════

NUMBER SYSTEMS
─────────────────────────────────────────
\mathbb{N}   ℕ  Natural numbers
\mathbb{Z}   ℤ  Integers
\mathbb{Q}   ℚ  Rationals
\mathbb{R}   ℝ  Reals
\mathbb{C}   ℂ  Complex numbers
\mathbb{F}   𝔽  Finite field

SET OPERATIONS
─────────────────────────────────────────
\in          ∈  Element of
\notin       ∉  Not element of
\subset      ⊂  Proper subset
\subseteq    ⊆  Subset or equal
\supset      ⊃  Proper superset
\supseteq    ⊇  Superset or equal
\cup         ∪  Union
\cap         ∩  Intersection
\setminus    \  Set difference
\emptyset    ∅  Empty set
\times       ×  Cartesian product

LOGIC
─────────────────────────────────────────
\land        ∧  Logical and
\lor         ∨  Logical or
\lnot        ¬  Logical not
\implies     ⟹  Implies
\iff         ⟺  If and only if
\forall      ∀  For all
\exists      ∃  Exists
\nexists     ∄  Does not exist

RELATIONS
─────────────────────────────────────────
\leq         ≤  Less or equal
\geq         ≥  Greater or equal
\neq         ≠  Not equal
\equiv       ≡  Equivalent/congruent
\sim         ∼  Similar
\simeq       ≃  Similar or equal
\cong        ≅  Congruent/isomorphic
\approx      ≈  Approximately
\propto      ∝  Proportional to

OPERATORS
─────────────────────────────────────────
\sum         Σ  Summation
\prod        Π  Product
\int         ∫  Integral
\oint        ∮  Contour integral
\partial     ∂  Partial derivative
\nabla       ∇  Gradient/del
\infty       ∞  Infinity

ARROWS
─────────────────────────────────────────
\to          →  Maps to
\mapsto      ↦  Maps to (function)
\leftarrow   ←  Left arrow
\Rightarrow  ⇒  Double right arrow
\Leftrightarrow ⇔ Double both
\hookrightarrow ↪ Inclusion
\twoheadrightarrow ↠ Surjection

GREEK LETTERS
─────────────────────────────────────────
\alpha α    \beta β     \gamma γ    \delta δ
\epsilon ε  \zeta ζ     \eta η      \theta θ
\iota ι     \kappa κ    \lambda λ   \mu μ
\nu ν       \xi ξ       \pi π       \rho ρ
\sigma σ    \tau τ      \upsilon υ  \phi φ
\chi χ      \psi ψ      \omega ω

% Variants
\varepsilon ε  \vartheta ϑ  \varpi ϖ
\varrho ϱ      \varsigma ς  \varphi φ

% Uppercase
\Gamma Γ    \Delta Δ    \Theta Θ    \Lambda Λ
\Xi Ξ       \Pi Π       \Sigma Σ    \Upsilon Υ
\Phi Φ      \Psi Ψ      \Omega Ω
```

### Custom Commands

```latex
DEFINING CUSTOM COMMANDS
═══════════════════════════════════════════════════════════════

BASIC SHORTCUTS
─────────────────────────────────────────
% Number systems
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}

% Common functions
\newcommand{\abs}[1]{\left|#1\right|}
\newcommand{\norm}[1]{\left\|#1\right\|}
\newcommand{\inner}[2]{\langle #1, #2 \rangle}
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}

% Probability and statistics
\newcommand{\E}{\mathbb{E}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\Prob}{\mathbb{P}}

% Calculus
\newcommand{\dd}{\,\mathrm{d}}  % differential d
\newcommand{\pd}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\td}[2]{\frac{\mathrm{d} #1}{\mathrm{d} #2}}

OPERATOR NAMES
─────────────────────────────────────────
% Standard operators (already defined)
\sin, \cos, \tan, \log, \exp, \det, \dim, \ker, \Im, \Re

% Custom operators
\DeclareMathOperator{\tr}{tr}         % trace
\DeclareMathOperator{\rank}{rank}     % rank
\DeclareMathOperator{\diag}{diag}     % diagonal
\DeclareMathOperator{\sgn}{sgn}       % sign
\DeclareMathOperator{\supp}{supp}     % support
\DeclareMathOperator{\argmax}{arg\,max}
\DeclareMathOperator{\argmin}{arg\,min}
\DeclareMathOperator*{\esssup}{ess\,sup}  % * for limits

% With limits placement
\DeclareMathOperator*{\argmax}{arg\,max}
% Then: \argmax_{x \in X} f(x) puts limit below

PAIRED DELIMITERS (mathtools)
─────────────────────────────────────────
\DeclarePairedDelimiter{\abs}{\lvert}{\rvert}
\DeclarePairedDelimiter{\norm}{\lVert}{\rVert}
\DeclarePairedDelimiter{\inner}{\langle}{\rangle}
\DeclarePairedDelimiter{\floor}{\lfloor}{\rfloor}
\DeclarePairedDelimiter{\ceil}{\lceil}{\rceil}
\DeclarePairedDelimiter{\set}{\{}{\}}

% Usage: \abs{x}, \abs*{x} (auto), \abs[\big]{x}
```

---

## Proof Formatting

### Proof Environment Patterns

```latex
PROOF FORMATTING
═══════════════════════════════════════════════════════════════

STANDARD PROOF
─────────────────────────────────────────
\begin{proof}
  Let $x \in A$ be arbitrary. By definition of $A$,
  we have $P(x)$. Since $P(x) \implies Q(x)$ (Lemma~\ref{lem:pq}),
  it follows that $Q(x)$. As $x$ was arbitrary, $\forall x \in A: Q(x)$.
\end{proof}

PROOF WITH CUSTOM QED
─────────────────────────────────────────
\begin{proof}[Proof of Theorem~\ref{thm:main}]
  The argument proceeds in three steps.

  \emph{Step 1.} We first establish that...

  \emph{Step 2.} Next, we show that...

  \emph{Step 3.} Finally, combining Steps 1 and 2...
\end{proof}

% Custom QED symbol
\renewcommand{\qedsymbol}{$\blacksquare$}

PROOF BY CASES
─────────────────────────────────────────
\begin{proof}
  We proceed by cases.

  \textbf{Case 1:} $n$ is even. Write $n = 2k$ for some $k \in \Z$.
  Then $n^2 = 4k^2 = 2(2k^2)$, which is even.

  \textbf{Case 2:} $n$ is odd. Write $n = 2k+1$ for some $k \in \Z$.
  Then $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, which is odd.

  In both cases, $n^2$ and $n$ have the same parity.
\end{proof}

PROOF BY INDUCTION
─────────────────────────────────────────
\begin{proof}
  We proceed by induction on $n$.

  \emph{Base case} ($n = 0$): We have $\sum_{i=0}^{0} i = 0 =
  \frac{0 \cdot 1}{2}$, so the claim holds.

  \emph{Inductive step}: Assume the claim holds for some $k \geq 0$.
  Then
  \begin{align*}
    \sum_{i=0}^{k+1} i &= \sum_{i=0}^{k} i + (k+1) \\
      &= \frac{k(k+1)}{2} + (k+1) \tag{by IH} \\
      &= \frac{(k+1)(k+2)}{2}.
  \end{align*}
  Thus the claim holds for $k+1$.

  By induction, the claim holds for all $n \geq 0$.
\end{proof}

PROOF SKETCH
─────────────────────────────────────────
\begin{proof}[Proof sketch]
  The main idea is to apply the contraction mapping theorem
  to the operator $T$. One verifies that $T: X \to X$ is a
  contraction with constant $\alpha < 1$, and the result follows.
  The details are left as an exercise.
\end{proof}
```

---

## Diagrams and Figures

### Commutative Diagrams

```latex
COMMUTATIVE DIAGRAMS WITH tikz-cd
═══════════════════════════════════════════════════════════════

\usepackage{tikz-cd}

BASIC SQUARE
─────────────────────────────────────────
\begin{tikzcd}
  A \arrow[r, "f"] \arrow[d, "g"'] & B \arrow[d, "h"] \\
  C \arrow[r, "k"'] & D
\end{tikzcd}

EXACT SEQUENCE
─────────────────────────────────────────
\begin{tikzcd}
  0 \arrow[r] & A \arrow[r, "f"] & B \arrow[r, "g"] & C \arrow[r] & 0
\end{tikzcd}

TRIANGLE
─────────────────────────────────────────
\begin{tikzcd}
  A \arrow[rr, "f"] \arrow[dr, "g"'] & & B \arrow[dl, "h"] \\
  & C &
\end{tikzcd}

ARROW STYLES
─────────────────────────────────────────
\arrow[r]                   % plain arrow
\arrow[r, "f"]              % labeled
\arrow[r, "f"']             % label below
\arrow[r, hook]             % injection ↪
\arrow[r, two heads]        % surjection ↠
\arrow[r, dashed]           % dashed
\arrow[r, dotted]           % dotted
\arrow[r, Rightarrow]       % double arrow ⇒
\arrow[r, bend left]        % curved
\arrow[r, shift left]       % parallel arrows
\arrow[r, "\sim"', sloped]  % isomorphism, label along arrow

PULLBACK/PUSHOUT
─────────────────────────────────────────
\begin{tikzcd}
  A \times_C B \arrow[r] \arrow[d] \arrow[dr, phantom, "\lrcorner",
    very near start] & B \arrow[d] \\
  A \arrow[r] & C
\end{tikzcd}
```

### Function Plots

```latex
FUNCTION PLOTS WITH pgfplots
═══════════════════════════════════════════════════════════════

\usepackage{pgfplots}
\pgfplotsset{compat=1.18}

BASIC FUNCTION PLOT
─────────────────────────────────────────
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  xlabel={$x$},
  ylabel={$y$},
  domain=-2:2,
  samples=100,
  width=8cm,
  height=6cm,
]
  \addplot[blue, thick] {x^2};
  \addplot[red, thick, dashed] {x^3};
  \legend{$x^2$, $x^3$}
\end{axis}
\end{tikzpicture}

MULTIPLE FUNCTIONS
─────────────────────────────────────────
\begin{tikzpicture}
\begin{axis}[
  axis lines=middle,
  domain=-pi:pi,
  samples=200,
  legend pos=north east,
]
  \addplot[blue, thick] {sin(deg(x))};
  \addplot[red, thick] {cos(deg(x))};
  \legend{$\sin x$, $\cos x$}
\end{axis}
\end{tikzpicture}

3D SURFACE
─────────────────────────────────────────
\begin{tikzpicture}
\begin{axis}[
  view={45}{30},
  colormap/viridis,
]
  \addplot3[surf, domain=-2:2, domain y=-2:2] {x^2 + y^2};
\end{axis}
\end{tikzpicture}
```

---

## Bibliography Management

### BibTeX Reference Formatting

```
BIBTEX ENTRY TYPES
═══════════════════════════════════════════════════════════════

JOURNAL ARTICLE
─────────────────────────────────────────
@article{AuthorYear,
  author  = {Last, First and Other, Author},
  title   = {Title of the Article},
  journal = {Journal Name},
  year    = {2024},
  volume  = {42},
  number  = {3},
  pages   = {100--150},
  doi     = {10.1234/example.doi},
}

BOOK
─────────────────────────────────────────
@book{AuthorYear,
  author    = {Last, First},
  title     = {Title of the Book},
  publisher = {Publisher Name},
  year      = {2024},
  edition   = {3rd},
  address   = {City},
  isbn      = {978-0-123456-78-9},
}

CONFERENCE PAPER
─────────────────────────────────────────
@inproceedings{AuthorYear,
  author    = {Last, First and Second, Author},
  title     = {Title of the Paper},
  booktitle = {Proceedings of the Conference},
  year      = {2024},
  pages     = {1--10},
  publisher = {Publisher},
  address   = {Location},
}

ARXIV PREPRINT
─────────────────────────────────────────
@misc{AuthorYear,
  author       = {Last, First},
  title        = {Title of the Preprint},
  year         = {2024},
  eprint       = {2401.12345},
  archiveprefix = {arXiv},
  primaryclass = {math.AG},
}

THESIS
─────────────────────────────────────────
@phdthesis{AuthorYear,
  author = {Last, First},
  title  = {Title of the Dissertation},
  school = {University Name},
  year   = {2024},
  type   = {{Ph.D.} Dissertation},
}

@mastersthesis{AuthorYear,
  author = {Last, First},
  title  = {Title of the Thesis},
  school = {University Name},
  year   = {2024},
}
```

### Citation Commands

```latex
CITATION COMMANDS
═══════════════════════════════════════════════════════════════

BASIC CITATIONS (natbib)
─────────────────────────────────────────
\cite{key}         →  [1] or (Author, 2024)
\citep{key}        →  (Author, 2024)     % parenthetical
\citet{key}        →  Author (2024)      % textual
\citep*{key}       →  (Author et al., 2024)
\citeauthor{key}   →  Author
\citeyear{key}     →  2024

% Multiple citations
\citep{key1, key2, key3}  →  (Author1, 2024; Author2, 2023)

% With page numbers
\citep[p.~42]{key}        →  (Author, 2024, p. 42)
\citep[see][]{key}        →  (see Author, 2024)
\citep[see][p.~42]{key}   →  (see Author, 2024, p. 42)

CROSS-REFERENCES (cleveref)
─────────────────────────────────────────
\cref{eq:main}     →  Equation (1)
\Cref{eq:main}     →  Equation (1) (sentence start)
\cref{thm:main}    →  Theorem 1
\cref{fig:plot}    →  Figure 1
\cref{sec:intro}   →  Section 1

% Ranges
\cref{eq:first,eq:second,eq:third}  →  Equations (1) to (3)

% Custom names
\crefname{equation}{Eq.}{Eqs.}
\crefname{theorem}{Thm.}{Thms.}
```

---

## Publication-Quality Checklist

```
MANUSCRIPT PREPARATION CHECKLIST
═══════════════════════════════════════════════════════════════

FORMATTING
─────────────────────────────────────────
□ Consistent theorem numbering throughout
□ All equations numbered that are referenced
□ Figures and tables have informative captions
□ All cross-references resolve correctly
□ Page limits respected (if applicable)
□ Font requirements met (if specified)

MATHEMATICS
─────────────────────────────────────────
□ All notation defined before first use
□ Consistent notation throughout (no conflicting meanings)
□ Display equations used for important formulas
□ Inline math properly spaced (\,dx not dx in integrals)
□ Proper use of \text{} in equations for words
□ Correct delimiter sizing

PROOFS
─────────────────────────────────────────
□ All proofs have explicit QED symbols
□ Proof structure clear (cases labeled, steps marked)
□ All references to lemmas/theorems correct
□ Induction hypotheses clearly stated
□ Base cases verified

BIBLIOGRAPHY
─────────────────────────────────────────
□ All citations have complete information
□ Journal names consistent (abbreviated or full)
□ DOIs included where available
□ arXiv references properly formatted
□ Author names in consistent format
□ No duplicate entries

FINAL CHECKS
─────────────────────────────────────────
□ No overfull/underfull hbox warnings
□ All labels resolve (no "??" in output)
□ Table of contents accurate (if included)
□ Index accurate (if included)
□ PDF bookmarks correct
□ Hyperlinks functional
□ Compile with no errors
```

---

## Common Errors and Fixes

```
TROUBLESHOOTING GUIDE
═══════════════════════════════════════════════════════════════

ERROR: Missing $ inserted
─────────────────────────────────────────
Problem: Math mode character outside math mode
Fix: Use $...$ or \(...\) for inline math
Example: x^2 → $x^2$

ERROR: Undefined control sequence
─────────────────────────────────────────
Problem: Command not defined or package missing
Fix: Add appropriate \usepackage{} or define command
Common: \R undefined → add \newcommand{\R}{\mathbb{R}}

ERROR: Package babel Error: You haven't loaded the option X
─────────────────────────────────────────
Problem: Language option conflict
Fix: Load babel with correct options before hyperref

ERROR: ! LaTeX Error: \begin{align} ended by \end{equation}
─────────────────────────────────────────
Problem: Mismatched environment names
Fix: Ensure \begin{X}...\end{X} match exactly

ERROR: Overfull \hbox
─────────────────────────────────────────
Problem: Content too wide for margins
Fixes:
  - Use \allowbreak in long formulas
  - Add \linebreak hints
  - Use multline for long equations
  - Rewrite to fit naturally

WARNING: Label `eq:foo' multiply defined
─────────────────────────────────────────
Problem: Same label used twice
Fix: Use unique labels; search for duplicates

WARNING: Citation `foo' on page X undefined
─────────────────────────────────────────
Problem: BibTeX key not in .bib file
Fixes:
  - Check spelling of citation key
  - Run bibtex/biber
  - Check .bib file is referenced correctly

SPACING ISSUES
─────────────────────────────────────────
Extra space around operators:
  Bad:  $f : X \to Y$  (spaces in source)
  Good: $f\colon X \to Y$

Missing thin space in integrals:
  Bad:  $\int f(x)dx$
  Good: $\int f(x)\,dx$

Improper operator spacing:
  Bad:  $sin(x)$
  Good: $\sin(x)$
```

---

## Integration with Agents

### Recommended Agent Combinations

- **proof-constructor**: Generates proofs for LaTeX formatting
- **axiom-architect**: Provides formal axiom system documentation
- **mathematical-modeler**: Creates model descriptions to typeset
- **counterexample-hunter**: Produces examples for illustration

---

## References

- Lamport, L. (1994). LaTeX: A Document Preparation System (2nd ed.)
- Mittelbach, F., et al. (2004). The LaTeX Companion (2nd ed.)
- Gratzer, G. (2016). More Math Into LaTeX (5th ed.)
- Kopka, H. & Daly, P. (2003). Guide to LaTeX (4th ed.)
- Downes, M. (2002). Short Math Guide for LaTeX (AMS)

