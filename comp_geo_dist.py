# Gallegos, Isaac 9-13-2018
# Homewrok 2

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.distance import great_circle

# Create a geolocator object to access geo data using Nominatum
geolocator = Nominatim(user_agent="comp_geo_dist.py")

# A query address
query1 = "1314 chavez st, las vegas, nm"
query2 = "1701 bryant st, denver, co"

# Build/retrieve a geopy Location object with query addresses
location1 = geolocator.geocode(query1)
location2 = geolocator.geocode(query2)

# Access the latitude and longitude from location objects
coordinates1 = (location1.latitude, location1.longitude)
coordinates2 = (location2.latitude, location2.longitude)
print(query1, coordinates1)
print(query2, coordinates2)

# Compute and print the distance between locations
distance = great_circle(coordinates1, coordinates2).miles
print("Distance in miles", distance)