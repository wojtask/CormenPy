import random
from unittest import TestCase

from hamcrest import *

from chapter16.exercise16_1_1 import dynamic_activity_selector
from test_chapter16.test_textbook16_1 import setup_activities, sort_activities_by_finish_time, decode_activities, \
    activities_compatible, activity_selector_bruteforce


class TestExercise16_1_1(TestCase):

    def test_dynamic_activity_selector_(self):
        n = random.randint(1, 15)
        start_times, finish_times = setup_activities(n)
        sort_activities_by_finish_time(start_times, finish_times)

        actual_activities = dynamic_activity_selector(start_times, finish_times)

        actual_activities_ids = decode_activities(actual_activities)
        assert_that(activities_compatible(actual_activities_ids, start_times, finish_times))
        expected_activities = activity_selector_bruteforce(start_times, finish_times)
        assert_that(actual_activities, has_length(expected_activities))
