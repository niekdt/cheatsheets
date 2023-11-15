---
layout: default
title: Polars
parent: Python
nav_order: 150
---

# Polars
{: .no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| Create series from list | `pl.Series('name', \[1, 2, 3])` |  |
| From lists | `pl.DataFrame('A': \[1, 2], 'fruits': \['banana', 'apple'])` | |
| From `pandas.DataFrame` | `pl.from_pandas(data)` | |
| From dict | `pl.DataFrame(dict)` | |
| From dict with schema | `pl.DataFrame(dict, schema = {'col1': pl.Float32, 'col2': pl.Int64, 'col3': pl.Date})` | |
| From array | `data = np.array(\[\[1, 2], \[3, 4]])`<br>`pl.DataFrame(data, schema = \['a', 'b'], orient = 'col')` | |
| From list of lists | `data = \[\[1, 2, 3], \[4, 5, 6]]`<br>`pl.DataFrame(data, schema=\['a', 'b', 'c'])` | |
| From CSV file | `pl.read_csv('derp.csv')` | |
| From list of data frames | `pl.concat(\[data, data2, ..., dataN])` | |
| From list of data frames with different columns | `pl.concat(\[data, data2, ..., dataN], how = 'diagonal')` | |

## Properties

| What | How | Details |
|---|---|---|
| Number of columns | `len(data.columns)` | ? |
| Column names | `data.columns` | |
| Column dtypes | `data.dtypes` | |
| Column-dtype map | `data.schema` | |
| Find column index by name | `data.find_idx_by_name('age')` | |
| Number of rows | `data.height` | |

## Query

Start a lazy query using a LazyFrame by `data.lazy()`. Operations on a LazyFrame are not executed until this is requested by either calling collect() or fetch().
Lazy operations are advised because they allow for query optimization and more parallelization.

### Columns

| What | How | Details |
|---|---|---|
| Single column | `data.select('col1')` | |
| Multiple columns | `data.select('col1', 'col2')` | |
| Multiple columns, dynamically | ? | |

### Rows

| What | How | Details |
|---|---|---|
| No rows | `data.clear()` | |
| $i$ th row | `data[i]` | |
| $i$ th row from end | `data[-i]` | |
| First $n$ rows | `data.head(n)` | |
| Last $n$ rows | `data.tail(n)` | |
| Slice of rows from $a$ to $b$ | `data[a:b]` or `data.slice(a, b)` | |
| By list of row numbers | `data\[rows]` | |
| Exclude the given row numbers | `data.with_row_count().filter(pl.col('row_nr').is_in(rows).not_())` | Leftover row_nr column |
| Exclude rows that contain null values | `data.drop_nulls()` | |
| Exclude rows that contain null values in certain columns | `data.drop_nulls(\['fruits', 'cars'])` | |
| Conditionally on column | `data.filter(pl.col('age') >= 18)` | |
| From multiple column conditions | <code lang='python'>data.filter((pl.col('age') >= 18) & (pl.col('sex') == 'male')) </code> | |
| Limit query to first $n$ rows | <code>data.limit(n)</code> | |
| Limit query to last $n$ rows | <code>data.limit(-n) | |
| Number of missing values | `data.null_count()` | |
| Number of unique values in a column | `data\['col1'].n_unique()` | |
| Number of unique rows over columns | ? | |

### Aggregate

### Grouped

<table>
<tr>
<th>What</th>
<th>How</th>
<th>Details</th>
</tr>
<tr>
<td>Mean of column</td>
<td><pre lang='python'>data.group_by('sex').agg(pl.col('age').mean())</pre></td>
<td></td>
</tr>
</table>

#### Over time

| What | How | Details |
|---|---|---|
| Moving average | <pre lang='python'>data.group_by_dynamic('ts', every='1d').agg(pl.col('value').mean()) | ? |

## Test

| What | How | Details |
|---|---|---|
| Empty | <pre lang='python'>data.is_empty() | |
| Data frames are equal | <pre lang='python'>data.frame_equal(data2) | |
| Column series are equal | <pre lang='python'>data\['sex'].series_equal(data\['sex2'].alias('sex')) | Series names must match! |
| Columns are equal (ignoring name) | ? | |
| Column has missing value | <pre lang='python'>data\['sex'].is_null().any() | |
| Column has no missing values | <pre lang='python'>data\['sex'].is_not_null().all() | |
| Column has no duplicate values | ? | |
| Column has duplicate values | ? | |
| Column is of dtype | <pre lang='python'>data.schema\['col1'] == dtype | | 
| Column is bool dtype | <pre lang='python'>data.schema\['alive'] == pl.Bool | |
| Column is string type | <pre lang='python'>data.schema\['sex'] == pl.Utf8 | |
| Column is integer type | <pre lang='python'>data.schema\['age'] in pl.datatypes.INTEGER_DTYPES | |
| Column is standard integer | <pre lang='python'>data.schema\['age'] == pl.Int64 | |

### Row masking

| What | How | Details |
|---|---|---|
| Duplicated rows | <pre lang='python'>data.is_duplicated() | |
| Unique rows | <pre lang='python'>data.is_unique() | |

## Update

| What | How | Details |
|---|---|---|
| Cast column dtype | <pre lang='python'>data.with_columns(pl.col('col1').cast(pl.Float32)) | |
| Cast columns to dtypes | <pre lang='python'>data.cast({'col1': pl.Float32, 'col2': pl.UInt8}) | |
| Rename column | <pre lang='python'>data.rename({'old1': 'new1', 'old2': 'new2'}) | |
| Update column values | <pre lang='python'>data.with_columns(pl.col('age') + 5) | |
| Update column values on condition | <pre lang='python'>df.with_columns(&#13;&#09;pl.when(pl.col('age') >= 18).&#13;&#09;then(pl.lit(1)).&#13;&#09;otherwise(pl.lit(-1))&#13;)
| Update column values on conditions | <pre lang='python'>df.with_columns(&#13;&#09;pl.when(pl.col('age') >= 18).&#13;&#09;then(pl.lit(1)).&#13;&#09;when(pl.col('Sex') == 'M').&#13;&#09;then(4).&#13;&#09;otherwise(pl.lit(-1))&#13;) | |
| Update column values for specific rows | <pre lang='python'>rows = \[1, 3, 5]&#13;data.with_row_count().with_columns(&#13;&#09;pl.when(pl.col('row_nr').is_in(rows)).&#13;&#09;then(pl.lit(True)).&#13;&#09;otherwise(pl.lit(False))&#13;)| |
| Fill nulls with zero | <pre lang='python'>data.fill_null(strategy = 'zero') | |
| Fill nulls with value | <pre lang='python'>data.fill_null(value) | |
| Fill nulls with LOCF | <pre lang='python'>data.fill_null(strategy='forward') | Wrong for grouped data |
| Fill NaNs with value | <pre lang='python'>data.fill_nan(value) | |
| Replace column inplace | <pre lang='python'>data.replace('age', newAgeSeries) | |
| Sort table by column | <pre lang='python'>data.sort('col1') | |

## Add

### New columns

| What | How | Details |
|---|---|---|
| Append constant numeric column | <pre lang='python'>data.with_columns(Intercept=pl.lit(1)) | |
| Append column from series | <pre lang='python'>s = pl.Series("apple", \[10, 20, 30])&#13;data.hstack(\[s]) | Note the brackets |
| Append column from series inplace | <pre lang='python'>data.hstack(s, in_place = True) | |
| Insert column from series inplace | <pre lang='python'>data.insert_at_idx(1, s) | |

### Derive new columns

| What | How | Details |
|---|---|---|
| Transform another column | <pre lang='python'>data.with_columns(AgeSq = pl.col('Age') ** 2) | |
| Multiple transformations from another column | <pre lang='python'>data.with_columns(&#13;&#09;Age2 = pl.col('Age') ** 2&#13;&#09;Age3 = pl.col('Age') ** 3&#13;) | |
| Conditional on the value of another column | <pre lang='python'>data.with_columns(&#13;&#09;pl.when(pl.col('age') >= 18).&#13;&#09;then(pl.lit(1)).&#13;&#09;otherwise(pl.lit(-1))&#13;)
| Map another column | <pre lang='python'>map = dict(1 = 'a', 2 = 'b', 3 = 'c')&#13;data.with_columns(&#13;&#09;NumCat = pl.col('Num').map_dict(map).cast(pl.Categorical)&#13;) | |
| Parse string column to date | <pre lang='python'>data.with_columns(&#13;&#09;Date=pl.col('RawDate').str.to_date()&#13;) | |
| Parse string column to date with known format | <pre lang='python'>data.with_columns(&#13;&#09;Date = pl.col("RawDate").str.to_date('%Y-%m-%d')&#13;) | |
| Week-day from date column | | |
| Month from date column | <pre lang='python'>data.with_columns(Month = pl.col('Date').dt.month()) | |
| Year from date column | <pre lang='python'>data.with_columns(Month = pl.col('Date').dt.year()) | |
| Group-wise from aggregate value | <pre lang='python'>data.with_columns(&#13;&#09;DaysSinceStart = pl.col('Date') - pl.col('Date').min().over('Subject').cast(pl.Int) + 1&#13;) | |

### Rows

| What | How | Details |
|---|---|---|
| Add row as tuple | ? | |
| Add list of tuples | ? | |
| Add data frame | |
| Add data frame inplace | <pre lang='python'>data.extend(data2) | |
| Add data frames inplace | <pre lang='python'>data.vstack(data2)&#13;data.vstack(dataN)&#13;data.rechunk() | |

## Remove

### Columns

| What | How | Details |
|---|---|---|
| Remove column | <pre lang='python'>data.drop('Age') | |
| Remove column inplace | <pre lang='python'>data.drop_in_place('Age') | Returns the dropped column |
| Remove columns | <pre lang='python'>data.drop(\['Age', 'Sex']) | |
| Remove all numeric columns | <pre lang='python'>data.drop(cs.numeric()) | |
| Remove columns based on selector | <pre lang='python'>data.drop(cs) | |

### Rows

## Reshape

| What | How | Details |
|---|---|---|
| From wide to long format | <pre lang='python'>data.melt(id_vars='sex', value_vars=['a', 'b']) | |
| To narrow format | <pre lang='python'>data.explode(?) | ? |

## Merge

| What | How | Details |
|---|---|---|
| Merge two data frames on the sorted key | <pre lang='python'>data.merge(data2) | |
| Inner join | <pre lang='python'>data.join(data2, on = \['sex', 'country']) | |
| Left join | <pre lang='python'>data.join(data2, on = \['sex', 'country'], how = 'left') | |
| Right join | <pre lang='python'>data.join(data2, on = \['sex', 'country'], how = 'right') | |
| Outer join | <pre lang='python'>data.join(data2, on = \['sex', 'country'], how = 'outer') | |
| Cross join | <pre lang='python'>data.join(data2, on = \['sex', 'country'], how = 'cross') | |
| Semi join (one match per index) | <pre lang='python'>data.join(data2, on = \['sex', 'country'], how = 'semi') | |
| Anti join (exclude matches from table 2) | <pre lang='python'>data.join(data2, on = \['sex', 'country'], how = 'anti') | |

## Extract

| What | How | Details |
|---|---|---|
| Get column (as series) | <pre lang='python'>data\['col1'] | |
| Get column (as list) | <pre lang='python'>list(data\['col1']) | ? |
| Get $i$ th row (as tuple) | <pre lang='python'>data.row(i) | |
| Get rows (as list of tuple) | <pre lang='python'>data.rows(...) | ? |
| First item (cell) | <pre lang='python'>data.item(0, 0) | |
| Item (cell) from row $i$ and column index $j$ | <pre lang='python'>data.item(i, j) | |
| Item (cell) from row $i$ and column name $name$ | <pre lang='python'>data.item(i, name) | |

## Convert

| What | How | Details |
|---|---|---|
| To `pandas.DataFrame` | <pre lang='python'>data.to_pandas() | |
| To list of series | <pre lang='python'>data.get_columns() | |
| Split into list of data frames based on column | <pre lang='python'>data.partition_by('sex') | |
| Split into list of data frames based on column tuples | <pre lang='python'>data.partition_by('sex', 'country') | |
| Split into dict of data frames based on column(s) | <pre lang='python'>data.partition_by('sex', 'country', as_dict = True) | |
| To CSV file | <pre lang='python'>data.write_csv('derp.csv') | |
| To Parquet file | <pre lang='python'>data.write_parquet('derp.parquet') | |
| To JSON | ? | |
