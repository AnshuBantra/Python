# %%
def greet(person: str, age: int) -> str:
  """_summary_

  Args:
      person (str): Name of the person
      age (int): Age of the person

  Returns:
      str: Greeting message 

  =>:
    greet('Person 1', 35) ==> 'Hello Person 1, 35 is a nice age'
  """
  return f'Hello {person}, {age} is a nice age'

print(greet('Person 2', 45))


# %%
class Person:
  def __init__(self, name: str, age: int) -> None:
    self.name = name
    self.age = age

  def __repr__(self) -> str:
    return f'Person(name={self.name!r}, age={self.age})'

  def __str__(self) -> str:
    return f'{self.name} is {self.age} years old'

p = Person('Person1', 35)
print(p)
print(repr(p))