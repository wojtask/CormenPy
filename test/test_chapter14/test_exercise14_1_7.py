from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.exercise14_1_7 import os_count_inversions


class TestExercise14_1_7(TestCase):

    def test_os_count_inversions(self):
        array, elements = get_random_array()

        actual_inversions = os_count_inversions(array)

        expected_inversions = sum(len([y for y in elements[i + 1:] if y < x]) for i, x in enumerate(elements))
        assert_that(actual_inversions, is_(equal_to(expected_inversions)))
