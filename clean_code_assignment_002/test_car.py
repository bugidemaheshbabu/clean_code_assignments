import pytest
from car import Car

"""
----Task1----Creating a car template---
1.create car instance with valid details
2.create car instance with invalid details like negative values for max_speed raises ValueError
3.create car instance with invalid details like negative values for acceleration raises ValueError
4.create car instance with invalid details like negative values for tyre_friction raises ValueError
5.handling other data types for car attributes

----Task2----Starting Car----
5.starting a car if is_engine_started returns true

----Task3----Display Car Speed----
6.current_speed when engine is started without accelerated returns 0
test_current_speed_when_engine_is_not_started_returns_string

----Task4----Increasing Car speed----
7.current_speed after acceleration returns acceleration value
8.acceleration without starting engine returns 'start the engine to accelerate
9.accelerating car more than max_speed returns max_speed

----Task5----Apply Brakes----
10.current_speed after applying brakes decreases by tyre_friction value if engine is started returns current_speed minus tyre_friction
11.applying brakes once if tyre_friction is greater than acceleration and accelerated once will come down to zero
12.applying brakes continuously returns current_speed to zero
13.applying brakes without starting engine returns current_speed zero

----Task6----Sound Horn----
14.sound_horn without starting engine displays start the engine to sound_horn
15.sound_horn if engine is started return sound_horn

----Task7----Stop engine----
16.stop_engine without starting engine returns is_engine_started False
17.stopping engine after starting engine returns is_engine_started False
18.stopping engine while car is in motion should gradually decreases current_speed and goes to zero returns zero

----Task8----Encapsulation----
19.test_encapsulation_for_current_speed
20.test_encapsulation_for_acceleration
21.test_encapsulation_for_max_speed
22.test_encapsulation_for_tyre_friction
"""


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
def test_stop_engine_without_starting_engine_return_False(car_obj1):
    # Arrange
    false = False

    # Act
    car_obj1.stop_engine()

    # Assert
    assert car_obj1.is_engine_started == false


def test_stop_engine_when_engine_is_on_returns_is_engine_started_False(
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
