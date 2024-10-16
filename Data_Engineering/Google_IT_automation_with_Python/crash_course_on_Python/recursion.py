# %%
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

# %%
def is_power_of(number, base):
    # Base case: 1 is a power of any base (base^0)
    if number == 1:
        return True
    # If number is less than the base or not divisible by base, it's not a power
    if number < base or number % base != 0:
        return False
    # Recursive case: divide the number by the base and check again
    return is_power_of(number // base, base)
