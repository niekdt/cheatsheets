**Contents**
* [Create](#creation)
* [Query](#query)
* [Test](#tests)
* [Update](#update)
* [Resize](#resize)
* [Derive](#derive)
* [Iterate](#iterate)
* [Convert](#convert)

# Uses
* Lists can be efficiently used as a stack through `append()` (for push) and `pop()`.

# Creation
| What | How | Details |
|---|---|---|
| Empty | `x = []` | |
| Define | `x = [1, 3, 9]` | |
| Define with $n$ repeated values $v$ | `x = [v] * n` | |
| Sample $n$ random numbers between [ $a$, $b$ ) with replacement | `random.choices(range(a, b), k=n)` | About 6 times faster than list comprehension |
| Sample $n$ random numbers between [ $a$, $b$ ) w/o replacement | `random.sample(range(a, b), n)` | |
| From tuple | `t = (1, 3, 9)`<br>`x = [t]` | Faster than `list(t)` |
| From iterator (consumes) | `x = list(iter)` | |
| Lists from zipped list | <pre lang='python'>a = (1, 2); b = (-1, -2)&#13;ab = zip(a, b)&#13;a2, b2 = zip(*ab) | |

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
| All elements True | `all(x)` | |
| Any element True | `any(x)` | |
| Are elements sorted | `x == sorted(x)` | |
| No duplicate elements | `len(x) == len(set(x))` | |
| Has duplicate elements | `len(x) != len(set(x))` | |

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

# Aggregate
| What | How | Details |
|---|---|---|
| Min | `min(x)` | | 
| Max | `max(x)` | |
| Sum | `sum(x)` | |
| Mean | `sum(x) / len(x)` | Faster than `fmean` and `mean` from `statistics` | 
| Most frequent element | `statistics.mode(x)` | |

# Update
All operations are in-place.
| What | How | Details |
|---|---|---|
| Update index $i$ | `x[i] = new_value` | |
| Update slice with list | `x[2:3] = [5, 6]` | |
| Reverse elements | `x.reverse()` | |
| Sort elements | `x.sort()` | |
| Sort on transformed elements | `x.sort(key=str.lower)` | |
| Reverse-sort elements | `x.sort(reverse=True)` | |
| Shuffle elements | `random.shuffle(x)` | |

# Resize
All operations are in-place.
| What | How | Details |
|---|---|---|
| Clear | `x.clear()` | |
| Clear by slicing | `x[:] = []` | Probably slower |
| Concatenate | `x + [1, 2]` | |
| Append/push element | `x.append(e)` | |
| Append/push elements | `x += [e1, e2]` | |
| Append/push elements | `x.extend([e1, e2])` | |
| Insert at index $i$ | `x.insert(i, e)` | |
| Remove at index $i$ | `del x[i]` | |
| Remove at index $i$ | `x[i] = []` | |
| Remove last index and return the element | `x.pop()` | |
| Remove at index $i$ and return the element | `x.pop(e, i)` |
| Remove slice | `del x[2:3]` | |
| Remove slice | `x[2:3] = []` | |
| Remove element (first occurrence) | `x.remove(e)` | |
| Remove all elements with value | ? | |
| Remove and get last element | `x.pop()` | |

# Derive
Shallow copies preserve references to the original object.
| What | How | Details |
|---|---|---|
| Shallow copy | `[*x]` | Fastest for small lists |
| Shallow copy | `x[:]` | Probably very slow |
| Shallow copy | `x.copy()` | Fastest for large lists |
| Shallow copy | `copy.copy(x)` | Not sure what the difference to `.copy()` is |
| Deep copy | `copy.deepcopy(x)` | Constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original. |
| Reversed order | `reversed(x)` | |
| Sorted | `sorted(x)` | Elements must be sortable |
| Reverse-sorted | `sorted(x, reverse=True)` | Elements must be sortable |
| Sorted by reference order | `[x for _, x in sorted(zip(ref_order, x))]` | Elements must be sortable |
| Map | `[e + 1 for e in x]` | |
| Map function | `[fun(e) for e in x]` | |
| Map function | `list(map(fun, x))` | Slow |
| Conditional update | `[e if e != 0 else -1 for e in x]` | |
| Ternary map | `[e if e > 2 else 10 for e in x]` | |
| Nested ternary map | `[e if e > 2 else 10 if e < 3 else 5 for e in x]` | Good luck reading this |
| Filter on condition | `[e for e in x if e > 0]` | |
| Filter on predicate function | `filter(fun, x)` | |
| Elements to string | `[str(e) for e in x]` | |
| Replicate $n$ times | `x * n` | |

# Iterate
| What | How | Details |
|---|---|---|
| Iterate | <pre lang='python'>for e in x: | |
| Iterate with index | <pre lang='python'>for i, e in enumerate(x): | |
| Iterate with index starting from $s$ | <pre lang='python'>for i, e in enumerate(x, s): | |
| Iterate over multiple lists | <pre lang='python'>for a, b in zip(x, y): | |
| Iterate over multiple lists with index | <pre lang='python'>for i, (a, b) in enumerate(zip(x, y)): | |
| Iterate over a list of lists for each nested element | <pre lang='python'>itertools.chain.from_iterable(x) | |

# Convert
| What | How | Details |
|---|---|---|
| Multiple assignment | <pre lang='python'>x = [1, 2]&#13;a, b = x | |
| Hash | `hash(tuple(x))` | |
| To tuple | `tuple(x)` | |
| To set | `set(x)` | | 
| To dict (from keys and values) | `dict(zip(keys, values))` | | 
| Flatten a list of lists | `list(itertools.chain.from_iterable(x))` | |
