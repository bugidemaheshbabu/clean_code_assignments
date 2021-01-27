import pytest
from truck import Truck


# ------Create Instances------
def test_create_truck_with_valid_details(truck1):
    # Assert
    assert truck1.color == "Red"
    assert truck1.max_speed == 25
    assert truck1.acceleration == 10
    assert truck1.tyre_friction == 3
    assert truck1.max_cargo_weight == 100
    assert truck1.current_cargo_weight == 0


def test_create_multiple_truck_with_valid_details(truck1, truck2):
    # Arrange
    false = False

    # Assert
    assert truck1.color == "Red"
    assert truck1.max_speed == 25
    assert truck1.acceleration == 10
    assert truck1.tyre_friction == 3
    assert truck1.max_cargo_weight == 100
    assert truck1.current_speed == 0
    assert truck1.is_engine_started == false
    assert truck1.current_cargo_weight == 0

    assert truck2.color == "Red"
    assert truck2.max_speed == 10
    assert truck2.acceleration == 10
    assert truck2.tyre_friction == 10
    assert truck2.max_cargo_weight == 100
    assert truck2.current_speed == 0
    assert truck2.is_engine_started == false
    assert truck2.current_cargo_weight == 0


def test_truck_instance_with_invalid_max_speed_attr_raises_error():
    # Arrange
    error_message = 'Invalid value for max_speed'

    # Act
    with pytest.raises(ValueError) as raised_error:
        Truck(color="Red", max_speed=0, acceleration=10,
              tyre_friction=3, max_cargo_weight=100)
    assert str(raised_error.value) == error_message  # Assert
    with pytest.raises(ValueError) as raised_error:
        Truck(color="Red", max_speed=-1,
              acceleration=10, tyre_friction=3, max_cargo_weight=100)
    assert str(raised_error.value) == error_message  # Assert


@pytest.mark.parametrize("acceleration", [0, -1])
def test_truck_instance_with_invalid_acceleration_attr_raises_error(
        acceleration):
    # Arrange
    error_message = 'Invalid value for acceleration'

    # Act
    with pytest.raises(ValueError) as raised_error:
        Truck(color="Blue", max_speed=10, acceleration=acceleration,
              tyre_friction=3, max_cargo_weight=100)
    assert str(raised_error.value) == error_message


@pytest.mark.parametrize("tyre_friction", [0, -1])
def test_truck_instance_with_invalid_tyre_friction_attr_raises_error(
        tyre_friction):
    # Arrange
    error_message = 'Invalid value for tyre_friction'

    # Act
    with pytest.raises(ValueError) as raised_error:
        Truck(color="Blue", max_speed=10, acceleration=5,
              tyre_friction=tyre_friction, max_cargo_weight=100)
    assert str(raised_error.value) == error_message


@pytest.mark.parametrize("max_cargo_weight", [0, -1])
def test_truck_instance_with_invalid_max_cargo_weight_attr_raises_error(
        max_cargo_weight):
    # Arrange
    error_message = 'Invalid value for max_cargo_weight'

    # Act
    with pytest.raises(ValueError) as raised_error:
        Truck(color="Blue", max_speed=10, acceleration=5,
              tyre_friction=3, max_cargo_weight=max_cargo_weight)
    assert str(raised_error.value) == error_message  # Assert


# -----start engine-----
def test_start_engine_returns_true(truck1):
    # Arrange
    true = True

    # Act
    truck1.start_engine()

    # Asseert
    assert truck1.is_engine_started == true


def test_start_engine_twice_returns_true(truck1):
    # Arrange
    truck1.start_engine()
    true = True

    # Act
    truck1.start_engine()

    # Assert
    assert truck1.is_engine_started == true


def test_start_engine_for_multiple_instance_returns_true(truck1, truck2):
    # Act
    truck1.start_engine()
    true = True
    false = False

    # Assert
    assert truck1.is_engine_started == true
    assert truck2.is_engine_started == false


# ----Task6----Sound Horn----
def test_sound_horn_without_starting_engine_returns_statement(truck1, capsys):
    # Arrange
    statement = "Start the engine to sound_horn\n"

    # Act
    truck1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_sound_horn_when_engine_is_on_returns_horn_sound(truck1, capsys):
    # Arrange
    horn_sound = "Honk Honk\n"
    truck1.start_engine()

    # Act
    truck1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == horn_sound


# ----Task8----Encapsulation----
def test_encapsulation_for_all_protected_attributes_raises_error(truck1):
    # Arrange
    error_message = "can't set attribute"

    # Assert
    with pytest.raises(AttributeError) as raised_error:
        truck1.color = "Green"
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        truck1.max_speed = 500
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        truck1.acceleration = 500
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        truck1.tyre_friction = 200
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        truck1.max_cargo_weight = 500
    assert str(raised_error.value) == error_message
