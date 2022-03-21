import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_1_8 import intersecting_chords
from datastructures.array import Array
from util import between


class TestExercise14_1_8(TestCase):

    def test_intersecting_chords(self):
        n = random.randint(1, 20)
        chords = Array(list(between(1, n)) * 2).shuffle()
        original = copy.deepcopy(chords)

        actual_intersections = intersecting_chords(chords)

        assert_that(chords, is_(equal_to(original)))
        expected_intersections = 0
        for endpoint in between(1, n):
            idx1 = chords.index(endpoint)
            idx2 = chords.index(endpoint, idx1 + 1)
            inner_endpoints = chords[idx1 + 1:idx2 - 1]
            outer_endpoints = chords[:idx1 - 1] + chords[idx2 + 1:]
            # count how many inner endpoints have their outer counterparts
            for inner_endpoint in inner_endpoints:
                expected_intersections += outer_endpoints.count(inner_endpoint)  # count will return either 0 or 1
        expected_intersections //= 2  # each intersection was actually counted twice
        assert_that(actual_intersections, is_(equal_to(expected_intersections)))
