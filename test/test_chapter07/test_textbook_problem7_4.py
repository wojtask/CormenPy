from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook_problem7_4 import quicksort_
from datastructures.array import Array


class TestTextbookProblem7_4(TestCase):

    def test_quicksort_(self):
        array, elements = get_random_array()

        quicksort_(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
