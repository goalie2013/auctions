import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from smth.current_enum import Current, curr_lst
from scrape_helper import get_datetime
from db import save_to_db, get_dataframe_from_db


# URL of the website to scrape
# base_url = 'https://example.com/'
# url = urljoin(base_url, 'housing')

while True:
    url = input("Enter URL: ")

    for idx, table in enumerate(curr_lst, start=1):
        print(idx, table)
    n = input("Add to which table: ")
    n = int(n)
    curr_table = curr_lst[n-1]
    print('selected table: ', curr_table)

    if url is not None and curr_table is not None:
        break

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all rows in the table
    rows = soup.find_all('tr')

    # Loop through each row
    count = 0
    datetime_lst = []

    for row in rows:
        final_datetime = get_datetime(row, 10)
        datetime_lst.append(final_datetime)
        count += 1
        
    print('count ', count)

    # Add datetime list to corresponding pandas dataframe
    df = get_dataframe_from_db(curr_table)

    df['Auction Time'] = datetime_lst

    # save to sqlite3 db
    save_to_db(df, curr_table)


else:
    print('Failed to retrieve the webpage')


