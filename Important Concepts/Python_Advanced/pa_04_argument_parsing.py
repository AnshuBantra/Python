# %% python3 python_file_name arguments

def test_function(*args, **kwargs):
  print(args[0])
  print(args[1])
  print(args[2])
  print(kwargs['First'])
  print(kwargs['Second'])

# %% Get filename and message and write message to file
import sys

#Usage python_file filename message
def write_to(filename, message):
  with open(filename, 'a+') as f:
    f.write(message+'\n')

# %% with getopt

import getopt

def opt_args():
  filename = 'text.txt'
  message = ''
  opts, args = getopt.getopt(sys.argv[1:], 'f:m:', ['filename', 'message'])
  for opt, arg in opts:
    if opt == '-f':
      filename = arg
    elif opt == '-m':
      message = arg
  write_to(filename, message)

# %% Main
def main():
  # test_function('Hello', 77, True, First='1st', Second='2nd')
  # write_to(sys.argv[1], sys.argv[2])
  opt_args()

if __name__=='__main__':
  main()