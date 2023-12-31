---
layout: default
title: Iterator
parent: Python
nav_order: 2.2
---

# Iterators
{:.no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| Create counter | `itertools.count()` | |
| Create counter starting from _n_ | `itertools.count(n)` | |
| Create counter starting from _n_ with step size _s_ | `itertools.count(n, s)` | |
| Create limited counter from _n_ to _m_ | ? | |
| Repeat constant _n_ times | `itertools.repeat(123, n)` | |
| 2D coordinates grid from (0, 0) to (_n - 1_, _m - 1_ ) | `itertools.product(range(n), range(m))` | |
| From string (over chars) | `iter(str)` | |
| From list | `iter(lst)` | |
| Index-element pairs from list | `enumerate(lst)` | |
| Key-value pairs from dict | `enumerate(dct)` | |
| Recycle through list | `itertools.cycle(lst)` | |
| Recycle through list _n_ times | `itertools.product(lst, n)` | |
| Concatenate lists | `itertools.chain(lst1, lst2)` | | 
| Create _n_ copies of iterable | `itertools.tee(x, 2)`<br>or<br>`x1, x2 = itertools.tee(x)` | |

## Using iterators
Note that each operation consumes element(s) of the iterator!

| What | How | Details |
|---|---|---|
| Iterate over iterator elements | `for i in iter:`<br>`print(i)` | |
| Consume fully | `collections.deque(x, maxlen=0)` | |
| Get next element | `next(iter)` | |
| Get next element with default if depleted | `next(iter, 0)` |
| Get _n_ th element | `next(itertools.islice(x, n, None), default)` | |
| Get first element according to criterion | `next(e for e in x if e == 1)`<br>or<br>`next(filter(lambda e: e == 1, x))` | | 
| Get last element according to criterion | ? | |
| Get index of first true element | ? | |
| Get index of first false element | ? | |
| Get index of last true element | ? | |
| Get index of last false element | ? | |
| Get remaining length | `sum(1 for _ in iter)` | |

## Map

| What | How |
|---|---|
| Map elements | `x + 1 for x in iter` |
| Map elements with function | `map(fun, iter)` |
| Invert boolean iterator | `map(lambda x: not x, bool_iter)`<br>or<br>`map(operator.not_, bool_iter)` |
| Cumulative sum | `itertools.accumulate(iter)` |
| Accumulate function (reduce() with keeping all results) | `itertools.accumulate(iter, fun)` |
| Combine iterable elements as tuple, stop on shortest iterable | `zip(x, y, ...)` |
| Combine iterable elements as tuple, expect equal length | `zip(x, y, ..., strict=True)` <details>Throws error if an iterable is depleted prematurely</details> |
| Combine iterable elements as tuple until all iterables are exhausted, with default value for depleted iterables | `itertools.zip_longest(x, y, ..., fillvalue = None)` |

## Shrink

| What | How | Details |
|---|---|---|
| First _n_ items of iterable | `itertools.islice(x, n)` | |
| Last _n_ items of iterable | `iter(collections.deque(x, maxlen = n))` | |
| Drop first _n_ items of iterable | `itertools.islice(x, start=n)` | |
| Slice based on (index) integer iterable | ? | |
| Filter based on boolean function | `filter(bool_fun, iterable)` | |
| Filter based on boolean iterable | `itertools.compress(x, mask_iter)` | |
| Filter iterables based on boolean function | `filter(lambda x: x[0] != x[1], zip(iter1, iter2))` | |
| Inverse filter iterable based on a boolean iterable | `itertools.filterfalse(mask, x)` | |
| Take while predicate is true | `itertools.takewhile(lambda x: x < 5, x)` | |
| Drop while predicate is true | `itertools.dropwhile(lambda x: x < 5, x)` | |

## Grow

| What | How | Details |
|---|---|---|
| Append iterable | `itertools.chain(iter, append_iter)` | |
| Prepend iterable | `itertools.chain(prepend_iter, iter)` | |
| Create combinations of pairs | `itertools.combinations(x, 2)` | |
| Create combinations of size _n_ | `itertools.combinations(x, n)` | |
| Create combinations of pairs with replacement (so including pairs of (A, A)) | `itertools.combinations_with_replacement(x, 2)` | |
| Create combinations of size n with replacement | `itertools.combinations_with_replacement(x, n)` | |
| Create permutations | `itertools.permutations(x)` | |
| Cartesian product of two or more iterables | `itertools.product(x, y, ...)` | |
| Repeat iterable indefinitely | `itertools.cycle(x)` | |
| Repeat iterable _n_ times | `itertools.repeat(x, n)` | |
| Repeat each element of iterable _n_ times | `itertools.chain.from_iterable(itertools.repeat(tuple(x), n))` | |
| Chain iterables | `itertools.chain.from_iterable(x, y, ...)` | |

## Aggregate

| What | How | Details |
|---|---|---|
| Min | `min(iter)` | |
| Max | `max(iter)` | |
| Sum | `sum(iter)` | |
| Hash | `hash(iter)` | |
| Reduce | `reduce(binary_fun, iter)` | |
| Group by | `for key, group in itertools.groupby(robots, key=lambda x: x['faction']):`<br>`print(key)`<br>`print(list(group))` | |

## Test

| What | How | Details |
|---|---|---|
| All elements are true | `all(bool_iter)` | |
| All elements are false | `not any(bool_iter)` | |
| All elements are equal | `g = groupby(x)`<br>`return next(g, True) and not next(g, False)` | |
| All elements are true conditional on function | `all(map(boolFun, iter))` | |
| Any element is true | `any(bool_iter)` | |
| Any element is false | `not all(bool_iter)` | |

## Convert

| What | How | Details |
|---|---|---|
| List | `list(iter)` | |
| Tuple | `tuple(iter)` | |
| Dict | `dict(zip(key_iter, value_iter))` | |
