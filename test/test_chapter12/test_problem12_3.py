from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter12.problem12_3 import randomly_built_tree_quicksort
from datastructures.array import Array


class TestProblem12_3(TestCase):

    def test_randomly_built_tree_quicksort(self):
        array, elements = get_random_array()

        randomly_built_tree_quicksort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
