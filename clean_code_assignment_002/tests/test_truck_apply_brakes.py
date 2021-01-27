from truck import Truck


# -------apply_brakes----
def test_apply_break_when_current_speed_is_greater_than_tyre_friction_returns_current_speed(truck1):
    # Arrange
    truck1.start_engine()
    truck1.accelerate()
    current_speed = 7

    # Act
    truck1.apply_brakes()

    # Assert
    assert truck1.current_speed == current_speed


def test_apply_break_when_current_speed_with_different_acceleration_more_than_tyre_friction_returns_current_speed():
    # Arrange
    truck = Truck(color="Red", max_speed=50, acceleration=10,
                  tyre_friction=3, max_cargo_weight=100)
    current_speed = 27
    truck.start_engine()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    # Act
    truck.apply_brakes()

    # Assert
    assert truck.current_speed == current_speed


def test_apply_break_when_current_speed_is_less_than_tyre_friction():
    # Arrange
    truck = Truck(color="Red", max_speed=50, acceleration=10,
                  tyre_friction=30, max_cargo_weight=100)
    current_speed = 0
    truck.start_engine()
    truck.accelerate()

    # Act
    truck.apply_brakes()

    # Assert
    assert truck.current_speed == current_speed


def test_apply_break_when_truck_is_at_rest_returns_current_speed_zero(truck1):
    # Arrange
    current_speed = 0

    # Act
    truck1.apply_brakes()

    # Assert
    assert truck1.current_speed == current_speed
