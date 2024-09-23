import typing as typ
import keyboard as kbd
import sys, time

def fibonacci_generator() -> typ.Generator[int, None, None]: #[yield type, send type, return type]
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a+b)

def main() -> None:
    fib_gen: typ.Generator[int, None, None] = fibonacci_generator()
    n: int = 10
    print(f'Tap "enter" for next {n} numbers in Fibonacci Series or "q" to exit: ')
    while True:
        if kbd.read_key() == 'enter':
            for _ in range(n):
                print(next(fib_gen), end=',')
        elif kbd.read_key() == 'esc':
            sys.exit()
        print()

if __name__ == '__main__':
    main()

# while True:
#   if kbd.read_key() == ('esc'):
#     print('Esc pressed')
#     break
#   elif kbd.read_key() == 'enter':
#     print('Enter pressed')
#   else:
#     print('Something else pressed')
#     break