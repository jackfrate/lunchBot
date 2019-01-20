"""
class that finds the locations nearby
uses the coordinates
"""


import random


class LocationFinder():

    def __init__(self, x_cord, y_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord

    def get_location(self):
        locs = [
            "Wendy's",
            "McDonald's",
            "Chipotle",
            "Pi Craft",
            "Smash Burger",
            "Amiel's",
            "starve"
        ]

        return locs[random.randint(0, len(locs) - 1)]
