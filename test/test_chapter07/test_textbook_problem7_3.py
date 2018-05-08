from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook_problem7_3 import stooge_sort
from datastructures.array import Array


class TestTextbookProblem7_3(TestCase):

    def test_stooge_sort(self):
        array, elements = get_random_array()

        stooge_sort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
