from race_car import RaceCar


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
