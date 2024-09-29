# import pandas as pd


# df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter','number'])
# df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter','number'])

# df_with_more_rows = pd.concat([df1, df2])
# df_with_more_columns = pd.concat([df1, df2], axis=1)

# print(df_with_more_rows)# Write your code here :-)


# def calculate_result(expression):
#     try:
#         # Use eval to evaluate the expression
#         result = eval(expression)
#         # Round the result to one decimal place
#         rounded_result = round(result, 1)
#         return rounded_result
#     except Exception as e:
#         return f"Error: {e}"

# # Get user input for the mathematical expression
# user_input = input("Enter a mathematical expression (e.g., 1 + 1, 4 / 3): ")

# # Call the function to calculate and display the result
# result = calculate_result(user_input)
# print(f"Result: {result}")

# import pandas as pd
# url = "https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version"

# # Read HTML tables from the webpage
# tables = pd.read_html(url)

# # # Print the number of tables found
# # print(f"Number of tables found: {len(tables)}")

# # # If tables are found, print the first table
# # if len(tables) > 0:
# #     print("\nFirst Table:")
# #     print(tables[0])

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version"

# # Send a GET request to the URL
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Find the table with the specified class
#     table = soup.find('table', class_='table-bordered')

#     if table:
#         # Extract table data
#         rows = table.find_all('tr')
#         table = []
#         for row in rows:
#             # Extract data from each cell in the row
#             cells = row.find_all(['td', 'th'])
#             row_data = [cell.get_text(strip=False) for cell in cells]
#             # if 'Sweet' in row_data: # and 'Cherries' in row_data:
#             #     print(row_data)
#             table.append(row_data)
#     else:
#         print("Table not found on the webpage.")
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# # print(cells)
# # print(row_data)
# heading = [_.replace('\n', ' ').replace('\t', '') for _ in table[0] ]
# # print(heading, end='\n\n\n')
# fruit_data = {}
# for row in table[1:]:
#     row_dict = {}
#     dict_key = ''
#     for sr, element in enumerate(row, start=1):
#         if '\n' in element:
#             # print(sr, heading[sr-1], element.split('\n')[0])
#             element = element.split('\n')[0]
#         if sr == 1:
#             dict_head = element
#         else:
#             row_dict[heading[sr-1]] = element
#     # fruit_data.append(row_dict)
#     fruit_data[dict_head] = row_dict

# for key in fruit_data.keys():
#     print(key, fruit_data[key]['Calories'])


# # for row in table[1:]:
# #     # row_dict = {}
# #     # dict_key = ''
# #     for sr, element in enumerate(row, start=1):
# #         if '\n' in element:
# #             # print(sr, heading[sr-1], element.split('\n')[0])
# #             print(  element, '\t',
# #                     # element.replace('\t', '')
# #                     element.split('\t')[0]
# #                 )


import requests
from bs4 import BeautifulSoup

url = "https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with the specified class
    table = soup.find('table', class_='table-bordered')

    if table:
        rows = table.find_all('tr')
        table = []
        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_data = [cell.get_text(strip=False) for cell in cells]
            table.append(row_data)
    else:
        print("Table not found on the webpage.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

heading = [_.replace('\n', ' ').replace('\t', '') for _ in table[0] ]
fruit_data = {}
for row in table[1:]:
    row_dict = {}
    dict_key = ''
    for sr, element in enumerate(row, start=1):
        if '\n' in element:
            element = element.split('\n')[0].strip()
        if sr == 1:
            dict_head = element.strip().upper()
        else:
            row_dict[heading[sr-1]] = element
    fruit_data[dict_head] = row_dict
fruit_data['HONEYDEW MELON'] = fruit_data.pop('HONEYDEW')
fruit_data['SWEET CHERRIES'] = fruit_data.pop('SWEET')

fruit = input('Item: ').upper()
if fruit in fruit_data:
    print(f"Calories: {fruit_data.get(fruit)['Calories']}")
