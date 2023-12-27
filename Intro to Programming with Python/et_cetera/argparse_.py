import argparse

parser = argparse.ArgumentParser(description='Meow like a cat')
parser.add_argument('-n',
                    default=1,
                    type=int,
                    help='Number of times to meow (int)'
                )
args = parser.parse_args()

print('meow\n'*args.n, end='')
