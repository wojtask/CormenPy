import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_2_2 import selection_sort


class TestExercise2_2_2(TestCase):

    def test_selection_sort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        selection_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
