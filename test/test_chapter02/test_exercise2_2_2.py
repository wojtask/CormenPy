from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_2_2 import selection_sort
from datastructures.array import Array


class TestExercise2_2_2(TestCase):

    def test_selection_sort(self):
        array, elements = get_random_array()

        selection_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
