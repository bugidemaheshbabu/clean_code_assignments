# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_car_instance_with_valid_details_returns_car_obj_with_valid_details car1_max_speed'] = 25

snapshots['test_create_car_instance_with_valid_details_returns_car_obj_with_valid_details car1_acceleration'] = 10

snapshots['test_create_car_instance_with_valid_details_returns_car_obj_with_valid_details car_tyre_friction'] = 3

snapshots['test_create_car_multiple_instances_with_valid_details_returns_mutliple_car_objs_with_valid_details car1_max_speed'] = 25

snapshots['test_create_car_multiple_instances_with_valid_details_returns_mutliple_car_objs_with_valid_details car1_acceleration'] = 10

snapshots['test_create_car_multiple_instances_with_valid_details_returns_mutliple_car_objs_with_valid_details car_tyre_friction'] = 3

snapshots['test_create_car_multiple_instances_with_valid_details_returns_mutliple_car_objs_with_valid_details car2_max_speed'] = 150

snapshots['test_create_car_multiple_instances_with_valid_details_returns_mutliple_car_objs_with_valid_details car2_acceleration'] = 20

snapshots['test_create_car_multiple_instances_with_valid_details_returns_mutliple_car_objs_with_valid_details car2_tyre_friction'] = 10

snapshots['test_starting_car_returns_is_engine_started_returns_true car1_is_engine_started'] = True

snapshots['test_starting_car_twice_returns_is_engine_started_returns_true car1_is_engine_started'] = True

snapshots['test_starting_multiple_car_engine_returns_true car1_is_engine_started'] = True

snapshots['test_starting_multiple_car_engine_returns_true car2_is_engine_started'] = True

snapshots['test_sound_horn_without_starting_engine_returns_statement statement'] = '''Start the engine to sound_horn
'''

snapshots['test_sound_horn_when_engine_is_on_returns_horn_sound horn_sound'] = '''Beep Beep
'''

snapshots['test_stop_engine_without_starting_engine_return_false car1_is_engine_started'] = False

snapshots['test_stop_engine_when_engine_is_on_returns_is_engine_started_false car1_is_engine_started'] = False

snapshots['test_encapsulation_for_all_protected_attributes_raises_error error_message'] = "can't set attribute"

snapshots['test_create_car_with_handling_edge_cases_for_max_speed_raises_error[Blue-0-10-3] max_speed_value_error'] = 'Invalid value for max_speed'

snapshots['test_create_car_with_handling_edge_cases_for_max_speed_raises_error[Blue--1-10-3] max_speed_value_error'] = 'Invalid value for max_speed'
