# def meow(n: int) -> str:
#     '''
#     meow: Meow n times.

#     Args:
#         n (int): Number of times to meow

#     Returns:
#         str: A string of n meows, one per line
#     '''
#     return 'meow\n'*3

# num: int = int(input('Number: '))
# meows: str = meow(num)

# print(meows, end='')

import sys

if len(sys.argv) == 1:
    print('meow')
elif len(sys.argv) == 3 and sys.argv[1] == '-n':
    print('meow\n'*int(sys.argv[2]), end='')
else:
    print('usage: meow.py | meow.py -n nums')