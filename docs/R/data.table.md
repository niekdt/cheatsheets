# data.table

## Create
| What | How | Details |
|---|---|---|
| From `data.frame` | <pre lang='R'>as.data.table(df)</pre> | |
| From `data.frame` byref | <pre lang='R'>setDT(df) | |
| From `data.frame`, storing row names as the first column | <pre lang='R'>as.data.table(df, keep.rownames=TRUE) | |
| From list of named vectors | <pre lang='R'>as.data.table(do.call(rbind, veclist)) | |
| From statistical object | <pre lang='R'>broom::tidy(lm) %>% as.data.table() | |
| From statistical object to one-row | <pre lang='R'>broom::glance(lm) %>% as.data.table() | |
| From RLE | <pre lang='R'>rle(x) %>% unclass() %>% as.data.table() | |
| From matrix to long format | <pre lang='R'>melt(data.table(x), measure = colnames(x), id=character()) | |
| From array to long format | <pre lang='R'>as.data.table(x) | Ensure that all dims are named |
| From CSV | <pre lang='R'>fread('derp.csv') | |

## Properties
| What | How | Details |
|---|---|---|
| Column names | <pre lang='R'>names(dt) | |
| Number of columns | <pre lang='R'>length(dt) | |
| Number of rows | <pre lang='R'>nrow(dt) | |
| Get key(s) | <pre lang='R'>key(dt) | |
| Set key(s) by symbols byref | <pre lang='R'>setkey(dt, Age, Sex) | |
| Set key(s) by names byref | <pre lang='R'>setkeyv(dt, c('Age', 'Sex')) | |
| Assign attribute byref | <pre lang='R'>setattr(dt, 'myAttr', value) | |
| Remove attribute byref | <pre lang='R'>setattr(dt, 'myAttr', NULL) | |
| Number of duplicated rows | <pre lang='R'>sum(duplicated(dt)) | |

## Sort
Data tables are sorted by the keys
| What | How | Details |
|---|---|---|
| Sort by column symbols byref | <pre lang='R'>setorder(dt, Age, Sex) | |
| Sort by column names byref | <pre lang='R'>setorderv(dt, c('Age', 'Sex')) | |

## Query
| What | How | Details |
|---|---|---|
| Select column | <pre lang='R'>dt$Age | |
| Select column | <pre lang='R'>dt\[, .(Age)] | |
| Select column by variable name | <pre lang='R'>dt\[\[x]] | |
| Select columns | <pre lang='R'>dt\[, .(Age, Sex)] | |
| Select all columns except | <pre lang='R'>dt\[, -c('Age', 'Sex')] | |
| Select columns and apply function | <pre lang='R'>dt\[, lapply(.SD, mean), .SDcols=c('Age', 'Sex')] | |
| Select rows by row number | <pre lang='R'>dt\[1:10] | |
| Select rows with key value | <pre lang='R'>dt\[dtquery\[query, .(ID)]] | |
| Select rows with key value, dropping factor levels | <pre lang='R'>dt\[c('a1', 'a2')] | Discards factor level order! |
| Select first/last row with key values | <pre lang='R'>dt\[c('a1', 'a2'), mult='first'] | |
| Select rows with value over multiple keys | <pre lang='R'>dt\[.('a1', 'b1')] | Notice the dot |
| Select rows of groups specified in table | <pre lang='R'>dtquery = data.table(..., by=keys); dt\[dtquery] | |
| Select rows of groups, excluding non-existent queried rows | <pre lang='R'>dtquery = data.table(..., by=keys); dt\[dtquery, nomatch=0] | |
| Select rows with values specified in table | <pre lang='R'>dtquery = data.table(...)&#13;merge(dt, dtquery, by=COLUMNS) | |
| Unique rows | <pre lang='R'>unique(dt) | |
| Unique rows by columns | <pre lang='R'>unique(dt, by = keys(dt)) | | 
| Duplicated rows | <pre lang='R'>dt\[duplicated(dt),] | |
| Sample rows | <pre lang='R'>dt\[sample(.N, 10),] | |
| Sample by key value | <pre lang='R'>dtquery = data.table(sample(levels(dt$Id), 5)); dt\[dtquery] | |
| Find row index of key value | <pre lang='R'>dt\['a1', which=TRUE] | |
| Repeat rows | <pre lang='R'>dt\[rep(1:.N, 10)] | |

## Aggregate

