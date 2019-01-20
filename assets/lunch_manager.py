"""
class that manages lunches
"""


import random
from location_finder import LocationFinder


class LunchManager:

    # coordinates for the workplace
    x_cord = 0
    y_cord = 0

    def __init__(self):
        self.location_finder = LocationFinder(self.x_cord, self.y_cord)

    def choose_lunch(self):
        return self.location_finder.get_location
