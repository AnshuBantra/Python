#%%
def safe_int(num):
    try:
        num = int(num)
    except ValueError:
        print(f'Cannot convert {num} to integer, resetting to 0')
        return 0
    return num

val_1 = safe_int(input('Enter a number (Value 1) : '))
val_2 = safe_int(input('Enter a number (Value 2) : '))

def add(val_1, val_2):
    c = val_1 + val_2
    print(f'{c=}')
    return c

print(add(val_1, val_2))

# %%
