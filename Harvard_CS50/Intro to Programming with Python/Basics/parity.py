def main():
    x = int( input('Input a number: ') )
    if is_even(x):
        print('Even')
    else:
        print('Odd')

def is_even(num):
    return num%2 == 0
    # return True if num%2 == 0 else False


main()