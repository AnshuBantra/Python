from abc import ABCMeta, abstractmethod, staticmethod

class IPerson(metaclass=ABCMeta):

  @abstractmethod
  @staticmethod
  def person_method(self):
    pass

p1 = IPerson()
p1.person_method()