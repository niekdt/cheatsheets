---
layout: default
title: Factor
parent: R
---

# Factor
{: .no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| From vector | `factor(x)` | |
| From vector, with renamed levels | `factor(x, levels=1:3, labels=LETTERS[1:3])` | |
| Generate by pattern | `gl(5, 2, labels=LETTERS[1:5])` | |
| Generate factor of interactions with another | `interaction(f1, f2)` | |
| Combine factors | `factor(c(as.character(x), as.character(y)), union(levels(x), levels(y)))` | |

## Get

| What | How | Details |
|---|---|---|
| Levels | `levels(f)` | |
| Number of levels | `nlevels(f)` | |
| Subset and drop unused levels | `f[1:2, drop=TRUE]` | |

## Update

| What | How | Details |
|---|---|---|
| Add NA as a factor level | `addNA(f)` | |
| Add NA as a factor level in `data.table` | `dt[is.na(f), f := 'NA']` | |
| Drop unused factors levels | `factor(f)` | |
| Drop factor levels | `droplevels(f, exclude=X)` | |
| Drop factor levels except for | `droplevels(f, except=X)` | |
| Remap factor | `x = factor(c('a1', 'b1', 'a2', 'c1'))`<br>`factor(x, levels=levels(x), labels=c('a', 'a', 'b', 'c'))` | |
