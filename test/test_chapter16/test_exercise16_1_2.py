import random
from unittest import TestCase

from hamcrest import *

from chapter16.exercise16_1_2 import greedy_activity_selector_
from test_chapter16.test_textbook16_1 import setup_activities, decode_activities, activities_compatible, \
    activity_selector_bruteforce


def sort_activities_by_start_time(s, f):
    sorted_tuples = sorted(zip(s, f), key=lambda x: x[0])
    s.elements = [x[0] for x in sorted_tuples]
    f.elements = [x[1] for x in sorted_tuples]


class TestExercise16_1_2(TestCase):

    def test_greedy_activity_selector_(self):
        n = random.randint(1, 15)
        start_times, finish_times = setup_activities(n)
        sort_activities_by_start_time(start_times, finish_times)

        actual_activities = greedy_activity_selector_(start_times, finish_times)

        actual_activities_ids = decode_activities(actual_activities)
        assert_that(activities_compatible(actual_activities_ids, start_times, finish_times))
        expected_activities = activity_selector_bruteforce(start_times, finish_times)
        assert_that(actual_activities, has_length(expected_activities))
