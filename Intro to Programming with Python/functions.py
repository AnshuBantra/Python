# Define a new function
def main():
    name = input('Your name please: ')
    hello(name)
    x = int( input('Enter a number: ') )
    print(f'{x} squared is {square(x)}')

def hello(to='world'):
    print(f'hello, {to}')

def square(num):
    return num**2

main()