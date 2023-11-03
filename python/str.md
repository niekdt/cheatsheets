# String

## Create
| What | How | Details |
|---|---|---|
| Empty | `''` | |
| String literal | `'hello world'` | |
| String literals (concatenate) | `'a' 'b' 'c'` | |
| Concatenate strings | `x + y` |
| From list with comma separator | `','.join(['a', 'b'])` | |
| Object to string | `str(x)` | |

## Format
| What | How | Details |
|---|---|---|
| Positional formatting | `'First {0} then {1}'.format(1 + 1, 2 * 2)` | |
| Named formatting | `'First {sum} then {mult}'.format(sum = 1 + 1, mult = 2 * 2)` | |
| Named element formatting | `'a0 = {a[0]}'.format(a=[1,2])` | |
| Named attribute formatting | `'Instance is of type: {p.type}'.format(p=Prop)` | |
| Dynamic formatting based on dict | `'Value of a and b is {a} and {b}'.format_map(dict(a=1, b=2))` | |
| Whole number | `'a = {:d}'.format(3)` | |
| Whole number with thousands separator | `'a = {:,d}'.format(1000)` | Outputs `'1 000'` |
| Named formatting of whole number | `'a = '{num:,}'.format(num = int_var)` | |
| Padded whole number | `'a = {:3d}'.format(3)` | Outputs `'  3'` |
| Zero-padded whole number | `'a = {:03d}'.format(3)` | Outputs `'003'` |
| Float | `'a = {:f}'.format(3.14)` | |
| Float as whole number | `'a = {:.0f}'.format(3.14)` | Outputs `'3'` |
| Float with decimal-point padding | `'a = {:06.2f}'.format(3.1234)` | |
| Datetime with format | `'{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))` | |

## Get
| What | How | Details |
|---|---|---|
| Length | `len(x)` | |
| Find index of substring | `x.index(substr)` | Raises error if not found |
| Try find index of substring | `x.find(substr)` | |
| Try find last index of substring | `x.rfind(substr)` | |
| Count number of non-overlapping substring occurrences | `x.count(substr)` | |
| Count number of non-overlapping substring occurrences in range \[$n$, $m$] | `x.count(substr, n, m)` | |

## Tests
| What | How | Details |
|---|---|---|
| String | `isinstance(x, str)` | |
| Empty | `if not x:` | |
| Not empty | `if x:` | |
| Equal | `x == y` | |
| Contains substring | `substr in x` | |
| Does not contain substring | `substr not in x` | |
| Starts with | `x.startswith(prefix)` | |
| Ends with | `x.endswith(suffix)` | |
| Letters only | `x.isalpha()` | |
| Digits only | `x.isdigit()` | |
| Alphanumeric characters only | `x.isalnum()` | |
| Matches regex pattern | `bool(re.search('\\w', 'abc'))` | |
| Contains $n$ regex substrings | `len(re.findall('\\w', 'a. a')) == n` | |

## Substring
| What | How | Details |
|---|---|---|
| First character | `x[0]` | |
| Character $i$ | `x[i]` | Index beyond length will raise error |
| Last character | `x[-1]` | |
| Substring (slice) | `x[2:3]` | |
| First $n$ characters | `x[:n]` | |
| Last $n$ characters | `x[-n:]` | |
| Strip leading whitespace | `x.strip()` | | 
| Strip leading characters | `x.strip('abc')` | |
| Substring up to first occurrence of _y_ | `x.split(y)[0]` | _y_ is excluded | 
| Substring up to first line break | `x.split('\n')[0]` | Line break is excluded | 
| Remove prefix | `x.removeprefix(y)` | |
| Remove suffix | `x.removesuffix(y)` | |
| Remove substring |  | |
| Remove regex group pattern | ? | |

## Transform
| What | How | Details |
|---|---|---|
| Lower case | `x.lower()` | |
| Upper case | `x.upper()` | |
| Capitalize | `x.capitalize()` | |
| Map from dict | `{'yes': 'ja', 'no': 'nee'}[x]` |
| Reverse | `x[::-1]` | |

## Grow
| What | How | Details |
|---|---|---|
| Left-pad to length $n$ | `x.ljust(n)` | |
| Right-pad to length $n$ | `x.rjust(n)` | |
| Left-right padding to length $n$ | `x.center(n)` | |
| Replicate $n$ times | `x * n` | |
| Concatenate | `x + y` | |
| Join with iterable | `x.join(iter)` | |

## Split
| What | How | Details |
|---|---|---|
| Split string into two parts by separator (as triplet) | `x.partition(sep)` | |
| Split string into multiple parts by comma (as list) | `x.split(sep=',')` | |
| Split string into lines (as list) | `x.splitlines()` | |

## Convert
| What | How | Details |
|---|---|---|
| Session hash | `hash(x)` | |
| To bytes | `x.encode()` | |
| To integer | `int(x)` | |
| To float | `float(x)` | |
| To date (unknown format) | `pandas.to_datetime('2023 Jan 5')` | Find better way |
| To date from known format | `datetime.strptime('2023-12-31', '%Y-%m-%d')` | |
