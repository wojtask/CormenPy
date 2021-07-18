import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.textbook2_3 import merge_sort


class TestTextbook2_3(TestCase):

    def test_merge_sort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        merge_sort(array, 1, array.length)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
