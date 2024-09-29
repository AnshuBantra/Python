# # import PyReadline

# # try:
# #     while True:
# #         user_input = input("Enter something (Ctrl-D or Ctrl-Z to exit): ")
# #         # Your code here, for example, print the user input
# #         if user_input == '♦':
# #             print('Here')
# #             raise EOFError()
# #         print("You entered:", user_input)
# # except OSError as e:
# #     if e.errno == 22:  # 22 is the error code for EOF on Windows
# #         print("\nEnd of input: Exiting the program.")
# # except EOFError:
# #     print("\nEOFError: Exiting the program.")
# # except KeyboardInterrupt:
# #     print("\nKeyboardInterrupt: Exiting the program.")

# menu = {
#     "Baja Taco": 4.25,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }

# total = 0
# try:
#     while True:
#         item = input('Item: ').capitalize()
#         if menu.get(item):
#             total += menu.get(item)
#             print(f'Total: {total}')
# except EOFError:
#     print("Pressed Ctrl-Z: Exiting the program.")

# grocery_lst = {}
# try:
#     while True:
#         item = input().strip().upper()
#         if item in grocery_lst:
#             grocery_lst[item] += 1
#         else:
#             grocery_lst[item] = 1
# except EOFError:
#     print('Pressed Ctrl-d/z: Exiting the List Input')
# items = sorted(grocery_lst)
# for item in items:
#     print(grocery_lst[item], item)

# # import PyReadline

# # try:
# #     while True:
# #         user_input = input("Enter something (Ctrl-D or Ctrl-Z to exit): ")
# #         # Your code here, for example, print the user input
# #         if user_input == '♦':
# #             print('Here')
# #             raise EOFError()
# #         print("You entered:", user_input)
# # except OSError as e:
# #     if e.errno == 22:  # 22 is the error code for EOF on Windows
# #         print("\nEnd of input: Exiting the program.")
# # except EOFError:
# #     print("\nEOFError: Exiting the program.")
# # except KeyboardInterrupt:
# #     print("\nKeyboardInterrupt: Exiting the program.")

# menu = {
#     "Baja Taco": 4.25,
#     "Burrito": 7.50,
#     "Bowl": 8.50,
#     "Nachos": 11.00,
#     "Quesadilla": 8.50,
#     "Super Burrito": 8.50,
#     "Super Quesadilla": 9.50,
#     "Taco": 3.00,
#     "Tortilla Salad": 8.00
# }

# total = 0
# try:
#     while True:
#         item = input('Item: ').capitalize()
#         if menu.get(item):
#             total += menu.get(item)
#             print(f'Total: {total}')
# except EOFError:
#     print("Pressed Ctrl-Z: Exiting the program.")

# grocery_lst = {}
# try:
#     while True:
#         item = input().strip().upper()
#         if item in grocery_lst:
#             grocery_lst[item] += 1
#         else:
#             grocery_lst[item] = 1
# except EOFError:
#     print('Pressed Ctrl-d/z: Exiting the List Input')
# items = sorted(grocery_lst)
# for item in items:
#     print(grocery_lst[item], item)

# months = [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]


# while True:
#     dt = input('Date: ').replace(',', '').strip()
#     # print('dt:',dt)
#     try:
#         if '/' in dt:
#             mn, dy, yr = dt.split('/')
#             # print('/',mn, dy, yr)
#         else:
#             mn, dy, yr = dt.split(' ')
#             # print('__',mn, dy, yr)
#             mn = str(months.index(mn)+1)
#             # print('__',mn, dy, yr)

#         print(f'{yr}-{mn.zfill(2)}-{dy.zfill(2)}')
#         break
#     except Exception:
#         pass


# import emoji
# print(f'Output: {emoji.emojize( input("Input: ") , language="alias")}')


