# %%
import re

def repeating_letter_a(text):
    result = re.search(r"(a.*a)", text, re.IGNORECASE)
    return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
# %%
print(re.search(r'colou?r', 'colour'))
print(re.search(r'colou?r', 'color'))
# %%

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))
print(re.search(r"\w* *", "This is an example"))
# %%
# Code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.
import re
def check_character_groups(text):
  result = re.search(r"(\w+) (\w+)", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
# %%
import re
pattern = r"^[a-zA-Z_ ][a-zA-Z0-9_ ]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isnt a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))
# %%

# code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 

import re
def check_sentence(text):
    result = re.search(r"^[A-Z][A-Za-z ]*[!|\.|\?]$", text)
    return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A STAR is born.")) # True
# %%
'''
The check_web_address function checks if the text passed qualifies as a
top-level web address, meaning that it contains alphanumeric characters
(which includes letters, numbers, and underscores), as well as periods, dashes,
and a plus sign, followed by a period and a character-only top-level domain such
as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using
escape characters, wildcards, repetition qualifiers, beginning and end-of-line
characters, and character classes.
'''

import re
def check_web_address(text):
    pattern = r'[www.]?[a-zA-Z]+\.[a-zA-Z]+$'
    result = re.search(pattern, text)
    return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
# %%

# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?

import re
def check_time(text):
    pattern = r'^[0|1]?[0-9]+:[0-5]+[0-9]+ ?[a|p]m$'
    result = re.search(pattern, text, re.IGNORECASE)
    return result, result != None

print(f'12:45pm        ==> {check_time("12:45pm")}') # True
print(f'9:59 AM        ==> {check_time("9:59 AM")}') # True
print(f'6:60am         ==> {check_time("6:60am")}') # False
print(f"five o'clock   ==> {check_time("five o'clock")}") # False
print(f'6:02 am        ==> {check_time("6:02 am")}') # True
print(f'6:02km         ==> {check_time("6:02km")}') # False
print(f'602 am         ==> {check_time("602 am")}') # False
# %%

import re
def contains_acronym(text):
  pattern = r'\([A-Z|0-9]+[a-zA-Z]+\)'
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True
# %%

import re

def correct_function(text):
  pattern = r" +([0-9]{5}-?[0-9]{,4})" # -?[0-9]{4}?
  result = re.search(pattern, text)  # Corrected regex pattern with space
  return re.findall(pattern, text), result is not None


def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False
# %%

import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])
# %%

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")
# %%

import re
def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Ritchie, Dennis")
# %%
import re
def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")
# %%
