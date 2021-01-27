import pytest
from race_car import RaceCar

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
