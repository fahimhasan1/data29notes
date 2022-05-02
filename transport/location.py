import random


class Location:
    import random

    def __init__(self):
        self.glasgow= {"Glasgow": 412}
        self.manchester = {"Manchester": 208}
        self.birmingham = {"Birmingham": 125}
        self.cardiff = {"Cardiff": 149}
        self.spain = {"Spain": 1073}
        self.australia = {"Australia": 9462}
        self.dist = 0

    def chosen_location(self):
        loc = [self.glasgow, self.manchester,self.birmingham, self.cardiff, self.spain, self.australia]
        a = random.choice(loc)
        location = a.popitem()
        self.dist = location[1]
        return f'You are currently in London and your destination is {location[0]} which is {location[1]} miles away.'










