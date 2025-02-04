# Geocoding with OpenStreetMap API (free service compared to Google Maps API)
import ssl
import certifi
import geopy.geocoders
import numpy as np

def setup_geolocator():
    """
    Connect to OpenStreetMap API for Geolocation
    Get around SSL issues
    """
    try:
      ctx = ssl.create_default_context(cafile=certifi.where())
      geopy.geocoders.options.default_ssl_context = ctx
      geolocator = geopy.geocoders.Nominatim(user_agent="gabriel.grinstein@gmail.com")
      return geolocator
    
    except Exception as error:
      print('setup_geolocator ERROR! ', error)

def service_geocode(geolocator, address):
    """
    Unique Address --> Lat/Lng
    If location not found during geocoding, return NaN
    Return string because sqlite3 does not accept tuple/s
    """
    location = geolocator.geocode(address)

    if location != None:

      print('location', location)
      
      #return (location.latitude, location.longitude)
      return f"{location.latitude}, {location.longitude}"
    else:
      return np.NaN, np.NaN
    

def geocode_location(geolocator, address):
  location = geolocator.geocode(address)

  if location != None:
    print('location: ', location)
    return location
  else:
    return np.NaN
  
def get_lat_lon(location):
   if location != None or location != np.NaN:
      return f"{location.latitude}, {location.longitude}"

def get_zipcode(location):
  if location != None or location != np.NaN:
    data = location.raw
    loc_data = data['display_name'].split()
    # print(loc_data)
    print("Zip code : ", loc_data[-3])
    zipcode = str(loc_data[-3]).rstrip(',')
    return zipcode