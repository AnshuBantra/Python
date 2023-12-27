def main():
    student = get_student()
    # print(f'{student[0]} from {student[1]}')
    print(f'{student["name"]} from {student["house"]}')

def get_input(val) -> str:
    return input(f'Enter your {val}: ').strip()

def get_student() -> str:
    '''
        accepts values of name & house of student and returns them
    '''
    name = get_input('name')   #input('Enter your name: ')
    house = get_input('house') #input('Enter your house: ')
    # return (name, house)
    # return [name, house]
    return {'name': name, 'house':house}
if __name__ == '__main__':
    main()