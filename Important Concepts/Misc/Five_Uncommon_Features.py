#  https://www.youtube.com/watch?v=sQ1Q96-Vhjk
#%% Slice Type Variable

numbers: list[int] = list(range(1,11))
text: str = 'Hello, world!'
rev: slice = slice(None, None, -1)
first_five: slice = slice(None, 5)

print(numbers[rev])
print(text[rev])

print(numbers[first_five])
print(text[first_five])

# %%  Sets Methods

set_a: set[int] = {1, 2, 3, 4, 5}
set_b: set[int] = {4, 5, 6, 7, 8, 9}

print(set_a | set_b) # Join sets
print(set_a - set_b) # Subtract 2nd set from 1st set
print(set_a & set_b) # Common elements
print(set_a ^ set_b) # Unique elements from both sets
# %%    f string formatter for classes

import typing as tp

class Book:
  def __init__(self, title: str, pages: int) -> None:
    self.title = title
    self.pages = pages
  
  def __format__(self, format_spec: tp.Any) -> str:
    match format_spec:
      case 'time':
        return f'{self.pages / 60:2f}h'
      case 'caps':
        return self.title.upper()
      case _:
        raise ValueError('Unknown specifier for Book()')
  
hairy_potter: Book = Book('A Very Hairy Potter', 400)
python_daily: Book = Book('Python Daily', 20)

print(f'{hairy_potter:caps}')
print(f'Time to read it ==> {hairy_potter:time}')

print(f'{python_daily:caps}')
print(f'Time to read it ==> {python_daily:time}')

 #%%  Walrus Operator

users = {0:'Bob', 1:'Mario'}

if user := users.get(0):
  print(f'{user} exists')
else:
  print(f'Code does not exist!')

def get_info(text: str) -> dict:
  return {
    'words' : (words := text.split()),
    'word_count': len(words),
    'character_count': len(''.join(words))
  }

print( get_info('Bob') )
print( get_info('Hello How are you') )
# %% Currying

import typing as tp

def multiply_setup(a: float) -> tp.Callable:
  def multiply(b: float) -> float:
    return a*b
  return multiply

double: tp.Callable = multiply_setup(2)
triple: tp.Callable = multiply_setup(3)

print(double(4))
print(triple(4))

# %%
