import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.problem7_4 import quicksort__


class TestProblem7_4(TestCase):

    def test_quicksort__(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        quicksort__(array, 1, array.length)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
