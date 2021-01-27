# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_create_racecar_with_valid_details racecar1_max_speed'] = 300

snapshots['test_create_racecar_with_valid_details racecar1_acceleration'] = 30

snapshots['test_create_racecar_with_valid_details racecar1_tyre_friction'] = 10

snapshots['test_create_racecar_with_valid_details racecar1_color'] = 'Red'

snapshots['test_create_racecar_with_valid_details racecar1_nitro'] = 0

snapshots['test_create_racecar_with_valid_details racecar1_current_speed'] = 0

snapshots['test_create_racecar_with_valid_details racecar1_is_engine_started'] = False

snapshots['test_create_multiple_racecar_with_valid_details racecar1_max_speed'] = 300

snapshots['test_create_multiple_racecar_with_valid_details racecar1_acceleration'] = 30

snapshots['test_create_multiple_racecar_with_valid_details racecar1_tyre_friction'] = 10

snapshots['test_create_multiple_racecar_with_valid_details racecar1_color'] = 'Red'

snapshots['test_create_multiple_racecar_with_valid_details racecar1_nitro'] = 0

snapshots['test_create_multiple_racecar_with_valid_details racecar1_current_speed'] = 0

snapshots['test_create_multiple_racecar_with_valid_details racecar1_is_engine_started'] = False

snapshots['test_create_multiple_racecar_with_valid_details racecar2_max_speed'] = 700

snapshots['test_create_multiple_racecar_with_valid_details racecar2_acceleration'] = 80

snapshots['test_create_multiple_racecar_with_valid_details racecar2_tyre_friction'] = 30

snapshots['test_create_multiple_racecar_with_valid_details racecar2_color'] = 'Red'

snapshots['test_create_multiple_racecar_with_valid_details racecar2_nitro'] = 0

snapshots['test_create_multiple_racecar_with_valid_details racecar2_current_speed'] = 0

snapshots['test_create_multiple_racecar_with_valid_details racecar2_is_engine_started'] = False

snapshots['test_sound_horn_without_starting_engine_returns_statement statement'] = '''Start the engine to sound_horn
'''

snapshots['test_sound_horn_when_engine_is_on_returns_horn_sound statement'] = '''Peep Peep
Beep Beep
'''

snapshots['test_encapsulation_for_all_protected_attributes_raises_error error_message'] = "can't set attribute"
