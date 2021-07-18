import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.textbook9_1 import minimum, minimum_maximum


class TestTextbook9_1(TestCase):

    def test_minimum(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        actual_min = minimum(array)

        assert_that(actual_min, is_(equal_to(min(original))))
        assert_that(array, is_(equal_to(original)))

    def test_minimum_maximum(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        actual_min, actual_max = minimum_maximum(array)

        assert_that(actual_min, is_(equal_to(min(original))))
        assert_that(actual_max, is_(equal_to(max(original))))
        assert_that(array, is_(equal_to(original)))
