import typing as typ
import keyboard as kbd
import sys
import inputs

def cumulative_sum() -> typ.Generator[float, float, str]: #[yield type, send type, return type]
    total: float = 0
    while True:
        total += yield total

def main() -> None:
    cum_sum_gen: typ.Generator[float, float, str] = cumulative_sum()
    next(cum_sum_gen)
    while True:
        # value: float = float(input('Enter a number: '))
        # current_sum: float = cum_sum_gen.send(value)
        # print(f'Cumulative sum: {current_sum}')
        value: float = inputs.get_float()
        if value == None:
            sys.exit()
        else:
            current_sum: float = cum_sum_gen.send(value)
            print(f'Cumulative sum: {current_sum}')

if __name__ == '__main__':
    main()
