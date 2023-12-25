# names = []

# for _ in range(3):
#     names.append(
#         input('Enter you name: ')
#     )

# print(names)
# print(sorted(names))

# file = open('names.txt', 'a')
# file.write(input('Enter you name: ')+'\n')
# file.write(f"{input('Enter you name: ')}\n")
# file.close()

with open('names.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(f'hello, {line}', end='')
print('--------------------------')

with open('names.txt', 'r') as file:
    for line in file:
        print(f'hello, {line.rstrip()}')
print('--------------------------')

names=[]
with open('names.txt', 'r') as file:
    for line in file:
        names.append( line.rstrip() )

for name in sorted(names):
    print(f'hello, {name}')
print('--------------------------')

names=[]
with open('names.txt', 'r') as file:
    for line in sorted(file, reverse=True):
        print(f'hello, {line.rstrip()}')
print('--------------------------')


# with open('students.csv', 'a') as file:
#     file.write(f"{input('Enter Student Name: ')} ,")
#     file.write(f"{input('Enter Student House: ')} \n")


with open('students.csv') as file:
    for line in file:
        name, house = line.rstrip().split(',')
        print(f'{name}\t{house}')
print('--------------------------')


students = []
with open('students.csv') as file:

    for line in file:
        name, house = line.rstrip().split(',')
        students.append({'name':name, 'house':house})

def get_name(students, key='name'):
    return students[key]

for student in sorted(students, key=get_name):
    print(f'{student["name"]} is in {student["house"]}')

for student in sorted( students, key= lambda student: get_name(student, key='house') ):
    print(f'{student["name"]} is in {student["house"]}')
print('--------------------------')

import csv

students = []
with open('students_1.csv') as file:
    reader = csv.reader(file)
    # for line in reader:
    #     students.append({'name':line[0], 'home':line[1]})
    for name, home in reader:
        students.append({'name':name, 'home':home})

for student in sorted( students, key= lambda student: student['name'] ):
    print(f'{student["name"]} grew up in {student["home"]}')
print('--------------------------')


import csv

students = []
with open('students_1.csv') as file:
    reader = csv.DictReader(file)
    # for line in reader:
    #     students.append({'name':line[0], 'home':line[1]})
    for row in reader:
        # students.append({'name':row['name'], 'home':row['home']})
        students.append(row)

for student in sorted( students, key= lambda student: student['name'] ):
    print(f'{student["name"]} grew up in {student["home"]}')
print('--------------------------')

import csv

name = input('Please, enter your name: ')
home = input('Please, enter your home: ')

with open('students_2.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
print('--------------------------')

import csv

name = input('Please, enter your name: ')
home = input('Please, enter your home: ')

with open('students_2.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({'name':name.rstrip(), 'home':home.rstrip()})
print('--------------------------')
