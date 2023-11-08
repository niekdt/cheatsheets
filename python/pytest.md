---
layout: default
title: Pytest
parent: Python
nav_order: 500
---

# Pytest
{: .no_toc}

1. TOC
{:toc}

## Assertions

| What | How | Details |
|---|---|---|
| Assert warning | `with pytest.warns(UserWarning):` | |
| Assert any error | `with pytest.raises(Exception) as excinfo:` | |
| Assert specific exception _e_ | `with pytest.raises(e) as excinfo:` | |
| Assert either exception _e1_ or _e2_ | `with pytest.raises((e1, e2)):` | |

## Conditional tests

| What | How | Details |
|---|---|---|
| Skip test | `@pytest.mark.skip(reason="no way to currently test this")` | |
| Conditional skip | `@pytest.mark.skipif(cond, reason)` | |
| Skip for Python version below _x.y_ | `@pytest.mark.skipif(sys.version_info < (x, y))` | |
| Skip if on Windows | `@pytest.mark.skipif(sys.platform == 'win32')` | |
| Skip if module is missing | `@pytest.importorskip('pandas')` | |
| Expect test to fail | `@pytest.mark.xfail()` | |
| Expect test to fail with exception _e_ | `@pytest.mark.xfail(raises=e)` | |
| Fail test if not completed within _n_ seconds | `@pytest.mark.timeout(n)` | |
| Fail test on Windows | `@pytest.mark.xfail(sys.platform == 'win32')` | |
| Parameterize test for argument _x_ | `@pytest.mark.parametrize('x', [1, 2, 3])` | |
| Parameterize test for multiple arguments | `@pytest.mark.parametrize('length', [1, 2, 3])`<br>`@pytest.mark.parametrize('value', [0, 1])` | |
| Parameterize for combination of arguments | `@pytest.mark.parametrize('length,value', [(1, 0), (2, 1), (3, 1)])` | |
| Parameterize using parameterized fixture | `@pytest.mark.parametrize('large_dynamic_data_file', ['big.csv', 'big2.csv'], indirect=True)` | |

## Within-test control flow 

| What | How | Details |
|---|---|---|
| Skip rest if module is missing | `docutils = pytest.importorskip("docutils")` | |

## Fixtures
Pytest caches fixtures within the defined scope (for the given parameters).

| What | How | Details |
|---|---|---|
| Define fixture | `@pytest.fixture`<br>`def first_entry():`<br>`return "a"` | |
| Define fixture with module scope | `@pytest.fixture(scope="module")` | |
| Define fixture with cleanup | Define clean-up after `yield` | |
| Define fixture for use in every test | `@pytest.fixture(autouse=True)` | |
| Disable GC for every test, collect in-between | `@pytest.fixture(autouse=True)`<br>`def cleanup():`<br>`    gc.collect()`<br>`    gc.disable()` | |
| Parameterized fixtures resulting in multiple tests | `@pytest.fixture(params=[1, 2, 3, 4, 5])`<br>`def number(request):`<br>`return request.param` | |
| Parameterized test using a parameterizable fixture | `@pytest.fixture`<br>`def tester(request):`<br>`return MyTester(request.param)`<br><br>`@pytest.mark.parametrize('tester', [['var1', 'var2']], indirect=True)`<br>`def test_tc1(self, tester):`<br>`tester.dothis()` | |


