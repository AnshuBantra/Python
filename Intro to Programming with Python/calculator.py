# # Integer
# x = input('Input number 1: ')
# y = input('Input number 2: ')
# x, y = int(x), int(y)
# print(x+y)

# # Float
# x, y = float(x), float(y)
# z = x+y
# print(f'{z:,}')

# # Division
# z = round(x/y, 2)
# print(f'{z:,}')
# print(f'{x/y:,.2f}')

def main():
    x = int( input('Enter a number: ') )
    print(f'x squared is {square(x)}')

def square(num):
    return num+num #num**2

if __name__ == '__main__':
    main()