""" **Distance Between Two Cities**
    Calculates the distance between two cities and allows the user
    to specify a unit of distance. This program may require finding
    coordinates for the cities like latitude and longitude.
"""


from pygeocoder import Geocoder
import numpy as np
import sys


def get_distance(loc_a, loc_b):
    # use haversine formula
    earth_rad = 6371.0
    dlat = np.deg2rad(loc_b[0] - loc_a[0])
    dlon = np.deg2rad(loc_b[1] - loc_a[1])
    a = np.sin(dlat/2) ** 2 + \
        np.cos(np.deg2rad(loc_a[0])) * np.cos(np.deg2rad(loc_b[0])) * \
        np.sin(dlon/2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return earth_rad * c


def get_latlongs(location):
    return Geocoder.geocode(location)[0].coordinates


def main():
    city_a = input("First city > ")
    city_b = input("Second city > ")

    print(get_distance(get_latlongs(city_a),
                       get_latlongs(city_b)))


if __name__ == '__main__':
    sys.exit(main())