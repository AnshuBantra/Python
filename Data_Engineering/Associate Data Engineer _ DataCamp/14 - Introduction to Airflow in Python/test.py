import numpy as np
import itertools

#%%
def is_palindrome(num: int) -> bool:
    str_num = str(num)
    return str_num == str_num[::-1]
#%%
def is_x_repeating(num: int, digit: int) -> bool:
    num = str(num)
    lst = [num.count(x) for x in num]
    return np.any(np.array(lst)==digit)
#%%
def x_palindromes(num: int, digits: int) -> list:
    rng = range(num+1,num+100000001)
    rng = filter(is_palindrome, rng)
    rng = filter(lambda x: is_x_repeating(x, digits), rng)
    return list(itertools.islice(rng, 3))
# %%
x_palindromes(8789700, 3)
# %%
import pandas as pd
df = pd.DataFrame(
    {
        'No. of Digits': [21, 684, 291, 1253, 656661, 8789700, 23504870, 570693998],
        'Repeats': [2, 2, 2, 4, 3, 3, 4, 4]
    }
)
df
# %%
ans = pd.DataFrame(
    df.apply(lambda x: x_palindromes(x['No. of Digits'], x['Repeats']), axis=1).to_list(),
    columns=['Ans1', 'Ans2', 'Ans3']
    )
# %%
pd.merge(df,ans,left_index=True, right_index=True)
# %%
row=6
col=8
lst = [*range(1,col+1)]
lst

# %%
rot = [*range(row)]
rot

# %%
ln = len(lst)
lst2=[]
for _ in rot:
    lst1=[]
    if _ != 0:
        lst1.extend([lst[_*-1:], lst[0:ln-_]])
        lst2.append(lst1)

# %%
lst2
# %%
[lst[_*-1:].extend(lst[0:ln-_]) for _ in rot]
# %%
import pandas as pd

# Create the DataFrame
data = {
    'Value': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'Row': [1, 2, 5, 1, 2, 3, 3, 4, 5],
    'Column': [3, 2, 4, 3, 4, 3, 3, 1, 4]
}

df = pd.DataFrame(data)

# Create an empty 5x5 grid
grid = [["" for _ in range(5)] for _ in range(5)]

# Populate the grid based on the DataFrame
for _, row in df.iterrows():
    r, c = row['Row'] - 1, row['Column'] - 1
    if grid[r][c] == "":
        grid[r][c] = row['Value']
    else:
        grid[r][c] += ", " + row['Value']

# Convert to DataFrame for better display
nums = [*range(1,6)]
grid_df = pd.DataFrame(grid, columns=nums, index=nums)

print(grid_df)

# %%
grid = [["" for _ in range(5)] for _ in range(5)]

# Populate the grid based on the DataFrame
for _, row in df.iterrows():
    r, c = row['Row'] - 1, row['Column'] - 1
    if grid[r][c] == "":
        grid[r][c] = row['Value']
    else:
        grid[r][c] += ", " + row['Value']

grid
# %%


import pandas as pd
import numpy as np

# Create the DataFrame
data = {
    'Value': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'Row': [1, 2, 5, 1, 2, 3, 3, 4, 5],
    'Column': [3, 2, 4, 3, 4, 3, 3, 1, 4]
}

df = pd.DataFrame(data)

# Create an empty 5x5 grid
# grid = np.empty((5, 5), dtype=object)
# grid[:] = ""
grid = np.full((5,5), "", dtype=object)

# Populate the grid based on the DataFrame
for _, row in df.iterrows():
    r = row['Row'] - 1
    c = row['Column'] - 1
    if grid[r, c] == "":
        grid[r, c] = row['Value']
    else:
        grid[r, c] += ", " + row['Value']

# Convert to DataFrame for better display
grid_df = pd.DataFrame(grid, columns=[1, 2, 3, 4, 5], index=[1, 2, 3, 4, 5])

print(grid_df)

# %%
grid = np.full((5,5), "", dtype=object)
grid
# %%
import pandas as pd

df = pd.DataFrame(
    {   'N1' : [-1, -4, 1, -4, 6, -2, -5, 5, -5]
        , 'N2' : [7, -7, 4, 6, 0, -3, -1, 5, 1]
        , 'N3' : [-3, -3, 7, 4, 9, 2, 3, 4, -2]
        , 'N4' : [1, -1, 2, -2, 8, -9, -1, -4, -2]
        , 'N5' : [7, -8, 5, -5, 2, 3, -8, 3, 5]
        , 'N6' : [6, -3, 4, -4, 3, 0, -1, 2, 2]
    }
)
df
# %%
import itertools
import numpy as np
# %%
np_df = np.array(df)
np_df
# %%
np_df[0]
lst =[]
for _ in itertools.combinations(np_df[0],3):
    # lst.append(min(np.prod(_)))
    print(min(np.prod(_)))
lst
    # print(_, np.prod(_))
# %%
def find_minimum_product(df_row):
    return min([np.prod(_) for _ in itertools.combinations(df_row,3)])
# %%
df['Min. Prod.'] = df.apply(lambda x: find_minimum_product(x))
df
# %%
find_minimum_product(df.loc[0,:])
# %%
find_minimum_product(df.loc[1,:])
# %%
df.apply(lambda x: find_minimum_product(x), axis=1)
# %%

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes_between(start=2, end=10):
    """Generate the first n prime numbers."""
    primes = []
    # while len(primes) < end:
    while start < end:
        if is_prime(start):
            primes.append(start)
        start += 1
    return primes

# Example usage
prime_numbers = generate_primes_between(10,100)
print(len(prime_numbers))

