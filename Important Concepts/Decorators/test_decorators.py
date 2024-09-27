import decorators_ as dec

# @dec.timer_simple
# def open_txt(path: str) -> int:
#   """Function to open a file and returns number of lines contained in the file

#   Args:
#       path (str): path & filename of the file

#   Returns:
#       int: number of rows in the file
  
#   >>> open_txt('file_with_3_lines.txt')
#     3
#   """
#   counter: int = 0
#   with open(path, 'r') as file:
#     for _ in file:
#       counter += 1
#   # print(func.__doc__)
#   return counter

# print(open_txt(r'../Data/AI.txt'))

@dec.timer_advanced
def open_txt(path: str) -> int:
  """Function to open a file and returns number of lines contained in the file

  Args:
      path (str): path & filename of the file

  Returns:
      int: number of rows in the file
  
  >>> open_txt('file_with_3_lines.txt')
    3
  """
  counter: int = 0
  with open(path, 'r') as file:
    for _ in file:
      counter += 1
  return counter

print(open_txt(r'../Data/AI.txt'))

print(open_txt(r'../Data/The_Tempest.txt'))

# import requests
# url = r'https://www.gutenberg.org/files/1801/1801.txt'
# response = requests.get(url)
# content=response.text
# with open('the_tempest.txt', 'w') as file:
#   file.write(content)
#   print('File saved!!!')
# # print(open_txt(content))