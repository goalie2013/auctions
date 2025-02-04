
def create_markers(df, min_price_filter = None, bid_date_filter = None) -> list:
    print('create_markers')
    # Prepare data for Jinja template
    marker_data = []

    for _, row in df.iterrows():
        
        price: float = row['Minimum Bid Owed']
        bid_time = str(row['Auction Time'])

        print(min_price_filter)

        # Optional query parameters 'min_price_filter' & 'bid_date_filter'
        if min_price_filter is not None and min_price_filter > price:
            continue
        
        if bid_date_filter is not None and bid_date_filter > bid_time:
            continue


        # Get indiv coordinates for lat & lon for markers
        lat_lon = row['LAT_LON']
        coord_arr = lat_lon.split(',')
        lat = coord_arr[0]
        lon = coord_arr[1]

        # Additional Info for Marker Popup (& for property estimate url)
        county = row['County Name'] # will need to change to 'County'
        state = row['State']
        address = row['Street Address']
        address2 = "+".join(address.split(' '))
        zipcode = row['Zipcode']

        # Format data for JavaScript
        marker_data.append({'lat': lat, 'lon': lon, 'price': price, 'address': address, 'address2': address2, 'zipcode': zipcode, 'county': county, 'state': state})

    return marker_data