def dashed_line() -> None:
    print('-'*40)

## PPRINT
import json

with open('json_example.json', 'r') as file:
    data = json.load(file)
print(data)
dashed_line()

import pprint
pprint.pprint(data, width=20)
dashed_line()

## DEFAULTDICT

fruits = ['apple', 'banana', 'banana', 'banana', 'orange', 'apple']

word_count = {}
for _ in fruits:
    if _ in word_count:
        word_count[_] += 1
    else:
        word_count[_] = 1

print(word_count)
dashed_line()

import collections as col

word_count = col.defaultdict(int)
for _ in fruits:
    word_count[_] +=1
print(dict(word_count))
dashed_line()

## PICKLE

import pickle

class Dog:
    def __init__(self, name, breed, age) -> None:
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f'My name is {self.name} and I am a {self.age} years old {self.breed}')


data = Dog('Peeku', 'AmStaff', 3)

with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)
loaded_data.bark()
dashed_line()

## ANY

nums = [0,1,2,3]
print(any(nums))
print(all(nums))

def is_odd(num: int) -> bool:
    return num%2==0

print(any([is_odd(num) for num in nums]))
print(all([is_odd(num) for num in nums]))
dashed_line()


## enumerate
words = ['the', 'be', 'to', 'of', 'and', 'in', 'that' ]
print([(idx, word) for idx, word in enumerate(words)])

sentence = 'Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop'
sentence = 'Enumerate'
print([(idx, word) for idx, word in enumerate(sentence, start=1)])
dashed_line()

## Counter
import collections as col

print(col.Counter(fruits))
print(dict(col.Counter(fruits)))
dashed_line()

## timeit

import timeit

# code1 = """
# a = [_*2 for _ in range(1,6)]
# """

def code1():
    a = [_*2 for _ in range(1,6)]

def code2():
    a = list( map( lambda x: x*2, range(1,6) ) )

print(timeit.timeit(code1, number=100000))
print(timeit.timeit(code2, number=100000))
dashed_line()

# itertools.chain


# dataclass

import dataclasses as dc

@dc.dataclass
class Person:
    name: str
    age: int
    job: str

# dc.asdict()

person = Person(name='Anshu', age=100, job='Data Analyst')
print(person)
dashed_line()


# ## Scraping WiKi

# import requests
# from bs4 import BeautifulSoup

# page = requests.get("https://en.wikipedia.org/wiki/Most_common_words_in_English")
# soup = BeautifulSoup(page.content, 'html.parser')
# # tables = soup.find(id='mw-content-text')
# # tables = soup.find('table', class_='wikitable').find_all('tr')
# # items = tables.find(class_="extiw")
# # result = items[0]
# # print(items.prettify())
# # print(tables)

# # //*[@id="mw-content-text"]/div[1]/table[1]
# # /html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]
# counter = 1
# for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
#     data = items.find_all('td')
#     try:
#         word = data[0].a.text
#         speech = data[1].a.text
#         rank = data[2].text
#     except :
#         pass
#     # print(f'{data[0]}==>{word}\n{data[1]}==>{speech}\n{data[2]}==>{rank}', end='-------\n')
#     print(f'{data} ==> {word}\t{speech}\t{rank}', end='\n---------------------------------------------------------------\n')
#     counter += 1
#     if counter == 10: break
#     # print(data)
#     # print(data)
#     # break


import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government"

res = requests.get(URL).text
soup = BeautifulSoup(res,'html.parser')
for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all(['th','td'])
    try:
        country = data[0].a.text
    except :pass
    try:
        title = data[1].a.text
    except :pass
    try:
        name = data[1].a.find_next_sibling().text
    except :pass    
    print("{}|{}|{}".format(country,title,name))