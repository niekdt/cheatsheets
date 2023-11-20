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
| Create series from list | `pl.Series('name', [1, 2, 3])` |  |
| From lists | `pl.DataFrame('A': [1, 2], 'fruits': ['banana', 'apple'])` | |
| From `pandas.DataFrame` | `pl.from_pandas(data)` | |
| From dict | `pl.DataFrame(dict)` | |
| From dict with schema | `pl.DataFrame(dict, schema = {'col1': pl.Float32, 'col2': pl.Int64, 'col3': pl.Date})` | |
| From array | `data = np.array([[1, 2], [3, 4]])`<br>`pl.DataFrame(data, schema = ['a', 'b'], orient = 'col')` | |
| From list of lists | `data = [[1, 2, 3], [4, 5, 6]]`<br>`pl.DataFrame(data, schema=['a', 'b', 'c'])` | |
| From CSV file | `pl.read_csv('derp.csv')` | |
| From list of data frames | `pl.concat([data, data2, ..., dataN])` | |
| From list of data frames with different columns | `pl.concat([data, data2, ..., dataN], how = 'diagonal')` | |

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
| _i_ th row | `data[i]` | |
| _i_ th row from end | `data[-i]` | |
| First _n_ rows | `data.head(n)` | |
| Last _n_ rows | `data.tail(n)` | |
| Slice of rows from _a_ to _b_ | `data[a:b]` or `data.slice(a, b)` | |
| By list of row numbers | `data[rows]` | |
| Exclude the given row numbers | `data.with_row_count().filter(pl.col('row_nr').is_in(rows).not_())` | Leftover row_nr column |
| Exclude rows that contain null values | `data.drop_nulls()` | |
| Exclude rows that contain null values in certain columns | `data.drop_nulls(['fruits', 'cars'])` | |
| Conditionally on column | `data.filter(pl.col('age') >= 18)` | |
| From multiple column conditions | <code lang='python'>data.filter((pl.col('age') >= 18) & (pl.col('sex') == 'male')) </code> | |
| Limit query to first _n_ rows | <code>data.limit(n)</code> | |
| Limit query to last _n_ rows | <code>data.limit(-n) | |
| Number of missing values | `data.null_count()` | |
| Number of unique values in a column | `data['col1'].n_unique()` | |
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

<td>

```python
data.group_by('sex').agg(pl.col('age').mean())
```

</td>
<td></td>
</tr>
</table>

#### Over time

| What | How | Details |
|---|---|---|
| Moving average | `data.group_by_dynamic('ts', every='1d').agg(pl.col('value').mean())` | ? |

## Test

| What | How | Details |
|---|---|---|
| Empty | `data.is_empty()` | |
| Data frames are equal | `data.frame_equal(data2)` | |
| Column series are equal | `data['sex'].series_equal(data['sex2'].alias('sex'))` | Series names must match! |
| Columns are equal (ignoring name) | ? | |
| Column has missing value | `data['sex'].is_null().any()` | |
| Column has no missing values | `data['sex'].is_not_null().all()` | |
| Column has no duplicate values | ? | |
| Column has duplicate values | ? | |
| Column is of dtype | `data.schema['col1'] == dtype` | | 
| Column is bool dtype | `data.schema['alive'] == pl.Bool` | |
| Column is string type | `data.schema['sex'] == pl.Utf8` | |
| Column is integer type | `data.schema['age'] in pl.datatypes.INTEGER_DTYPES` | |
| Column is standard integer | `data.schema['age'] == pl.Int64` | |

### Row masking

| What | How | Details |
|---|---|---|
| Duplicated rows | `data.is_duplicated()` | |
| Unique rows | `data.is_unique()` | |

## Update

| What | How | Details |
|---|---|---|
| Cast column dtype | `data.with_columns(pl.col('col1').cast(pl.Float32))` | |
| Cast columns to dtypes | `data.cast({'col1': pl.Float32, 'col2': pl.UInt8})` | |
| Rename column | `data.rename({'old1': 'new1', 'old2': 'new2'})` | |
| Update column values | `data.with_columns(pl.col('age') + 5)` | |
| Update column values on condition | `df.with_columns(`<br>`    pl.when(pl.col('age') >= 18).`<br>`    then(pl.lit(1)).`<br>`    otherwise(pl.lit(-1))`<br>`)` | |
| Update column values on conditions | `df.with_columns(`<br>`    pl.when(pl.col('age') >= 18).`<br>`    then(pl.lit(1)).`<br>`    when(pl.col('Sex') == 'M').`<br>`    then(4).`<br>`    otherwise(pl.lit(-1))`<br>`)` | |
| Update column values for specific rows | `rows = [1, 3, 5]`<br>`data.with_row_count().with_columns(`<br>`    pl.when(pl.col('row_nr').is_in(rows)).`<br>`    then(pl.lit(True)).`<br>`    otherwise(pl.lit(False))`<br>`)` | |
| Fill nulls with zero | `data.fill_null(strategy = 'zero')` | |
| Fill nulls with value | `data.fill_null(value)` | |
| Fill nulls with LOCF | `data.fill_null(strategy='forward')` | Wrong for grouped data |
| Fill NaNs with value | `data.fill_nan(value)` | |
| Replace column inplace | `data.replace('age', newAgeSeries)` | |
| Sort table by column | `data.sort('col1')` | |

