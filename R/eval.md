---
layout: default
title: Evaluation
parent: R
nav_order: 0.2
---

# Evaluation
{: .no_toc}

1. TOC
{:toc}

## Variables

| What | How | Details |
|---|---|---|
| Generate valid variable names from string(s) | `make.names('a@b')` | |
| Generate unique variable names from string(s) | `make.unique(rep('a', 2))` | |
| Check if variable exists | `exists('var')` | |
| Get variable name from expression | `deparse(substitute(expr))` | |
| Fill in variable values in expression | `substitute(expr, env)` | Useful when expression is called in another function |
| Force evaluation of variable | `force(arg)` | |

## Environment

| What | How | Details |
|---|---|---|
| Create new environment | `environment()` | |
| Check if variable exists in environment | `exists('var', envir=env)` | |
| Get current environment | `sys.frame()` | |
| Get parent environment | `parent.frame()` | |
| Get package environment | `getNamespace('package')` | |
| Find environment of variable | `pryr::where('var')` | |
| Get value of variable in environment | `get('var', envir=env)` | |
| Try get value of variable, with default return | `get0('var', envir=env, ifnotfound='default value')` | |

## Dynamic evaluation

| What | How | Details |
|---|---|---|
| Create call | `call = quote(A = 1)` | |
| Create expression | `expr = expression(A = 1)` | |
| Create expression from string | `expr = parse(text='A = 1')` | |
| Evaluate call | `eval(call)` | |
| Evaluate expression | `eval(expr)` | |
| Evaluate expression with undefined terms | `a = 1`<br>`q = quote(a + b)`<br>`eval(q, list(b=3))` | |
| Force evaluation of variable | `force(arg)` | |
| Lazy-evaluate a variable assignment through expression | `delayedAssign('x', 2 + 2)` | |
| Call inline function | `{function(x) x + 1}(5)` | |
| Call function with some arguments forced | `forceAndCall(f)` | |
| Call function with arguments in list | `do.call(fun, list(5))` | |
| Call function with arguments in list, ignoring unused | `R.utils::doCall(fun, n=100, args=env)` | |
| Substitute a call | `do.call(substitute, list(CALL, env=ENV))` | where CALL is stored in a variable |
| Get expression as string | `deparse(expr, width.cutoff=500)` | |

## Chained evaluation

| What | How | Details |
|---|---|---|
| Chain function calls | `y = x %>% table %>% prop.table` | |
| Chain function calls, using the former input as a later argument | `z = data.table(…) %>% .[, mean(x)]` | call must be placed in brackets for embedded function calls |
| Call consecutive function  but return the former value | `y = x %>% table %T>% print` | |
| Call functions and update the LHS | `x %<>% sort %>% abs` | |

## Functions

| What | How | Details |
|---|---|---|
| Get all arguments, including defaults | `mget(names(formals()),sys.frame(sys.nframe()))` | |
| Get all specified arguments, including ellipsis | `as.list(match.call()[-1])` | |
| Pass all specified arguments to a nested function | `match.call() %>% eval()` | |
| Pass all specified arguments to a nested function | `call = match.call()`<br>`call$extra = 'test'`<br>`eval(call)` | |
| Pass all specified arguments to another function | `call = match.call()`<br>`call[[1] ] = as.symbol('newFunction')`<br>`eval(call)` | |
| Get name of the parent calling function | `parentCall = sys.calls()[[sys.nframe()-2]]`<br>`as.character(parentCall[[1]])` | |


