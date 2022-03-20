import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.exercise16_1_3 import activity_scheduler
from datastructures.array import Array
from util import between


def max_overlapping_activities(s, f):
    n = s.length
    max_overlaps = 0
    for i in between(1, n):
        overlaps = 0
        for j in between(1, n):
            if s[j] <= s[i] < f[j]:
                overlaps += 1
        max_overlaps = max(max_overlaps, overlaps)
    return max_overlaps


def assert_schedule_consistent(schedule, s, f):
    n = s.length
    for i in between(1, n - 1):
        for j in between(i + 1, n):
            if s[i] < f[j] and s[j] < f[i]:
                assert_that(schedule[i], is_(not_(equal_to(schedule[j]))))


class TestExercise16_1_3(TestCase):

    def test_activity_scheduler(self):
        n = random.randint(1, 15)
        start_times = get_random_array(size=n, max_value=49)
        finish_times = Array(start_time + random.randint(1, 50) for start_time in start_times)

        actual_schedule = activity_scheduler(start_times, finish_times)

        actual_halls_needed = len(set(hall_number for hall_number in actual_schedule))
        expected_halls_needed = max_overlapping_activities(start_times, finish_times)
        assert_that(actual_halls_needed, is_(equal_to(expected_halls_needed)))
        assert_schedule_consistent(actual_schedule, start_times, finish_times)
