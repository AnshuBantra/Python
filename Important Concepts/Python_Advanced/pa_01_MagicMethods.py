from typing import Any


class Person:

  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def __del__(self):
    print(f'Object {self.name} is being deconstructed')

p = Person('Mike', 25)

class Vector:

  def __init__(self, x, y) -> None:
    self.x = x
    self.y = y
  
  def __add__(self, other):
    return Vector(self.x+other.x, self.y+other.y)
  
  def __str__(self) -> str:
    return f'Vector with x={self.x} and y={self.y}'

  def __len__(self):
    return self.x+self.y
  
  def __call__(self, *args: Any, **kwds: Any) -> Any:
    print( f'Hello I was called {self}')
  
v1 = Vector(10, 20)
v2 = Vector(30, 40)
v3 = v1 + v2    # TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
print(v3)
v3()