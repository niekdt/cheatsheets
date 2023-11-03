---
layout: default
title: Dictionary
parent: Python
---

# Dict
{: .no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Create

| What | How | Details |
|:-------------|:------------------|:------|
| Empty | `x = {}` | |
| Define with string keys | `x = {'color': 'blue', 'size': 'large'}` | |
| Define from keys (iterator) and constant value $v$ | `dict.fromkeys(key_iter, v)` | |
| Define dynamically from iterators for keys and values | `x = dict(zip(key_iter, value_iter))` | |
| Merge dictionaries | `z = x \| y` | |
| Merge dictionaries | `z = {**x, **y}` | ? |

## Get
| What | How | Details |
|---|---|---|
| Value | `x['color']` | Throws an error if missing |
| Try get value | `x.get('color')` | Returns `None` if missing |
| Try get value with default $v$ | `x.get('color', v)` | |
| Values from list of keys | `[x[k] for k in keys_list]` | | 
| Keys (as dict_keys) | `x.keys()` | |
| Keys as list | `list(x)` | |
| Keys as sorted list | `sorted(x)` | |
| Values (as dict_values) | `x.values()` | |
| Values as list | `list(x.values())` | |
| Values sorted by keys | `[x[k] for k in sorted(x)]` | |
| Entries (as list of tuples) | `x.items()` | |
| First key with value $v$ | `next(k for k in x if x[k] == v)` | |
| All keys with value $v$ | `[k for k in x if x[k] == v]` | |

## Test

| What | How | Details |
|---|---|---|
| Empty | `if x:` | |
| Not empty | `if not x:` | |
| Contains key $k$ | `k in x` | |
| Contains value $v$ | `v in x.values()` | |
| Contains duplicate values | `len(x) != len(set(x.values()))` | |

## Update

| What | How | Details |
|---|---|---|
| Set default entry value for missing key | `x.setdefault('size', 'medium')` |
| Update entry value | `x['size'] = 'small'` | |
| Update entry, error if missing | ? | |

## Grow

| What | How | Details |
|---|---|---|
| Add/update entry | `x['size'] = 'small'` | |
| Merge with another dictionary | `x \|= y` | |
| Merge with another dictionary | `x.update(y)` | |

## Shrink

| What | How | Details |
|---|---|---|
| Remove key | `del x['size']` | |
| Remove keys | `for k in keys: del x[k]` | |
| Remove key, get value | `x.pop('size')` | |
| Remove keys, get values | `[x.pop(k) for k in keys]` | | 
| Remove last item, get value | `x.popitem()` | |
| Clear | `x.clear()` | |

## Derive

| What | How | Details |
|---|---|---|
| Copy | `x.copy()` | |
| Copy | `dict(x)` | ? |
| Subset for keys | `{k: x[k] for k in keys}` | Error if a key is missing |
| Subset for keys with default $v$ | `{k: x.get(k, default=v) for k in keys}` | |
| Subset (intersection) for keys | `{k: x[k] for k in x.keys() if k in keys}` | Returns empty dict if all keys are missing |
| Subset except for keys | `{k: x[k] for k in x.keys() if k not in keys}` | |

## Convert

| What | How | Details |
|---|---|---|
| Pretty print | `pprint.pprint(x)` | |
| List of key-value tuples | `x.items()` | |
