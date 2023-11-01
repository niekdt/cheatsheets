def test_simple():
  assert 1 == 1
  # Expect exception
  with pytest.raises(ZeroDivisionError) as excinfo:
    1 / 0
  # Expect one of the defined exceptions
  with pytest.raises((ValueError, ZeroDivisionError)):
    1 / 0
  # Expect warning
  with pytest.warns(UserWarning):
        warnings.warn('caution!')

    
@pytest.mark.skip(reason='disabled')
def test_skip():
  assert 1 == 1
  

@pytest.importorskip('pandas')
def test_if_package_not_installed():
  data = pd.DataFrame()
  

@pytest.mark.skipif(sys.platform == 'win32', reason='on windows')
def test_skip_windows():
  assert 1 == 1
    
  
@pytest.mark.xfail()
def test_fail():
  raise Exception('error')

  
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_fail_div_by_zero():
  1 / 0
  

@pytest.mark.xfail(sys.platform == 'win32', reason='should fail on windows')
def test_fail_on_windows():
  assert 1 == 1


@pytest.mark.parametrize('length', [1, 2, 3])
def test_parameterized(length)
  a = [0] * length
  assert len(a) == length
  
  
@pytest.mark.parametrize('length', [1, 2, 3])
@pytest.mark.parametrize('value', [0, 1])
def test_parameterized_cartesian(length, value)
  a = [value] * length
  assert len(a) == length
  assert max(a) == value

  
@pytest.mark.parametrize('length,value', [(1, 0), (2, 1), (3, 1)])
def test_parameterized_paired(length, value)
  a = [value] * length
  assert len(a) == length
  assert max(a) == value

  
@pytest.mark.timeout(5)
def test_with_timeout():
  time.sleep(10)
  assert 1 == 1
  

@pytest.fixture
def data_frame():
  return pd.DataFrame(...)


@pytest.fixture(scope='session')
def large_data_file():
  return load_large_data_file()


@pytest.fixture(scope='session')
def large_dynamic_data_file(request):
  return load_large_data_file(path=request.param)


# Garbage collect upon every test and ensure GC is disabled
@pytest.fixture(autouse=True)
def cleanup():
    gc.collect()
    gc.disable()

    
# Test using a fixture
def test_dynamic_load_file(data_frame):
  assert isinstance(data_frame, pd.DataFrame)
    
    
# Test using a parameterized fixture
@pytest.mark.parametrize('large_dynamic_data_file', ['big.csv', 'big2.csv'], indirect=True)
def test_dynamic_load_file(large_dynamic_data_file):
  assert isinstance(large_dynamic_data_file, pd.DataFrame)
