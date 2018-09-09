from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.problem16_2 import average_time_schedule
from datastructures.array import Array


def get_min_average_completion_time_bruteforce(processing_times):
    return compute_average_completion_time(Array(sorted(processing_times)))


def compute_average_completion_time(schedule):
    average_completion_time = 0
    completion_time = 0
    for processing_time in schedule:
        completion_time += processing_time
        average_completion_time += completion_time
    return average_completion_time / schedule.length


class TestProblem16_2(TestCase):

    def test_average_time_schedule(self):
        processing_times, processing_times_elements = get_random_array()
        original_processing_times = Array(processing_times_elements)

        actual_average_completion_time = average_time_schedule(processing_times)

        expected_min_average_completion_time = get_min_average_completion_time_bruteforce(original_processing_times)
        assert_that(actual_average_completion_time, is_(equal_to(expected_min_average_completion_time)))
        average_completion_time_from_schedule = compute_average_completion_time(processing_times)
        assert_that(average_completion_time_from_schedule, is_(equal_to(expected_min_average_completion_time)))
