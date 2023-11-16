---
layout: default
title: Numeric
parent: Python
nav_order: 0
---

# Numeric
{: .no_toc}

1. TOC
{:toc}

## Constants

| What | How | Details |
|---|---|---|
| NaN | `math.nan` | |
| NaN | `float('nan')` | |
| NaN | `numpy.nan` | |
| Infinity | `math.inf` | |
| Infinity | `float('inf')` | |
| Infinity | `numpy.inf` | |
| Negative infinity | `-math.inf` | |
| Negative infinity | `float('-inf')` | |
| Negative infinity | `numpy.NINF` | |
| Pi | `math.pi` | |
| e | `math.e` | |
| Min int | `-sys.maxsize` | |
| Max int | `sys.maxsize` | |
| Float epsilon (smallest representable difference) | `sys.float_info.epsilon` | |
| Min float | `sys.float_info.min` | |
| Max float | `sys.float_info.max` | |


## Create
`int()` and `float()` throw `ValueError` if the input cannot be parsed.

| What | How | Details |
|---|---|---|
| Binary integer | `[sign]0b[b2int]` | e.g., `-0b10` (-2) |
| Hex integer | `[sign]0x[b16int]` | e.g., `-0xF` (-16) |
| Integer from string | `int(x)` | |
| Integer from hex string (base 16) | `int(x, 16)` | `e.g., DEADBEEF` |
| Integer from string with base determined by prefix | `int(x, 0)` | Base 10 by default, base-16 for `0x`, base-2 for `0b` |
| Integer from string according to locale | `locale.atoi(x)` | |
| Unsigned integer from bytes | `int.from_bytes(x, byteorder='big')` | |
| Signed integer from bytes | `int.from_bytes(x, byteorder='big', signed=True)` | |
| Float from string | `float(x)` | Throws `ValueError` if string cannot be parsed |
| Float from packed `struct` bytes | `struct.unpack('f', x)[0]` | e.g., `b'\x00\x00 @'`|
| Float from hex string representation | `float.fromhex(x)` | |
| Float from string for locale | `locale.atof(x)`
| Float from string for temporary locale | `Babel.parse_decimal('1,25', locale='nl_NL.utf8')` | No way to do this cleanly and thread-safe in standard Python... |
| Float from string for temporary locale | `loc = locale.getlocale(locale.LC_NUMERIC)`<br>`locale.setlocale(locale.LC_NUMERIC, 'nl_NL')`<br>`f = locale.atof(x)`<br>`locale.setlocale(locale.LC_NUMERIC, loc)` | |


## Extract

| What | How | Details |
|---|---|---|
| Number of bits needed to represent the integer (ignoring sign) | `x.bit_length()` | Same as `floor(log2(|x|))` |

## Test

| What | How | Details |
|---|---|---|
| Integer | | |
| Whole number | `float.is_integer(x)` | e.g., `TRUE` for `5.0` |
| Approximately equal | `math.isclose(x, y)` | Uses proportional tolerance |
| Approximately equal with absolute tolerance _tol_ | `math.isclose(x, y, abs_tol=tol)` | |
| Approximately equal with proportional tolerance _tol_% | `math.isclose(x, y, rel_tol=tol)` | |
| NaN | `math.isnan(x)` | Does not work for complex numbers |
| Finite | `math.isfinite(x)` | |
| Infinite | `math.isinf(x)` | |
| Positive infinity | `math.isinf(x) and x > 0` | |
| Negative infinity | `math.isinf(x) and x < 0` | |

## Convert

| What | How | Details |
|---|---|---|
| String | `str(x)` | |
| Float to string according to locale | `locale.str(float)` | |
| Hash | `hash(x)` | |
| Count to bytes | `x.to_bytes(8, byteorder='big')` | `OverflowError` is raised if the integer is not representable with the given number of bytes |
| Count to byte array (mutable) | `bytearray(x) ` | |
| Integer to bytes | `x.to_bytes(8, byteorder='big', signed=True)` | |
| Float to bytes | `struct.pack('f', x)` | |
| Int to hex string | `hex(x)` | Format: `[sign] ['0x'] integer` |
| Float to hex string representation | `x.hex()` | Format: `[sign] ['0x'] integer ['.' fraction] ['p' exponent]`, e.g., `0x1.400000p+1` |
