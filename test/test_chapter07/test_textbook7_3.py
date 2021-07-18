import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook7_3 import randomized_quicksort


class TestTextbook7_3(TestCase):

    def test_randomized_quicksort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        randomized_quicksort(array, 1, array.length)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
