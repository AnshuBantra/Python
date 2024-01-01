import sys

def main():
    try:
        print(convert(input('Enter fraction: ')))
    except (ValueError, ZeroDivisionError) as e:
        if e.args[0] == "invalid literal for int() with base 10: 'a'":
            sys.exit('Values in a fraction should be \'INT\'')
        elif e.args[0] == "division by zero":
            sys.exit('Divisor in a fraction can not be \'0\'')
        else:
            sys.exit('Dividend can not be greater than Divisor')

def convert(fraction):
    dividend, divisor = fraction.replace(' / ', '/').strip().split('/')
    dividend, divisor = int(dividend), int(divisor)
    if  dividend > divisor and divisor != 0:
        raise ValueError("Dividend can not be greater than Divisor")
    return gauge( round( (dividend/divisor) *100 ) )

def gauge(percentage):
    if  percentage <= 1:    percentage = 'E'
    elif percentage >= 99:  percentage = 'F'
    else:                   percentage = f'{percentage}%'
    return percentage

if __name__ == '__main__':
    main()

# import sys

# def main():
#     print(convert(input('Enter fraction: ')))

# def convert(fraction):
#         fraction = fraction.replace(' / ', '/').strip()
#         try:
#             dividend = int(fraction.split('/')[0])
#             divisor = int(fraction.split('/')[1])
#             if    divisor == 0:
#                 raise ZeroDivisionError()
#             elif  dividend > divisor:
#                 raise ValueError('In fraction X/Y, X cannot be > than Y')
#             elif '.' in fraction:
#                 raise ValueError('In fraction X/Y, X and Y need to be integers')
#             return gauge(round(eval(fraction)*100))
#         except ZeroDivisionError:
#             sys.exit('Divisor (Y) cannot be 0')
#         except (NameError, ValueError) as e:
#             if e.args[0] == "invalid literal for int() with base 10: 'a'":
#                 sys.exit(f'ValueError: Input not an integer')
#             else:
#                 sys.exit(f'ValueError: {e}')
#         except Exception as e:
#             sys.exit(f'Error: {e}, {type(e)}')

# def gauge(percentage):
#     if  percentage <= 1:
#         percentage = 'E'
#     elif percentage >= 99:
#         percentage = 'F'
#     else:
#         percentage = f'{percentage}%'
#     return percentage


# if __name__ == "__main__":
#     main()
