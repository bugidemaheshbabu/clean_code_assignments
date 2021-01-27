class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.check_for_positive_values("max_speed", max_speed)
        self.check_for_positive_values("acceleration", acceleration)
        self.check_for_positive_values("tyre_friction", tyre_friction)
        self._color = color
        self._acceleration = acceleration
        self._max_speed = max_speed
        self._tyre_friction = tyre_friction
        self._is_engine_started = False
        self._current_speed = 0

    @staticmethod
    def check_for_positive_values(attri, value):
        if value > 0:
            pass
        else:
            raise ValueError("Invalid value for {}".format(attri))

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def acceleration(self):
        return self._acceleration

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def tyre_friction(self):
        return self._tyre_friction

    @property
    def color(self):
        return self._color

    @property
    def is_engine_started(self):
        return self._is_engine_started

    def start_engine(self):
        self._is_engine_started = True

    def accelerate(self):
        if self.is_engine_started:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
            else:
                self._current_speed = self.max_speed
        else:
            print("Start the engine to accelerate")

    def apply_brakes(self):
        if self.is_engine_started:
            if self.current_speed - self.tyre_friction > 0:
                self._current_speed -= self._tyre_friction
            else:
                self._current_speed = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")

    def stop_engine(self):
        if self.is_engine_started:
            self._is_engine_started = False
