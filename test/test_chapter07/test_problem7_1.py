import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.problem7_1 import hoare_quicksort


class TestProblem7_1(TestCase):

    def test_hoare_quicksort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        hoare_quicksort(array, 1, array.length)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
