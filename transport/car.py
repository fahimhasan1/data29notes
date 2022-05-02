import vehicle

class Car(vehicle.Vehicle):
    def __init__(self):
        super().__init__()

    def move(self):
        self._current_speed = 0
        self.speed_cont = 30
        self._max_speed = 120
        return f'Your current speed is {self.current_speed} mph'
