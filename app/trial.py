import pandas as pd
import numpy as np
import os
from .geocoding import setup_geolocator, geocode_location, get_zipcode, get_lat_lon
from .db import save_to_db
from .csvs import csv_dict
from .scrape.property_estimate import get_property_estimate

"""
# CSV file to pandas dataframe
CSVFile = 'CA_KERN_Auctions.csv'
auctions = pd.read_csv(CSVFile)

# Make new table/df with only desired columns
df = auctions[["Auction ID", "Unique #", "State", "County Name", "Parcel Location", "Minimum Bid Owed", "Property Description"]]

# FOR TEMP FILE ONLY: use only first 3 rows
temp_df = df[:3]

temp_df['Parcel Location'] = temp_df['Parcel Location'].str.replace('BAKERSFIELD', '')
temp_df['Parcel Location'] = temp_df['Parcel Location'].str.strip()
temp_df = temp_df.rename(columns={"Parcel Location": "Street Address"})
print(temp_df["Street Address"])

# Combine Address w/ county, state, & country for geocoding to work
# temp_df.loc[:, 'Country'] = 'USA'
temp_df['Country'] = 'USA'
l_cols_concat = ['County Name','State','Country']
temp_df['Unique_Address'] = temp_df['Street Address'].str.cat(others=temp_df[l_cols_concat], sep=', ',na_rep='')

# geocode
geolocator = setup_geolocator()
temp_df['LAT_LON'] = temp_df['Unique_Address'].apply(lambda d: service_geocode(geolocator, d))


# save to sqlite3 db
save_to_db(temp_df, 'kern_ca_temp')

#if __name__ == "__main__":
#    app.run(debug=True)
"""

FOLDER = "app/csv/"
new_csv_dict = {}

def get_unused_csv_files():
    """
    Get csv files from csv/ folder
    Iterate through files; if filename already in dictionary
    then remove from new list.
    If filename not in dictionary, then add to new dictionary to use to create table/db
    """
    
    csv_files = os.listdir(FOLDER)
    print(csv_files, len(csv_files))

    for csv in csv_files:
        if csv in csv_dict:
            print(f"{csv} is in")
            csv_files.remove(csv)
        else:
            d_val = csv.removesuffix(".csv")
            new_csv_dict[csv] = d_val

    print(csv_files, len(csv_files))
    return csv_files


def _drop_row_if_addr_null(df):
    print(df["Street Address"])
    print('length df BEFORE drop: ', len(df))
    df = df.dropna(subset=["Street Address"])
    print('length df AFTER drop: ', len(df))
    df = df.reset_index()
    df = df.drop(columns=['index'])
    return df

def create_table(filename):
    auctions = pd.read_csv(filename)
    
    # Make new table/df with only desired columns
    df = auctions[["Auction ID", "Unique #", "State", "County Name", "Parcel Location", "Minimum Bid Owed", "Property Description"]]

    # Rename & create more columns
    df = df.rename(columns={"Parcel Location": "Street Address", "County Name": "County"})
    df["Min Bid 2x"] = df["Minimum Bid Owed"].apply(lambda x: x * 2)
    df["Min Bid 3x"] = df["Minimum Bid Owed"].apply(lambda x: x * 3)
    df['Country'] = 'USA'

    # FOR TEMP FILE ONLY: use only first 5 rows
    temp_df =  df[:2]
    temp_df = _drop_row_if_addr_null(temp_df)

    return temp_df

def update_st_addr_col():
    #temp_df['Parcel Location'] = temp_df['Parcel Location'].str.replace('BAKERSFIELD', '')
    #temp_df['Parcel Location'] = temp_df['Parcel Location'].str.strip()
    temp_df["Street Address"] = temp_df["Street Address"].str.replace('BAKERSFIELD', '')
    temp_df["Street Address"] = temp_df["Street Address"].str.strip()
    

def create_full_address(df):
    # Combine Address w/ county, state, & country for geocoding to work
    l_cols_concat = ['County','State','Country']
    df['Unique_Address'] = df['Street Address'].str.cat(others=df[l_cols_concat], sep=', ',na_rep='')
    return df

def create_lat_lon_column(df):
    # geocode
    geolocator = setup_geolocator()
    df['location'] = df['Unique_Address'].apply(lambda d: geocode_location(geolocator, d))
    df['Zipcode'] = df['location'].apply(lambda loc: get_zipcode(loc))
    df['LAT_LON'] = df['location'].apply(lambda loc: get_lat_lon(loc))
    
    df['Property Estimate'] = df.apply(lambda x: get_property_estimate(x['Street Address'], x['Zipcode']), axis=1)

    df = df.drop(columns=['location'])

    #df['LAT_LON'] = df['Unique_Address'].apply(lambda d: service_geocode(geolocator, d))
    return df

def create_estimate_column(df):
     for _, row in df.iterrows():
        address = row["Street Address"]
        zipcode = row["Zipcode"]



"""
csv_files = get_unused_csv_files()
for csv in csv_files:
    temp_df = create_table(f"{FOLDER}{csv}")
    update_st_addr_col()
    temp_df = create_full_address(temp_df)
    temp_df = create_lat_lon_col(temp_df)

    # save to sqlite3 db
    save_to_db(temp_df, new_csv_dict[csv])
"""

#csv_files = get_unused_csv_files()
#for csv in csv_files:
#temp_df = create_table(f"{FOLDER}{csv}")
CSVFile = 'app/csv/CA_KERN_Auctions.csv'
temp_df = create_table(CSVFile)

#TODO: SPECIFIC TO ONE CSV!!!!!
temp_df["Street Address"] = temp_df["Street Address"].str.replace('BAKERSFIELD', '')
temp_df["Street Address"] = temp_df["Street Address"].str.strip()

# Combine Address w/ county, state, & country for geocoding to work
l_cols_concat = ['County','State','Country']
temp_df['Unique_Address'] = temp_df['Street Address'].str.cat(others=temp_df[l_cols_concat], sep=', ',na_rep='')

# geocode: create column for lat/lon of addresses
#geolocator = setup_geolocator()
#temp_df['LAT_LON'] = temp_df['Unique_Address'].apply(lambda x: service_geocode(geolocator, x))
temp_df = create_lat_lon_column(temp_df)
print(temp_df)

# save dataframe to sqlite3 db
#save_to_db(temp_df, new_csv_dict[csv])
# save_to_db(temp_df, 'new_ca_kern_trial')