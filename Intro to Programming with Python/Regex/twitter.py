import re

url = input('Please enter your Twitter URL: ').strip()

username = url.replace('https://twitter.com/', '')
print(url, username)

username = url.removeprefix('https://twitter.com/')
print(url, username)

username = re.sub(r'(https?://)?(www\.)?twitter\.com/', '', url)
print(url, username)

if ( matches := re.search(r'twitter\.com\/(\w+)', url, re.IGNORECASE) ):
    # print(matches.group(1).removeprefix('twitter.com/'))
    print(matches.group(1))
else:
    print('Not a valid Twitter Handle')
