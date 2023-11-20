---
layout: default
title: data.table
parent: R
nav_order: 50
---

# data.table
{: .no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| From `data.frame` | `as.data.table(df)` | |
| From `data.frame` byref | `setDT(df)` | |
| From `data.frame`, storing row names as the first column | `as.data.table(df, keep.rownames=TRUE)` | |
| From list of named vectors | `as.data.table(do.call(rbind, veclist))` | |
| From statistical object | `broom::tidy(lm) %>% as.data.table()` | |
| From statistical object to one-row | `broom::glance(lm) %>% as.data.table()` | |
| From RLE | `rle(x) %>% unclass() %>% as.data.table()` | |
| From matrix to long format | `melt(data.table(x), measure = colnames(x), id=character())` | |
| From array to long format | `as.data.table(x)` | Ensure that all dims are named |
| From CSV | `fread('derp.csv')` | |

## Properties

| What | How | Details |
|---|---|---|
| Column names | `names(dt)` | |
| Number of columns | `length(dt)` | |
| Number of rows | `nrow(dt)` | |
| Get key(s) | `key(dt)` | |
| Set key(s) by symbols byref | `setkey(dt, Age, Sex)` | |
| Set key(s) by names byref | `setkeyv(dt, c('Age', 'Sex'))` | |
| Assign attribute byref | `setattr(dt, 'myAttr', value)` | |
| Remove attribute byref | `setattr(dt, 'myAttr', NULL)` | |
| Number of duplicated rows | `sum(duplicated(dt))` | |

## Sort
Sorting can be handled automatically by setting a column as one of the keys through `setkey()`.

| What | How | Details |
|---|---|---|
| Sort by column symbols byref | `setorder(dt, Age, Sex)` | |
| Sort by column names byref | `setorderv(dt, c('Age', 'Sex'))` | |

## Query

| What | How | Details |
|---|---|---|
| Select column | `dt$Age` | |
| Select column | `dt[, .(Age)]` | |
| Select column by variable name | `dt[[x]]` | |
| Select columns | `dt[, .(Age, Sex)]` | |
| Select all columns except | `dt[, -c('Age', 'Sex')]` | |
| Select columns and apply function | `dt[, lapply(.SD, mean), .SDcols=c('Age', 'Sex')]` | |
| Select rows by row number | `dt[1:10]` | |
| Select rows with key value | `dt[dtquery[query, .(ID)]]` | |
| Select rows with key value, dropping factor levels | `dt[c('a1', 'a2')]` | Discards factor level order! |
| Select first/last row with key values | `dt[c('a1', 'a2'), mult='first']` | |
| Select rows with value over multiple keys | `dt[.('a1', 'b1')]` | Notice the dot |
| Select rows of groups specified in table | `dtquery = data.table(..., by=keys); dt[dtquery]` | |
| Select rows of groups, excluding non-existent queried rows | `dtquery = data.table(..., by=keys); dt[dtquery, nomatch=0]` | |
| Select rows with values specified in table | `dtquery = data.table(...)`<br>`merge(dt, dtquery, by=COLUMNS)` | |
| Unique rows | `unique(dt)` | |
| Unique rows by columns | `unique(dt, by = keys(dt))` | | 
| Duplicated rows | `dt[duplicated(dt),]` | |
| Sample rows | `dt[sample(.N, 10),]` | |
| Sample by key value | `dtquery = data.table(sample(levels(dt$Id), 5)); dt[dtquery]` | |
| Find row index of key value | `dt['a1', which=TRUE]` | |
| Repeat rows | `dt[rep(1:.N, 10)]` | |

## Aggregate

### Grouped

| What | How | Details |
|---|---|---|
| By key | `dt[,, by = ID]` | |
| By string key | `dt[,, by = 'ID']` | |
| By variable key | `dt[,, by=(var)]` | |
| By keys | `dt[,, by = .(IDa, IDb)]` | |
| By string keys | `dt[,, by = c('IDa', 'IDb')]` | |
| By range of keys | `dt[,, by = IDa:IDc]` | |
| By fixed-sized bins | `dt[ , , by=findInterval(X, seq(1, 100, by=7))]` | |
| By key using its value | `dt[, {id = first(ID); dt2[id]}, by=ID]` | |
| By key using its factor value | `dt[, {id = levels(ID)[.GRP]; dt2[id]}, by=ID]` | |
| Select columns by key | `dt[, .(x, y), by=ID]` | |
| Select rows by key | `dt[dt[, .I[1:10], by=ID]]` | |

### Rolling

| What | How | Details |
|---|---|---|
| Right-aligned rolling sum of size _w_ | `dt[, RMean := Reduce('+', shift(x, 1:w-1, fill=0)) / pmin(w, .I)]` | |

### Grouped rolling

| What | How | Details |
|---|---|---|
| Right-aligned rolling sum of size _w_ | `dt[, RSum := Reduce('+', shift(x, 0:(w-1), fill=0)), by=ID]` | Easily 50 times faster than `zoo::rollapply` |
| Right-aligned rolling mean with fixed window _w_ (zero-filled) | `dt[, RMean := Reduce('+', shift(x, 0:(w-1), fill=0)) / w, by=ID]` | |
| Right-aligned rolling mean (partial windows) | `dt[, RMean := Reduce('+', shift(x, 0:(w-1), fill=0)) / pmin(w, 1:.N), by=ID]` | |
| Right-aligned rolling mean (ignoring NAs) | `dt[, RMean := Reduce('+', shift(ifelse(is.na(x), 0, x), 0:(W-1), fill=0)) / `<br>`Reduce('+', shift(is.finite(x), 0:(W-1), fill=0)), by=ID]` | |
| Centered rolling mean (fixed window of size $W$ (inserting zeroes)) | `dt[, CMean := Reduce('+', shift(x, -floor(W/2):floor(W/2), fill=0)) / W, by=ID]` | |
| Centered rolling mean (partial windows) | `dt[, CMean := Reduce('+', shift(x, -floor(W/2):floor(W/2), fill=0)) / `<br>`pmin(W, c(1:ceiling(.N/2), floor(.N/2):1)), by=ID]` | |
| Centered rolling mean (ignoring NAs) | `dt[, CMean := Reduce('+', shift(x, -floor(W/2):floor(W/2), fill=0)) / `<br>`Reduce('+', shift(is.finite(x), -floor(W/2):floor(W/2), fill=0)), by=ID]` | |
| Mark consecutive matching rows | `dt[, CMatch := {r = rle(MATCH)`<br>`r$values = replace(r$values, r$lengths < GAP_SIZE & r$values, FALSE)`<br>`inverse.rle(r)`<br>`}, by=ID]` | |
| Count column for consecutive matches | `dt[, MatchNr := {function(x) cumsum(x) + cummin(c(0, diff(x)) * cumsum(x))}(MATCH), by=ID]` | |
| Impute NA values | `dt[, X := Hmisc::impute(X, mean), by=ID]` |  |

## Row masking

## Test

## Update

| What | How | Details |
|---|---|---|
| Fill NAs by zero | `dt[is.na(dt)] = 0` | |

## Append rows

| What | How | Details |
|---|---|---|
| Insert missing rows based on missing combination of keys | `dt[CJ(unique(IDa), unique(IDb))]` | |
| Replace missing values using LOCF | `locf = function(x) x[cummax(c(TRUE, tail(is.finite(x) * seq_along(x), -1)))]`<br>`dt[, x := locf(x), by=ID]` | |
| Replace missing values using NOCB | `locf = function(x) x[cummax(c(TRUE, tail(is.finite(x) * seq_along(x), -1)))]`<br>`nocb = function(x) rev(locf(rev(x))`<br>`dt[, x := nocb(x), by=ID]` | |

## Update (byref)

| What | How | Details |
|---|---|---|
| Assign/update column byref | `dt[, x:=1]` | |
| Update columns byref | `dt[, ':='(x=1, y=2)]` | |
| Update columns dynamically byref | `dt[, c('x', 'y') := .(1, 2)]` | |
| Update columns from matrix columns byref | `mat = matrix(1:8, ncol=2)`<br>`dt[, c('a' ,'b') := split(mat, col(mat))]` | |
| Update columns from matrix rows byref | `mat = matrix(1:8, nrow=2)`<br>`dt[, c('a' ,'b') := split(mat, row(mat))]` | |
| Update columns from another table byref | `dt2 = data.table(…)`<br>`dt[dt2, (vars) := mget(vars)]` | |
| Update column per key | `dt[, x:=mean(y), by=ID]` | |
| Update subset | `dt[is.na(x), y:=1]` | |
| Update value per key | `dtg = data.table(…, x=2, key=Group)`<br>`dt[dtg, x := i.x]` | |
| Update subset per key | `GroupValue = data.table(..., key=Group)`<br>`dt[, x:=GroupValue[.BY], by=ID]` | Slow, can be done faster |
| Replace factor NA by new level | `dt[is.na(f), f := 'N/A']` | |
| Remove column | `dt[, x := NULL]` | |
| Remove columns | `dt[, ':='(x=NULL, y=NULL)]` | |
| Remove columns dynamically | `dt[, c('x', 'y') := NULL]` | |

## Derive columns

## Transform

| What | How | Details |
|---|---|---|
| Inner join | `merge(dt1, dt2)` or `dt1[dt2, nomatch=0]` | |
| Inner join with mismatching keys | `merge(dt1, dt2, by.x=c('a1', 'b1'), by.y=c('b1', 'b2'))` | |
| Outer join | `merge(dt1, dt2, all=TRUE)` | |
| Outer join (mem efficient) | `dt12 = d[dt2, nomatch=0]`<br>`rbind(dt1[!dt12], dt12, dt2[!dt12])` | |
| Left join | `merge(dt1, dt2, all.x = TRUE)` | |
| Left join with identical column names | `dt12 = dt2[dt1, .(x1=x, x2=i.x)]` | |
| Left join byref | `cols = c('x', 'y')`<br>`dt2[dt1, (cols) := mget(paste0('i.', cols))]` | |
| Right join | `merge(dt1, dt2, all.y = TRUE)` | |
| Anti join | `dt1[!dt2]` | |
| Union | `funion(dt, dt2)` | |
| Intersection | `fintersect(dt, dt2)` | |
| Set difference | `fsetdiff(dt, dt2)` | |
| Set equal | `fsetequal(dt, dt2)` | |
| Combine two tables, repeating rows for all unique pairs (`expand.grid`) | `data.table(dt1[rep(1:.N, nrow(dt2))], dt2[rep(1:.N, each=nrow(dt1))])` | |
| To wide format | `dcast(dt, IDa + IDb ~ Param, value.var = 'Value')` | `...` represents all variables, and `.` represents no variable |
| To wide format with aggregation | `dcast(dt, IDa + IDb ~ Param, value.var='Value', fun.aggregate=list(first, last), fill=NA)` | |
| To wide format on a single grouping factor | `dcast(dt, ... ~ Group, value.var = "Value")` | |
| To wide format with value column prefix | `dcast(dt, IDa + IDb ~ paste0('prefix', Param), value.var='Value')` | |
| To wide format without index | ` unstack(dt, Value ~ Param) %>% as.data.table()` | |
| To long format | `melt(dt, id=c('IDa', 'IDb'), measure=c('Param1', 'Param2'))` | |
| To long format for specific columns (no index) | `melt(dt, id=character(), measure=c('Param1', 'Param2'))` | |
| Transpose | `t(dt) %>% as.data.table()` | Drops column names! |
| Repeat rows by group | `dt[, lapply(.SD, rep, 10), by=ID]` | |
| Repeat data.table along a sequence | `s = LETTERS[1:5]`<br>`dt2 = replicate(length(s), dt, simplify=FALSE) %>% setNames(s) %>% rbindlist(idcol=TRUE)` | |


## Convert

| What | How | Details |
|---|---|---|
| Data.frame | `as.data.frame(dt)` | |
| Grouped list | `split(dt, by='Id')` | |
| Matrix | `data.matrix(dt)` | |


## Syntax notes
* `.()` is a shortcut for list(), alternative is `J()`
* `:=` operator assigns by reference
* `(variable)` to refer to the column names stored in the variable
* `get(...)` evaluates expression to column name
* `%>%` pipe operator (magrittr package) to chain function calls in a more readable manner, e.g. `dt[, mean(x), by=ID] %>% .[, mean(x)]`. Calling functions without data argument is done by enclosing in a new block: `dt %>% {table(.$Var)} %>% as.data.table`
* `%chin%` faster version of %in% for character vectors
* `%between%` checks if value between range, e.g. a `%between% c(1,9)`, or a `%between% list(c(1,3), c(4,5))`. Seems slow to use
* `%inrange%` checks if value in range
* `%like%` regular expression check
* `mult='first'` argument provides a useful shortcut for dropping group columns
* Perform merges prior to row subsetting to preserve the keys. Row subsetting followed by a merge drops the obsolete keys, for some reason.
