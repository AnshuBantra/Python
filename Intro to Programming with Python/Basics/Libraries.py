# # %%
# # Random Library
# import random
# random.choice(['heads', 'tails'])
# random.randint(2,9)
# x = list(range(10))
# random.shuffle(x)       # Shuffles inplace
# print(x)


# # %%
# #   Statistics Library
# import statistics
# statistics.mean([100,90])

# # %%
# #   Sys Library
# import sys
# if len(sys.argv) > 2:
#     sys.exit('Too many arguments')
# elif len(sys.argv)<2:
#     sys.exit('Too few arguments')

# print(f'hello, my name is {sys.argv[1]}')


# # %%
# # Packages

# #   CowSay
# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow(f'hello, {sys.argv[1]}')
#     cowsay.trex(f'hello, {sys.argv[1]}')

#   Requests
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit('Need one argument with app name')

response = requests.get('https://itunes.apple.com/search?entity=song&limit=10&term='+sys.argv[1])
# print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o['results']:
    print(f"{result['trackName']}, ==> {result['isStreamable']}")
