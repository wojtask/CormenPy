import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.textbook8_3 import radix_sort


class TestTextbook8_3(TestCase):

    def test_radix_sort(self):
        d = 5
        array = get_random_array(max_value=10 ** d - 1)
        original = copy.deepcopy(array)

        radix_sort(array, d)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
