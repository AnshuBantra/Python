# -*- coding: utf-8 -*-
"""
Python Lambda Functions

@author: Anshu Bantra
"""

#%%
# https://www.freecodecamp.org/news/lambda-expressions-in-python/
#Lambda Functions
square = lambda x: x**2
print(square(2))

#%%
print(square(5))

#%%
# Lambda Function to find Even / Odd Numbers
lambda_func = lambda x: 'Even' if x%2 == 0 else 'Odd'
print(lambda_func(3)) # Returns False
print(lambda_func(4)) # Returns True

#%%
#Lambda with Dictionary
my_dict = {"A": 1, "B": 2, "C": 3}
sorted(my_dict, key=lambda x: my_dict[x]%3) # Returns ['C', 'A', 'B']
print(sorted(my_dict, key=lambda x: my_dict[x]%3))

#%%
#Lambda with Filter Function
my_list = list(range(1,11,1))
filtered = list(filter(lambda x : x%2 != 0, my_list))

print(filtered)

#%%
#Lambda with Filter Function
my_list = list(range(1,11,1))
extract_list = filter(lambda x : x, my_list)
print(list(extract_list))

#%%
# https://www.freecodecamp.org/news/python-map-explained-with-examples/
"""
The map() function (which is a built-in function in Python) 
is used to apply a function to each item in an iterable 
(like a Python list or dictionary).
It returns a new iterable (a map object) that you can use in other parts of your code.
"""

cube = lambda x: x**3
cube_list = list(map(cube, my_list))
print(my_list)
print(cube_list)

print(list(map(lambda x: x**3, my_list)))


#%%

word_list = ['Hello', 'Name', 'Python']
print(list(map(len, word_list)))

#%%

base = [1,2,3,4,5]
power = [2,3,2,2, 4]

print(list(map(pow, base,power)))

rtp = lambda x,y: x**y
print(list(map(rtp, base,power)))

#%%
# https://www.freecodecamp.org/news/python-regex-tutorial-how-to-use-regex-inside-lambda-expression/

import re

fruits = ['apple', 'mango', 'banana', 'cherry', 'apricot', 'raspberry', 'avocado']
fruits_end_o = filter(lambda fruit: re.search('o$', fruit), fruits)
fruits_start_a = filter(lambda fruit: re.search('^a', fruit), fruits)

print(list(fruits_start_a))
print(list(fruits_end_o))
print(list(filter(lambda fruit: re.search(r'^a.*o$', fruit), fruits)))

#%%

fruits2 = ['opple', 'bonono', 'cherry', 'dote', 'berry']
modified_fruits = map(lambda fruit: re.sub('o', 'a', fruit), fruits2)

# convert the new fruits to another list and print it
print(list(modified_fruits)) # ['apple', 'banana', 'cherry', 'date', 'berry']

#%%

fruits3 = [ 'banana', 'fig', 'grapefruit']

# sort fruits based on the number of vowels

fruits3.sort(key=lambda x: len(re.findall('[aeiou]', x)), reverse=True)
print(fruits3)

#%%

is_even_list = lambda x: x * 10, list(range(1, 5))
print(list(is_even_list))