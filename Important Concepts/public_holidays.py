import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://business.vic.gov.au/business-information/public-holidays/victorian-public-holidays-2025"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing public holidays (assuming it is in a table)
    table = soup.find('table')

    # Extract the header and rows from the table
    headers = [header.text.strip() for header in table.find_all('th')]
    rows = table.find_all('tr')[1:]  # Skip the header row

    # Create a list to store the public holidays
    public_holidays = []

    # Iterate through the rows and extract the data
    for row in rows:
        columns = row.find_all('td')
        holiday = {headers[i]: columns[i].text.strip() for i in range(len(headers))}
        public_holidays.append(holiday)

    # Print the public holidays
    for holiday in public_holidays:
        print(holiday)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
