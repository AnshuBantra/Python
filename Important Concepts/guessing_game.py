import random, sys

def guess_number(a:str|int, b:str|int) -> int:
    try:
        a = int(a)
        b = int(b)
    except:
        a, b = 1, 100
    return random.randint(a, b)

def user_guess(guess:int) -> bool:
    while True:
        user_input = int(input('What\'s your guess: '))
        print('Too big!') if user_input > guess else\
        print('Too small') if user_input < guess else\
        sys.exit(f'You guessed right. The number is {guess}')
    

def main() -> None:
    a = input('Input a number (1): ')
    b = input('Input a number (100): ')
    guess = guess_number(a, b)
    user_guess(guess)


if __name__ == '__main__':
    main()