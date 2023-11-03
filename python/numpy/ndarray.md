---
layout: default
title: ND-array
parent: Numpy
---

# N-D array operations
{: .no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| Ensure at least 1D array | `np.atleast_1d(x)` | |
| Ensure at least 2D array | `np.atleast_2d(x)` | |
| Ensure at least 3D array | `np.atleast_3d(x)` | |

## Properties

| What | How | Details |
|---|---|---|
| Number of dimensions | `x.ndim` | |
| Dimension sizes | `x.shape` | |
| Size of the first dimension | `len(x)` | |
| Number of elements | `x.size` | |

## Get

| What | How | Details |
|---|---|---|

## Aggregate to scalar

| What | How | Details |
|---|---|---|
| Sum of all elements | `np.sum(a)` | |

## Aggregate along axis

| What | How | Details |
|---|---|---|
| Sum | `np.sum(a, axis=ax)` | |

## Map

| What | How | Details |
|---|---|---|
| Cumulative sum along axis | `np.cumsum(a, axis=ax)` | |

## Shrink

| What | How | Details |
|---|---|---|
| Drop singular dimensions | `a.squeeze()` | |
| Drop singular dimensions | `np.squeeze(a)` | |
| Difference along axis | `np.diff(a, axis=ax)` | |
| Difference along axis with lag $l$ | `np.diff(a, n=l, axis=ax)` | |

## Reshape

| What | How | Details |
|---|---|---|
| Reshape to dimensions $d$ | `x.reshape(d)` |  

## Convert

| What | How | Details |
|---|---|---|
| Bytes | `x.tobytes()` | Not sure what difference with `data.tobytes()` is |
| Hash | `hash(x.data.tobytes())` | |
