import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.textbook8_2 import counting_sort
from datastructures.array import Array


class TestTextbook8_2(TestCase):

    def test_counting_sort(self):
        k = 20
        array = get_random_array(max_value=k)
        original = copy.deepcopy(array)
        actual_sorted_array = Array.indexed(1, array.length)

        counting_sort(array, actual_sorted_array, k)

        expected_array = original.sort()
        assert_that(actual_sorted_array, is_(equal_to(expected_array)))
