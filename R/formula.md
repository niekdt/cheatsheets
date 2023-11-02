# Creation
| What | How | Details |
|---|---|---|
| With intercept and single variable | `y ~ x` | |
| Without intercept, and single variable | `y ~ -1 + x` | |
| With all variables | `y ~ .` | |
| From string | `as.formula(str)` | |
| From string | `eval(parse(text='y ~ x'))` | Not recommended | 

# Tests
| What | How | Details |
|---|---|---|
| Is formula | `is(f, 'formula')` | |
| Formulas are equal | `f1 == f2` | |
| Formulas are equal | `isTRUE(all.equal(f1, f2))` | |

# Extract
| What | How | Details |
|---|---|---|
| Get variable names | `all.vars(f)` | |
| Get left-hand side variable names | `all.vars(update(y ~ x,  ~ 1))` | |
| Get right-hand side variable names | `all.vars(update(y ~ x,  1 ~ .))` | |
| Get the environment of the formula | `environment(f)` | |

# Update
| What | How | Details |
|---|---|---|
| Change terms | `update(y~x, ~ w + z)` | |
| Append terms | `update(y~x, ~ . + w)` | |
| Change response | `update(y~x, z ~ .)` | |
| Drop response | `formula(delete.response(terms(y ~ x)))` | |
| Remove the environment | `environment(f) = NULL` | |

# Evaluate
| What | How | Details |
|---|---|---|
| Evaluate a formula with known coefficients | `mm = model.matrix( ~ a + poly(b, 2, raw=TRUE), data.frame(a=1, b=2:4))`<br>`pred = coef %*% t(mm)` | |

# Convert
| What | How | Details |
|---|---|---|
| String | `deparse(f)` | |
| String array | `as.character(y~x)` | |