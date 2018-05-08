from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.textbook6_4 import heapsort
from datastructures.array import Array


class TestTextbook6_4(TestCase):

    def test_heapsort(self):
        array, elements = get_random_array()

        heapsort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
