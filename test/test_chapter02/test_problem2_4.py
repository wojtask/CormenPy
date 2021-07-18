import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.problem2_4 import count_inversions
from datastructures.array import Array


class TestProblem2_4(TestCase):

    def test_count_inversions(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        actual_inversions = count_inversions(array, 1, array.length)

        expected_inversions = sum(
            Array(y for y in original[i + 1:] if y < x).length for i, x in enumerate(original, start=1))
        assert_that(actual_inversions, is_(equal_to(expected_inversions)))
