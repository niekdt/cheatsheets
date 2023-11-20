---
layout: default
title: Vector
parent: R
nav_order: 0
---

# Vector
{: .no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| Define vector | `c(1, 2, 3)` | |
| Zeros, length _n_ | `numeric(n)` | |
| Zeros, length _n_ | `vector('numeric', n)` | |
| NaNs, length _n_ | `NaN[1:3]` | |
| Sequence from _a_ to _b_ | `seq(a, b)` | |
| Sequence between _a_ to _b_ of length _n_ | `seq(a, b, length.out=n)` | |
| Repeat vector | `rep(x, 2)` | |
| Repeat vector up to length _n_ | `rep_len(x, n)` | |
| Create vector or matrix depending on the columns | `mat.or.vec(1:5, nc=2)` | |

## Get

| What | How | Details |
|---|---|---|
| Length | `length(x)` | |
| Element names | `names(x)` | |
| First element | `x[0]` | |
| Last element | `last(x)` | |

## Reorder 

| What | How | Details |
|---|---|---|
| Sort descending | `sort(x)` | |
| Reverse | `rev(x)` | |
| Shuffle | `sample(x)` | |

## Indexing

| What | How | Details |
|---|---|---|
| `TRUE` values | `which(x)` | |
| Largest value | `which.max(x)` | |
| Smallest value | `which.min(x)` | |
| Order by value, breaking ties with further args | `order(x)` | |
| Ranking, with ties option | `rank(x, ties='first')` | |

## Update (element-wise)

| What | How | Details |
|---|---|---|
| If-else | `ifelse(x == TRUE, 1, 0)` |
| If-else with consecutive output | `ifelse(x, seq(-1, -100, by=-1), 1:100)` | |
| Replace NAs by zeros | `ifelse(is.na(x), 0, x)` | |
| Replace specific values by zeros | `ifelse(x %in% values, 0, x)` | |
| Replace elements at index with given values | `replace(x, c(2, 4), c(NA, Inf))` | |
| Clip values below _a_ | `pmin(x, a)` | |
| Clip values above _b_ | `pmax(x, b)` | |
| Find element-wise min/max values between vectors | `pmax(x, y)` | |
| Discretize values into bin number | `findInterval(1:4, c(0, 2, 4))` | |
| Discretize values into _n_ levels | `cut(x, n)` | |
| Discretize values in intervals | `cut(x, breaks)` | |
| Linear interpolation | `approxfun(x, method='linear')(x2)` | |
| Spline interpolation | `splinefun(x)(x2)` | |
| Smoothing spline interpolation | `smooth.spline(x) %>% predict(x2)` | |

## Aggregate

| What | How | Details |
|---|---|---|
| Sum | `sum(x)` | |
| Mean | `mean(x)` | |
| Mode | `table(x) %>% sort() %>% names() %>% last()` | |
| Mode of positive integers `1:K` | `tabulate(x) %>% which.max()` | |
| Compute function per group, as list | `tapply(x, INDEX = rep_len(1:2, length(x)), mean)` | outputs a list with the results per group |

## Shrink

| What | How | Details |
|---|---|---|
| Exclude NA | `na.exclude(x)` | |
| Exclude NA | `x[!is.na(x)]` | |
| Exclude NA | `Filter(Negate(is.na), x)` | |
| Exclude non-finite values | `x[is.finite(x)]` | |
| Exclude non-finite values | `Filter(is.finite, x)` | |
| Lagged difference | `diff(x)` | |
| Sample _n_ elements | `sample(x, n)` | |

## Convert

| What | How | Details |
|---|---|---|
| Split vector into list of vectors, according to grouping | `split(1:10, rep(1:2, 5)` | Can be undone by `unsplit(x, rep(1:2, 5))` |
| Running-length encoding | `rle(x)` | |
