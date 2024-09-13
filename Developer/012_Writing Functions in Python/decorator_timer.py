# Add a decorator that will make timer() a context manager
import contextlib
import time

@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)

# %%

def sleep_n_seconds(n=1):
    '''
    sleep_n_seconds: Pause processing for n seconds.

    Parameters
    ----------
    n : int, optional
        The number of seconds to pause for, by default 1
    '''
    time.sleep(n)
# %%
print(sleep_n_seconds.__doc__)
# %%

def timer(func) :
    '''A decorator that prints how Long a function took to Run'''
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start
        print(f'{func.__name__} took {t_total}s')
        return result
    return wrapper
# %%

@timer
def sleep_n_seconds(n=1):
    '''
    sleep_n_seconds: Pause processing for n seconds.

    Parameters
    ----------
    n : int, optional
        The number of seconds to pause for, by default 1
    '''
    time.sleep(n)
# %%
print(sleep_n_seconds.__doc__)
print(sleep_n_seconds.__name__)
# %%
from functools import wraps

def timer(func) :
    '''A decorator that prints how Long a function took to Run'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start
        print(f'{func.__name__} took {t_total}s')
        return result
    return wrapper
# %%

@timer
def sleep_n_seconds(n=1):
    '''
    sleep_n_seconds: Pause processing for n seconds.

    Parameters
    ----------
    n : int, optional
        The number of seconds to pause for, by default 1
    '''
    time.sleep(n)
# %%
print(sleep_n_seconds.__doc__)
print(sleep_n_seconds.__name__)
# %%
