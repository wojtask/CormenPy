import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.textbook2_1 import insertion_sort


class TestTextbook2_1(TestCase):

    def test_insertion_sort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        insertion_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
