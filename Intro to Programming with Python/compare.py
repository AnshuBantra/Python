x = int( input('Input value for X: ') )
y = int( input('Input value for Y: ') )

if x<y:
    print('x is less than y')
elif x>y:
    print('x is greater than y')
else:
    print('x is equal to y')

if x<y or x>y:
    print('x is not equal to y')
else:
    print('x is equal to y')