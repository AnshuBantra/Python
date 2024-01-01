# # Step 1
# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f'{student.name} from {student.house}')

# def get_input(val) -> str:
#     return input(f'Enter your {val}: ').strip()

# def get_student() -> str:
#     student = Student()
#     student.name = get_input('name')
#     student.house = get_input('house')
#     return student

# if __name__ == '__main__':
#     main()

# # Step 2
# class Student:
#     def __init__(self, name, house, patronus=None) -> None:
#         self.name = name
#         self.house = house
#         self.patronus = patronus
    
#     def __str__(self) -> str:
#         return f'{self.name} from {self.house} ==> {self.charm()}'
    
#     def charm(self) -> str:
#         match self.patronus:
#             case 'Stag':
#                 return '🦒'
#             case 'Otter':
#                 return '🦫'
#             case 'Dog':
#                 return '🦊'
#             case _:
#                 return '🪄'
    
#     @property
#     def name(self) -> str:
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError('Missing Name')
#         else:
#             self._name = name
    
#     @property
#     def house(self) -> str:
#         return self._house
    
#     @house.setter
#     def house(self, house):
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError('Invalid house')
#         else:
#             self._house = house


# def main():
#     student = get_student()
#     print(student)

# def get_input(val) -> str:
#     return input(f'Enter your {val}: ').strip()

# def get_student() -> str:
#     student = Student(get_input('name'), get_input('house'), get_input('patronus'))
#     return student

# if __name__ == '__main__':
#     main()

class Student:
    def __init__(self, name, house, patronus=None) -> None:
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self) -> str:
        return f'{self.name} from {self.house} ==> {self.charm()}'
    
    def charm(self) -> str:
        match self.patronus:
            case 'Stag':
                return '🦒'
            case 'Otter':
                return '🦫'
            case 'Dog':
                return '🦊'
            case _:
                return '🪄'
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing Name')
        else:
            self._name = name
    
    @property
    def house(self) -> str:
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid house')
        else:
            self._house = house

    @classmethod
    def get_input(cls, val) -> str:
        return input(f'Enter your {val}: ').strip()

    @classmethod
    def get(cls) -> str:
        return cls(cls.get_input('name'), cls.get_input('house'), cls.get_input('patronus'))

def main():
    student = Student.get()
    print(student)

if __name__ == '__main__':
    main()