import re

name = input('Please enter your name: ').strip()
# matches = re.search(r'^(.+), (.+)$', name)
# if matches:

if ( matches := re.search(r'^(.+), (.+)$', name) ) :
    last, first = matches.groups()
    name = f'{first} {last}'

print(f'hello, {name}')
print(f'{matches.group(0)} | {matches.group(1)} | {matches.group(2)}')