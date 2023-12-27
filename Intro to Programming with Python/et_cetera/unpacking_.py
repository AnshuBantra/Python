def total(galleons=0, sickles=0, knuts=0):
    return (galleons*17 + sickles) * 29 +knuts

coins = [100,50,25]
print(f'{total(*coins)} knuts')

coins = {'galleons':100, 'sickles':50, 'knuts':25}
print(f'{total(*coins.values())} knuts')
print(f'{total(**coins)} knuts')


# --------------------------------------------

def f(*args, **kwargs):
    print(f'Positional: {args}')
    print(f'Named: {kwargs}')

f(100,10,90)
f(name='Anshu', age=47)