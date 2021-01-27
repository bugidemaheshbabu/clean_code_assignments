import math
import pytest
from race_car import RaceCar


# ------Create Instances------
def test_create_racecar_with_valid_details(racecar1):
    # Arrange
    false = False

    # Assert
    assert racecar1.color == "Red"
    assert racecar1.max_speed == 300
    assert racecar1.acceleration == 30
    assert racecar1.tyre_friction == 10
    assert racecar1.nitro == 0
    assert racecar1.current_speed == 0
    assert racecar1.is_engine_started == false


def test_create_multiple_racecar_with_valid_details(racecar1, racecar2):
    # Arrange
    false = False

    # Assert
    assert racecar1.color == "Red"
    assert racecar1.max_speed == 300
    assert racecar1.acceleration == 30
    assert racecar1.tyre_friction == 10
    assert racecar1.nitro == 0
    assert racecar1.current_speed == 0
    assert racecar1.is_engine_started == false

    assert racecar2.color == "Red"
    assert racecar2.max_speed == 700
    assert racecar2.acceleration == 80
    assert racecar2.tyre_friction == 30
    assert racecar2.current_speed == 0
    assert racecar2.is_engine_started == false
    assert racecar2.nitro == 0


# ------accelerate-------


@pytest.mark.parametrize(
    "max_speed, acceleration, tyre_friction, current_speed",
    [(15, 5, 3, 5), (1, 1, 1, 1)])
def test_accelerate_racecar_returns_current_speed(
        max_speed, acceleration, tyre_friction, current_speed):
    # Arrange
    racecar = RaceCar(color="Red", max_speed=max_speed,
                      acceleration=acceleration, tyre_friction=tyre_friction)
    racecar.start_engine()

    # Act
    racecar.accelerate()

    # Assert
    assert racecar.current_speed == current_speed


def test_accelerate_racecar_more_than_max_speed_returns_current_speed_equal_to_max_speed():
    # Arrange
    racecar = RaceCar(color="Red", max_speed=50, acceleration=10,
                      tyre_friction=3)
    current_speed = 50
    racecar.start_engine()

    # Act
    racecar.accelerate()
    racecar.accelerate()
    racecar.accelerate()
    racecar.accelerate()
    racecar.accelerate()
    racecar.accelerate()
    racecar.accelerate()

    # Assert
    assert racecar.current_speed == current_speed


def test_accelerate_when_car_engine_is_not_started(racecar1, capsys):
    # Arrange
    statement = 'Start the engine to accelerate\n'

    # Act
    racecar1.accelerate()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_accelerate_racecar_with_different_acceleration():
    # Arrange
    racecar = RaceCar(color="Red", max_speed=50, acceleration=10,
                      tyre_friction=3)
    current_speed = 30
    racecar.start_engine()

    # Act
    racecar.accelerate()
    racecar.accelerate()
    racecar.accelerate()

    # Assert
    assert racecar.current_speed == current_speed


def test_accelerate_racecar_when_nitro_is_available_returns_current_speed(
        racecar1):
    # Arrange
    racecar1.start_engine()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.apply_brakes()

    # Act
    racecar1.accelerate()

    # Assert
    assert racecar1.current_speed == 239


def test_decrease_nitro_on_accelerate(racecar1):
    # Arrange
    racecar1.start_engine()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.apply_brakes()

    # Act
    racecar1.accelerate()

    # Assert
    assert racecar1.nitro == 0


def test_accelerate_racecar_more_than_max_limit_without_nitro_returns_current_speed():
    # Arrange
    racecar = RaceCar(color="Red", max_speed=25, acceleration=10, tyre_friction=7)
    racecar.start_engine()
    racecar.accelerate()
    racecar.accelerate()

    # Act
    racecar.accelerate()

    # Assert
    assert racecar.current_speed == 25


def test_accelerate_racecar_more_than_max_limit_with_nitro_returns_current_speed():
    # Arrange
    racecar = RaceCar(color="Red", max_speed=25, acceleration=10, tyre_friction=7)
    racecar.start_engine()
    racecar.accelerate()
    racecar.accelerate()
    racecar.apply_brakes()

    # Act
    racecar.accelerate()

    # Assert
    assert racecar.current_speed == 25


def test_accelerate_racecar_with_minimal_values_returns_current_speed():
    # Arrange
    racecar = RaceCar(color="Red", max_speed=1, acceleration=1, tyre_friction=1)
    racecar.start_engine()

    # Act
    racecar.accelerate()

    # Assert
    assert racecar.current_speed == 1


# ----apply brakes------
def test_apply_breake_racecar_current_equals_to_half_max_speed_returns_nitro_zero():
    # Arrange
    racecar = RaceCar(color="Red", max_speed=30, acceleration=15, tyre_friction=7)
    racecar.start_engine()
    racecar.accelerate()

    # Act
    racecar.apply_brakes()

    # Assert
    assert racecar.nitro == 0


def test_apply_break_when_current_speed_is_less_than_half_max_speed_returns_nitro_zero(racecar1):
    # Arrange
    racecar1.start_engine()
    racecar1.accelerate()
    racecar1.accelerate()

    # Act
    racecar1.apply_brakes()

    # Assert
    assert racecar1.nitro == 0
    assert racecar1.current_speed == 50


def test_apply_break_more_than_half_max_speed_continously_update_nitro_speed(racecar1):
    # Arrange
    racecar1.start_engine()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()

    # Act
    racecar1.apply_brakes()
    racecar1.apply_brakes()
    racecar1.apply_brakes()

    # Assert
    assert racecar1.nitro == 30


def test_apply_break_when_current_speed_is_more_than_half_max_speed_returns_nitro(racecar1):
    # Arrange
    racecar1.start_engine()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()

    # Act
    racecar1.apply_brakes()

    # Assert
    assert racecar1.nitro == 10
    assert racecar1.current_speed == 170


def test_apply_break_when_current_speed_is_less_than_max_speed_returns_current_speed():
    # Arrange
    racecar1 = RaceCar(color="None", max_speed=100, acceleration=10, tyre_friction=1)
    racecar1.start_engine()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.accelerate()
    racecar1.apply_brakes()

    # Act
    racecar1.accelerate()

    # Assert
    assert racecar1.current_speed == 92


# ----Task6----Sound Horn----
def test_sound_horn_without_starting_engine_returns_statement(
        racecar1, capsys):
    # Arrange
    statement = "Start the engine to sound_horn\n"

    # Act
    racecar1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == statement


def test_sound_horn_when_engine_is_on_returns_horn_sound(racecar1, capsys):
    # Arrange
    horn_sound = "Peep Peep\nBeep Beep\n"
    racecar1.start_engine()

    # Act
    racecar1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    assert captured.out == horn_sound


# ----Task8----Encapsulation----
def test_encapsulation_for_all_protected_attributes_raises_error(racecar1):
    # Arrange
    error_message = "can't set attribute"

    # Assert
    with pytest.raises(AttributeError) as raised_error:
        racecar1.color = "Green"
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        racecar1.max_speed = 500
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        racecar1.acceleration = 500
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        racecar1.tyre_friction = 200
    assert str(raised_error.value) == error_message
    with pytest.raises(AttributeError) as raised_error:
        racecar1.nitro = 500
    assert str(raised_error.value) == error_message
