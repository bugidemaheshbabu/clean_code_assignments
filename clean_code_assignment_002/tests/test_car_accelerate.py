import pytest
from car import Car


# ----Task3----Display Car Speed----
def test_current_speed_when_engine_is_started_returns_zero(car_obj1):
    # Arrange
    current_speed = 0

    # Act
    car_obj1.start_engine()

    # Assert
    assert car_obj1.current_speed == current_speed


def test_current_speed_when_engine_is_not_started_returns_current_speed_zero(
        car_obj1):
    # Arrange
    current_speed = 0

    # Assert
    assert car_obj1.current_speed == current_speed


# ----Task4----Increasing Car speed----
def test_accelerate_car_once_returns_current_speed_with_acceleration_value(
        car_obj1):
    # Arrange
    current_speed = 10
    car_obj1.start_engine()

    # Act
    car_obj1.accelerate()

    # Assert
    assert car_obj1.current_speed == current_speed


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction, current_speed",
                         [(1, 1, 1, 1), (3, 1, 1, 2)])
def test_current_speed_after_accelerating_once_returns_acceleration_value_in_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    car = Car(color="Blue", max_speed=max_speed,
              acceleration=acceleration, tyre_friction=tyre_friction)

    # Act
    car.start_engine()
    car.accelerate()
    car.accelerate()

    # Assert
    assert car.current_speed == current_speed


def test_current_speed_after_accelerating_more_than_max_speed_returns_max_speed_value(car_obj1):
    # Act
    car_obj1.start_engine()
    car_obj1.accelerate()
    car_obj1.accelerate()
    car_obj1.accelerate()
    car_obj1.accelerate()
    car_obj1.accelerate()
    car_obj1.accelerate()
    car_obj1.accelerate()

    # Assert
    assert car_obj1.current_speed == 25


def test_accelerating_without_starting_engine_returns_message(
        car_obj1, capsys):
    # Arrange
    error_message = "Start the engine to accelerate\n"

    # Act
    car_obj1.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == error_message
