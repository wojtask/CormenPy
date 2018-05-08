from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.textbook2_1 import insertion_sort
from datastructures.array import Array


class TestTextbook2_1(TestCase):

    def test_insertion_sort(self):
        array, elements = get_random_array()

        insertion_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
