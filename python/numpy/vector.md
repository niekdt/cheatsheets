1D array operations (row vectors)

# Creation
| What | How | Details |
|---|---|---|
| Undefined, length $n$ | `np.empty(n)` | Warning: don't use the initial values |
| Zeros (FP, length $n$) | `np.zeros(n)` | |
| Zeros (int, length $n$) | `np.zeros(n, dtype=np.int64)` | |
| Ones (length $n$) | `np.ones(n)` | |
| True values (bool, length $n$) | `np.full(n, fill_value=True)` | |
| False values (bool, length $n$) | `np.full(n, fill_value=False)` | |
| Fill with value $v$ (bool, length $n$) | `np.full(n, fill_value=v)` | |
| Increasing numbers [0, $b$-1] | `np.arrange(b)` | |
| Increasing numbers [ $a$, $b$] | `np.arrange(a, b)` | |
| Numbers from $a$ to $b$ with step size $s$ | `np.arrange(a, b, s)` | |
| Linear range from $a$ to $b$ of length $n$ | `np.linspace(a, b, num=n)` | |
| From tuple | `np.array(tuple)` | |
| From list | `np.array(list)` | |
| From iter | `np.fromiter(iter)` | |
| From iter (max length $n$) | `np.fromiter(iter, count=n)` | |
| From two vectors | `np.append(v1, v2)` | |
| From vectors (concat) | `np.concatenate((v1, v2))` | |

# Test
| What | How | Details |
|---|---|---|
| Vector | `v.ndim == 1` | |
| Logical type | `v.dtype == np.bool_` | |
| Float type | `v.dtype == np.float_` | |
| Integer type | `v.dtype == np.int_` | |
| Contains `nan` | `np.isnan(v).any()` | |
| Contains `inf` | `np.isinf(v).any()` | |
| Contains value | `value in v` | |
| Does not contain value | `value not in v` | |
| All finite | `np.isfinite(v).all()` | |
| All elements are equal to value | `(v == value).all()` | |
| All elements are equal to valu | `np.all(v == value)` | |
| All numerical elements are close to value | `np.all(np.isclose(v, value))` | |
| All numerical elements are equal | `np.ptp(v) == 0` | |
| Vectors are equal | `np.array_equal(v, v2)` | |

# Update
Operations are in-place.
| What | How | Details |
|---|---|---|
| Set first element | `v[0] = value` | |
| Set last element | `v[-1] = value` | |
| Set value for element $i$ | `v[i] = value` | |
| Fill | `v[:] = value` | |
| Fill first $n$ values | `v[:n] = value` | |
| Sort elements ascending | `v.sort()` | NaNs are put last|
| Sort elements descending | `v[::-1].sort()` | Note that this puts NaNs first! |

# Query
| What | How | Details |
|---|---|---|
| Unique values | `numpy.unique(v)` | |
| Unique values | `set(v)` | |
| Number of unique values | `len(numpy.unique(v))` | |
| Count non-zero values | `np.count_nonzero(v)` | |
| Count per unique value | `np.unique(v, return_counts=True)` | |
| Count per positive integer from [0, `max(v)`] | `np.bincount(v)` | Elements must be nonnegative ints|

# Aggregate
All operations produce a scalar value.
| What | How | Details |
|---|---|---|
| Min | `np.min(v)` | Use `nanmin()` if NaNs are present |
| Max | `np.max(v)` | |
| Max - min | `np.ptp(v)` | |
| Index of first max element | `np.argmax(v)` | Returns index of NaN if present! |
| Index of first min element | `np.argmin(v)` | Returns index of NaN if present! |
| Sum | `np.sum(v)` | |
| Mean | `np.mean(v)` | |
| Standard deviation | `np.std(v)` | |
| Variance | `np.var(v)` | |
| Median | `np.median(v)` | |
| Quantile $q$ | `np.quantile(v, q)` | |

# Map
| What | How | Details |
|---|---|---|
| Clip (truncate) between [ $a$, $b$ ] | `np.clip(v, a_min=a, a_max=b)` | |
| Bin index | `np.digitize(v, bins)` | |
| Linear interpolation of coordinate mapping `xp -> yp` | `np.interp(v, xp, yp)` | No option for extrapolation! |

# Reorder
| What | How | Details |
|---|---|---|
| Reverse elements | `v[::-1]` | |
| Reverse elements | `np.flip(v)` | |
| Shift elements forwards (roll) | `np.roll(v, 1)` | |
| Shift elements backwards (roll) | `np.roll(v, -1)` | |
| Ascending order indices | `np.argsort(v)` | |
| Descending order indices | `np.argsort(-v)` | |
| Sort ascending | `np.sort(v)` | NaNs are last |
| Sort descending | `v[np.argsort(-v)]` | NaNs are last |

# Shrink
| What | How | Details |
|---|---|---|
| Difference | `np.diff(v)` | |
| Difference with lag $l$ | `np.diff(v, n=l)` | |

# Grow
| What | How | Details |
|---|---|---|
| Pad with value | `np.pad(v, pad_width=1, constant_values=v)` | | 
| Pad with edge elements | `np.pad(v, pad_width=1, mode='edge')` | |
| Replicate $n$ times | `np.repeat(v, n)` | |
| Append vector | `np.append(v1, v2)` | |
| Concatenate vectors | `np.concatenate((v1, v2, v3))` | |

# Convert
| What | How | Details |
|---|---|---|
| Bytes | `v.tobytes()` | |
| Tuple | `tuple(v)` | |
| List | `v.tolist()` | |
| Set | `set(v)` | |