# # pip install pyfiglet
# # https://www.youtube.com/watch?v=88pl8TuuKz0
# # pip install pyfiglet
# # https://www.youtube.com/watch?v=88pl8TuuKz0
# import argparse
# from pyfiglet import Figlet
# import random

# figlet = Figlet()
# fonts = figlet.getFonts()

# parser = argparse.ArgumentParser( description='Output in FigLet Style'
#                                 , exit_on_error=False
#                                 , conflict_handler='error')
# parser.add_argument(    '-f', '--font',
#                         default=random.choices(fonts),
#                         type=str,
#                         nargs=1,
#                         help='Name of the font'
#                     )# args = parser.parse_args(['-f'])

# try:
#     args = parser.parse_args()
#     figlet.setFont(font=args.font[0])
#     print(figlet.renderText( input('Input: ') ))
# except Exception as e: #figlet.FontNotFound(font):
#     print('Invalid usage:')


# import inflect
# p = inflect.engine()
# # UNCONDITIONALLY FORM THE PLURAL
# word = 'test'
# print("The plural of ", word, " is ", p.plural(word))


# # CONDITIONALLY FORM THE PLURAL
# cat_count = 23
# print("I saw", cat_count, p.plural("cat", cat_count))


# # # FORM PLURALS FOR SPECIFIC PARTS OF SPEECH

# # print(
# #     p.plural_noun("I", N1),
# #     p.plural_verb("saw", N1),
# #     p.plural_adj("my", N2),
# #     p.plural_noun("saw", N2),
# # )

# try:
#     print()
# except EOFError
# # Professor.py
# import random

# def main():
#     level = get_level()
#     nums = list(eval(generate_integer(level)))
#     # print(min(nums), max(nums), len(nums))
#     score = 0
#     err = 0
#     for _ in range(10):
#         num1 = random.choice(nums)
#         num2 = random.choice(nums)
#         while True:
#             if num1+num2 == int(input(f'{num1} + {num2} = ')):
#                 score += 1
#                 break
#             else:
#                 err += 1
#                 if err == 3:
#                     print(f'{num1} + {num2} = {num1+num2}')
#                     err = 0
#                     break
#                 else:
#                     print('EEE')
#     print(f'Score: {score}')

# def get_level():
#     num=None
#     while num == None:
#         try:
#             num = int( input(f'Level: ') )
#             if num <= 0:
#                 num = None
#             elif num in [1,2,3]:
#                 return num
#             else:
#                         num = None
#         except ValueError:
#             # return (num:=None)
#             pass

# def generate_integer(level):
#     if level == 1:
#         equation = f"range(0, int('9'*level)+1)"
#     else:
#         equation = f"range(int('9'*(level-1))+1, int('9'*level)+1)"
#     return equation

# if __name__ == '__main__':
#     main()

# import argparse
# import sys
# import requests
# import json

# parser = argparse.ArgumentParser( description='Number of Bitcoind to buy: '
#                                 , exit_on_error=False
#                                 )
# parser.add_argument(    'bitcoins',
#                         # type=float,
#                         nargs=1,
#                         help='Number of Bitcoind to buy: '
#                     )

# try:
#     sys.argv[1]
#     args = parser.parse_args()
#     bitcoins = float( args.bitcoins[0] )
# except IndexError:
#     sys.exit(f'Missing command-line arugument')
# except Exception as e:
#     sys.exit(f'Command-line arugument is not a number')

# try:
#     response = requests.get(r'https://api.coindesk.com/v1/bpi/currentprice.json')
#     response_json = response.json()
#     print(f"${bitcoins*response_json['bpi']['USD']['rate_float']:,.4f}")
# except requests.RequestException:
#     pass


# import re

# def main():
#     inpt = input('Input: ')
#     print(shorten(inpt))

# def shorten(word):
#     return re.sub(r"[aeiouAEIOU]", "", word)

# if __name__ == '__main__':
#     main()

def empty_lst(lst):
    return not lst

