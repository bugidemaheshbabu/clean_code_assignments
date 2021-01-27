import math
from car import Car


class RaceCar(Car):
    def __init__(self, max_speed, acceleration, tyre_friction, color=None):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._nitro = 0

    @property
    def nitro(self):
        return self._nitro

    def sound_horn(self):
        if self.is_engine_started:
            print("Peep Peep\nBeep Beep")
        else:
            print("Start the engine to sound_horn")

    def apply_brakes(self):
        if self.current_speed > self.max_speed * 0.5:
            self._nitro += 10
        super().apply_brakes()

    def accelerate(self):
        super().accelerate()
        if self.nitro:
            self._nitro -= 10
            self._current_speed += math.ceil(self.acceleration * 0.3)
            if self._current_speed >= self.max_speed:
                self._current_speed = self._max_speed
