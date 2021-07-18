import itertools
import math
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.exercise16_2_4 import greedy_refueling
from util import between


def stops_valid(stops, stations, max_range):
    previous_stop = 0
    for stop in sorted(stops):
        if sum(stations[previous_stop + 1:stop]) > max_range:
            return False
        previous_stop = stop
    return sum(stations[previous_stop + 1:stations.length]) <= max_range


def refueling_bruteforce(stations, n):
    min_stops = math.inf
    m = stations.length
    for nstops in between(0, m):
        for stops in itertools.combinations(between(1, m), nstops):
            if stops_valid(stops, stations, n):
                min_stops = min(min_stops, nstops)
                break
    return min_stops


class TestExercise16_2_4(TestCase):

    def test_greedy_refueling(self):
        n = random.randint(1, 100)
        m = random.randint(1, 15)
        stations = get_random_array(size=m + 1, max_value=n)

        actual_stops = greedy_refueling(stations, n)

        valid = stops_valid(actual_stops, stations, n)
        assert_that(valid, is_(True))
        expected_min_stops = refueling_bruteforce(stations, n)
        assert_that(len(actual_stops), is_(equal_to(expected_min_stops)))
