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
| Current working directory | `os.getcwd()` | Can be set using `os.chdir()` |
| From directory for given file name | `os.path.join(dir_path, filename)` | | 
| Temporary file path | `tempfile.mktemp()` | |
| Temporary file path in directory | `tempfile.mktemp(dir=dir_path)` | |
| Temporary file path with extension (suffix) | `tempfile.mktemp('.txt')` | |
| Open temporary file with clean-up | `with tempfile.NamedTemporaryFile() as file:`<br>`    path = file.name` | |
| Temporary directory path | `tempfile.mkdtemp()` | |
| Temporary directory path in directory | `tempfile.mkdtemp(dir=dir_path)` | |
| Directory path obtained interactively from user via dialog | `import tkinter`<br>`from tkinter import filedialog`<br>`tkinter.Tk().withdraw()`<br>`path = tkinter.filedialog.askdirectory()` | `withdraw()` is needed to prevent an annoying empty window from opening |
| File path obtained interactively from user via dialog | `import tkinter`<br>`from tkinter import filedialog`<br>`tkinter.Tk().withdraw()`<br>`path = tkinter.filedialog.askopenfile()` | `withdraw()` is needed to prevent an annoying empty window from opening |

## Generate paths from directory
All snippets return a list of string paths.

| What | How | Details |
|---|---|---|
| File names | `os.listdir(dir_path)` | |
| File names that match Unix filter | `fnmatch.filter(os.listdir(dir_path), '*.csv')` | |
| File names that match regex pattern | `[f for f in os.listdir(dir_path) if re.match('\.csv$', f)]` | |
| File paths | `[os.path.join(dir_path, f) for f in os.listdir(dir_path)]` | |
| File paths that match Unix filter | `glob.glob(os.path.join(path, '*.csv'))` | |
| File paths that match regex pattern | `[os.path.join(dir_path, f) for f in os.listdir(dir_path) if re.match(r'.+\.csv$', f)]` | |
| File paths that match Unix filter, including nested entries (recursive) | `glob.glob(os.path.join(path, '**\*.csv'), recursive = True)` | The `**\` is required for recursive search to do anything. |

## Test

| What | How | Details |
|---|---|---|
| File/dir exists | `os.path.exists(path)` | |
| File | `os.path.isfile(path)` | |
| Empty file | `os.path.getsize(path) == 0` | Throws error if the file does not exist |
| Directory | `os.path.isdir(path)` | |
| Empty directory | `not os.listdir(path)` | |
| Absolute path | `os.path.isabs(path)` | |
| Paths refer to same file | `os.path.samefile(path1, path2)` | |
| Parent of | ? | |
| Child of | ? | |

## Path manipulation

| What | How | Details |
|---|---|---|
| Normalize path | `os.path.normpath(path)` | |
| Absolute path | `os.path.abspath(path)` | Paths are relative to the working directory |
| Canonical path (resolving symlinks) | `os.path.realpath(path)` | |
| Parent path | `os.path.dirname(r'C:\Files\derp.csv')` | Returns `C:\Files` | | 
| Relative path to directory | `os.path.relpath(path, start=dir_path)` | |
| Get common parent path between two or more paths | `os.path.commonpath(paths)` | |
| Extend path with subdirectories | `os.path.join(path, ..., dirN, file)` | |
| File path without extension | `os.path.splitext(path)[0]` | |
| Split path into parent path and basename | `parent_path, base_name = os.path.split(path)` | |
| Split path into file path and extension | `file_path, ext = os.path.splitext(path)` | |


## Directory manipulation

To be moved to filesystem cheatsheet when created.

| What | How | Details |
|---|---|---|
| Create directory | `os.mkdir(path)` | Error when directory already exists |
| Create directory if needed | `Path(path).mkdir(exist_ok=True)` | |
| Create directories recursively | `os.makedirs(dest_dir)` | |
| Create directories recursively if needed | `os.makedirs(dest_dir, exist_ok=True)` | |


## File info

| What | How | Details |
|---|---|---|
| Filename | `os.path.basename(r'C:\Files\derp.csv')` | Returns `derp.csv` |
| Filename without extension | `os.path.splitext(os.path.basename(r'C:\Files\derp.csv'))[0]` | Returns `derp` |
| File extension | `os.path.splitext(r'C:\Files\derp.csv')[1]` | Returns `.csv` |
| Parent directory name | `os.path.basename(os.path.dirname((r'C:\Files\derp.csv'))` | Returns `Files` |
| File size | `os.path.getsize(path)` | |
