---
layout: default
title: Matrix
parent: Numpy
grand_parent: Python
nav_order: 2
---

# Matrix: 2D array operations
{: .no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| Undefined (size _n_ x _m_) | `np.empty((n, m))` | Warning: don't use the initial values |
| Zeros (size _n_ x _m_) | `np.zeros((n, m))` | |
| Ones (size _n_ x _m_) | `np.ones((n, m))` | |
| True values (size _n_ x _m_) | `np.full((n, m), fill_value=True)` | |
| False values (size _n_ x _m_) | `np.full((n, m), fill_value=False)` | |
| Fill with value _v_ (size _n_ x _m_) | `np.full((n, m), fill_value=v)` | |
| Identity matrix of size _n_ x _m_ | `np.eye(n, m)` | |
| Diagonal matrix from vector | `np.diag(v)` | |
| From vectors as rows | `np.row_stack((v1, v2))` | |
| From vectors as rows | `np.vstack((v1, v2))` | |
| From vectors as rows | `np.array([v1, v2])` | |
| From vectors as columns | `np.column_stack((v1, v2))` | |
| From vectors as columns | `np.stack((v1, v2), axis=1)` | |
| From vectors as columns | `np.vstack((v1, v2)).transpose()` | |

## Get

| What | How | Details |
|---|---|---|
| Element at row _i_, column _j_ | `m[i,j]` | |

## Update
All operations are in-place.

| What | How | Details |
|---|---|---|
| Update element at row _i_, column _j_ | `m[i,j] = v` | |
| Fill with scalar value | `m.fill(v)` | |
| Fill with array values | `m[...] = np.array(3)` | |
| Fill row _i_ with value | `m[i] = v` | | 
| Fill column _j_ with value | `m[:,j] = v` | |
| Resize to shape, fill with zeros | `m.resize(m, d)` | |

## Map
Operations are element-wise and preserve the shape of the matrix.

| What | How | Details |
|---|---|---|
| Increment all elements | `m + v` | |
| Increment elements by the respective element of another matrix | `m + m2` | Must be equal shape |
| Find min between two matrices | `np.fmin(m, m2)` | |
| Find max between two matrices | `np.fmax(m, m2)` | |
| Clip (truncate) between \[_a_, _b_] | `np.clip(m, a_min=a, a_max=b)` | `a_min < a_max` is not checked |

## Reorder
Operations preserve the shape of the matrix.

| What | How | Details |
|---|---|---|
| Reverse elements | `np.flip(m)` | Flattened view in reverse order |
| Sort elements descending | `np.sort(m)` | NaNs are last |
| Reverse column order | `np.fliplr(m)` | |
| Reverse row order | `np.flipud(m)` | |
| Sort elements by column descending | `np.sort(m, axis=0)` | |
| Sort elements per row descending | `np.sort(m, axis=1)` | |

## Aggregate (per column)
Summarize along an axis. Set `axis=1` for per-row operation.

| What | How | Details |
|---|---|---|
| Min | `np.min(m, axis=0)` | Use `nanmin()` to ignore NaNs |
| Max | `np.max(m, axis=0)` | Use `nanmax()` to ignore NaNs |
| Max - min | `np.ptp(m, axis=0)` | |
| Sum | `np.sum(m, axis=0)` | Use `nansum()` to ignore NaNs |
| Mean | `np.mean(m, axis=0)` | Use `nanmean()` to ignore NaNs |
| Median | `np.median(m, axis=0)` | Use `nanmedian()` to ignore NaNs |

## Shrink

| What | How | Details |
|---|---|---|
| Diagonal vector | `np.diag(m)` | | 

## Grow

| What | How | Details |
|---|---|---|
| Pad with value | `np.pad(m, pad_width=1, constant_values=v)` | |
| Pad with edge element | `np.pad(m, pad_width=1, mode='edge')` | |

## Reshape

| What | How | Details |
|---|---|---|
| Transpose | `m.T` | |
| Transpose | `m.transpose()` | |
| Rotate | `np.rot90(m)` | |
| Reshape to dimensions | `m.reshape(d)` | |

## Convert

| What | How | Details |
|---|---|---|
| 1D array (concat rows) | `m.flatten()` | |
| 1D array (concat columns) | `m.T.flatten()` | More intuitive than specifying mode |
| 1D array (concat columns) | `m.flatten(mode='F')` | |
| List of rows | `m.tolist()` | |
