import pytest
from car import Car
from truck import Truck
from race_car import RaceCar

@pytest.fixture
def car_obj1():
    car_instance1 = Car(
        color='Blue', max_speed=25,
        acceleration=10, tyre_friction=3)
    return car_instance1


@pytest.fixture
def truck1():
    truck_obj1 = Truck(color="Red", max_speed=25,
                   acceleration=10, tyre_friction=3, max_cargo_weight=100)
    return truck_obj1


@pytest.fixture
def truck2():
    truck_obj2 = Truck(color="Red", max_speed=10,
                   acceleration=10, tyre_friction=10, max_cargo_weight=100)
    return truck_obj2


@pytest.fixture
def racecar1():
    racecar_obj1 = RaceCar(color='Red', max_speed=300, acceleration=30, tyre_friction=10)
    return racecar_obj1


@pytest.fixture
def racecar2():
    racecar_obj2 = RaceCar(color='Red', max_speed=700, acceleration=80, tyre_friction=30)
    return racecar_obj2
