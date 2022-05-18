import math
from math import radians, sin, cos, asin, sqrt

cities = [{"name": "Buenos Aires", "lat": -34.58333333, "lon": -58.666667},
          {"name": "Vienna", "lat": 48.2, "lon": 16.366667},
          {"name": "Baku", "lat": 40.38333333, "lon": 49.866667},
          {"name": "Beijing", "lat": 39.91666667, "lon": 116.383333},
          {"name": "Paris", "lat": 48.86666667, "lon": 2.333333},
          {"name": "Berlin", "lat": 52.51666667, "lon": 13.4},
          {"name": "Dublin", "lat": 53.31666667, "lon": -6.233333},
          {"name": "Mexico City	", "lat": 19.43333333, "lon": -99.133333},
          {"name": "Lisbon", "lat": 38.71666667, "lon": -9.133333},
          {"name": "Washington", "lat": 38.883333, "lon": -77},
          {"name": "Ankara", "lat": 39.93333333, "lon": 32.866667},
          ]

city_name = []
city_lat = []
city_lon = []


for dic in cities:
    city_name.append(dic["name"])
    city_lat.append(dic["lat"]) 
    city_lon.append(dic["lon"])

def haversine(departure, arrival):
    r = 6371 # r : Radius of the earth which is 6371 km
    dep_lat = math.radians(city_lat[city_name.index(departure)])
    dep_lon = math.radians(city_lon[city_name.index(departure)])
    arr_lat = math.radians(city_lat[city_name.index(arrival)])
    arr_lon = math.radians(city_lon[city_name.index(arrival)])
    
    
    d = 2 * r * math.asin(math.sqrt(math.sin((arr_lat - dep_lat) / 2)**2 + math.cos(dep_lat) * math.cos(arr_lat) * math.sin((arr_lon-dep_lon)/2)**2))
    # returns the distance between two points in kilometers and data type is integer
    return int(d) 

def table_data(cities):
    # returns two different values which are :
    distance_data = []    
    for city in city_name:
        x = []
        for a in city_name:
            x.append(haversine(city, a))
        
        distance_data.append(x)

    name_of_cities = city_name
    return name_of_cities, distance_data



# This method will print data in tabular format to console.
def print_table(cities, distance_data):
    row_format = "{:15}" * (len(cities) + 1)
    print(row_format.format("", *cities))
    for city, row in zip(cities, distance_data):
        print(row_format.format(city, *row))


# These two lines required entry point of your program, code execution will be started from here
name_of_cities, distance_data = table_data(cities)
print_table(name_of_cities, distance_data)