s_chars = [chr(_) for _ in range(32,48,1)]
# for plate in ['CS50', 'AB10', 'XY1000', 'MEL100', 'APB101', 'CS50A', 'XYZ10B', 'ABCD']:
#     print(plate, end='\t')
#     chr_pos=[]
#     num_pos=[]
#     for chr in plate:
#         if chr.isalpha():
#             chr_pos.append(plate.index(chr))
#         elif chr.isnumeric():
#             num_pos.append(plate.index(chr))
#     if not num_pos:
#         num_pos.append(max(chr_pos)+1)
#     print( max(chr_pos), max(num_pos), max(chr_pos) < max(num_pos)  )
    # print(
    #         empty_lst([_ for _ in list(plate) if _ in s_chars])
    #     )

# import re
# aString = '111A222B333C'
# res = re.split('(\d+)', aString)
# print(res)

# for plate in ['CS50', 'AB10', 'XY1000', 'MEL100', 'APB101', 'CS050', 'XYZ012', 'ABCD01']:
#     num_pos=[]
#     num_pos = [ num_pos.append(chr)
#                 for chr in plate
#                 if chr.isnumeric()
#             ]
#     # print(num_pos.index('0'), num_pos.index('0') != 0)
#     print(num_pos)

# for plate in ['CS50', 'AB10', 'XY1000', 'MEL100', 'APB101', 'CS050', 'XYZ012', 'ABCD01']:
#     num_pos=[]
#     for chr in plate:
#         if chr.isnumeric():
#             num_pos.append(chr)
#     # assert plates.is_valid(plate) == (num_pos.index('0') != 0)
#     print(plate,'\t', (num_pos.index('0') != 0))

# def test_convert_int():
#     x = [1,2,3,4,5,6,'a']
#     y = ['a',4,5,6,7,8,9]
#     for _ in range(len(x)):
#         print(f'{x[_]}/{y[_]}')
#         int(x[_])/int(y[_])

# test_convert_int()

import sys

def main():
    print(convert(input('Enter fraction: ')))

def convert(fraction):
        fraction = fraction.replace(' / ', '/').strip()
        try:
            dividend = int(fraction.split('/')[0])
            divisor = int(fraction.split('/')[1])
            if    divisor == 0:
                raise ZeroDivisionError()
            elif  dividend > divisor:
                raise ValueError('In fraction X/Y, X cannot be > than Y')
            elif '.' in fraction:
                raise ValueError('In fraction X/Y, X and Y need to be integers')
            return gauge(round(eval(fraction)*100))
        except ZeroDivisionError:
            sys.exit('Divisor (Y) cannot be 0')
        except (NameError, ValueError) as e:
            if e.args[0] == "invalid literal for int() with base 10: 'a'":
                sys.exit(f'ValueError: Input not an integer')
            else:
                sys.exit(f'ValueError: {e}')
        except Exception as e:
            sys.exit(f'''{e}\n{e.args[0]}\n{type(e)}''')

def gauge(percentage):
    if  percentage <= 1:
        percentage = 'E'
    elif percentage >= 99:
        percentage = 'F'
    else:
        percentage = f'{percentage}%'
    return percentage



if __name__ == "__main__":
    main()

# %%
import sys

def to_int(n):
    try:
        int(n)
    # except ValueError as e:
    #     if e.args[0] == "invalid literal for int() with base 10: 'a'":
    #         sys.exit(f'ValueError: Input not an integer')
    #     else:
    #         sys.exit(f'ValueError: {e}')
    except Exception as e:
            msg = "invalid literal for int() with base 10: 'a'"
            sys.exit(f"{e}, {e==msg}")

def test_convert_int():
    x = [1,2,3,4,5,6,'a']
    y = ['a',4,5,6,7,8,9]
    for _ in range(len(x)):
        # assert fuel.convert(f'{x[_]}/{y[_]}') == 
        to_int(x[_]) / to_int(y[_])

test_convert_int()
# %%
