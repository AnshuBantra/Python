# %% [Course Links]

#   https://endeavourgroup.udemy.com/course/rest-api-flask-and-python/learn/lecture/5960054#overview
#   https://rest-apis-flask.teclado.com/docs/course_intro/
#   https://github.com/tecladocode/python-refresher

#   https://blog.teclado.com/how-to-set-up-visual-studio-code-for-python-development/

# %%
for char in "Hello Python":
    if char in ["a", "e", "i", "o", "u"]:
        print(f"{char} => Vowel")
    else:
        if char.isupper():
            print(f"{char} is Upper")
        else:
            print(char)

# %%

#   https://blog.teclado.com/python-formatting-numbers-for-printing/
#   https://docs.python.org/3/library/string.html#format-specification-mini-language

x = 4863.4343091

print(f"{x:.6}")
print("{:.6}".format(x))

print(f"{x:.3}")
print(f"{x:.3f}")

print(f"{x:,.2f}")

score = 23
total = 30
print(score / total)
print(f"{score/total:.2%}")
# %%
# User Input

name = input("Enter your name: ")
print(name)

size_input = input("How big is your house (Sq. Feet)")
size_input = float(size_input)
print(f"{size_input:.2f} Sq.Feet = {size_input / 10.8:.2f} Sq.Meters")
# %%
#   First Python App
age = int(input("Enter your age : "))
months = age * 12
print(f"Your age is {age}, which calculates to {months} months")
# %%
#   Lists, Tuples & Sets
lst = ["Bob", "Rolf", "Anne"]
tpl = ("Bob", "Rolf", "Anne")
s3t = {"Bob", "Rolf", "Anne"}

#   https://blog.teclado.com/python-set-operators/
#   https://blog.teclado.com/python-symmetric-difference/
set_1 = {1, 2, 3, 4, 5}
set_2 = {3, 4, 5, 6, 7}
set_3 = {5, 6, 7, 8, 9}

# Combine set_1 and set_2
print(set_1.union(set_2))
print(set_1 | set_2)
print(set_1 | set_2 | set_3)

# Find common elements in set_1 and set_2
print(set_1.intersection(set_2))
print(set_1 & set_2)

# Find elements in set_1 which are not in set_2
print(set_1.difference(set_2))
print(set_1 - set_2)
print(set_2.difference(set_1))
print(set_2 - set_1)

print(set_1.symmetric_difference(set_2))

# %%
#   https://teclado.com/30-days-of-python/

# %%
tup = 1, 2, 3
type(tup)
# %%
#   BOOLEANS
print(5 == 5)

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
abroad2 = friends.copy()
abroad3 = friends

print(friends == abroad)
print(friends is abroad)
print(friends is abroad2)
print(friends is abroad3)

# %%
# IF

day_of_week = input("What day of the week is it today? ").capitalize()

if day_of_week == "Monday":
    print(f"Today is {day_of_week}! Have a great start to your week.")
elif day_of_week == "Tuesday":
    print(f"It is {day_of_week}, already!")
else:
    print(f"It's {day_of_week}; Full speed ahead!")

# %%
#   IN Keyword

friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends)

movies_watched = {"Matrix", "Croods", "50 First Dates"}
print("Croods" in movies_watched)

# %%

# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

# %%
print(evens)
# %%
# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")

# %%
#   LIST COMPREHENSION

lst1 = [1, 2, 3, 4]
lst2 = [num * 2 for num in lst1]

print(lst1, lst2)

friends = ["Sam", "Rolf", "Samantha", "Jen", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)

# %%
#   DICTIONARIES

dict_1 = {"Rolf": 30, "Bob": 26, "Anne": 23}

print(dict_1.items())
print(dict_1.keys())
print(dict_1.values())

print(list(dict_1))
print(list(dict_1.values()))

# %%
# DESTRUCTING (UNPACKING) IN PYTHON
#   https://blog.teclado.com/destructuring-in-python/

x, y = 5, 11
print(x, y)

x, y = (5, 11)
print(x, y)

my_dict = {"name": "Bob", "age": 25}
x, y = my_dict
print(x, y)

my_dict = {"name": "Bob", "age": 25}
x, y = my_dict.values()
print(x, y)

example_list = ["A", "B", "C"]
for counter, letter in enumerate(example_list):
    print(counter, letter)

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person = ("Bob", 42, "Mechanic")
name, _, profession = person
print(name, profession)

head, *tail = [1, 2, 3, 4, 5]
print(head, tail)

*head, tail = [1, 2, 3, 4, 5]
print(head, tail)

head, *middle, tail = [1, 2, 3, 4, 5]
print(head, middle, tail)

first, second, third, *rest = [1, 2, 3, 4, 5]
print(first, second, third, rest)

# %%
#   FUNCTIONS


def hello():
    print("Hello :-)")


hello()


def add(x=0, y=0):
    return x + y


print(add())
print(add(5, y=7))
# print(add(x=5,7))     # SyntaxError: positional argument follows keyword argument


# Complete the function by making sure it returns 42. .
def return_42():
    return 42
    pass  # 'pass' just means "do nothing". Make sure to delete this!


print(return_42())


# """Create a function below, called my_function, that takes two arguments
#  and returns the result of its two arguments multiplied together."""
def multiply(a=0, b=0):
    return a * b


print(multiply())
print(multiply(1))
print(multiply(2, 3))

# %%
#   LAMBDA FUNCTIONS

