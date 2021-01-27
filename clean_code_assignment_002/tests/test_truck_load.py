import pytest
from truck import Truck


# ----load-----
def test_load_cargo_when_car_is_at_rest_returns_current_cargo_weigt(truck1):
    # Arrange

    # Act
    truck1.load(50)

    # Assert
    assert truck1.current_cargo_weight == 50


def test_load_cargo_more_than_max_limit_when_truck_is_at_rest_returns_statement(truck1, capsys):
    # Arrange
    statement = "Cannot load cargo more than max limit: 100\n"

    # Act
    truck1.load(200)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_load_cargo_more_than_max_limit_when_truck_is_in_motion_returns_statement(truck1, capsys):
    # Arrange
    statement = "Cannot load cargo during motion\n"
    truck1.start_engine()
    truck1.accelerate()

    # Act
    truck1.load(200)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_load_cargo_less_than_max_limit_when_truck_is_in_motion_returns_statement(truck1, capsys):
    # Arrange
    statement = "Cannot load cargo during motion\n"
    truck1.start_engine()
    truck1.accelerate()

    # Act
    truck1.load(50)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_load_cargo_with_different_weights_at_rest_returns_current_cargo_weight(truck1):
    # Arrange
    current_cargo_weight = 95

    # Act
    truck1.load(25)
    truck1.load(30)
    truck1.load(40)

    # Assert
    assert truck1.current_cargo_weight == current_cargo_weight


def test_load_cargo_when_truck_is_stopped_and_current_speed_is_zero_returns_current_cargo_weight():
    # Arrange
    truck = Truck(color="Red", max_speed=50, acceleration=10,
                  tyre_friction=30, max_cargo_weight=100)
    truck.start_engine()
    current_cargo_weight = 50

    # Act
    truck.stop_engine()
    truck.load(50)

    # Assert
    assert truck.current_cargo_weight == current_cargo_weight


def test_load_cargo_when_truck_is_stopped_and_current_speed_is_not_zero_returns_statement(capsys):
    # Arrange
    truck = Truck(color="Red", max_speed=50, acceleration=10,
                  tyre_friction=30, max_cargo_weight=100)
    truck.start_engine()
    truck.accelerate()
    statement = "Cannot load cargo during motion\n"

    # Act
    truck.stop_engine()
    truck.load(50)
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_load_cargo_when_multiple_trucks_are_started_and_loaded_returns_current_cargo_weights(truck1, truck2):
    # Arrange
    truck2.start_engine()

    # Act
    truck2.load(100)

    # Assert
    assert truck1.current_cargo_weight == 0
    assert truck2.current_cargo_weight == 100


def test_load_cargo_with_invalid_data_raises_error(truck1):
    # Act
    with pytest.raises(ValueError) as raised_error:
        truck1.load(-50)
    assert str(raised_error.value) == 'Invalid value for cargo_weight'
