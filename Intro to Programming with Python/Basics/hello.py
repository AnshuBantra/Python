# Ask user for their input
#   All inputs received in Python are Strings (Text)
name = input("What's your name? ")

# Print Function
print('hello,', name)

# Using Function methods to transform a String
print('hello, '+ name.strip().capitalize())
print('hello,', name.strip().title())
first, last = name.split()
print(first, last)