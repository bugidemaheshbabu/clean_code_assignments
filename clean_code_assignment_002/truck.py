from car import Car


class Truck(Car):
    def __init__(self, color, max_speed,
                 acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        super().check_for_positive_values("max_cargo_weight", max_cargo_weight)
        self._max_cargo_weight = max_cargo_weight
        self.current_cargo_weight = 0

    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight

    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")

    def load(self, cargo_weight):
        if not self.current_speed:
            super().check_for_positive_values("cargo_weight", cargo_weight)
            self.current_cargo_weight += cargo_weight
            if self.current_cargo_weight > self.max_cargo_weight:
                self.current_cargo_weight -= cargo_weight
                print("Cannot load cargo more than max limit: {}"
                      .format(self.max_cargo_weight))
        else:
            print("Cannot load cargo during motion")

    def unload(self, cargo_weight):
        if not self.current_speed:
            super().check_for_positive_values("cargo_weight", cargo_weight)
            self.current_cargo_weight -= cargo_weight
            if self.current_cargo_weight < 0:
                self.current_cargo_weight = 0
        else:
            print("Cannot unload cargo during motion")
