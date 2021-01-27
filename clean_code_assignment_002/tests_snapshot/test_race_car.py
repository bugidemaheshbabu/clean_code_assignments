import pytest


# ------Create Instances------
def test_create_racecar_with_valid_details(racecar1, snapshot):
    # Arrange

    # Assert
    snapshot.assert_match(racecar1.max_speed, 'racecar1_max_speed')
    snapshot.assert_match(racecar1.acceleration, 'racecar1_acceleration')
    snapshot.assert_match(racecar1.tyre_friction, 'racecar1_tyre_friction')
    snapshot.assert_match(racecar1.color, 'racecar1_color')
    snapshot.assert_match(racecar1.nitro, 'racecar1_nitro')
    snapshot.assert_match(racecar1.current_speed, 'racecar1_current_speed')
    snapshot.assert_match(racecar1.is_engine_started, 'racecar1_is_engine_started')
    



def test_create_multiple_racecar_with_valid_details(racecar1, racecar2, snapshot):
    # Arrange

    # Assert
    snapshot.assert_match(racecar1.max_speed, 'racecar1_max_speed')
    snapshot.assert_match(racecar1.acceleration, 'racecar1_acceleration')
    snapshot.assert_match(racecar1.tyre_friction, 'racecar1_tyre_friction')
    snapshot.assert_match(racecar1.color, 'racecar1_color')
    snapshot.assert_match(racecar1.nitro, 'racecar1_nitro')
    snapshot.assert_match(racecar1.current_speed, 'racecar1_current_speed')
    snapshot.assert_match(racecar1.is_engine_started, 'racecar1_is_engine_started')

    snapshot.assert_match(racecar2.max_speed, 'racecar2_max_speed')
    snapshot.assert_match(racecar2.acceleration, 'racecar2_acceleration')
    snapshot.assert_match(racecar2.tyre_friction, 'racecar2_tyre_friction')
    snapshot.assert_match(racecar2.color, 'racecar2_color')
    snapshot.assert_match(racecar2.nitro, 'racecar2_nitro')
    snapshot.assert_match(racecar2.current_speed, 'racecar2_current_speed')
    snapshot.assert_match(racecar2.is_engine_started, 'racecar2_is_engine_started')


# ----Task6----Sound Horn----
def test_sound_horn_without_starting_engine_returns_statement(
        racecar1, capsys, snapshot):
    # Arrange

    # Act
    racecar1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    snapshot.assert_match(captured.out, "statement")


def test_sound_horn_when_engine_is_on_returns_horn_sound(
        racecar1, capsys, snapshot):
    # Arrange
    horn_sound = "Peep Peep\nBeep Beep\n"
    racecar1.start_engine()

    # Act
    racecar1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    snapshot.assert_match(captured.out, "statement")


# ----Task8----Encapsulation----
def test_encapsulation_for_all_protected_attributes_raises_error(
        racecar1, snapshot):
    # Arrange
    error_message = "can't set attribute"

    # Assert
    with pytest.raises(AttributeError) as raised_error:
        racecar1.color = "Green"
    snapshot.assert_match(str(raised_error.value), "error_message")
    with pytest.raises(AttributeError) as raised_error:
        racecar1.max_speed = 500
    snapshot.assert_match(str(raised_error.value), "error_message")
    with pytest.raises(AttributeError) as raised_error:
        racecar1.acceleration = 500
    snapshot.assert_match(str(raised_error.value), "error_message")
    with pytest.raises(AttributeError) as raised_error:
        racecar1.tyre_friction = 200
    snapshot.assert_match(str(raised_error.value), "error_message")
    with pytest.raises(AttributeError) as raised_error:
        racecar1.nitro = 500
    snapshot.assert_match(str(raised_error.value), "error_message")
