import typing as typ
import keyboard as kbd
import sys

def fibonacci_generator() -> typ.Generator[int, None, None]: #[yield type, send type, return type]
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a+b)

def main() -> None:
    fib_gen: typ.Generator[int, None, None] = fibonacci_generator()
    n: int = 10
    print(f'Tap "enter" for next {n} numbers in Fibonacci Series or "Esc" to exit: ')
    while True:
        for _ in range(n):
            print(next(fib_gen), end=',')
            input()
        while True:
            if kbd.is_pressed('esc'):
                sys.exit()
            elif kbd.is_pressed('enter'):
                break

if __name__ == '__main__':
    main()