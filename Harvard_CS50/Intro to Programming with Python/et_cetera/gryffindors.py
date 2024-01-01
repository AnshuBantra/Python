students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student['name'] for student in students if student['house'] == 'Gryffindor'
]

print(*sorted(gryffindors))

def isgryffindor(s):
    return s['house'] == 'Gryffindor'

gryffindors = filter(isgryffindor, students)
for gryffindor in sorted(gryffindors, key=lambda s: s['name']):
    print(gryffindor['name'])

gryffindors = filter(lambda s: s['house']=='Gryffindor', students)
for gryffindor in sorted(gryffindors, key=lambda s: s['name']):
    print(gryffindor['name'])


students = ["Hermione","Harry","Ron"]
s = [{'name':student, 'house':'Gryffindor'} for student in students]
print(s)


students = ["Hermione","Harry","Ron"]
s = {student:'Gryffindor' for student in students}
print(s)


students = ["Hermione","Harry","Ron"]
for rank, student in enumerate(sorted(students),1,):
    print(rank, student)