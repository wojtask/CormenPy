from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.textbook2_3 import merge_sort
from datastructures.array import Array


class TestTextbook2_3(TestCase):

    def test_merge_sort(self):
        array, elements = get_random_array()

        merge_sort(array, 1, array.length)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
