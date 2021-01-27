import pytest
from truck import Truck


# -----accelerating the truck-------
@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, current_speed",
    [(15, 5, 3, 5), (1, 1, 1, 1)])
def test_accelerate_truck_returns_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    truck = Truck(color="Red", max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction, max_cargo_weight=100)
    truck.start_engine()

    # Act
    truck.accelerate()

    # Assert
    assert truck.current_speed == current_speed


def test_accelerate_truck_more_than_max_speed_returns_current_speed_equal_to_max_speed():
    # Arrange
    truck = Truck(color="Red", max_speed=50, acceleration=10,
                  tyre_friction=3, max_cargo_weight=100)
    current_speed = 50
    truck.start_engine()

    # Act
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    # Assert
    assert truck.current_speed == current_speed


def test_accelerate_when_car_engine_is_not_started(truck1, capsys):
    # Arrange
    statement = 'Start the engine to accelerate\n'

    # Act
    truck1.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_accelerate_truck_with_different_acceleration():
    # Arrange
    truck = Truck(color="Red", max_speed=50, acceleration=10,
                  tyre_friction=3, max_cargo_weight=100)
    current_speed = 30
    truck.start_engine()

    # Act
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()

    # Assert
    assert truck.current_speed == current_speed
