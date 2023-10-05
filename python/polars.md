% Polars quick reference sheet

# Creation
| What | How | Details |
|---|---|---|
| Create series | <pre lang='python'>pl.Series('name', [1, 2, 3]) |  |
| Create data frame | <pre lang='python'>pl.DataFrame('A': [1, 2], 'fruits': ['banana', 'apple']) | |
| Clone (create new instance) | <pre lang='python'>data.clone() | |
| From dict | <pre lang='python'>pl.DataFrame(dict) | |
| From dict with schema | <pre lang='python'>pl.DataFrame(dict, schema = {'col1': pl.Float32, 'col2': pl.Int64, 'col3': pl.Date} | |
| From array | <pre lang='python'>data = np.array([[1, 2], [3, 4]])&#13;pl.DataFrame(data, schema = ['a', 'b'], orient = 'col') | |
| From list of lists | <pre lang='python'>data = [[1, 2, 3], [4, 5, 6]]&#13;pl.DataFrame(data, schema=['a', 'b', 'c']) | |
| From CSV file | <pre lang='python'>pl.read_csv('derp.csv') | |
| From list of data frames | <pre lang='python'>pl.concat([data, data2, ..., dataN]) | |
| From list of data frames with different columns | <pre lang='python'>pl.concat([data, data2, ..., dataN], how = 'diagonal') | |

# Properties
| What | How | Details |
|---|---|---|
| Number of columns | <pre lang='python'>len(data.columns) | ? |
| Column names | <pre lang='python'>data.columns | |
| Column dtypes | <pre lang='python'>data.dtypes | |
| Column-dtype map | <pre lang='python'>data.schema | |
| Find column index by name | <pre lang='python'>data.find_idx_by_name('age') | |
| Number of rows | <pre lang='python'>data.height | |

# Extract
| What | How | Details |
|---|---|---|
| Get column (as series) | <pre lang='python'>data['col1'] | |
| Get column (as list) | <pre lang='python'>list(data['col1']) | ? |
| Get $i$ th row (as tuple) | <pre lang='python'>data.row(i) | |
| Get rows (as list of tuple) | <pre lang='python'>data.rows(...) | ? |
| First item (cell) | <pre lang='python'>data.item(0, 0) | |
| Item (cell) from row $i$ and column index $j$ | <pre lang='python'>data.item(i, j) | |
| Item (cell) from row $i$ and column name $name$ | <pre lang='python'>data.item(i, name) | |

# Query (as data frame)
Start a lazy query using a LazyFrame by data.lazy(). Operations on a LazyFrame are not executed until this is requested by either calling collect() or fetch().
Lazy operations are advised because they allow for query optimization and more parallelization.

## Columns
| What | How | Details |
|---|---|---|
| Single column | <pre lang='python'>data.select('col1') | |
| Multiple columns | <pre lang='python'>data.select('col1', 'col2') | |

## Rows
| What | How | Details |
|---|---|---|
| No rows | `data.clear()` | |
| $i$ th row | `data[i]` | |
| $i$ th row from end | `data[-i]` | |
| First $n$ rows | `data.head(n)` | |
| Last $n$ rows | `data.tail(n)` | |
| Slice of rows from $a$ to $b$ | `data[a:b]` or `data.slice(a, b)` | |
| By list of row numbers | <pre lang='python'>data[rows] | |
| Exclude the given row numbers | <pre lang='python'>data.with_row_count().filter(pl.col('row_nr').is_in(rows).not_()) | Leftover row_nr column |
| Exclude rows that contain null values | <pre lang='python'>data.drop_nulls() | |
| Exclude rows that contain null values in certain columns | <pre lang='python'>data.drop_nulls(['fruits', 'cars']) | |
| Conditionally on column | <pre lang='python'>data.filter(pl.col('age') >= 18) | |
| From multiple column conditions | <pre lang='python'>data.filter((pl.col('age') >= 18) & (pl.col('sex') == 'male')) | |
| Limit query to first $n$ rows | <pre lang='python'>data.limit(n) | |
| Limit query to last $n$ rows | <pre lang='python'>data.limit(-n) | |
| Number of missing values | <pre lang='python'>data.null_count() | |
| Number of unique values in a column | <pre lang='python'>data['col1'].n_unique() | |
| Number of unique rows over columns | ? | |

# Aggregate
## Grouped
| What | How | Details |
|---|---|---|
| Mean of column | <pre lang='python'>data.group_by('sex').agg(pl.col('age').mean()) | |

## Over time
| What | How | Details |
|---|---|---|
| Moving average | <pre lang='python'>data.group_by_dynamic('ts', every='1d').agg(pl.col('value').mean()) | ? |

# Row masking
| What | How | Details |
|---|---|---|
| Duplicated rows | <pre lang='python'>data.is_duplicated() | |
| Unique rows | <pre lang='python'>data.is_unique() | |

# Column masking

# Tests
| What | How | Details |
|---|---|---|
| Empty | <pre lang='python'>data.is_empty() | |
| Data frames are equal | <pre lang='python'>data.frame_equal(data2) | |
| Column series are equal | <pre lang='python'>data['sex'].series_equal(data['sex2'].alias('sex')) | Series names must match! |
| Columns are equal (ignoring name) | ? | |
| Column has missing value | <pre lang='python'>data['sex'].is_null().any() | |
| Column has no missing values | <pre lang='python'>data['sex'].is_not_null().all() | |
| Column is of dtype | <pre lang='python'>data.schema['col1'] == dtype | | 
| Column is bool dtype | <pre lang='python'>data.schema['alive'] == pl.Bool | |
| Column is string type | <pre lang='python'>data.schema['sex'] == pl.Utf8 | |
| Column is integer type | <pre lang='python'>data.schema['age'] in pl.datatypes.INTEGER_DTYPES | |
| Column is standard integer | <pre lang='python'>data.schema['age'] == pl.Int64 | |

# Update
| What | How | Details |
|---|---|---|
| Rename column | <pre lang='python'>data.rename({'old1': 'new1', 'old2': 'new2'}) | |
| Update column values | <pre lang='python'>data.with_columns(pl.col('age') + 5) | |
| Update column values on condition | <pre lang='python'>df.with_columns(&#13;pl.when(pl.col('age') >= 18).&#13;then(pl.lit(1)).&#13;otherwise(pl.lit(-1))&#13;)
| Update column values on conditions | <pre lang='python'>df.with_columns(&#13;pl.when(pl.col('age') >= 18).&#13;then(pl.lit(1)).&#13;when(pl.col('Sex') == 'M').&#13;then(4).&#13;otherwise(pl.lit(-1))&#13;)
| Update row values | ? | |
| Fill nulls with zero | <pre lang='python'>data.fill_null(strategy = 'zero') | |
| Fill nulls with value | <pre lang='python'>data.fill_null(value) | |
| Fill nulls with LOCF | <pre lang='python'>data.fill_null(strategy='forward') | Wrong for grouped data |
| Fill NaNs with value | <pre lang='python'>data.fill_nan(value) | |
| Replace column inplace | <pre lang='python'>data.replace('age', newAgeSeries) | |
| Sort table by column | <pre lang='python'>data.sort('col1') | |

## Casting / parsing
| What | How | Details |
|---|---|---|
| Cast column dtype | <pre lang='python'>data.with_columns(pl.col('col1').cast(pl.Float32)) | |
| Cast columns to dtypes | <pre lang='python'>data.cast({'col1': pl.Float32, 'col2': pl.UInt8}) | |
| Parse string column to date | <pre lang='python'>data.with_columns(pl.col('Date').str.to_date()) | |
| Parse string column to date with known format | <pre lang='python'>data.with_columns(pl.col("Date").str.to_date('%Y-%m-%d')) | |

# Append rows
| What | How | Details |
|---|---|---|
| Append row (as tuple) | ? | |
| Append rows (as list of tuples) | ? | |
| Append data frame | |
| Append data frame inplace | <pre lang='python'>data.extend(data2) | |
| Append data frames inplace | <pre lang='python'>data.vstack(data2)&#13;data.vstack(dataN)&#13;data.rechunk() | |

# Add/remove columns
# Derive columns
| What | How | Details |
|---|---|---|
| Month from date | <pre lang='python'>data['Date'].dt.month() | |


# Transform
| What | How | Details |
|---|---|---|
| From wide to long format | <pre lang='python'>data.melt(id_vars='sex', value_vars=['a', 'b']) | |
| To narrow format | <pre lang='python'>data.explode(?) | ? |
| Merge two data frames on the sorted key | <pre lang='python'>data.merge(data2) | |
| Inner join | <pre lang='python'>data.join(data2, on = ['sex', 'country']) | |
| Left join | <pre lang='python'>data.join(data2, on = ['sex', 'country'], how = 'left') | |
| Right join | <pre lang='python'>data.join(data2, on = ['sex', 'country'], how = 'right') | |
| Outer join | <pre lang='python'>data.join(data2, on = ['sex', 'country'], how = 'outer') | |
| Cross join | <pre lang='python'>data.join(data2, on = ['sex', 'country'], how = 'cross') | |
| Semi join (one match per index) | <pre lang='python'>data.join(data2, on = ['sex', 'country'], how = 'semi') | |
| Anti join (exclude matches from table 2) | <pre lang='python'>data.join(data2, on = ['sex', 'country'], how = 'anti') | |

# Convert
| What | How | Details |
|---|---|---|
| To list of series | <pre lang='python'>data.get_columns() | |
| Split into list of data frames based on column | <pre lang='python'>data.partition_by('sex') | |
| Split into list of data frames based on column tuples | <pre lang='python'>data.partition_by('sex', 'country') | |
| Split into dict of data frames based on column(s) | <pre lang='python'>data.partition_by('sex', 'country', as_dict = True) | |
| To CSV file | <pre lang='python'>data.write_csv('derp.csv') | |
| To Parquet file | <pre lang='python'>data.write_parquet('derp.parquet') | |
| To JSON | ? | |
