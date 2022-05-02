import vehicle

class Plane(vehicle.Vehicle):
    def __init__(self, altitude=0):
        self.altitude = altitude
        super().__init__()

    def move(self):
        self._current_speed = 15
        self.altitude = 31000
        self.speed_cont = 120
        self._max_speed = 500
        return f'The current altitude is {self.altitude} feet and your current speed is {self.current_speed} mph'

