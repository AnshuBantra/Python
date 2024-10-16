# %% Simple Decorator
def decorator_func(func):

  def wrapper():
    print(f'I am decorating function {func.__name__} ==> {func.__doc__}')
    func()
  return wrapper

@decorator_func
def hello():
  """_summary_: Simple Hello Function
  """
  print( f'Hello')
  print()

# hello()

# %%  

def decorator_func(func):

  def wrapper(*args, **kwargs):
    print(f'I am decorating function {func.__name__} ==> {func.__doc__}')
    return func(*args, **kwargs)
  return wrapper

@decorator_func
def hello(person):
  """Simple Hello Function
  """
  return f'Hello {person}'

# print(hello('Anshu'))

# %%  Logging
import sys
import datetime as dtt

def logger(func):
  def wrapper(*args, **kwargs):
    return_val = func(*args, **kwargs)
    with open('logfile.txt', 'a+') as f:
      fname = func.__name__
      f.write(f'\nFunction {fname} callled at {dtt.datetime.now()} and returned value {return_val}')
    return return_val
  return wrapper

@logger
def add(x, y):
  return int(x)+int(y)

# %% Timing

import time

def timer(func):
  def wrapper(*args, **kwargs):
    before = time.time()
    func(*args, **kwargs)
    print(f'{func.__name__} took {time.time()-before} seconds to execute')
  return wrapper

@timer
def my_sleep_func(x: int):
  time.sleep(int(x))

def main():
  print(add(sys.argv[1], sys.argv[2]))
  my_sleep_func(sys.argv[1])

if __name__=='__main__':
  main()