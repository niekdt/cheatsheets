---
layout: default
title: nlme
parent: R
nav_order: 60
---

# nlme (WIP)
{: .no_toc}

1. TOC
{:toc}

Useful links:
 * https://quantdev.ssri.psu.edu/sites/qdev/files/ILD_Ch06_2017_MLMwithHeterogeneousVariance.html

## Specify

| What | How | Details |
|---|---|---|
| Random intercept model with _subject_ as grouping factor | `lme(fixed = y ~ x, random = ~ 1 | subject)` | |
| With random intercept | `random = ~ 1 | subject` | |
| With random intercept | `random = list(subject = pdSymm(form = ~ 1))` | |
| With random intercept, different between-subject SD per group | `random = list(subject = pdDiag(form = ~ diagnosis))` | |
| With factor-dependent within-subject error | `weights = varIdent(form = ~ 1 | diagnosis)` | |
| With AR-1 correlation structure | `correlation = corAR1(form = ~ 1 | subject)` | |


## Extract

Extract info from a fitted model.

| What | How | Details |
|---|---|---|
| Fixed effects coefficients | `fixef(model)` | |
| Fixed effects coefficient intervals | `intervals(model)` | |
| Variance and SD summary | `VarCorr(model)` | |
| Variance-covariance matrix | `vcov(model)` | |
| Within-subject variance | `sigma(model)^2` | |
| Within-subject SD | `sigma(model)` | |
| Within-subject SD for group _$GROUP_ (when using `weights=varIdent`) | `sigma(model) * coef(model$modelStruct$varStruct, unconstrained = FALSE, allCoef = TRUE)['$GROUP']` | |
| Between-subject variance | `VarCorr(model)['Residual', 'Variance']` | |
| Between-subject SD | `VarCorr(model)['Residual', 'StdDev']` | |

## Model fit

| What | How | Details |
|---|---|---|
| Log-likelihood | `logLik(model)` | |
| AIC | `AIC(model)` | |
| BIC | `BIC(model)` | |
| Marginal pseudo R-squared | `r.squaredGLMM(model)[1, 'R2m']` | |
| Conditional pseudo R-squared | `r.squaredGLMM(model)[1, 'R2c']` | |
| Plot residuals against predicted | `plot(model)` | |
| Plot random effects | `plot(ranef(model))` | |
| Q-Q plot | `car::qqPlot(residuals(model))` | |

## Statistical testing

| What | How | Details |
|---|---|---|
| Coefficient significance | `car::Anova(model)` | |
| Nested model improvement (likelihood ratio test) | `anova(model0, model1)` | |
