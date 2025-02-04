import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from ..smth.current_enum import curr_lst
from .scrape_helper import get_datetime
from ..db import save_to_db, get_dataframe_from_db
from .ex_rows import ex_rows
#import sys
#print(sys.path)

# CLI Menu to choose which table to perform scraping on
while True:
    for idx, table in enumerate(curr_lst, start=1):
        print(idx, table)
    n = input("Add to which table: ")
    n = int(n)
    if n < 0 or n > len(curr_lst):
        print('Not a selection. Try Again\n')
        continue
    
    selected_table = curr_lst[n-1]
    print('selected table: ', selected_table)

    # if url is not None and selected_table is not None:
    if selected_table is not None:
        break


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(ex_rows, 'html.parser')
    
# Find all rows in the table
rows = soup.find_all('tr')

# Loop through each table row and extract the time (only up to 3 for trial)
datetime_lst = []
TD_COL_NUM = 10

for row in rows:
    final_datetime = get_datetime(row, TD_COL_NUM)
    datetime_lst.append(final_datetime)

    if len(datetime_lst) >= 5:
        break
    
print('count ', len(datetime_lst), datetime_lst)

# Add datetime list to corresponding pandas dataframe
df = get_dataframe_from_db(selected_table)

df['Auction Time'] = datetime_lst

# save to sqlite3 db
save_to_db(df, selected_table)


#else:
#    print('Failed to retrieve the webpage')


