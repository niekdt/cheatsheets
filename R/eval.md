# Environment
| What | How | Details |
|---|---|---|
| Create new environment | `environment()` | |
| Check if variable exists | `exists('var')` | |
| Check if variable exists in env | `exists('var', envir=env)` | |
| Get value of variable | `get('var', envir=env)` | |
| Try get value, with default return | `get0('var', envir=env, ifnotfound='default value')` | |
| Get current environment | `sys.frame()` | |
| Get parent environment | `parent.frame()` | |
| Get package environment | `getNamespace('package')` | |
| Find environment of variable | `pryr::where('var')` | |

# Dynamic evaluation
| What | How | Details |
|---|---|---|
| Create call | `call = quote(A = 1)` | |
| Create expression | `expr = expression(A = 1)` | |
| Create expression from string | `expr = parse(text='A = 1')` | |
| Evaluate call | `eval(call)` | |
| Evaluate expression | `eval(expr)` | |
| Evaluate expression with undefined terms | `a = 1`<br>`q = quote(a + b)`<br>`eval(q, list(b=3))` | |
| Force evaluation of variable | `force(arg)` | |
| Call function with some arguments forced | `forceAndCall(f)` | |
| Fill in variable values in expression | `substitute(expr, env)` | Useful when expression is called in another function |
| Get variable name | `deparse(substitute(expr))` | |
| Get expression as string | `deparse(expr, width.cutoff=500)` | |
| Substitute a call | `do.call(substitute, list(CALL, env=ENV))` | where CALL is stored in a variable |
| Evaluate an expression of a variable upon request | `delayedAssign('x', 2 + 2)` | |

# Chained evaluation
| What | How | Details |
|---|---|---|
| Chain function calls | `y = x %>% table %>% prop.table` | |
| Chain function calls, using the former input as a later argument | `z = data.table(…) %>% .[, mean(x)]` | call must be placed in brackets for embedded function calls |
| Call consecutive function  but return the former value | `y = x %>% table %T>% print` | |
| Call functions and update the LHS | `x %<>% sort %>% abs` | |
