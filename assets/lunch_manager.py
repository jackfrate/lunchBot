"""
class that manages lunches
"""


import random


class LunchManager:

    locations = [
        "Wendy's",
        "McDonald's",
        "Chipotle",
        "Pi Craft",
        "Smash Burger",
        "Amiel's",
        "starve"
    ]

    def choose_lunch(self):
        return self.locations[random.randint(0, len(self.locations) - 1)]