### Grouped
| What | How | Details |
|---|---|---|
| By key | <pre lang='R'>dt\[,, by = ID] | |
| By string key | <pre lang='R'>dt\[,, by = 'ID'] | |
| By variable key | <pre lang='R'>dt\[,, by=(var)] | |
| By keys | <pre lang='R'>dt\[,, by = .(IDa, IDb)] | |
| By string keys | <pre lang='R'>dt\[,, by = c('IDa', 'IDb')] | |
| By range of keys | <pre lang='R'>dt\[,, by = IDa:IDc] | |
| By fixed-sized bins | <pre lang='R'>dt\[ , , by=findInterval(X, seq(1, 100, by=7))] | |
| By key using its value | <pre lang='R'>dt\[, {id = first(ID); dt2\[id]}, by=ID] | |
| By key using its factor value | <pre lang='R'>dt\[, {id = levels(ID)\[.GRP]; dt2\[id]}, by=ID] | |
| Select columns by key | <pre lang='R'>dt\[, .(x, y), by=ID] | |
| Select rows by key | <pre lang='R'>dt\[dt\[, .I\[1:10], by=ID]] | |

### Rolling
| What | How | Details |
|---|---|---|
| Right-aligned rolling sum of size $w$ | <pre lang='R'>dt\[, RMean := Reduce('+', shift(x, 1:w-1, fill=0)) / pmin(w, .I)] | |