## Add

### New columns

| What | How | Details |
|---|---|---|
| Append constant numeric column | `data.with_columns(Intercept=pl.lit(1))` | |
| Append column from series | `s = pl.Series("apple", [10, 20, 30])`<br>`data.hstack([s])` | Note the brackets |
| Append column from series inplace | `data.hstack(s, in_place = True)` | |
| Insert column from series inplace | `data.insert_at_idx(1, s)` | |

### Derive new columns

| What | How | Details |
|---|---|---|
| Transform another column | `data.with_columns(AgeSq = pl.col('Age') ** 2)` | |
| Multiple transformations from another column | `data.with_columns(`<br>`    Age2 = pl.col('Age') ** 2`<br>`    Age3 = pl.col('Age') ** 3`<br>`)` | |
| Conditional on the value of another column | `data.with_columns(`<br>`    pl.when(pl.col('age') >= 18).`<br>`    then(pl.lit(1)).`<br>`    otherwise(pl.lit(-1))`<br>`)` | |
| Map another column | `map = dict(1 = 'a', 2 = 'b', 3 = 'c')`<br>`data.with_columns(`<br>`    NumCat = pl.col('Num').map_dict(map).cast(pl.Categorical)`<br>`)` | |
| Parse string column to date | `data.with_columns(`<br>`    Date=pl.col('RawDate').str.to_date()`<br>`)` | |
| Parse string column to date with known format | `data.with_columns(`<br>`    Date = pl.col("RawDate").str.to_date('%Y-%m-%d')`<br>`)` | |
| Week-day from date column | | |
| Month from date column | `data.with_columns(Month = pl.col('Date').dt.month())` | |
| Year from date column | `data.with_columns(Month = pl.col('Date').dt.year())` | |
| Group-wise from aggregate value | `data.with_columns(`<br>`    DaysSinceStart = pl.col('Date') - pl.col('Date').min().over('Subject').cast(pl.Int) + 1`<br>`)` | |

### Rows

| What | How | Details |
|---|---|---|
| Add row as tuple | ? | |
| Add list of tuples | ? | |
| Add data frame | |
| Add data frame inplace | `data.extend(data2)` | |
| Add data frames inplace | `data.vstack(data2)`<br>`data.vstack(dataN)`<br>`data.rechunk()` | |

## Remove

### Columns

| What | How | Details |
|---|---|---|
| Remove column | `data.drop('Age')` | |
| Remove column inplace | `data.drop_in_place('Age')` | Returns the dropped column |
| Remove columns | `data.drop(['Age', 'Sex'])` | |
| Remove all numeric columns | `data.drop(cs.numeric())` | |
| Remove columns based on selector | `data.drop(cs)` | |

### Rows

## Reshape

| What | How | Details |
|---|---|---|
| From wide to long format | `data.melt(id_vars='sex', value_vars=['a', 'b'])` | |
| To narrow format | `data.explode(?)` | ? |

## Merge

| What | How | Details |
|---|---|---|
| Merge two data frames on the sorted key | `data.merge(data2)` | |
| Inner join | `data.join(data2, on = ['sex', 'country'])` | |
| Left join | `data.join(data2, on = ['sex', 'country'], how = 'left')` | |
| Right join | `data.join(data2, on = ['sex', 'country'], how = 'right')` | |
| Outer join | `data.join(data2, on = ['sex', 'country'], how = 'outer')` | |
| Cross join | `data.join(data2, on = ['sex', 'country'], how = 'cross')` | |
| Semi join (one match per index) | `data.join(data2, on = ['sex', 'country'], how = 'semi')` | |
| Anti join (exclude matches from table 2) | `data.join(data2, on = ['sex', 'country'], how = 'anti')` | |

## Extract

| What | How | Details |
|---|---|---|
| Get column (as series) | `data['col1']` | |
| Get column (as list) | `list(data['col1'])` | ? |
| Get _i_ th row (as tuple) | `data.row(i)` | |
| Get rows (as list of tuple) | `data.rows(...)` | ? |
| First item (cell) | `data.item(0, 0)` | |
| Item (cell) from row _i_ and column index _j_ | `data.item(i, j)` | |
| Item (cell) from row _i_ and column name _name_ | `data.item(i, name)` | |

## Convert

| What | How | Details |
|---|---|---|
| To `pandas.DataFrame` | `data.to_pandas()` | |
| To list of series | `data.get_columns()` | |
| Split into list of data frames based on column | `data.partition_by('sex')` | |
| Split into list of data frames based on column tuples | `data.partition_by('sex', 'country')` | |
| Split into dict of data frames based on column(s) | `data.partition_by('sex', 'country', as_dict = True)` | |
| To CSV file | `data.write_csv('derp.csv')` | |
| To Parquet file | `data.write_parquet('derp.parquet')` | |
| To JSON | ? | |
