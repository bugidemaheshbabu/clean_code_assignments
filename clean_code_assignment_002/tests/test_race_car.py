import pytest


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
