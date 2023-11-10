---
layout: default
title: Pandas
parent: Python
nav_order: 151
---

# Pandas (WIP)
Pandas.DataFrame seems to be the MS Excel of the Python data processing universe. Slow, write-once, inconsistent API, and many ways to achieve the same thing (the true pythonic way), but useful for quick & dirty data manipulation and popular for that reason.

Words of caution:

* Index columns are not usable as data. Don't bother with index columns unless you want to polute your code with many `reset_index()` calls.
* MultiIndex versus multiple indices. Just don't. If you cared about speed you would not be using pandas anyway.
* Complex queries will be a series of data variable updates, which is hard to read, and guaranteed to lead to bugs at a later stage during refactoring.

{: .no_toc}

1. TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| Empty | ? | |
| Single column from list | `DataFrame([1, 2, 3])` | |
| Column per dictionary entry | `dict = {'Name': ['John', 'Sue'], 'Age': [40, 35]}`<br>`DataFrame(dict)` | |
| Numpy 2D array | `arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`<br>`DataFrame(arr, columns = ['a', 'b', 'c'])` | |

## Properties

| What | How | Details |
|---|---|---|
| Column names (list) | `list(data)` | |
| Column names (set) | `set(data)` | |
| Columns (index object) | `data.columns` | |
| Row names | `data.index` | |
| Number of columns | `len(data.columns)` | |
| Number of columns | `data.shape[1]` | |
| Number of rows | `len(data)` | |
| Number of rows | `data.shape[0]` | |
| Number of cells | `data.size` | |
| Dimensions (tuple) | `data.shape` | |


## Query

| What | How | Details |
|---|---|---|
| Select column | `data[['Name']]` | |
| Select columns | `data[['Name', 'Age']]` | |
| Cell at row _i_, col _j_ | `data.at[i, j]` | |
| First row (Series) | `data.iloc[0]` | |
| First _n_ rows | `data.head(n)` | |
| Last _n_ rows | `data.tail(n)` | |
| Row by row number _i_ | `data.iloc[i]` | |
| Row by index _i_ | `data.loc[i]` | |
| String query | `data.query(...)` | |

## Test

| What | How | Details |
|---|---|---|
| Empty | `data.empty` | |
| Has column _col_ | `col in data` | |
| Has columns _cols_ | `set(cols).issubset(data)` | |
| Has columns _cols_ | `data.columns.isin(cols).all()` | |
| Only contains columns _cols_ | `set(data) == set(cols)` | |
| Has any of these columns _cols_ | `data.columns.isin(cols).any()` | |
| Has any of these columns _cols_ | `set(data).issuperset(cols)` | |
| Does not have these columns _cols_ | `set(cols).isdisjoint(data)` | |
| Column _col_ is boolean type | `pandas.api.types.is_bool_dtype(data[col])` | |
| Column _col_ is string type | `pandas.api.types.is_string_dtype(data[col])` | |
| Column _col_ is numeric type | `pandas.api.types.is_numeric_dtype(data[col])` | |
| Column _col_ is integer type | `pandas.api.types.is_integer_dtype(data[col])` | |
| Column _col_ is datetime type | `pandas.api.types.is_datetime64_dtype(data[col])` | |
| Column _col_ is datetime type | `data.dtypes[col] == numpy.dtype('datetime64[ns]'))` | |
| Column _col_ contains missing value | `data[col].isna().values.any()` | |
| Column _col_ contains no missing values | `data[col].notnull().values.all()` | |
| Multiple columns _cols_ contain no missing values | `data[['col1', 'col2']].notnull().all().all()` | |

## Update
All operations are in-place.

| What | How | Details |
|---|---|---|
| Rename column | `data.rename(columns={'old': 'new'}, inplace=True)` | |
| Rename multiple columns | `data.rename(columns={'old1': 'new1', 'old2': 'new2'}, inplace=True)` | |
| Rename columns dynamically | `data.rename(columns=dict(zip(oldNames, newNames)), inplace=True)` | Ugh |
| All columns to lowercase | `data.rename(str.lower, axis='columns', inplace=True)` | |
| Set cell at row _i_, col _j_ to value _v_ | `data.at[i, j] = v` | |
| Replace missing values for _v_ | `data.fillna(v)` | |
| Replace specific values | `data.replace(?)` | | 


## Derive
All operations create a new instance.

| What | How | Details |
|---|---|---|
| Rename column | `data.rename(columns={'old': 'new'})` | |
| Rename multiple columns | `data.rename(columns={'old1': 'new1', 'old2': 'new2'})` | |
| Rename columns dynamically | `data.rename(columns=dict(zip(oldNames, newNames)))` | Ugh |
| All columns to lowercase | `data.rename(str.lower, axis='columns')` | |
| Mask for NaNs | `data.isnull()` | |
| Mask for NaNs | `data.isna()` | |
| Mask for non-missing values | `data.notnull()` | |
| Mask for non-missing values | `data.notna()` | |
| Mask for duplicates | `data.duplicated()` | |

## Shrink

| What | How | Details |
|---|---|---|
| Pop row | `data.pop()` | |
| Drop rows list _rows_ | `data.drop(rows)` | |
| Drop duplicated rows | `data.drop_duplicates()` | |
| Drop duplicated columns | ? | |
| Drop column _col_ | `data.drop(columns=col)` | |
| Drop columns list _cols_ | `data.drop(columns=cols)` | |
| Drop rows with a missing value in any column | `df.dropna()` | |
| Drop rows with a missing value in the given columns list _cols_ | `df.dropna(subset=cols)` | |
| Drop rows with at least _n_ non-missing values across columns | `df.dropna(thresh=n)` | |
| Drop rows with missing values in every column | `df.dropna(how='all')` | |
| Drop columns with a missing value in any row | `data.dropna(axis='columns')` | |


## Grow

| What | How | Details |
|---|---|---|
| Append column | ? | |
| Append columns | ? | |
| Insert column | `data.insert(x)` | |
| Insert columns | ? | |

## Reshape

| What | How | Details |
|---|---|---|
| Melt | `data.melt(?)` | |
| Dcast | `data.explode(?)` | |
| Transpose | `data.T` | |


## Iterate 

| What | How | Details |
|---|---|---|
| Over rows (index, series) | `for i, row in data.iterrows():` | |
| Over rows (as tuples) | `for row in data.itertuples():` | |
| Over rows (col, series) | `for col, row_series in data.items():` | |
| Over columns (lists) | `for col in data.columns:` | |

## Convert

| What | How | Details |
|---|---|---|
| Numpy 2D array | `data.values` | |
