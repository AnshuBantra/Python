import decorators_ as dec

# @dec.timer
# def open_txt(path: str) -> None:
#   with open(path, 'r') as file:
#     for line in file:
#       print(line)

# open_txt(r'../Data/AI.txt')


def func1():
  print('Testing function 1')

func1_copy = func1

func1
func1()
func1_copy
func1_copy()

# del func1
# func1_copy()

print(func1)
print(func1_copy)