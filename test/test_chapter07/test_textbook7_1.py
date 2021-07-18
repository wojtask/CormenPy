import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook7_1 import quicksort


class TestTextbook7_1(TestCase):

    def test_quicksort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        quicksort(array, 1, array.length)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
