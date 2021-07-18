import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.textbook_problem2_2 import bubble_sort


class TestTextbookProblem2_2(TestCase):

    def test_bubble_sort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        bubble_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
