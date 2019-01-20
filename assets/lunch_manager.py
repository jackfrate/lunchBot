"""
class that manages lunches
"""


import random


class LunchManager:

    # coordinates for the workplace
    x_cord = 0
    y_cord = 0

    def choose_lunch(self):
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
