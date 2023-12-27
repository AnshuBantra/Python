# %%        # SETS
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
for student in students:
    if student['house'] not in houses:
        houses.append(student['house'])

for house in sorted(houses):
    print(house, end=', ')

houses = set()
for student in students:
    houses.add(student['house'])

for house in sorted(houses):
    print(house, end=', ')

# %%        # GLOBAL & LOCAL VARIABLES
balance = 0

def main():
    print(f'Balance: {balance}')
    deposit(100)
    withdraw(50)
    print(f'Balance: {balance}')

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == '__main__':
    main()
# %%        # Global & Local Variables using OOP
class Account():
    def __init__(self) -> None:
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account= Account()
    print(f'Balance: {account.balance}')
    account.deposit(100)
    account.withdraw(50)
    print(f'Balance: {account.balance}')

if __name__ == '__main__':
    main()
# %%        # MEOWS
class Cat:
    MEOWS = 3

    @classmethod
    def meow(self):
        for _ in range(self.MEOWS):
            print('meow')

Cat.meow()
# %%
def meow(n: int):
    for _ in range(n):
        print('meow')

num = input('Number: ')
meow(num)
# %%
