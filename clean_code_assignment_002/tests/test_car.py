import pytest
from car import Car


# ----Task1----Creating a car template---
def test_create_car_instance_with_valid_details_returns_car_obj_with_valid_details(car_obj1):
    # Arrange

    # Assert
    assert car_obj1.max_speed == 25
    assert car_obj1.acceleration == 10
    assert car_obj1.tyre_friction == 3


def test_create_car_multiple_instances_with_valid_details_returns_mutliple_car_objs_with_valid_details():
    # Arrange
    car1 = Car(color='Blue', max_speed=50, acceleration=10, tyre_friction=3)

    # Act
    car2 = Car(color='Blue', max_speed=150, acceleration=20, tyre_friction=10)

    # Assert
    assert car1.max_speed == 50
    assert car1.acceleration == 10
    assert car1.tyre_friction == 3
    assert car2.max_speed == 150
    assert car2.acceleration == 20
    assert car2.tyre_friction == 10


@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction",
                         [('Blue', 0, 10, 3),
                          ('Blue', -1, 10, 3)])
def test_create_car_with_handling_edge_cases_for_max_speed_raises_error(
        color, max_speed, acceleration, tyre_friction):
    # Arrange

    # Assert
    with pytest.raises(ValueError) as raised_error:
        Car(color=color, max_speed=max_speed,
            acceleration=acceleration, tyre_friction=tyre_friction)
    assert str(raised_error.value) == 'Invalid value for max_speed'


@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction",
                         [('Blue', 10, 0, 3),
                          ('Blue', 10, -1, 3)])
def test_create_car_with_handling_edge_cases_for_acceleration_raises_error(
        color, max_speed, acceleration, tyre_friction):
    # Arrange

    # Assert
    with pytest.raises(ValueError) as raised_error:
        Car(color=color, max_speed=max_speed,
            acceleration=acceleration, tyre_friction=tyre_friction)
    assert str(raised_error.value) == 'Invalid value for acceleration'


@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction",
                         [('Blue', 10, 5, 0),
                          ('Blue', 10, 5, -1)])
def test_create_car_with_handling_edge_cases_for_tyre_friction_raises_error(
        color, max_speed, acceleration, tyre_friction):
    # Arrange

    # Assert
    with pytest.raises(ValueError) as raised_error:
        Car(color=color, max_speed=max_speed,
            acceleration=acceleration, tyre_friction=tyre_friction)
    assert str(raised_error.value) == 'Invalid value for tyre_friction'


# ----Task2----Starting Car----
def test_starting_car_returns_is_engine_started_returns_true(car_obj1):
    # Act
    car_obj1.start_engine()
    true = True

    # Assert
    assert car_obj1.is_engine_started == true


def test_starting_car_twice_returns_is_engine_started_returns_true(car_obj1):
    # Act
    car_obj1.start_engine()
    car_obj1.start_engine()
    true = True

    # Assert
    assert car_obj1.is_engine_started == true


def test_starting_multiple_car_engine_returns_true():
    # Arrange
    car1 = Car(color='Blue', max_speed=25, acceleration=10, tyre_friction=3)
    car2 = Car(color='Blue', max_speed=250, acceleration=10, tyre_friction=3)
    true = True
    false = False

    # Act
    car1.start_engine()

    # Assert
    assert car1.is_engine_started == true
    assert car2.is_engine_started == false


# ----Task6----Sound Horn----
def test_sound_horn_without_starting_engine_returns_statement(
        car_obj1, capsys):
    # Arrange
    statement = "Start the engine to sound_horn\n"

    # Act
    car_obj1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_sound_horn_when_engine_is_on_returns_horn_sound(car_obj1, capsys):
    # Arrange
    horn_sound = "Beep Beep\n"
    car_obj1.start_engine()

    # Act
    car_obj1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == horn_sound


# ----Task7----Stop engine----
def test_stop_engine_without_starting_engine_return_false(car_obj1):
    # Arrange
    false = False

    # Act
    car_obj1.stop_engine()

    # Assert
    assert car_obj1.is_engine_started == false


def test_stop_engine_when_engine_is_on_returns_is_engine_started_false(
        car_obj1):
    # Arrange
    car_obj1.start_engine()
    false = False

    # Act
    car_obj1.stop_engine()

    # Assert
    assert car_obj1.is_engine_started == false


# ----Task8----Encapsulation----
def test_encapsulation_for_all_protected_attributes_raises_error(car_obj1):
    # Arrange
    error_message = "can't set attribute"

    # Assert
    with pytest.raises(AttributeError) as raised_error:
        car_obj1.color = "Green"
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        car_obj1.max_speed = 500
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        car_obj1.acceleration = 500
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        car_obj1.tyre_friction = 200
    assert str(raised_error.value) == error_message
