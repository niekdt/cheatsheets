---
layout: default
title: File system path
parent: Python
nav_order: 10
---

# File system paths
{: .no_toc}

1. TOC
{:toc}

## Generate path

| What | How | Details |
|---|---|---|
| From directory for given file name | `os.path.join(dir_path, filename)` | | 
| Temporary file path | `tempfile.mktemp()` | |
| Temporary file path in directory | `tempfile.mktemp(dir=dir_path)` | |
| Temporary file path with extension (suffix) | `tempfile.mktemp('.txt')` | |
| Open temporary file with clean-up | `with tempfile.NamedTemporaryFile() as file:`<br>`    path = file.name` | |
| Temporary directory path | `tempfile.mkdtemp()` | |
| Temporary directory path in directory | `tempfile.mkdtemp(dir=dir_path)` | |

## Generate paths from directory
All snippets return a list of string paths.

| What | How | Details |
|---|---|---|
| File names | `os.listdir(dir_path)` | |
| File names that match Unix filter | `fnmatch.filter(os.listdir(dir_path), '*.csv')` | |
| File names that match regex pattern | `[f for f in os.listdir(dir_path) if re.match('\.csv$', f)]` | |
| File paths | `[os.path.join(dir_path, f) for f in os.listdir(dir_path)]` | |
| File paths that match regex pattern | `[os.path.join(dir_path, f) for f in os.listdir(dir_path) if re.match(r'.+\.csv$', f)]` | |

## Test

| What | How | Details |
|---|---|---|
| File/dir exists | `os.path.exists(path)` | |
| File | `os.path.isfile(path)` | |
| Directory | `os.path.isdir(path)` | |
| Absolute path | `os.path.isabs(path)` | |
| Paths refer to same file | `os.path.samefile(path1, path2)` | |

## Path manipulation

| What | How | Details |
|---|---|---|
| Normalize path | `os.path.normpath(path)` | |
| Absolute path | `os.path.abspath(path)` | |
| Canonical path (resolving symlinks) | `os.path.realpath(path)` | |
| Relative path to directory | `os.path.relpath(path, start=dir_path)` | |
| Get common parent path between two or more paths | `os.path.commonpath(paths)` | |
| Extend path with subdirectories | `os.path.join(path, ..., dirN, file)` | |
| File path without extension | `os.path.splitext(path)[0]` | |
| Split path into parent path and basename | `parent_path, base_name = os.path.split(path)` | |
| Split path into file path and extension | `file_path, ext = os.path.splitext(path)` | |

## File info

| What | How | Details |
|---|---|---|
| Filename | `os.path.basename(r'C:\Files\derp.csv')` | Returns `derp.csv` |
| Filename without extension | `os.path.splitext(os.path.basename(r'C:\Files\derp.csv'))[0]` | Returns `derp` |
| File extension | `os.path.splitext(r'C:\Files\derp.csv')[1]` | Returns `.csv` |
| Parent directory name | `os.path.dirname(r'C:\Files\derp.csv')` | Returns `Files` |
| File size | `os.path.getsize(path)` | |
