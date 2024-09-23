# %%
# Simple Function
print('Simple Function')
def squared_numbers(lst):
  return [_*_ for _ in lst]

lst = range(5)
print(squared_numbers(lst))

# # %%
# Simple Generator
print('Simple Generator')
def squared_numbers(lst):
  for _ in lst:
    yield _*_

lst = range(5)
print(squared_numbers(lst))


# # %%
# Generator Comprehension
print('Generator Comprehension')
lst = (_*_ for _ in range(5))
print(squared_numbers(lst))