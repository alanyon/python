""" 

 A module defining a function that reads in two latitude/longitude coordinates 
  and returns the distance and angular seperation between them.

"""

# Import modules
from math import radians, cos, sin, asin, sqrt
import numpy as np

def haversine(lat1, lon1, lat2, lon2, arc = False, \
              bearing = False, components = False):

    '''

     A function to return the distance (and angle) between two lat/lon points

    '''

    # Set Earth's mean radius constant, in km
    earth_radius = 6371

    # Convert latitude/longitude values into radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Calculate difference in latitude and longitude coordinates 
    dlon = lon1 - lon2
    dlat = lat1 - lat2
    
    # Haversine formula components
    a_NS = sin(dlat/2)**2
    a_EW = cos(lat1) * cos(lat2) * sin(dlon/2)**2
    
    # Calculate angular displacement and length of arc between points 
    c = 2 * asin(sqrt(a_NS + a_EW)) 
    km = earth_radius * c
    
    # Calculate arc NS/EW components
    c_NS = 2 * asin(sqrt(a_NS)) 
    km_NS = earth_radius * c_NS
    
    c_EW = 2 * asin(sqrt(a_EW)) 
    km_EW = earth_radius * c_EW
    
    # Convert into x/y values
    if lat1 < lat2:
        km_NS = -1*km_NS

    if lon1 < lon2:
        km_EW = -1*km_EW
    
    # Calculate the bearing between the points
    pts_bearing = np.arctan2(km_EW, km_NS)

    return_list = [km]

    # Return distance between points AND/OR angular displacement AND/OR bearing 
    #  between points AND/OR NS/EW components of displacement
    if arc == True:
        return_list.append(c)
    if bearing == True:
        return_list.append(pts_bearing)
    if components == True:
        return_list.extend([km_EW, km_NS])

    return return_list