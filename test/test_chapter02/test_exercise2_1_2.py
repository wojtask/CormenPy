import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_1_2 import nonincreasing_insertion_sort


class TestExercise2_1_2(TestCase):

    def test_nonincreasing_insertion_sort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        nonincreasing_insertion_sort(array)

        expected_array = original.sort(reverse=True)
        assert_that(array, is_(equal_to(expected_array)))
