# youtube.com/watch?v=JG1livF44_E


class Car:
  def __init__(self, brand: str) -> None:
    self.brand = brand

volvo: Car = Car(brand='Volvo')
print(volvo)
print(volvo.brand)
# print(volvo.fuel_type)  # AttributeError: 'Car' object has no attribute 'fuel_type'
# volvo.drive() # AttributeError: 'Car' object has no attribute 'drive'

import math
# import nothing  # ModuleNotFoundError: No module named 'nothing'


names: list[str] = ['John', 'Tom']
numbers: tuple[int, ...] = (1,2,3,4,5)

print(names[1])
# print(names[2])   # IndexError: list index out of range
print(numbers[3])
# print(numbers[8])   # IndexError: tuple index out of range


data: dict[str: str] = {
  'name': 'John',
  'job': 'looking for',
  'skill': 'don\'t know'
}
print(data['job'])
# print(data['salary']) # KeyError: 'salary'
print(data.get('salary', 'N/A'))


# print(var_not_defined)  # NameError: name 'var_not_defined' is not defined

def some_func() -> None:
  score = 10

# print(score)  # NameError: name 'var_not_defined' is not defined


def new_function() -> None :
  pass

new_function()


# def new_function() -> None :
#   raise NotImplementedError('Not yet completed!!!')

# new_function()


import typing as typ

def number_generator() -> typ.Generator[int, None, None]:
  for _ in range(2):
    yield _

my_gen: typ.Generator[int, None, None] = number_generator()
print(next(my_gen))
print(next(my_gen))
# print(next(my_gen)) # StopIteration


# SyntaxError

# IndentationError


# ValueError    TypeError

print(int('10'))
# print(int('ten')) # ValueError

# print(int(['1', '2'])) # TypeError
# print(int(None)) # TypeError