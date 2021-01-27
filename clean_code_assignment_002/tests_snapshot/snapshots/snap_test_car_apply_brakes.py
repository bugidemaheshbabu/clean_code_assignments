# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_apply_break_when_current_speed_less_than_or_equal_to_tyre_friction car1_current_speed'] = 0

snapshots['test_apply_break_when_car_is_in_motion[130-10-3-7] car1_current_speed'] = 7

snapshots['test_apply_break_when_car_is_in_motion[8-3-10-0] car1_current_speed'] = 0

snapshots['test_apply_break_when_car_is_in_motion[10-2-1-1] car1_current_speed'] = 1

snapshots['test_apply_break_multiple_times_returns_current_speed car1_current_speed'] = 15

snapshots['test_apply_brake_after_starting_engine_returns_zero car1_current_speed'] = 0

snapshots['test_apply_break_when_car_engine_is_not_started_returns_current_speed_zero car1_current_speed'] = 0

snapshots['test_apply_break_continiously_when_car_accelerated_returns_current_speed_zero car1_current_speed'] = 0
