import re

email = input('Enter your email: ').strip()

# username, domain = email.split('@')
# if username and '.' in domain:
#     print('Valid')
# else:
#     print('Invalid')

if re.search(r'^[\w\.]+@[\w\.]+\.[a-z]+', email, re.IGNORECASE):  
    print('Valid')
else:
    print('Invalid')