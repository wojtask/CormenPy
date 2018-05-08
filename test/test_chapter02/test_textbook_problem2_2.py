from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.textbook_problem2_2 import bubble_sort
from datastructures.array import Array


class TestTextbookProblem2_2(TestCase):

    def test_bubble_sort(self):
        array, elements = get_random_array()

        bubble_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
