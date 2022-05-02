class Vehicle:

    def __init__(self, current_speed=0, speed_cont=60, max_speed=151):
        self._current_speed = current_speed
        self.speed_cont = speed_cont
        self._max_speed = max_speed

    def move(self):
        return self.current_speed


    @property #get
    def current_speed(self):
        return self._current_speed

    @current_speed.setter #set
    def current_speed(self, new_current_speed):
        if new_current_speed < 0:
            self._current_speed = 0
        elif new_current_speed > self._max_speed:
            self._current_speed = self._max_speed
        else:
            self._current_speed = new_current_speed



