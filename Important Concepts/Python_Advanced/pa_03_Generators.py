# %%    Sequence 1 to 9,000,000
import sys
import pa_02_Decorators as dec

@dec.timer
def range_func():
  lst = [_ for _ in range(1, 9000001)]
  print(sys.getsizeof(lst))

range_func()

# %% with generator

@dec.timer
def generator_func():
  for _ in range(1, 9000001):
    yield _

gen_obj = generator_func()
print(sys.getsizeof(gen_obj))