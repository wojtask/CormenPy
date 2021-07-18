import copy
import itertools
import math
import random
import re
from unittest import TestCase

from hamcrest import *

from chapter16.textbook16_1 import recursive_activity_selector, greedy_activity_selector
from datastructures.array import Array
from util import between


def get_activities_sorted_by_start_time(n):
    s, f = setup_activities(n)
    sorted_tuples = sorted(zip(s, f), key=lambda x: x[0])
    return Array((x[0] for x in sorted_tuples), start=0), Array((x[1] for x in sorted_tuples), start=0)


def get_activities_sorted_by_finish_time(n):
    s, f = setup_activities(n)
    sorted_tuples = sorted(zip(s, f), key=lambda x: x[1])
    return Array((x[0] for x in sorted_tuples), start=0), Array((x[1] for x in sorted_tuples), start=0)


def setup_activities(n):
    start_times = Array.indexed(0, n + 1)
    finish_times = Array.indexed(0, n + 1)
    for i in between(1, n):
        start_times[i] = random.randint(0, 49)
        finish_times[i] = start_times[i] + random.randint(1, 50)
    start_times[0], finish_times[0] = 0, 0
    start_times[n + 1], finish_times[n + 1] = math.inf, math.inf
    return start_times, finish_times


def activities_compatible(activities_ids, s, f):
    for a1 in activities_ids:
        for a2 in activities_ids:
            if a1 != a2 and s[a1] < f[a2] and s[a2] < f[a1]:
                return False
    return True


def decode_activities(activities):
    return Array(int(re.search(r'a(\d+)', activity).group(1)) for activity in activities)


def activity_selector_bruteforce(s, f):
    n = s.length - 2
    max_size = 0
    for m in between(1, n):
        for activities_ids in itertools.combinations(between(1, n), m):
            if activities_compatible(activities_ids, s, f):
                max_size = max(max_size, m)
    return max_size


class TestTextbook16_1(TestCase):

    def test_recursive_activity_selector(self):
        n = random.randint(1, 15)
        start_times, finish_times = get_activities_sorted_by_finish_time(n)
        original_start_times = copy.deepcopy(start_times)
        original_finish_times = copy.deepcopy(finish_times)

        actual_activities = recursive_activity_selector(start_times, finish_times, 0, n)

        actual_activities_ids = decode_activities(actual_activities)
        assert_that(activities_compatible(actual_activities_ids, start_times, finish_times))
        expected_activities_size = activity_selector_bruteforce(original_start_times, original_finish_times)
        assert_that(actual_activities, has_length(expected_activities_size))

    def test_greedy_activity_selector(self):
        n = random.randint(1, 15)
        start_times, finish_times = get_activities_sorted_by_finish_time(n)
        original_start_times = copy.deepcopy(start_times)
        original_finish_times = copy.deepcopy(finish_times)

        actual_activities = greedy_activity_selector(start_times, finish_times)

        actual_activities_ids = decode_activities(actual_activities)
        assert_that(activities_compatible(actual_activities_ids, start_times, finish_times))
        expected_activities_size = activity_selector_bruteforce(original_start_times, original_finish_times)
        assert_that(actual_activities, has_length(expected_activities_size))
