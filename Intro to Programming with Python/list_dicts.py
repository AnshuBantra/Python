students = ["Hermione","Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

for student in students:
    print(f'{student} => {houses[students.index(student)]}')


hogwarts = {
    'Hermione': 'Gryffindor',
    'Harry': 'Gryffindor',
    'Ron': 'Gryffindor',
    'Draco': 'Slytherin'
}

for key, value in hogwarts.items():
    print(f'{key} => {value}')

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student['name'], student['house'], student['patronus'], sep=' | ')