### Grouped rolling
| What | How | Details |
|---|---|---|
| Right-aligned rolling sum of size $w$ | <pre lang='R'>dt\[, RSum := Reduce('+', shift(x, 0:(w-1), fill=0)), by=ID] | Easily 50 times faster than `zoo::rollapply` |
| Right-aligned rolling mean with fixed window $w$ (zero-filled) | <pre lang='R'>dt\[, RMean := Reduce('+', shift(x, 0:(w-1), fill=0)) / w, by=ID] | |
| Right-aligned rolling mean (partial windows) | <pre lang='R'>dt\[, RMean := Reduce('+', shift(x, 0:(w-1), fill=0)) / pmin(w, 1:.N), by=ID] | |
| Right-aligned rolling mean (ignoring NAs) | <pre lang='R'>dt\[, RMean := Reduce('+', shift(ifelse(is.na(x), 0, x), 0:(W-1), fill=0)) / &#13;Reduce('+', shift(is.finite(x), 0:(W-1), fill=0)), by=ID] | |
| Centered rolling mean (fixed window of size $W$ (inserting zeroes)) | <pre lang='R'>dt\[, CMean := Reduce('+', shift(x, -floor(W/2):floor(W/2), fill=0)) / W, by=ID] | |
| Centered rolling mean (partial windows) | <pre lang='R'>dt\[, CMean := Reduce('+', shift(x, -floor(W/2):floor(W/2), fill=0)) / &#13;pmin(W, c(1:ceiling(.N/2), floor(.N/2):1)), by=ID] | |
| Centered rolling mean (ignoring NAs) | <pre lang='R'>dt\[, CMean := Reduce('+', shift(x, -floor(W/2):floor(W/2), fill=0)) / &#13;Reduce('+', shift(is.finite(x), -floor(W/2):floor(W/2), fill=0)), by=ID] | |
| Mark consecutive matching rows | <pre lang='R'>dt\[, CMatch := {r = rle(MATCH)&#13;r$values = replace(r$values, r$lengths < GAP_SIZE & r$values, FALSE)&#13;inverse.rle(r)&#13;}, by=ID] | |
| Count column for consecutive matches | <pre lang='R'>dt\[, MatchNr := {function(x) cumsum(x) + cummin(c(0, diff(x)) * cumsum(x))}(MATCH), by=ID] | |
| Impute NA values | <pre lang='R'>dt\[, X := Hmisc::impute(X, mean), by=ID] |  |

## Row masking

## Test

## Update
| What | How | Details |
|---|---|---|
| Fill NAs by zero | <pre lang='R'>dt\[is.na(dt)] = 0 | |

## Append rows
| What | How | Details |
|---|---|---|
| Insert missing rows based on missing combination of keys | <pre lang='R'>dt\[CJ(unique(IDa), unique(IDb))] | |
| Replace missing values using LOCF | <pre lang='R'>locf = function(x) x\[cummax(c(TRUE, tail(is.finite(x) * seq_along(x), -1)))]&#13;dt[, x := locf(x), by=ID] | |
| Replace missing values using NOCB | <pre lang='R'>locf = function(x) x\[cummax(c(TRUE, tail(is.finite(x) * seq_along(x), -1)))]&#13;nocb = function(x) rev(locf(rev(x))&#13;dt[, x := nocb(x), by=ID] | |

## Update (byref)
| What | How | Details |
|---|---|---|
| Assign/update column byref | <pre lang='R'>dt\[, x:=1] | |
| Update columns byref | <pre lang='R'>dt\[, ':='(x=1, y=2)] | |
| Update columns dynamically byref | <pre lang='R'>dt\[, c('x', 'y') := .(1, 2)] | |
| Update columns from matrix columns byref | <pre lang='R'>mat = matrix(1:8, ncol=2)&#13;dt\[, c('a' ,'b') := split(mat, col(mat))] | |
| Update columns from matrix rows byref | <pre lang='R'>mat = matrix(1:8, nrow=2)&#13;dt\[, c('a' ,'b') := split(mat, row(mat))] | |
| Update columns from another table byref | <pre lang='R'>dt2 = data.table(…)&#13;dt\[dt2, (vars) := mget(vars)] | |
| Update column per key | <pre lang='R'>dt\[, x:=mean(y), by=ID] | |
| Update subset | <pre lang='R'>dt\[is.na(x), y:=1] | |
| Update value per key | <pre lang='R'>dtg = data.table(…, x=2, key=Group)&#13;dt\[dtg, x := i.x] | |
| Update subset per key | <pre lang='R'>GroupValue = data.table(..., key=Group)&#13;dt\[, x:=GroupValue\[.BY], by=ID] | Slow, can be done faster |
| Replace factor NA by new level | <pre lang='R'>dt\[is.na(f), f := 'N/A'] | |
| Remove column | <pre lang='R'>dt\[, x := NULL] | |
| Remove columns | <pre lang='R'>dt\[, ':='(x=NULL, y=NULL)] | |
| Remove columns dynamically | <pre lang='R'>dt\[, c('x', 'y') := NULL] | |

## Derive columns

## Transform
| What | How | Details |
|---|---|---|
| Inner join | <pre lang='R'>merge(dt1, dt2)</pre>or<pre lang='R'>dt1\[dt2, nomatch=0] | |
| Inner join with mismatching keys | <pre lang='R'>merge(dt1, dt2, by.x=c('a1', 'b1'), by.y=c('b1', 'b2')) | |
| Outer join | <pre lang='R'>merge(dt1, dt2, all=TRUE) | |
| Outer join (mem efficient) | <pre lang='R'>dt12 = d\[dt2, nomatch=0]&#13;rbind(dt1\[!dt12], dt12, dt2\[!dt12]) | |
| Left join | <pre lang='R'>merge(dt1, dt2, all.x = TRUE) | |
| Left join with identical column names | <pre lang='R'>dt12 = dt2\[dt1, .(x1=x, x2=i.x)] | |
| Left join byref | <pre lang='R'>cols = c('x', 'y')&#13;dt2\[dt1, (cols) := mget(paste0('i.', cols))] | |
| Right join | <pre lang='R'>merge(dt1, dt2, all.y = TRUE) | |
| Anti join | <pre lang='R'>dt1\[!dt2] | |
| Union | <pre lang='R'>funion(dt, dt2) | |
| Intersection | <pre lang='R'>fintersect(dt, dt2) | |
| Set difference | <pre lang='R'>fsetdiff(dt, dt2) | |
| Set equal | <pre lang='R'>fsetequal(dt, dt2) | |
| Combine two tables, repeating rows for all unique pairs (`expand.grid`) | <pre lang='R'>data.table(dt1\[rep(1:.N, nrow(dt2))], dt2\[rep(1:.N, each=nrow(dt1))]) | |
| To wide format | <pre lang='R'>dcast(dt, IDa + IDb ~ Param, value.var = 'Value') | `...` represents all variables, and `.` represents no variable |
| To wide format with aggregation | <pre lang='R'>dcast(dt, IDa + IDb ~ Param, value.var='Value', fun.aggregate=list(first, last), fill=NA) | |
| To wide format on a single grouping factor | <pre lang='R'>dcast(dt, ... ~ Group, value.var = "Value") | |
| To wide format with value column prefix | <pre lang='R'>dcast(dt, IDa + IDb ~ paste0('prefix', Param), value.var='Value') | |
| To wide format without index | <pre lang='R'> unstack(dt, Value ~ Param) %>% as.data.table() | |
| To long format | <pre lang='R'>melt(dt, id=c('IDa', 'IDb'), measure=c('Param1', 'Param2')) | |
| To long format for specific columns (no index) | <pre lang='R'>melt(dt, id=character(), measure=c('Param1', 'Param2')) | |
| Transpose | <pre lang='R'>t(dt) %>% as.data.table() | Drops column names! |
| Repeat rows by group | <pre lang='R'>dt\[, lapply(.SD, rep, 10), by=ID] | |
| Repeat data.table along a sequence | <pre lang='R'>s = LETTERS\[1:5]&#13;dt2 = replicate(length(s), dt, simplify=FALSE) %>% setNames(s) %>% rbindlist(idcol=TRUE) | |

## Convert
| What | How | Details |
|---|---|---|
| To grouped list | <pre lang='R'>split(dt, by='Id') | |
| To matrix | <pre lang='R'>data.matrix(dt) | |


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
