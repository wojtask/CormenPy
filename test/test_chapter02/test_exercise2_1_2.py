from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_1_2 import nonincreasing_insertion_sort
from datastructures.array import Array


class TestExercise2_1_2(TestCase):

    def test_nonincreasing_insertion_sort(self):
        array, elements = get_random_array()

        nonincreasing_insertion_sort(array)

        expected_array = Array(sorted(elements, reverse=True))
        assert_that(array, is_(equal_to(expected_array)))