# %%
arr = np.array(range(11))
arr

# %%

# %%
def is_reverse_prime(num):
    return is_prime(int(str(num)[::-1]))
# %%
rng = range(10,100)
# prime = 
emirp = filter(is_reverse_prime, filter(is_prime, rng))
[*emirp]
# %%
print([*prime])
print([*emirp])
# %%
from sympy import isprime
# %%
! pip install sympy
# %%
from sympy import isprime
import pandas as pd

# Create a function to identify emirp numbers

def isemirp(num):
 rev = int(str(num)[::-1])
 emirp = isprime(num) and isprime(rev) and num != rev
 return emirp

# Perform data munging 
numbers = filter(isemirp, range(10,10000000)) 
df = pd.DataFrame(data={"My Answer": numbers})

# Display the final results
df
# %%
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_emirp(num):
    forward = str(num)
    backward = forward[::-1]
    return is_prime(num) and is_prime(int(backward)) and forward!=backward

rng = range(10,10000000)
[*filter(is_emirp, rng)]
# %%
from sympy import isprime

def is_emirp(num):
    forward = str(num)
    backward = forward[::-1]
    return isprime(int(backward)) and forward!=backward

rng = range(10,10000000)
[*filter(is_emirp, rng)]
# %%
from sympy import primerange, isprime

rng = primerange(10, 10000000)
[*filter(is_emirp, rng)]

# %%

[f'file{x}.txt' for x in range(30)]

# %%
import numpy as np
import pandas as pd
# %%
rng = pd.date_range(start='1/1/2000', end='12/31/2999')

# %%

date_range = pd.date_range(start='2000-01-01', end='2099-12-31', freq='D')
print(date_range)

# %%
import datetime

def year_boundary(yr: int):
    return datetime.date(yr,1,1), datetime.date(yr,12,31)
# %%
start_, end_ = year_boundary(2000)
date_range = pd.date_range(start_, end_)
print(date_range)
# %%

import calendar

def count_long_weekend(year, month):
    cal = calendar.Calendar()
    days_in_month = cal.itermonthdays2(year, month)
    weekdays = [weekday for day, weekday in days_in_month if day != 0]

    return weekdays.count(4)==5, weekdays.count(5)==5, weekdays.count(6)==5

# %%
all(count_fridays(2000, 12))
# cal = calendar.Calendar()
# days_in_month = cal.itermonthdays2(2000,12)
# [weekday for _, weekday in days_in_month if _ != 0].count(4)
# # .itermonthdays2(2000, 12,)
# # fri = sum(1 for day, weekday in days_in_month if weekday == 4 and day != 0)
# for day, weekday in days_in_month:
#     print(day, weekday)


# %%
import datetime

all_dts = []
for yr in range(2000,2999):
    dts = []
    for mnth in range(1,13):
        if all(count_long_weekend(yr, mnth)):
            dts.append(datetime.date(yr, mnth, 1).strftime("%b-%Y"))
    if dts:
        all_dts.append(dts)
# %%
all_dts

# %%

import calendar
import datetime 

def long_weekend_months(yr):
    cal = calendar.Calendar()
    dts=[]
    for mnth in range(1, 13):
        days_in_month = cal.itermonthdays2(yr, mnth)
        weekdays = [weekday for day, weekday in days_in_month if day != 0]
        if weekdays.count(4)==5 and weekdays.count(5)==5 and weekdays.count(6)==5:
            dts.append(datetime.date(yr, mnth, 1).strftime("%b-%Y"))
    return ', '.join(dts)

all_dts = []
for yr in range(2000,2012):
    if dts:=long_weekend_months(yr):
        all_dts.append(dts)
all_dts
    # dts = []
    # for mnth in range(1,13):
    #     if all(count_long_weekend(yr, mnth)):
    #         dts.append(datetime.date(yr, mnth, 1).strftime("%b-%Y"))
    # if dts:
    #     all_dts.append(dts)
# %%
@contextlib.contextmanager
def my_context():
    print('hello')
    yield 42
    print('bye')


# %%

[_ for _ in my_context()]
# %%
wrd = 'abc'
# %%



# %%
def word_sq(wrd: str) -> None:
    len_ = len(wrd)
    lst = []
    for _ in range(len_):
        print(wrd[_], end='')
        if _ == 0:
            print(wrd[_+1:len_-1], end='')
        elif _ == len_-1:
            print(wrd[::-1][1:-1], end='')
        else:
            print(' '*(len_-1), end='')
        print(wrd[-(_+1)])
    
# %%
word_sq('abc')
# %%
word_sq('microsoft')
# %%
def split_word(wrd):
    return [w for w in wrd]
# %%
split_word('abc')
# %%
def word_sq_list(wrd: str) -> None:
    len_ = len(wrd)
    lst = []
    for _ in range(len_):
        lst.append(split_word(wrd))
        if _ == 0:
            print(wrd[_+1:len_-1], end='')
        elif _ == len_-1:
            print(wrd[::-1][1:-1], end='')
        else:
            print(' '*(len_-1), end='')
        print(wrd[-(_+1)])

#%%

import pandas as pd

def create_word_sq(word):
    n = len(word)
    df = pd.DataFrame('', index=range(n), columns=range(n))
    df.iloc[0] = list(word)
    df.iloc[-1] = list(word[::-1])

    # Fill the left and right columns
    for i in range(1, n-1):
        df.iat[i, 0] = word[i]
        df.iat[i, -1] = word[::-1][i]

    return df

# Example usage
word = "abcd"
df = create_word_sq(word)
print(df)
