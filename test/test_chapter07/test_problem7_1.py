from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.problem7_1 import hoare_quicksort
from datastructures.array import Array


class TestProblem7_1(TestCase):

    def test_hoare_quicksort(self):
        array, elements = get_random_array()

        hoare_quicksort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
