---
layout: default
title: Command-line interface
parent: Python
nav_order: 10
---

# Command-line interface
{: .no_toc}

1. TOC
{:toc}

## Execute

| What | How | Details |
|---|---|---|
| Start Python script, wait for completion | `os.system('python script.py')` | |
| Start Python script with arguments, wait for completion | `os.system('python script.py -file "hello.csv"')` | |


## Parse arguments

Uses the [argparse](https://docs.python.org/3/library/argparse.html#) module.

| What | How | Details |
|---|---|---|
| Test if no arguments were provided | `len(sys.argv) <= 1` | |
| Number of arguments | `len(sys.argv)` | |
| Get program or script that invoked the process | `sys.argv[0]` | |

### Define argument parser

Requires a parser instance to be created first.
```python
import argparse
parser = argparse.ArgumentParser(
  prog = 'My CLI program',
  description = 'Description of functionality here',
  epilog = 'Text at the bottom of the help file'
)
```

| What | How | Details |
|---|---|---|
| Define positional argument | `parser.add_argument('file')` | |
| Define optional positional argument | `parser.add_argument('dest', nargs='?')` | |
| Define positional argument accepting multiple values | `parser.add_argument('files', type = str, nargs='+')` | |
| Define flag to enable a feature (default is `False`) | `parser.add_argument('-f', '--force', action = 'store_true')` | |
| Define flag to disable a feature (default is `True`) | `parser.add_argument('--disable', action = 'store_false')` | |
| Define string option | `parser.add_argument('-s', '--source', type = str)` | |
| Define int option | `parser.add_argument('--seed', type = int)` | |
| Define float option | `parser.add_argument('value', type = float)` | |
| Define categorical option | `parser.add_argument('answer', choices = ['a', 'b', 'c'])` | |
| Define valid path option | `parser.add_argument('path', type = pathlib.Path)` | |
| Define openable file option | `parser.add_argument('file', type = open)` | |
| Define writable file option | `parser.add_argument('dest', type = argparse.FileType('w'))` | |
| Define option that optionally takes a value | `parser.add_argument('--seed', nargs = '?')` | |
| Define option that takes a value | `parser.add_argument('--seed')` | |
| Define required option | `parser.add_argument('--seed', required = True)` | Required options are considered bad form. Preferably use positional arguments instead. |

Then parse arguments using:

```python
args = parser.parse_args()
```
