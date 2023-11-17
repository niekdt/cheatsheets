---
layout: default
title: File system
parent: Python
has_children: true
nav_order: 10
---

# File system operations
{: .no_toc}

1. TOC
{:toc}


## Test

| What | How | Details |
|---|---|---|
| File/dir exists | `os.path.exists(path)` | |
| File | `os.path.isfile(path)` | |
| Empty file | `os.path.getsize(path) == 0` | Throws error if the file does not exist |
| Directory | `os.path.isdir(path)` | |
| Empty directory | `not os.listdir(path)` | |
| Parent of | ? | |
| Child of | ? | |


## File info

| What | How | Details |
|---|---|---|
| Filename | `os.path.basename(r'C:\Files\derp.csv')` | Returns `derp.csv` |
| Filename without extension | `os.path.splitext(os.path.basename(r'C:\Files\derp.csv'))[0]` | Returns `derp` |
| File extension | `os.path.splitext(r'C:\Files\derp.csv')[1]` | Returns `.csv` |
| Parent directory name | `os.path.basename(os.path.dirname((r'C:\Files\derp.csv'))` | Returns `Files` |
| File size | `os.path.getsize(path)` | |

## Directory info

## File manipulation

## Directory manipulation

| What | How | Details |
|---|---|---|
| Create directory | `os.mkdir(path)` | Error when directory already exists |
| Create directory if needed | `Path(path).mkdir(exist_ok=True)` | |
| Create directories recursively | `os.makedirs(dest_dir)` | |
| Create directories recursively if needed | `os.makedirs(dest_dir, exist_ok=True)` | |
| Delete directory and underlying files | `shutil.rmtree(path)` | Error if the path does not exist |
| Delete directory and underlying files if needed | `shutil.rmtree(path, ignore_error = True)` | |
