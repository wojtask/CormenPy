from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.exercise14_1_7 import os_count_inversions
from datastructures.array import Array


class TestExercise14_1_7(TestCase):

    def test_os_count_inversions(self):
        array = get_random_array()

        actual_inversions = os_count_inversions(array)

        assert_that(array.is_modified(), is_(False))
        expected_inversions = sum(Array(y for y in array[i + 1:] if y < x).length for i, x in enumerate(array, start=1))
        assert_that(actual_inversions, is_(equal_to(expected_inversions)))
