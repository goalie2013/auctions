import pandas as pd
import numpy as np
import os
from .geocoding import setup_geolocator, service_geocode
from .db import save_to_db
from .csvs import csv_dict


FOLDER = "app/csv/"
new_csv_dict = {}


def create_table(filename):
    auctions = pd.read_csv(filename)
    
    # Make new table/df with only desired columns
    df = auctions[["Auction ID", "Unique #", "State", "County Name", "Parcel Location", "Minimum Bid Owed", "Property Description"]]

    df = df.rename(columns={"Parcel Location": "Street Address"})
    df["Min Bid 2x"] = df["Minimum Bid Owed"].apply(lambda x: x * 2)
    df["Min Bid 3x"] = df["Minimum Bid Owed"].apply(lambda x: x * 3)
    df['Country'] = 'USA'

    # FOR TEMP FILE ONLY: use only first 3 rows
    return df[:80]

def drop_row_if_addr_null(df):
    print(df["Street Address"])
    print('length df BEFORE drop: ', len(df))
    df = df.dropna(subset=["Street Address"])
    print('length df AFTER drop: ', len(df))
    df = df.reset_index()
    df = df.drop(columns=['index'])
    return df

def update_st_addr_col():
    #temp_df['Parcel Location'] = temp_df['Parcel Location'].str.replace('BAKERSFIELD', '')
    #temp_df['Parcel Location'] = temp_df['Parcel Location'].str.strip()
    temp_df["Street Address"] = temp_df["Street Address"].str.replace('BAKERSFIELD', '')
    temp_df["Street Address"] = temp_df["Street Address"].str.strip()
    

def create_full_address(df):
    # Combine Address w/ county, state, & country for geocoding to work
    l_cols_concat = ['County Name','State','Country']
    df['Unique_Address'] = df['Street Address'].str.cat(others=df[l_cols_concat], sep=', ',na_rep='')
    return df



CSVFile = 'app/csv/CA_KERN_Auctions.csv'
temp_df = create_table(CSVFile)
temp_df = drop_row_if_addr_null(temp_df)

#TODO: SPECIFIC TO ONE CSV!!!!!
temp_df["Street Address"] = temp_df["Street Address"].str.replace('BAKERSFIELD', '')
temp_df["Street Address"] = temp_df["Street Address"].str.strip()

# Combine Address w/ county, state, & country for geocoding to work
l_cols_concat = ['County Name','State','Country']
temp_df['Unique_Address'] = temp_df['Street Address'].str.cat(others=temp_df[l_cols_concat], sep=', ',na_rep='')

print(temp_df)