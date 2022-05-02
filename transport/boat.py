import vehicle

class Boat(vehicle.Vehicle):
    def __init__(self):
        super().__init__()

    def move(self):
        self._current_speed = 8
        self.speed_cont = 15
        self._max_speed = 150
        return f'Your current speed is {self.current_speed} mph'
