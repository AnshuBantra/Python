# %%

def email_list(domains):
	emails = []
	for domain, users in domains.items():
	  for user in users:
	    emails.append(user+"@"+domain)
	return(emails)

dict_1 = {  "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
		    "yahoo.com": ["barbara.gordon", "jean.grey"],
			"hotmail.com": ["bruce.wayne"]
		}

print(email_list(dict_1))

# %%
import pprint as ppt
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# print(group, users)
		
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
			# user_groups[user] = user_groups.get(user).append(group)

	return(user_groups)

d1 = {  "local": ["admin", "userA"],
        "public":  ["admin", "userB"],
		"administrator": ["admin"]
	}

ppt.pprint(groups_per_user(d1))
# %%

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
wardrobe
# %%

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for value in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += value
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {   "bananas": 1.56,
			    "apples": 2.50,
				"oranges": 0.99,
				"bread": 4.59,
				"coffee": 6.99,
				"milk": 3.39,
				"eggs": 2.98,
				"cheese": 5.44
			}

print(add_prices(groceries)) # Should print 28.44
# %%
