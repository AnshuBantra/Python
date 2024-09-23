import typing as typ
import keyboard as kbd
import sys

def read(path: str) -> typ.Generator[str, None, str]: #[yield type, send type, return type]
    with open(path, 'r') as file:
        for _ in file:
            yield _.strip()
    return 'This is the end!'

def main() -> None:
    reader: typ.Generator[str, None, str] = read(r'..\Data\AI.txt')
    while True:
        if kbd.read_key() == 'enter':
            try:
                print(next(reader), end='')
            except StopIteration as e:
                print(f'Stop Iteration: {e}')
                sys.exit()
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