import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.textbook6_4 import heapsort


class TestTextbook6_4(TestCase):

    def test_heapsort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        heapsort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
