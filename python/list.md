Lists can be efficiently used as a stack through `append()` and `pop()`.

# Creation
| What | How | Details |
|---|---|---|
| Define | `x = [1, 3, 9]` | |
| Define with $n$ repeated values | `x = [0] * n` | |
| From tuple | `x = list(tup)` | |
| From iterator (consumes) | `x = list(iter)` | |

# Query
| What | How | Details |
|---|---|---|
| Length | `len(x)` | |
| Get first element | `x[0]` | |
| Get last element | `x[-1]` | |
| Slice | `x[1:3]` | |
| Get first $n$ elements | `x[:n]` | |
| Get last $n$ elements | `x[-n:]` | |
| Count number of occurrences of element | `x.count(e)` | |
| Find index of element | `x.index(e)` | Throws error if not found |
| Find index of element in slice [a,b] | `x.index(e, a, b)` | Throws error if not found |

# Tests
| What | How | Details |
|---|---|---|
| Is list | `isinstance(x, list)` | |
| Empty | `if x:` | |
| Not empty | `if not x:` | |
| Contains `None` | `None in x` | |
| Contains element | `e in x` | |
| Does not contain element | `e not in x` | |
| Elements are all of type | `all(isinstance(e, str) for e in x)` | |
| Are elements sorted | ? | |
| No duplicate elements | ? | |
| Has duplicate elements | ? | |

# Update
All operations are in-place.
| What | How | Details |
|---|---|---|
| Update index $i$ | `x[i] = new_value` | |
| Update slice with list | `x[2:3] = [5, 6] | |
| Reverse elements | `x.reverse()` | |
| Sort elements | `x.sort()` | |
| Sort on transformed elements | `x.sort(key=str.lower)` | |
| Reverse-sort elements | `x.sort(reverse=True)` | |

# Resize
| What | How | Details |
|---|---|---|
| Clear | `x.clear()` | |
| Clear by slicing | `x[:] = []` | Probably slower |
| Replicate $n$ times | `x * n` | |
| Concatenate | `x + [1, 2]` | |
| Append/push element | `x.append(e)` | |
| Append/push elements | `x.extend([e1, e2])` | |
| Insert at index $i$ | `x.insert(i, e)` | |
| Remove at index $i$ | `x[i] = []` | |
| Remove at index $i$ | `del x[i]` | |
| Remove last index and return the element | `x.pop()` | |
| Remove at index $i$ and return the element | `x.pop(e, i)` |
| Remove slice | `x[2:3] = []` | |
| Remove element (first occurrence) | `x.remove(e)` | |
| Remove all elements with value | ? | |
| Remove and get last element | `x.pop()` | |

# Derive list
Shallow copies preserve references to the original object.
| What | How | Details |
|---|---|---|
| Shallow copy | `[*x]` | Fastest for small lists |
| Shallow copy | `x[:]` | Probably very slow |
| Shallow copy | `x.copy()` | Fastest for large lists |
| Shallow copy | `copy.copy(x)` | Not sure what the difference to `.copy()` is |
| Deep copy | `copy.deepcopy(x)` | Constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original. |
| Sorted | `sorted(x)` | |
| Reverse-sorted | `sorted(x, reverse=True)` | |
| Reversed order | `reversed(x)` | |
| Filter on condition | `[e for e in x if e > 0]` | |
| Filter function | `filter(fun, x)` | |
| Ternary map | `[e if e > 2 else 10 for e in x]` | |
| Nested ternary map | `[e if e > 2 else 10 if e < 3 else 5 for e in x]` | Good luck reading this |
| Map | `[fun(e) for e in x]` | |
| Map function | `list(map(fun, x))` | Slow |
| Elements to string | `[str(e) for e in x]` | |

# Iterating
| What | How | Details |
|---|---|---|
| Iterate | <pre lang='python'>for e in x: | |
| Iterate over multiple lists | <pre lang='python'>for a, b in zip(x, y): | |

# Convert
| What | How | Details |
|---|---|---|
| Multiple assignment | <pre lang='python'>x = [1, 2]&#13;a, b = x | |
| To tuple | `tuple(x)` | |
| To set | `set(x)` | | 
| To dict (from keys and values) | `dict(zip(keys, values))` | | 
