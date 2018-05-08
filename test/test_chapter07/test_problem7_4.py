from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.problem7_4 import quicksort__
from datastructures.array import Array


class TestProblem7_4(TestCase):

    def test_quicksort__(self):
        array, elements = get_random_array()

        quicksort__(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
