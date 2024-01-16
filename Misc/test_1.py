import re

def chk_tuple(tup):
    return all( tuple( 0 <= int(element) <= 255  for element in tup) )

inpt = input('IPv4 Address: ')

# if not (matches := re.findall(r'\d[0-255]\.\d[0-255]\.\d[0-255]\.\d[0-255]', inpt)):
#     print('Invalid input')
# matches = re.findall(r'\d[0-255]\.\d[0-255]\.\d[0-255]\.\d[0-255]', inpt)
# matches = re.findall(r'\d{0,255}\.\d{0,255}\.\d{0,255}\.\d{0,255}', inpt)
if inpt.count('.') ==3:
    matches = re.findall(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', inpt)
    if not matches:
        print( 'Invalid Input' )
    else:
        for match in matches:
            print( chk_tuple( match ) )
else:
    print( 'Invalid Input' )