import pytest
from truck import Truck


"""
1.test_create_truck_with_valid_details
2.test_create_multiple_truck_with_valid_details
3.test_invalid_max_speed_attr
4.test_invalid_acceleration_attr
5.test_invalid_tyre_friction_attr
5.test_invalid_max_cargo_weight_attr
6.test_start_engine
7.test_start_engine_for_multiple_objects
8.test_start_engine_when_engine_is_started_twice
9.test_current_speed_when_engine_is_started_for_newly_created_object_returns_zero
10.test_current_speed_for_newly_created_object_returns_zero
11.test_accelerate_when_car_engine_is_not_started_prints_string
12.test_accelerate_truck_once_returns_current_speed_equlas_to_acceleration_value
13.test_accelerate_truck_more_than_max_speed
14.test_acceleration_when_acceleration_value_greater_than_max_speed_returns_max_speed
"""


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
    truck1.is_engine_started == true


def test_start_engine_twice_returns_true(truck1):
    # Arrange
    truck1.start_engine()
    true = True

    # Act
    truck1.start_engine()

    # Assert
    truck1.is_engine_started == true


def test_start_engine_for_multiple_instance_returns_true(truck1, truck2):
    # Act
    truck1.start_engine()
    true = True
    false = False

    # Assert
    assert truck1.is_engine_started == true
    assert truck2.is_engine_started == false


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


# ----unload cargo------
def test_unload_cargo_when_current_truck_load_is_more_than_given_cargo_weight_when_truck_is_at_rest(truck1):
    # Arrange
    truck1.load(50)

    # Act
    truck1.unload(20)

    # Assert
    assert truck1.current_speed == 0
    assert truck1.current_cargo_weight == 30


def test_unload_cargo_with_invalid_data_raises_error(truck1):
    # Arrange
    truck1.load(90)

    # Act
    with pytest.raises(ValueError) as raised_error:
        truck1.unload(-50)
    assert str(raised_error.value) == 'Invalid value for cargo_weight'  # Asseert


def test_unload_cargo_when_current_truck_load_is_more_than_given_cargo_weight_and_is_in_motion(truck1, capsys):
    # Arrange
    truck1.load(50)
    truck1.start_engine()
    truck1.accelerate()
    statement = "Cannot unload cargo during motion\n"

    # Act
    truck1.unload(20)
    captured = capsys.readouterr()

    # Assert
    assert truck1.current_speed == 10
    assert captured.out == statement


def test_unload_cargo_when_truck_is_started_and_is_at_rest(truck1):
    # Arrange
    truck1.load(100)
    truck1.start_engine()

    # Act
    truck1.unload(100)

    # Asseert
    assert truck1.current_speed == 0
    assert truck1.current_cargo_weight == 0


def test_unload_cargo_when_truck_is_stopped_and_is_at_rest(truck1):
    # Arrange
    truck1.load(100)
    truck1.start_engine()

    # Act
    truck1.stop_engine()
    truck1.unload(100)

    # Asseert
    assert truck1.current_speed == 0
    assert truck1.current_cargo_weight == 0


def test_unload_cargo_when_truck_is_stopped_and_current_speed_is_not_zero_returens_statement(truck1, capsys):
    # Arrange
    truck1.load(99)
    truck1.start_engine()
    truck1.accelerate()
    statement = "Cannot unload cargo during motion\n"

    # Act
    truck1.stop_engine()
    truck1.unload(99)
    captured = capsys.readouterr()

    # Assert
    assert truck1.current_speed == 10
    assert captured.out == statement


def test_unload_cargo_more_than_max_limit_and_is_at_rest_returns_zero(truck1):
    # Arrange
    truck1.load(99)

    # Act
    truck1.unload(200)

    # Assert
    assert truck1.current_speed == 0
    assert truck1.current_cargo_weight == 0