add = lambda x, y: x + y
print(add(2, 3))

print((lambda x, y: x + y)(2, 3))


def double(x):
    return x * 2


seq = [1, 3, 5, 9]
doubled = [double(x) for x in seq]
print(doubled)

doubled = list(map(double, seq))
print(doubled)

print(list(map(lambda x: x * 2, seq)))

# %%
#   DISCTIONARY COMPREHENSION

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)

# %%
# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)}

print(student)

for key, value in student.items():
    print(f"Key({key}):Value({value})")


# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)


# print(average_grade(student))


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])

    return total / count


# %%
#   UNPACKING KEYWORD ARGUMENTS


def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)


def named(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}
# named(details)
named(details, 25)
named(**details)


def named(**kwargs):
    print(kwargs)


details = {"name": "Bob", "age": 25}
# named(details)
named(**details)

# %%
#   OBJECT ORIENTED PROGRAMMING


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


stu_1 = Student("Rolf", (90, 90, 93, 78, 90))
print(stu_1.name, stu_1.grades)
print(stu_1.average())

stu_2 = Student("Bob", (100, 98, 93, 88, 90))
print(stu_2.name, stu_2.grades)
print(stu_2.average())
print(stu_2)


#   OBJECT ORIENTED PROGRAMMING
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # def __str__(self) -> str:
    #     return f"'{self.name}' is {self.age} years old."

    def __repr__(self) -> str:
        return f"<'{self.name}' is {self.age} years old.>"


p1 = Person("Bob", 25)
print(p1)


# %%
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        return sum([item["price"] for item in self.items])


sto = Store("A1")
sto.add_item("b", 25)
sto.add_item("c", 10)
print(sto.items)
sto.stock_price()


# %%
class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    def __str__(self) -> str:
        return "Class ClassTest"

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method.")


test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()


# %%
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __str__(self) -> str:
        return f"Name:{self.name}, Type:{self.book_type}, Weight:{self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)

print(book.name)

hcb = Book.hardcover("Harry Potter", 1500)
pbb = Book.paperback("Python 101", 600)

print(hcb)
print(pbb)


# %%
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item["price"]
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def store_details(cls):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return f"{cls.name}, total stock price {cls.stock_price()}"


s1 = Store("test")

s2 = Store("corner")
s2.add_item("KB", 120)

print(Store.franchise(s1))
print(Store.store_details(s1))

print(Store.franchise(s2))
print(Store.store_details(s2))

# %%
#   CLASS INHERITANCE


class Device:
    def __init__(self, name, connected_by) -> None:
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self) -> str:
        return f"Device {self.name} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


printer = Device("Printer", "USB")
print(printer)
printer.disconnect()


class Printer(Device):
    def __init__(self, name, connected_by, capacity) -> None:
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remainin_pages = capacity

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.remainin_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remainin_pages -= pages


p1 = Printer("Printer", "USB", 500)
print(p1)
p1.print(20)
print(p1)
p1.disconnect()
p1.print(30)

# %%
#   CLASS COMPOSITION


class Bookshelf:
    def __init__(self, quantity) -> None:
        self.quantity = quantity

    def __str__(self) -> str:
        return f"Bookshelf with capacity {self.quantity}"


shelf = Bookshelf(300)


class Book(Bookshelf):
    def __init__(self, name, quantity) -> None:
        super().__init__(quantity)
        self.name = name


book = Book()

# %%

#   Type Hinting


def list_avg(seq: list) -> float:
    return sum(seq) / len(seq)


list_avg([1, 2, 3])

# %%
#   IMPORTING IN PYTHON
from mymodule import divide

print(divide(45, 9))

# %%
#   ERRORS IN PYTHON

try:
    ___
except:
    ___
else:
    ___
finally:
    ___

# %%
#       FIRST CALSS FUNCTIONS


def calculate(*nums, operator):
    return operator(nums)


print(calculate(2, 3, 4, 5, 6, operator=sum))

# %%

#   DECORATORS

import functools

user = {"username": "Anshu", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password():
    return "12345"


@make_secure
def get_user_name():
    return user["username"]


print(get_admin_password(), get_admin_password.__name__)
print(get_user_name(), get_user_name.__name__)
# %%

# DECORATORING FUNCTIONS WITH PARAMETERS

import functools

user = {"username": "Anshu", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


@make_secure
def get_admin_password(panel):
    if panel == "admin":
        return "12345"
    elif panel == "billing":
        return "super_secure_password"


@make_secure
def get_user_name():
    return user["username"]


print(get_admin_password("admin"), get_admin_password.__name__)
print(get_user_name(), get_user_name.__name__)

# %%

# DECORATORS WITH PARAMETERS
import functools

user = {"username": "Anshu", "access_level": "guest"}


def dec(access_level):
    def make_secure(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No admin permissions for {user['username']} - {access_level}."

        return secure_function

    return make_secure


@dec("admin")
def get_admin_password():
    return "admin: 12345"


@dec("user")
def get_user_password():
    return "user: user_password"


print(get_admin_password(), get_admin_password.__name__)
print(get_user_password(), get_user_password.__name__)
# %%

#   MUTABILITY IN PYTHON

str1 = "abcd"
print(str1)
# str1[1] = 'z'
print(str1)

a = []
b = a
print(a, b)
a.append(56)
print(a, b)

a = "Hi"
b = a
print(a, b)
a += " person"
print(a, b)
