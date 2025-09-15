---
layout: post
title: "Statistical Testing for Observational Studies"
---
Statistical tests help quantify relationships in data collected without controlled experiments.

## What it is
Observational studies track phenomena without assigning treatments. Statistical testing evaluates whether observed differences or associations are likely due to chance.

## Key considerations before doing stat testing
- Check data quality and missingness.
- Assess whether treatment assignment is ignorable or if confounding needs adjustment.
- Ensure sample size and power are adequate.
- Pre-specify hypotheses and avoid data dredging.

## Key tests
- **t-tests** and **ANOVA** for mean comparisons.
- **Chi-square tests** for categorical associations.
- **Regression-based tests** for covariate-adjusted effects.
- **Non-parametric tests** like Mann-Whitney or Wilcoxon when assumptions fail.

## When to use them
Use tests that align with your outcome type, distributional assumptions, and study design. For example, chi-square tests suit categorical outcomes, while regression is flexible for continuous or binary outcomes with covariate adjustment.

## Pros and cons
**Pros**
- Provide quantitative evidence for associations.
- Enable covariate adjustment when using regression.

**Cons**
- Vulnerable to hidden bias and confounding.
- May yield misleading p-values if assumptions are violated.

## Common pitfalls and limitations
- Ignoring multiple testing leads to inflated false positives.
- Treating observational estimates as causal without accounting for confounders.
- Over-reliance on p-values without considering effect size or confidence intervals.

## Interpretation guide
A small p-value suggests the observed association is unlikely under the null hypothesis, not that the effect is causal. Interpret results in context, examining assumptions, effect sizes, and potential biases.
