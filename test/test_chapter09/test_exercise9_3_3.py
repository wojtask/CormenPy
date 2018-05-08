from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.exercise9_3_3 import best_case_quicksort
from datastructures.array import Array


class TestExercise9_3_3(TestCase):

    def test_best_case_quicksort(self):
        array, elements = get_random_array()

        best_case_quicksort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
