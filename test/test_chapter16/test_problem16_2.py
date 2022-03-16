import copy
import math
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.problem16_2 import act_schedule, preemptive_act_schedule, Activity
from datastructures.array import Array
from util import between


def get_min_act_bruteforce(processing_times):
    return compute_act(processing_times.sort())


def compute_act(schedule):
    act = 0
    completion_time = 0
    for processing_time in schedule:
        completion_time += processing_time
        act += completion_time
    return act / schedule.length


def get_min_schedule(activities, schedule, time):
    min_schedule_cost = math.inf
    min_schedule = copy.deepcopy(schedule)
    earliest_future_release_time = math.inf
    for i in between(1, activities.length):
        activity = activities[i]
        if activity.r <= time and activity.p > 0:
            activity.p -= 1
            deleted = False
            if activity.p == 0:
                schedule[activity.id] = time + 1
                activities.pop(i)
                deleted = True
            schedule = get_min_schedule(activities, schedule, time + 1)
            cost = sum(schedule.elements)
            if cost < min_schedule_cost:
                min_schedule_cost = cost
                min_schedule = copy.deepcopy(schedule)
            if deleted:
                activities.insert(i, activity)
            activity.p += 1
        if activity.r > time and activity.p > 0:
            earliest_future_release_time = min(earliest_future_release_time, activity.r)
    if earliest_future_release_time < math.inf:
        schedule = get_min_schedule(activities, schedule, earliest_future_release_time)
        if sum(schedule.elements) < min_schedule_cost:
            return copy.deepcopy(schedule)
    return min_schedule


def get_min_preemptive_act_bruteforce(processing_times, release_times):
    n = processing_times.length
    activities = Array(Activity(i, processing_times[i], release_times[i]) for i in between(1, n))
    schedule = Array.indexed(1, n)
    return sum(get_min_schedule(activities, schedule, 0)) / n


class TestProblem16_2(TestCase):

    def test_act_schedule(self):
        processing_times = get_random_array()
        original_processing_times = copy.deepcopy(processing_times)

        actual_schedule = act_schedule(processing_times)

        actual_min_act = sum(actual_schedule.elements) / actual_schedule.length
        expected_min_act = get_min_act_bruteforce(original_processing_times)
        assert_that(actual_min_act, is_(equal_to(expected_min_act)))

    def test_preemptive_act_schedule(self):
        n = random.randint(1, 4)
        processing_times = get_random_array(size=n, min_value=1, max_value=3)
        release_times = get_random_array(size=n, max_value=15)
        # sort activities by release time
        sorted_tuples = sorted(zip(processing_times, release_times), key=lambda x: x[1])
        processing_times, release_times = Array(x[0] for x in sorted_tuples), Array(x[1] for x in sorted_tuples)
        release_times.append(math.inf)
        original_processing_times = copy.deepcopy(processing_times)
        original_release_times = copy.deepcopy(release_times)

        actual_schedule = preemptive_act_schedule(processing_times, release_times)

        for i in between(1, n):
            assert_that(actual_schedule[i], is_(greater_than(release_times[i])))
        actual_min_act = sum(actual_schedule.elements) / actual_schedule.length
        expected_min_act = get_min_preemptive_act_bruteforce(original_processing_times, original_release_times)
        assert_that(actual_min_act, is_(equal_to(expected_min_act)))
