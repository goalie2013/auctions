import pandas as pd
from geocoding import setup_geolocator, service_geocode
from db import save_to_db

# CSV file to pandas dataframe
CSVFile = 'CA_KERN_Auctions.csv'
auctions = pd.read_csv(CSVFile)

# Make new table/df with only desired columns
df = auctions[["Auction ID", "Unique #", "State", "County Name", "Parcel Location", "Minimum Bid Owed", "Property Description"]]

df.rename(columns={"Parcel Location": "Street Address"})
df['Street Address'] = df['Street Address'].str.replace('BAKERSFIELD', '')
df['Street Address'] = df['Street Address'].str.strip()

# Combine Address w/ county, state, & country for geocoding to work
df.loc[:, 'Country'] = 'USA'
l_cols_concat = ['County Name','State','Country']
df['Unique_Address'] = df['Street Address'].str.cat(others=df[l_cols_concat], sep=', ',na_rep='')

# geocode
geolocator = setup_geolocator()
df['LAT_LON'] = df['Unique_Address'].apply(lambda d: service_geocode(geolocator, d))


# save to sqlite3 db
save_to_db(df, 'kern_ca')


# Go through csv folder; skip if name already in enum/list/dict
# use name from csv file; lowercase and ....
def create_table():
    pass