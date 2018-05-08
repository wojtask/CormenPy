import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_8 import intersecting_chords
from datastructures.array import Array


class TestExercise14_1_8(TestCase):

    def test_intersecting_chords(self):
        n = random.randint(1, 20)
        endpoints = [i for i in range(1, n + 1)] * 2
        random.shuffle(endpoints)
        chords = Array(endpoints)

        actual_intersections = intersecting_chords(chords)

        expected_intersections = 0
        for endpoint in range(1, n + 1):
            idx1 = endpoints.index(endpoint)
            idx2 = endpoints.index(endpoint, idx1 + 1)
            inner_endpoints = endpoints[idx1 + 1:idx2]
            outer_endpoints = endpoints[:idx1] + endpoints[idx2 + 1:]
            # count how many inner endpoints have their outer counterparts
            for inner_endpoint in inner_endpoints:
                expected_intersections += outer_endpoints.count(inner_endpoint)  # count will return either 0 or 1
        expected_intersections //= 2  # each intersection was actually counted twice
        assert_that(actual_intersections, is_(equal_to(expected_intersections)))
