class Wizard:
    def __init__(self, name) -> None:
        if not name:
            raise ValueError('Missing Name')
        self.name = name
    
    def __str__(self) -> str:
        return f'{self.name} a Wizard'
    
    @classmethod
    def get_input(cls, val) -> str:
        return input(f'Enter your {val}: ').strip()
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Missing Name')
        else:
            self._name = name

class Student(Wizard):
    def __init__(self, name, house, patronus=None) -> None:
        super().__init__(name)
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
    def house(self) -> str:
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid house')
        else:
            self._house = house

    @classmethod
    def get(cls) -> str:
        return cls(cls.get_input('name'), cls.get_input('house'), cls.get_input('patronus'))

class Professor(Wizard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject
    
    def __str__(self) -> str:
        return f'{self.name} Wizard and Professor of {self.subject}'
    
def main():
    wizard = Wizard('Albus')
    prof = Professor('Severus', 'Defense Against the Dark Arts')
    student = Student.get()
    print(wizard)
    print(prof)
    print(student)


if __name__ == '__main__':
    main()