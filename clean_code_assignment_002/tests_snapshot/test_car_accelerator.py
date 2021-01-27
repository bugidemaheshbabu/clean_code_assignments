import pytest
from car import Car


# ----Task3----Display Car Speed----
def test_current_speed_when_engine_is_started_returns_zero(car_obj1, snapshot):
    # Arrange
    current_speed = 0

    # Act
    car_obj1.start_engine()

    # Assert
    snapshot.assert_match(car_obj1.current_speed, 'car1_current_speed')


def test_current_speed_when_engine_is_not_started_returns_current_speed_zero(
        car_obj1, snapshot):
    # Arrange
    current_speed = 0

    # Assert
    snapshot.assert_match(car_obj1.current_speed, 'car1_current_speed')


# ----Task4----Increasing Car speed----
def test_accelerate_car_once_returns_current_speed_with_acceleration_value(
        car_obj1, snapshot):
    # Arrange
    current_speed = 10
    car_obj1.start_engine()

    # Act
    car_obj1.accelerate()

    # Assert
    snapshot.assert_match(car_obj1.current_speed, 'car1_current_speed')


@pytest.mark.parametrize("max_speed, acceleration, tyre_friction, current_speed",
                         [(1, 1, 1, 1), (3, 1, 1, 2)])
def test_current_speed_after_accelerating_once_returns_acceleration_value_in_current_speed(
        max_speed, acceleration, tyre_friction, current_speed, snapshot):
    # Arrange
    car = Car(color="Blue", max_speed=max_speed,
              acceleration=acceleration, tyre_friction=tyre_friction)

    # Act
    car.start_engine()
    car.accelerate()
    car.accelerate()

    # Assert
    snapshot.assert_match(car.current_speed, 'car1_current_speed')


def test_current_speed_after_accelerating_more_than_max_speed_returns_max_speed_value(
        car_obj1, snapshot):
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
    snapshot.assert_match(car_obj1.current_speed, 'car1_current_speed')



def test_accelerating_without_starting_engine_returns_message(
        car_obj1, capsys, snapshot):
    # Arrange
    error_message = "Start the engine to accelerate"

    # Act
    car_obj1.accelerate()
    captured = capsys.readouterr()

    # Assert
    snapshot.assert_match(captured.out, 'error_message')
