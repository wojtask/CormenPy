from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook7_1 import quicksort
from datastructures.array import Array


class TestTextbook7_1(TestCase):

    def test_quicksort(self):
        array, elements = get_random_array()

        quicksort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
