---
layout: default
title: Matrix
parent: R
nav_order: 0.1
---

# Matrix
WIP
{: .no_toc}

1. TOC
{:toc}


## Create

| What | How | Details |
|---|---|---|
| From vector to column matrix | `matrix(x)` | |
| From vector to column matrix | `cbind(x)` | |

## Get

| What | How | Details |
|---|---|---|
| Elements by (row,col) pairs | `mat[matrix(c(2,3), c(4,5)), ncol=2)]` | |

## Test

| What | How | Details |
|---|---|---|
| Check if each column contains at most 1 unique value (i.e. all equal) | `apply(x, 2, uniqueN) == 1` | |
| Check if all rows are equal | `all(mat[1,] == t(mat))` | |

## Convert

| What | How | Details |
|---|---|---|
| To list of row vectors | `split(mat, row(mat))` | |
| To list of column vectors | `split(mat, col(mat))` | |
| To list of submatrices grouped by row | `lapply(split(mat, rowFactor), matrix, ncol = ncol(mat))` | |
