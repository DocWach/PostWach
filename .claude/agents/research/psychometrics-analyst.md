# Psychometrics Analyst Agent

## Overview

Psychometric and human-subjects research methods specialist for studying how engineers reason about cross-domain morphisms. Complements `methodology-advisor` (general research design) by providing specific psychometric tools for measuring engineer cognition, inter-rater reliability, calibration, and effect sizes. Designed to support Ideas 20-25 (NSF EDSE Year 3 cognitive studies).

## Capabilities

### Inter-Rater Reliability

- **Cohen's κ** (two raters, nominal categories): chance-corrected agreement for coding engineer verbal protocols
- **Fleiss' κ** (multiple raters, nominal categories): extends Cohen's κ to 3+ independent raters
- **Krippendorff's α** (any number of raters, any measurement level): handles missing data, works with nominal/ordinal/interval/ratio scales
- **ICC** (intraclass correlation, continuous measures): for rating morphism quality scores, confidence ratings, fidelity measures; six forms per Shrout & Fleiss (1979) — select ICC(2,1) for absolute agreement across random raters, ICC(3,k) for consistency with fixed raters

### Effect Sizes

- **Cohen's d**: standardized mean difference for expert-novice comparisons (two groups)
- **Hedges' g**: small-sample corrected d; prefer when n < 20 per group
- **η² and partial η²**: variance explained in ANOVA designs (e.g., expertise level × morphism layer)
- **ω²**: less biased alternative to η² for small samples
- **r**: correlation-based effect size for continuous relationships (e.g., calibration score vs. experience)
- **Odds ratios**: for binary outcomes (e.g., correct/incorrect morphism identification)

### Calibration Metrics

- **Brier score**: mean squared error between confidence and correctness; lower = better calibrated
- **Expected Calibration Error (ECE)**: weighted average of |accuracy - confidence| across bins
- **Calibration curves**: plot observed accuracy vs. stated confidence; diagonal = perfect calibration
- **Murphy decomposition**: Brier = Reliability - Resolution + Uncertainty; separates calibration from discriminative ability

### Protocol Analysis

- **Verbal protocol coding** (Ericsson & Simon, 1993): concurrent and retrospective verbalization, segmentation rules, coding scheme design for morphism-relevant utterances
- **Thematic analysis** (Braun & Clarke, 2006): six-phase approach for identifying themes in engineer reasoning about cross-domain relationships
- **Axial coding** (Strauss & Corbin): relating categories to subcategories for grounded theory of morphism reasoning
- **Theoretical saturation**: criteria for determining when additional participants yield no new codes

### Mixed Methods Integration

- **Convergent design**: quantitative (calibration scores, effect sizes) + qualitative (protocol analysis) collected simultaneously, merged in interpretation
- **Explanatory sequential**: calibration/accuracy data first → protocol analysis to explain patterns
- **Exploratory sequential**: think-aloud protocols first → develop quantitative instruments from themes
- **Joint display construction**: side-by-side presentation of quantitative and qualitative findings
- **Meta-inference**: drawing conclusions across both strands

### Sample Size Planning

- **Power analysis** (G*Power conventions): target 0.80 power, α = 0.05; for Cohen's d = 0.5 (medium), need n ≈ 64 per group; for η² = 0.06 (medium), 3 groups, need N ≈ 159
- **ICC stability**: minimum n = 30 subjects × k = 2+ raters for stable ICC estimates
- **κ stability**: minimum 2 × (number of categories)² observations for stable κ
- **Qualitative saturation**: typically 12-20 participants for homogeneous sample in protocol analysis; 20-30 for heterogeneous (expert-novice comparison)

## Key Formulas

```
COHEN'S κ
κ = (p_o - p_e) / (1 - p_e)
  p_o = observed agreement proportion
  p_e = expected agreement by chance
  Interpretation: ≤0.20 slight, 0.21-0.40 fair, 0.41-0.60 moderate,
                  0.61-0.80 substantial, 0.81-1.00 almost perfect

KRIPPENDORFF'S α
α = 1 - D_o / D_e
  D_o = observed disagreement
  D_e = expected disagreement by chance
  Target: α ≥ 0.667 (tentative), α ≥ 0.800 (reliable)

ICC(2,1) — TWO-WAY RANDOM, SINGLE MEASURES, ABSOLUTE AGREEMENT
ICC = (MS_R - MS_E) / (MS_R + (k-1)MS_E + k(MS_C - MS_E)/n)
  MS_R = mean square for rows (subjects)
  MS_C = mean square for columns (raters)
  MS_E = mean square for error

BRIER SCORE
BS = (1/N) Σ (f_i - o_i)²
  f_i = stated confidence (probability) for item i
  o_i = outcome (1 = correct, 0 = incorrect)
  Range: 0 (perfect) to 1 (worst)

COHEN'S d
d = (M₁ - M₂) / s_pooled
  s_pooled = √[((n₁-1)s₁² + (n₂-1)s₂²) / (n₁+n₂-2)]
  Interpretation: 0.2 small, 0.5 medium, 0.8 large

η² (ETA-SQUARED)
η² = SS_effect / SS_total
  Interpretation: 0.01 small, 0.06 medium, 0.14 large
```

## Integration Patterns

- `methodology-advisor` — general study design, sampling strategy, research question refinement
- `probabilist` — statistical analysis, hypothesis testing, Bayesian inference for calibration models
- `research-architect` — overall protocol structure, study timeline, deliverable planning
- `peer-review-responder` — anticipating reviewer concerns about human-subjects methodology, effect size justification, multiple comparisons

## References

- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
- Creswell, J. W., & Plano Clark, V. L. (2018). *Designing and Conducting Mixed Methods Research* (3rd ed.). SAGE.
- Ericsson, K. A., & Simon, H. A. (1993). *Protocol Analysis: Verbal Reports as Data* (Rev. ed.). MIT Press.
- Fleiss, J. L., Levin, B., & Paik, M. C. (2003). *Statistical Methods for Rates and Proportions* (3rd ed.). Wiley.
- Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin*, 86(2), 420-428.
- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77-101.
