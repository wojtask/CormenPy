import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter16.exercise16_1_2 import greedy_activity_selector_
from test_chapter16.test_textbook16_1 import decode_activities, activities_compatible, activity_selector_bruteforce, \
    get_activities_sorted_by_start_time


class TestExercise16_1_2(TestCase):

    def test_greedy_activity_selector_(self):
        n = random.randint(1, 15)
        start_times, finish_times = get_activities_sorted_by_start_time(n)
        original_start_times = copy.deepcopy(start_times)
        original_finish_times = copy.deepcopy(finish_times)

        actual_activities = greedy_activity_selector_(start_times, finish_times)

        actual_activities_ids = decode_activities(actual_activities)
        assert_that(activities_compatible(actual_activities_ids, start_times, finish_times))
        expected_activities = activity_selector_bruteforce(original_start_times, original_finish_times)
        assert_that(actual_activities, has_length(expected_activities))
