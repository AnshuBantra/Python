class Person:

  def __init__(self, name, age, gender) -> None:
    self.__name = name
    self.__age = age
    self.__gender = gender

  @property
  def Name(self):
    return self.__name

  @Name.setter
  def Name(self, name):
    self.__name = name

  def __str__(self) -> str:
    return f'{self.__name} is {self.__age} year old, {"Female" if self.__gender=='F' else "Male" }'
  
  @staticmethod
  def greeting():
    print(f'Hello and welcome to {Person.__name__}')

p = Person('P1', 35, 'F')
print(p)
p.name = 'Her'
print(p)
p.Name='Her'
print(p)
Person.greeting()