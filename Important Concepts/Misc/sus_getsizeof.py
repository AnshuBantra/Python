import sys

rng = range(10000)
print(sys.getsizeof(rng))

lst = [*rng]
print(sys.getsizeof(lst))