# Capturing Groups

# %%

import re
def rearrange_name(name):
    pattern = r"^([\w \.]*), ([\w \.]*)$"
    result = re.search(pattern, name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)
# %%
    # Return words atleast 7 chars long

import re
def long_words(text):
    pattern = r'\w{7,}'
    result = re.findall(pattern, text)
    return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

# %%


import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR [123] Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.findall(regex, log)
print(result)
# %%

print(re.search(regex, "99 elephants in a [12f3]"))
# %%
# e extract_pid function, to return the uppercase message in parenthesis, after the process id

import re
def extract_pid(log_line):
    regex = r"\[(\d+)\].* ([A-Z]{2,})"
    # result = re.search(regex, log_line)
    return re.findall(regex, log_line)
    # if result is None:
    #     return None
    # return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

# %%

my_emails = 'anshu.bantra@egd.com.au, anshubantra@gmail.com, anshu_bantra@yahoo.com'
re.findall(r"[\w.%+-]+@[\w.-]+", my_emails)
re.findall(r"([\w.%+-]+)@", my_emails)
re.findall(r"@([\w.-]+)", my_emails)

# %%
## Advanced RegEx Quiz

# Question 1
'''You’re working with a CSV file that contains employee information. Each record has a name field, followed by a phone number field, and a role
field. The phone number field contains U.S. phone numbers and needs to be modified to the international format, with "+1-" in front of the phone
number. The rest of the phone number should not change. Fill in the regular expression, using groups, to use the transform_record function to do
that.'''

import re
def transform_record(record):
    new_record = re.sub(r'(\w+),([0-9]{3}-[0-9]{3}-?[0-9]{4}),(\w+)', r'\1,+1-\2,\3', record)
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
# %%

# Question 2
# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.

import re
def multi_vowel_words(text):
    pattern = r' ?(\w+[a|e|io|u]{3,}\w+) ?'
    result = re.findall(pattern, text)
    return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

# %%


import re
def transform_comments(line_of_code):
    result = re.sub(r'(\w+)? ?([#]+)([\w\s]+)', r'\1 // \3', line_of_code)
    return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

# %%


import re
def transform_comments(line_of_code):
    result = re.sub(r'#+', r'//', line_of_code)
    return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"

# %%

re.sub(r'(\w+)? ?([#]+)([\w\s]+)', r'//','### Start of program')
# %%

import re
def convert_phone_number(phone):
    result = re.sub(r'(.*)([0-9]{3})-([0-9]{3}-[0-9]{4})(.*)', r'\1(\2) \3\4', phone)
    return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

# %%

re.findall(r'(.*)([0-9]{3})-([0-9]{3}-[0-9]{4})(.*)', "My number is 212-345-9999.")
# %%

re.sub(r'(.*)([0-9]{3})-([0-9]{3}-[0-9]{4})(.*)', r'\1(\2) \3\4',"My number is 212-345-9999.")
# %%


import re

def transform_comments(line):
    # Substitute any number of hash marks at the beginning of a line with double slashes
    return re.sub(r'#+', '//', line)

# Example usage
print(transform_comments("# This is a comment"))
print(transform_comments("what is ## This is another comment"))
print(transform_comments("### Another one"))

# %%


import re

def convert_phone_number(phone):
    # This regex pattern matches the phone number format XXX-XXX-XXXX
    pattern = r'\b(\d{3})\b-(\d{3})-(\d{4})'
    # Substitute with the desired format (XXX) XXX-XXXX
    formatted_phone = re.sub(pattern, r'(\1) \2-\3', phone)
    return formatted_phone

# Example usage
print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300

# %%
