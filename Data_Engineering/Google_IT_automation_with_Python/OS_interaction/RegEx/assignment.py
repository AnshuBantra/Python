# %%
import re

def secure_website_domain(website):
    pattern = r'https://www.(.+)\.com?$' # enter the regex pattern here
    result = re.search(pattern, website) # enter the re method here
    if result is None:
        return ""
    return result[1]# enter the correct capturing group


print(secure_website_domain("http://www.text.com")) #Should return nothing
print(secure_website_domain("https://www.text.com")) #Should return text
print(secure_website_domain("http://www.text.co")) #Should return nothing
print(secure_website_domain("https://www.text.co")) #Should return text
# %%

def parse_sentences(sentence):
 pattern =r' ' #enter the regex pattern here
 result = re.split(pattern, sentence) #enter the re method  here
 return result

print(parse_sentences("Hello! How are you doing?")) # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("what a beautiful day it is")) # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("2 + 2 is definitely 4!")) # should return ['2', '+', '2', 'is', 'definitely', '4!']

# %%

def find_isbn(list):
  pattern = r'^\d{3}-\d-\d{2}-(\d{6})-\d$' #enter the regex pattern here
  result = re.search(pattern, list) #enter the re method  here
  if result is None:
    return ""
  return result[1] #return the correct capturing group


print(find_isbn("123-4-12-098754-0")) # Should return 098754
print(find_isbn("223094-AB-30")) # result should be blank
print(find_isbn("1123-4-12-098754-0")) # result should be blank
# %%

def find_gov_urls(website):
 pattern = r'^https://www.' #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result


print(find_gov_urls("https://www.data.gov is a great place to find open source datasets!")) # Should return ['https://www.data.gov']
print(find_gov_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov.")) # Should return ['https://www.nps.gov', 'https://www.recreation.gov']
print(find_gov_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!")) # Should return ['https://www.loc.gov']
print(find_gov_urls("The Library of Congress (www.loc.gov) is an incredible resource!")) # Should return []
# %%
"https://www.data.gov is a great place to find open source datasets!")) # Should return ['https://www.data.gov']
"Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov.")) # Should return ['https://www.nps.gov', 'https://www.recreation.gov']
"The Library of Congress (https://www.loc.gov) is an incredible resource!")) # Should return ['https://www.loc.gov']
"The Library of Congress (www.loc.gov) is an incredible resource!")) # Should return []

# %%

import re

def find_https_urls(text):
    pattern = r'https://[\w.-]+'
    return re.findall(pattern, text)

# Test the function
print(find_https_urls("https://www.data.gov is a great place to find open source datasets!"))
# Should return ['https://www.data.gov']

print(find_https_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov."))
# Should return ['https://www.nps.gov', 'https://www.recreation.gov']

print(find_https_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!"))
# Should return ['https://www.loc.gov']

print(find_https_urls("The Library of Congress (www.loc.gov) is an incredible resource!"))
# Should return []

# %%


def parse_city_country(text):
    pattern = r'[,|.|!]' #enter the regex pattern here
    result = re.split(pattern, text) #enter the re method  here
    if len(result) != 2:
        return ""
    return result[0]#return the correct capturing group

print(parse_city_country("Paris, France")) # should return Paris
print(parse_city_country("Mumbai, India")) # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil")) # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank


# %%
def parse_city_country(text):
    pattern = r'([\w ]*)[,|.|!]([ \w]+)' #enter the regex pattern here
    result = re.search(pattern, text) #enter the re method  here
    print(type(result))
    return result[0]
    # if len(result) != 2:
    #     return ""
    # return result[1]#return the correct capturing group

print(f'Paris, France          ==> {parse_city_country("Paris, France")}') # should return Paris
print(f'Mumbai, India          ==> {parse_city_country("Mumbai, India")}') # should return Mumbai
print(f'Rio de Janeiro. Brazil ==> {parse_city_country("Rio de Janeiro. Brazil")}') # should return Rio de Janeiro
print(f'Tokyo! Japan           ==> {parse_city_country("Tokyo! Japan")}')  # result should be blank
# %%
