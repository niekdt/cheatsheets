# Creation
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

# Properties
| What | How | Details |
|---|---|---|
| Length | `len(x)` | |

# Tests
| What | How | Details |
|---|---|---|
| Empty | `if not x:` | |
| Not empty | `if x:` | |
| Contains value $v$ | `v in x` | |
| Does not contain value $v$ | `v not in x` | |
| Contains duplicate values | `len(v) != len(set(v))` | |
| All elements are True | `all(x)` | |
| Any element is True | `any(x)` | |
| No elements are True | `not any(x)` | |

# Query
| What | How | Details |
|---|---|---|
| Value at index $i$ | `x[i]` | |
| Value from end index $i$ | `x[-i]` | |
| Count occurrences of value $v$ | `x.count(v)` | |
| First index of value $v$ | `x.index(v)` | Error if missing |
| First index of value $v$ between index range [$n$, $m$] | `x.index(v, n, m)` | Error if missing in range |
| Sum elements | `sum(x)` | |
| Min of elements | `min(x)` | |
| Max of elements | `max(x)` | |

# Derive
Creates a new immutable copy.
| What | How | Details |
|---|---|---|
| Subset between [$n$, $m$] (slice) | `x[n:m]` | |
| First $n$ elements | `x[:n]` | |
| Last $n$ elements | `x[-n:]` | |
| Append element | `x += (1,)` | |
| Append tuple | `x += y` | |
| Reverse | `x[::-1]` | |
| Reverse | `tuple(reversed(x))` | Much slower in all cases |
| Sort | `tuple(sorted(x))` | |
| Shuffle | `tuple(random.sample(x, k=len(x)))` | |
| Replicate elements $n$ times | `x * n` | |

# Convert
| What | How | Details |
|---|---|---|
| Multiple assignment | `a, b = x` | |
| Hash | `hash(x)` | |
| Comma-separated string | `str(x)` | |
| List | `[*x]` | |
| List | `list(x)` | |
| Set | `set(x)` | |
| Set | `{*x}` | Same speed as `set(x)` |
