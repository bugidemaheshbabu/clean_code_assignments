# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_current_speed_when_engine_is_started_returns_zero car1_current_speed'] = 0

snapshots['test_current_speed_when_engine_is_not_started_returns_current_speed_zero car1_current_speed'] = 0

snapshots['test_accelerate_car_once_returns_current_speed_with_acceleration_value car1_current_speed'] = 10

snapshots['test_current_speed_after_accelerating_more_than_max_speed_returns_max_speed_value car1_current_speed'] = 25

snapshots['test_accelerating_without_starting_engine_returns_message error_message'] = '''Start the engine to accelerate
'''

snapshots['test_current_speed_after_accelerating_once_returns_acceleration_value_in_current_speed[1-1-1-1] car1_current_speed'] = 1

snapshots['test_current_speed_after_accelerating_once_returns_acceleration_value_in_current_speed[3-1-1-2] car1_current_speed'] = 2
