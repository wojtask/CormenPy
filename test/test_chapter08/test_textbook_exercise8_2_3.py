from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.textbook_exercise8_2_3 import unstable_counting_sort
from datastructures.array import Array


class TestTextbookExercise8_2_3(TestCase):

    def test_unstable_counting_sort(self):
        k = 20
        array, elements = get_random_array(max_value=k)
        actual_sorted_array = Array.indexed(1, array.length)

        unstable_counting_sort(array, actual_sorted_array, k)

        expected_array = Array(sorted(elements))
        assert_that(actual_sorted_array, is_(equal_to(expected_array)))
