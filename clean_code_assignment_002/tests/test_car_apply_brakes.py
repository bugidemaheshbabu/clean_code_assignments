import pytest
from car import Car


# ----Task5----Apply Brakes----
def test_apply_break_when_current_speed_less_than_or_equal_to_tyre_friction():
    # Arrange
    car = Car(color="Red", max_speed=1, acceleration=1, tyre_friction=1)
    current_speed = 0
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction, current_speed",
                         [(130, 10, 3, 7), (8, 3, 10, 0), (10, 2, 1, 1)])
def test_apply_break_when_car_is_in_motion(
        max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    car = Car(color="Red", max_speed=max_speed,
              acceleration=acceleration, tyre_friction=tyre_friction)
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed


def test_apply_break_multiple_times_returns_current_speed():
    # Arrange
    car = Car(color="Blue", max_speed=250, acceleration=20, tyre_friction=13)
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    current_speed = 15

    # Act
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed


def test_apply_brake_after_starting_engine_returns_zero():
    # Arrange
    car = Car(color="Blue", max_speed=10, acceleration=2, tyre_friction=1)
    car.start_engine()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == 0


def test_apply_break_when_car_engine_is_not_started_returns_current_speed_zero(car_obj1):
    # Assert
    assert car_obj1.current_speed == 0


def test_apply_break_continiously_when_car_accelerated_returns_current_speed_zero():
    # Arrange
    car = Car(color="Blue", max_speed=10, acceleration=4, tyre_friction=3)

    # Act
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    # Assert
    assert car.current_speed == 0
