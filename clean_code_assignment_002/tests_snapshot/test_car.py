import pytest
from car import Car

# ----Task1----Creating a car template---
def test_create_car_instance_with_valid_details_returns_car_obj_with_valid_details(car_obj1, snapshot):

 	snapshot.assert_match(car_obj1.max_speed, 'car1_max_speed')
 	snapshot.assert_match(car_obj1.acceleration, 'car1_acceleration')
 	snapshot.assert_match(car_obj1.tyre_friction, 'car_tyre_friction')

def test_create_car_multiple_instances_with_valid_details_returns_mutliple_car_objs_with_valid_details(
		car_obj1, snapshot):
	# Arrange
	car1 = car_obj1

	# Act
	car2 = Car(color='Blue', max_speed=150, acceleration=20, tyre_friction=10)

	# Assert
	snapshot.assert_match(car1.max_speed, 'car1_max_speed')
	snapshot.assert_match(car1.acceleration, 'car1_acceleration')
	snapshot.assert_match(car1.tyre_friction, 'car_tyre_friction')
	snapshot.assert_match(car2.max_speed, 'car2_max_speed')
	snapshot.assert_match(car2.acceleration, 'car2_acceleration')
	snapshot.assert_match(car2.tyre_friction, 'car2_tyre_friction')


@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction",
                         [('Blue', 0, 10, 3),
                          ('Blue', -1, 10, 3)])
def test_create_car_with_handling_edge_cases_for_max_speed_raises_error(
        color, max_speed, acceleration, tyre_friction, snapshot):
    # Arrange

    # Assert
    with pytest.raises(ValueError) as raised_error:
        Car(color=color, max_speed=max_speed,
            acceleration=acceleration, tyre_friction=tyre_friction)
    snapshot.assert_match(str(raised_error.value), 'max_speed_value_error')

# ----Task2----Starting Car----
def test_starting_car_returns_is_engine_started_returns_true(car_obj1, snapshot):
    # Act
    car_obj1.start_engine()
    true = True

    # Assert
    snapshot.assert_match(car_obj1.is_engine_started , 'car1_is_engine_started')

def test_starting_car_twice_returns_is_engine_started_returns_true(car_obj1, snapshot):
    # Act
    car_obj1.start_engine()
    car_obj1.start_engine()
    true = True

    # Assert
    snapshot.assert_match(car_obj1.is_engine_started , 'car1_is_engine_started')


def test_starting_multiple_car_engine_returns_true(snapshot):
    # Arrange
    car1 = Car(color='Blue', max_speed=25, acceleration=10, tyre_friction=3)
    car2 = Car(color='Blue', max_speed=250, acceleration=10, tyre_friction=3)
    true = True
    false = False

    # Act
    car1.start_engine()

    # Assert
    snapshot.assert_match(car1.is_engine_started , 'car1_is_engine_started')
    snapshot.assert_match(car1.is_engine_started , 'car2_is_engine_started')



# ----Task6----Sound Horn----
def test_sound_horn_without_starting_engine_returns_statement(
        car_obj1, capsys, snapshot):
    # Arrange
    statement = "Start the engine to sound_horn"

    # Act
    car_obj1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    snapshot.assert_match(captured.out, "statement")

def test_sound_horn_when_engine_is_on_returns_horn_sound(car_obj1, capsys, snapshot):
    # Arrange
    horn_sound = "Beep Beep"
    car_obj1.start_engine()

    # Act
    car_obj1.sound_horn()
    captured = capsys.readouterr()

    # Assert
    snapshot.assert_match(captured.out, "horn_sound")


# ----Task7----Stop engine----
def test_stop_engine_without_starting_engine_return_false(snapshot, car_obj1):
    # Arrange
    false = False

    # Act
    car_obj1.stop_engine()

    # Assert
    snapshot.assert_match(car_obj1.is_engine_started , 'car1_is_engine_started')


def test_stop_engine_when_engine_is_on_returns_is_engine_started_false(
        car_obj1, snapshot):
    # Arrange
    car_obj1.start_engine()
    false = False

    # Act
    car_obj1.stop_engine()

    # Assert
    snapshot.assert_match(car_obj1.is_engine_started , 'car1_is_engine_started')


# ----Task8----Encapsulation----
def test_encapsulation_for_all_protected_attributes_raises_error(car_obj1, snapshot):
    # Arrange
    error_message = "can\'t set attribute"

    # Assert
    with pytest.raises(AttributeError) as raised_error:
        car_obj1.color = "Green"
    snapshot.assert_match(str(raised_error.value), "error_message")
    with pytest.raises(AttributeError) as raised_error:
        car_obj1.max_speed = 500
    snapshot.assert_match(str(raised_error.value), "error_message")
    with pytest.raises(AttributeError) as raised_error:
        car_obj1.acceleration = 500
    snapshot.assert_match(str(raised_error.value), "error_message")
    with pytest.raises(AttributeError) as raised_error:
        car_obj1.tyre_friction = 200
    snapshot.assert_match(str(raised_error.value), "error_message")
