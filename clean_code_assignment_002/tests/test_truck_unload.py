import pytest


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
