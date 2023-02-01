## orasiadagi asofa


# Importing the geodesic module from the library
from geopy.distance import geodesic
  
# Loading the lat-long data for Kolkata & Delhi
# kolkata = p1
# delhi = p2
  
# Print the distance calculated in km
# dd = (geodesic(kolkata, delhi).km)
# p = (int(dd))
# print(p,'km')








## eng qisaqa

# Importing the great_circle module from the library
from geopy.distance import great_circle
  
# Loading the lat-long data for Kolkata & Delhi
# kolkata = p1
# delhi = p2
  
# Print the distance calculated in km
# print(great_circle(kolkata, delhi).km)






def distnca_city(A,B):
    birinchi_shaxar = A
    ikkinchi_shaxar = B
    return (great_circle(birinchi_shaxar, ikkinchi_shaxar).km)

# p1 = [41.324625, 69.238781]
# p2 = [41.224739, 69.249369]

# dd = distnca_city(p1, p2)
# print(dd)
# butun = int(dd)
# print(butun,'-' ,'km')

    







































# import math


# p1 = [41.324625, 69.238781]
# p2 = [41.224739, 69.249369]

# distance = math.sqrt((( p1[0] - p2[0])  **2 )  +  (( p1[1] - p2[1] ) ** 2 ))

# print(distance)





# from shapely.geometry import LineString, Polygon
# line = LineString(p1, p2)
# part_outside_len = float(line.difference(polygon).length) / float(line.length)





















# # from shapely.geometry import Point
# # patch = Point(0.0, 0.0).buffer(10.0)
# # print(patch)







# #### shaxar malumotlari 


# # from opencage.geocoder import OpenCageGeocode
# # from pprint import pprint



# key = '74947a47d301407ab39b67d79737c615'
# geocoder = OpenCageGeocode(key)

# results = geocoder.reverse_geocode(41.324625, 69.238781)
# # pprint(results)























# ##### geodaniyi

# from opencage.geocoder import OpenCageGeocode
# key = '74947a47d301407ab39b67d79737c615'  # get api key from: https://opencagedata.com
# geocoder = OpenCageGeocode(key)
# query = 'toshkent' 
# results = geocoder.geocode(query)
# lat = results[0]['geometry']['lat']
# lng = results[0]['geometry']['lng']
# print (  lat, lng)







































#  ## mSOfani chiqarish

# # def find_distance(A,B):
# #     key = '74947a47d301407ab39b67d79737c615'  # get api key from:  https://opencagedata.com
# #     geocoder = OpenCageGeocode(key)
    
# #     result_A = geocoder.geocode(A)
# #     lat_A = result_A[0]['geometry']['lat']
# #     lng_A = result_A[0]['geometry']['lng']
    
# #     result_B = geocoder.geocode(B)
# #     lat_B = result_B[0]['geometry']['lat']
# #     lng_B = result_B[0]['geometry']['lng']  
    
# #     print(geodesic((lat_A,lng_A), (lat_B,lng_B)).kilometers)




# # find_distance('41.324625, 69.238781','41.224739,69.249369')










