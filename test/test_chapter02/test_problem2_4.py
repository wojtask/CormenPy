from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.problem2_4 import count_inversions


class TestProblem2_4(TestCase):

    def test_count_inversions(self):
        array, elements = get_random_array()

        actual_inversions = count_inversions(array, 1, array.length)

        expected_inversions = sum(len([y for y in elements[i + 1:] if y < x]) for i, x in enumerate(elements))
        assert_that(actual_inversions, is_(equal_to(expected_inversions)))
