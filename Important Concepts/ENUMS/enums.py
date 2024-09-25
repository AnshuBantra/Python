import enum
import typing as typ
import collections as col

class Color(enum.Enum):
  RED: str = 'R'
  BLUE: str = 'B'
  GREEN: str = 'G'

lst = ['Color("R")', 'Color.RED', 'repr(Color.RED)', 'Color.RED.name', 'Color.RED.value']
def enum_general_use() -> None:
  for _ in lst:
    print(f'{_:16} {eval(_)}')

def create_product(color: Color) -> None:
  match color:
    case Color.RED:
      print(f'A {color.name} coloured product is being generated')
    case Color.BLUE:
      print(f'A {color.name} coloured product is being generated')
    case Color.GREEN:
      print(f'A {color.name} coloured product is being generated')
    case _:
      print(f'{color} not found!!!')

typ.Iterable

enum_general_use()
print('--------------------------------')

create_product(Color.BLUE)
create_product('PINK')
print('--------------------------------')

class Colors(enum.Flag):
  RED : int = enum.auto()
  BLUE : int = enum.auto()
  BLACK : int = enum.auto()
  YELLOW : int = enum.auto()
  GREEN : int = enum.auto()

cool_colors: Colors = Colors.RED | Colors.BLUE | Colors.GREEN | Colors.YELLOW

for _ in cool_colors:
  print(_)
print('--------------------------------')

new_color: Colors = Colors.BLUE | Colors.YELLOW
print(new_color)
print(new_color.value)
print('--------------------------------')


# import pandas as pd

# def isodd(num):
#   return int(num)%2 == 1 if num != None else False

# def textjoin(row, lst):
#   lst.append(''.join(row.apply(lambda x: str(x))))
#   lst.append(''.join(row[::-1].apply(lambda x: str(x))))

# def dfjoin(df):
#   row, col = df.shape
#   lst = []
#   lst.extend( textjoin(df.iloc[_,:], lst) for _ in range(0, row, 1) )
#   lst.extend( textjoin(df.iloc[:,_], lst) for _ in range(0, col, 1) )
#   return lst

# df = pd.DataFrame({0:[2,4], 1:[3,5]})
# print(', '.join([*(filter(isodd, dfjoin(df)))]))