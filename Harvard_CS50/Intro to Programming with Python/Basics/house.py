name = input('Your name please: ')
if name =='Harry':
    print('Gryffindor')
elif name == 'Hermione':
    print('Gryffindor')
elif name == 'Ron':
    print('Gryffindor')
elif name == 'Draco':
    print('Slytherin')
else:
    print('Who?')

match name:
    case 'Harry' | 'Hermione' | 'Ron':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('Who?')

