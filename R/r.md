---
layout: default
title: R
has_children: true
---

# R
{: .no_toc}

1. TOC
{:toc}

## Options

| What | How | Details |
|---|---|---|
| Debug (browse) on error | `options(error=recover)` | |
| Treat warnings as errors | `options(warn=2)` | |
| Readable traceback | `options(error=function() traceback(max.lines=3))` | |
| Disable scientific notation | `options(scipen=999)` | |

## Sourcing

| What | How | Details |
|---|---|---|
| Run R script (source) | `source('file.R')` | |
| Get sourced file from within script | `as.character(sys.call(1))[2]` | Does not work during start-up! |
| Get sourced directory from within script | `dirname(as.character(sys.call(1))[2])` | |

## Output

| What | How | Details |
|---|---|---|
| Output | `cat('hello')` | |
| Output object | `cat(x)` | |
| Generic print | `print('hello')` | |
| Show message | `message('msg')` | |
| Show warning | `warning('warning')` | |
| Show warning right now | `warning('warning', .immediate=TRUE)` | |
| Trigger and show error | `stop('error')` | |
| Redirect output to file | `sink('log.txt')` | Use `sink()` to restore |
| Capture any output as string | `txt = capture.output({...})` | |
| Suppress automatic printing in interactive mode | `invisible(x)` | |
| Suppress all output | `capture.output({...})` | |
| Suppress all output | `sink('nul:')` | `'/dev/null'` on linux? |
| Suppress messages |  `suppressMessages({...})` | |
| Suppress package messages on load | `suppressPackageStartupMessages({...})` | |
| Suppress warnings | `suppressWarnings({...})` | |

## Version check

| What | How | Details |
|---|---|---|
| Run code conditional on R version | <pre lang='R'>if (compareVersion(paste(version$major, version$minor, sep='.'), '3.6.0') >= 0) {&#13;&#09;RNGkind(sample.kind='Rounding') # fix to reproduce RNG of R 3.5.0&#13;}</pre> | |
