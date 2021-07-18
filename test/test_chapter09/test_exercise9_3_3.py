import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.exercise9_3_3 import best_case_quicksort


class TestExercise9_3_3(TestCase):

    def test_best_case_quicksort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        best_case_quicksort(array, 1, array.length)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
