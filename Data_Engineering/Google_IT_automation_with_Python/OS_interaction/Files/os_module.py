# os_module.py
# %%
import os
os.getcwd()
# %%
os.listdir()
# %%
os.path.exists('hello_world.py')
# %%
os.path.exists('hi.py')
# %%
os.path.getsize('C2M2L1_Reading_And_Writing_Files.ipynb')
# %%
os.path.getmtime('C2M2L1_Reading_And_Writing_Files.ipynb')
# %%
import datetime as dtt
dtt.datetime.fromtimestamp(os.path.getmtime('C2M2L1_Reading_And_Writing_Files.ipynb'))
# %%
import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    # print("File not found")
# %%
 dir = os.getcwd()
 for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
          print("{} is a directory".format(fullname))
     else:
          print("{} is a file".format(fullname))
# %%
import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w'):
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))
# %%
os.path.isdir('abc')
# %%
os.listdir()
# %%
import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)
  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, 'w') as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))
# %%
import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w'): pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    mod = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion 
    # Hint: how many characters are in “yyyy-mm-dd”? 
    return ("{}-{:02}-{:02}".format(mod.year, mod.month, mod.day))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
# %%

import os
def parent_directory():
    # Create a relative path to the parent 
    # of the current working directory 
    relative_parent = os.path.join(os.pardir, os.getcwd())
    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)

print(parent_directory())
# %%
os.getcwd()
# %%

import os

def parent_directory():
    # Get the current working directory
    current_directory = os.getcwd()

    # Go up to the parent directory
    parent_directory = os.path.join(current_directory, os.pardir)

    # Resolve the parent directory to its absolute path
    parent_directory = os.path.abspath(parent_directory)

    # Return the name of the parent directory
    return parent_directory

# Example usage
print(parent_directory())

# %%
os.getcwd()
# %%
os.pardir
# %%
print(os.path.join(os.getcwd(), '..'))
# %%
def band_group(lst):
    num = ''
    lst_len = len(lst)
    cont = False
    for idx, _ in enumerate(lst):
        if idx==0:
            num += str(_)
        elif idx+1 == lst_len and lst[idx-1] == lst[idx]-1:
            num += '-' + str(_)
        elif lst[idx-1] == lst[idx]-1:
            cont = True
        elif lst[idx]-1 != lst[idx-1]:
            if cont:
                num += '-'+ str(lst[idx-1]) + ',' + str(_)
            else:
                num += ',' + str(_)
            cont = False

    return num, len(num.split(','))
# %%
lst = [1,2,3,6,9,10]
print(band_group(lst))
# %%
print(band_group([5]))
# %%
print(band_group([7,9,10,14,138]))
# %%
print(band_group([10,20,30]))
# %%
import pandas as pd
df = pd.DataFrame(
    {   'Product': ['A','A','A','A','A','A','B','C','C','C','C','C','D','D','D'],
        'Numbers':[1,2,3,6,9,10,5,7,9,10,14,138,10,20,30]
    }
    # columns=['Product', 'Numbers']
)
df

# %%
df_grp = df.groupby(by='Product')
# %%
df_grp['A']
# %%
for _ in df_grp:
    print(_['Numbers'])
# %%
df_grp.get_group('A')['Numbers'].to_list()
# %%
ans = []
for _ in df['Product'].unique():
    grp, count = band_group(df_grp.get_group(_)['Numbers'].to_list())
    ans.append([_, grp, count] )
# %%
ans
# %%
len('1-3,6,9-10'.split(','))
# %%
for _ in df_grp:
    print(_.)
# %%
