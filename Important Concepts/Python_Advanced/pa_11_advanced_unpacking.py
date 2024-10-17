# https://www.youtube.com/watch?v=6ViGc5NgdSw&t=19s

# %% Basic Unpacking
# Basic Unpacking
a, b, c = [1, 2, 3]
print(f'a:{a}, b:{b}, c:{c}')

a, b, c = 'ABC'
print(f'a:{a}, b:{b}, c:{c}')

# a, b, c = 'ABCD'  # ValueError: too many values to unpack (expected 3)
# print(f'a:{a}, b:{b}, c:{c}')

a, b, *c = 'ABCDEF'
print(f'a:{a}, b:{b}, c:{c}')

a, *b, c = 'ABCDEF'
print(f'a:{a}, b:{b}, c:{c}')

_, _, c = 'ABC'
print(f'_:{_}, _:{_}, c:{c}')

# %% Unpacking Nested Structures
# Unpacking Nested Structures
data = ('Person1', (45, 'DA/DE'))
# name, age, profession = data #ValueError: not enough values to unpack (expected 3, got 2)
name, (age, profession) = data
print(f'name:{name}, age:{age}, profession:{profession}')

# %% Unpacking in Functions
# Unpacking in Functions
def print_names(names):
  for name in names:
    print(name)

print_names(['P1', 'P2', 'P3'])
# print_names('P1', 'P2', 'P3') #TypeError: print_names() takes 1 positional argument but 3 were given

def print_names(*names):
  for name in names:
    print(name)

print_names(['P1', 'P2', 'P3'])
print_names('P1', 'P2', 'P3') #TypeError: print_names() takes 1 positional argument but 3 were given

# %% Combining Lists with Unpacking
# Combining Lists with Unpacking
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [*lst1, *lst2]
print(lst3)
print(*lst3)
# %% Unpacking Dictrionaries
# Unpacking Dictrionaries
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
dict3 = {**dict1, **dict2}
print(dict3)
# print(**dict3)  #TypeError: 'a' is an invalid keyword argument for print()

# %% Swapping Variables
# Swapping Variables
x, y = 10, 20
print(f'x:{x} & y:{y}')
x, y = y, x
print(f'x:{x} & y:{y}')