from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.textbook8_3 import radix_sort
from datastructures.array import Array


class TestTextbook8_3(TestCase):

    def test_radix_sort(self):
        d = 5
        array, elements = get_random_array(max_value=10 ** d - 1)

        radix_sort(array, d)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
