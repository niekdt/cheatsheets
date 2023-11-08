---
layout: default
title: Date & time
parent: Python
nav_order: 1.9
---

# Date & time
{: .no_toc}

- TOC
{:toc}

## Create

| What | How | Details |
|---|---|---|
| Define date | `datetime.date(year, month, day)` | |
| Define time | `datetime.time(hour, minute, second)` | |
| Define datetime | `datetime.datetime(year, month, day, hour, minute, second)` | |
| Current date | `datetime.now().date()` | |
| Current time | `datetime.now().time()` | |
| Current datetime | `datetime.now()` | |
| Current datetime in UTC timezone | `datetime.now(timezone.utc)` | |
| Date from any valid [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date string | `date.fromisoformat(date_string)` | e.g., `2023-01-30` or `20230130` |
| Time from any valid [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) time string | `datetime.time.fromisoformat(time_str)` | e.g. `23:59:01` |
| Datetime from any valid [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime string | `datetime.datetime.fromisoformat(datetime_str)` | e.g. `2023-01-30 23:59`, `2023-01-30T23:59:01` |
| Date from YYYY-MM-DD string | `datetime.strptime(datetime_str, '%y-%m-%d')` | |
| Date from DD-MMM-YYYY string | `datetime.strptime(datetime_str, '%d-%b-%y')` | |
| Datetime from YYYY-MM-DD HH\:mm:ss | `x.strptime('%y-%m-%d %H:%M:%S')` | |
| Datetime from string (unknown format) | `pandas.to_datetime('2023 Jan 5')` | |
| Date from timestamp _f_ (float) | `date.fromtimestamp(f)` | |

## Extract

| What | How | Details |
|---|---|---|
| Year | `x.year` | |
| Month | `x.month` | |
| Day | `x.day` | |
| Hour | `x.hour` | |
| Minute | `x.minute` | |
| Second | `x.second` | |
| Microsecond | `x.microsecond` | |
| Weekday number | `x.isoweekday()` | Mon=1, Sun=7 |
| Weekday number (zero-based) | `x.weekday()` | Mon=0, Sun=6 |

# Test
| What | How | Details |
|---|---|---|
| Same moment | `x == y` | Up to `x.resolution` precision (usually 1μs) |
| Happens before _y_ | `x < y` | |
| Happens after _y_ | `x > y` | |

## Difference

| What | How | Details |
|---|---|---|
| Difference between dates | `x - y` | `timedelta` object |
| Difference between dates, in whole days | `(x - y).days` | |
| Difference between dates, in seconds | `(x - y).total_seconds()` | |

## Derive

| What | How | Details |
|---|---|---|
| Change to first day of year | `x.replace(month=1, day=1)` | |
| Change to first day of month | `x.replace(day=1)` | |
| Change year to _y_ | `x.replace(year=y)` | |
| In UTC timezone | `datetime.now(timezone.utc)` | |
| Shift forward by _n_ days | `x + timedelta(days=n)` | |
| Shift forward by _n_ seconds | `x + timedelta(seconds=n)` | |
| Shift forward by _n_ days, _m_ hours | `x + timedelta(days=n, hours=m)` | |

## Convert

| What | How | Details |
|---|---|---|
| Timestamp (float) | `x.timestamp()` | |
| Named tuple of  | `x.timetuple()` | |
| Format date as [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | `x.isoformat()` | e.g., `2023-01-01` |
| Format time as [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | `x.isoformat()` | e.g., `23:59:00` |
| Format datetime as [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | `x.isoformat()` | e.g., `2023-01-01T23:59:00` |
| Format readable datetime of consistent length | `x.ctime()` | e.g., `Sun Jan  1 23:59:00 2023` | 
| Format datetime as YYYY-MM-DD | `x.date().isoformat()` | e.g., `01-Jan-2023` |
| Format datetime as DD-MMM-YYYY | `x.strftime('%d-%b-%Y')` | e.g., `01-Jan-2023` |
| Format datetime as HH\:mm | `x.strftime('%H:%M')` | e.g., `23:59` |
| Format datetime as HH\:mm:ss | `x.strftime('%H:%M:%S')` | e.g., `23:59:00` |
| Format datetime as YYYY-MM-DD HH\:mm:ss | `x.strftime('%y-%m-%d %H:%M:%S')` | |
