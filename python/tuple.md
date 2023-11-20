---
layout: default
title: Tuple
parent: Python
nav_order: 2
---

# Tuple
{: .no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| Empty | `()` | |
| Single element | `(1,)` | Comma is important |
| Multiple elements | `(1, 2, 3)` | |
| Multiple assignment | `x = 1, 2, 3` | |
| From multiple tuples | `a + b + c` | |
| From iterator | `tuple(a)` | |
| From iterator by unpacking | `(*a,)` | |
| From comprehension | `tuple(v * 2 for v in a)` | |

## Test

| What | How | Details |
|---|---|---|
| Empty | `if not x:` | |
| Not empty | `if x:` | |
| Contains value _v_ | `v in x` | |
| Does not contain value _v_ | `v not in x` | |
| Contains duplicate values | `len(v) != len(set(v))` | |
| All elements are True | `all(x)` | |
| Any element is True | `any(x)` | |
| No elements are True | `not any(x)` | |

## Get

| What | How | Details |
|---|---|---|
| Length | `len(x)` | |
| Value at index _i_ | `x[i]` | |
| Value from end index _i_ | `x[-i]` | |
| Count occurrences of value _v_ | `x.count(v)` | |
| First index of value _v_ | `x.index(v)` | Error if missing |
| First index of value _v_ between index range \[ _n_, _m_ ] | `x.index(v, n, m)` | Error if missing in range |
| Sum elements | `sum(x)` | |
| Min of elements | `min(x)` | |
| Max of elements | `max(x)` | |

## Derive
Creates a new immutable copy.

| What | How | Details |
|---|---|---|
| Subset between \[ _n_, _m_ ] (slice) | `x[n:m]` | |
| First _n_ elements | `x[:n]` | |
| Last _n_ elements | `x[-n:]` | |
| Append element | `x += (1,)` | |
| Append tuple | `x += y` | |
| Reverse | `x[::-1]` | |
| Reverse | `tuple(reversed(x))` | Much slower in all cases |
| Sort | `tuple(sorted(x))` | |
| Shuffle | `tuple(random.sample(x, k=len(x)))` | |
| Replicate elements _n_ times | `x * n` | |

## Convert

| What | How | Details |
|---|---|---|
| Multiple assignment | `a, b = x` | |
| Hash | `hash(x)` | |
| Comma-separated string | `str(x)` | |
| List | `[*x]` | |
| List | `list(x)` | |
| Set | `set(x)` | |
| Set | `{*x}` | Same speed as `set(x)` |
