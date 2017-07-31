import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.textbook import minimum, minimum_maximum, randomized_select, select


class Textbook09Test(TestCase):

    def test_minimum(self):
        array, data = get_random_array()

        actual_min = minimum(array)

        assert_that(actual_min, is_(equal_to(min(data))))

    def test_minimum_maximum(self):
        array, data = get_random_array()

        actual_min, actual_max = minimum_maximum(array)

        assert_that(actual_min, is_(equal_to(min(data))))
        assert_that(actual_max, is_(equal_to(max(data))))

    def test_randomized_select(self):
        array, data = get_random_array()
        i = random.randint(1, array.length)

        actual_order_statistic = randomized_select(array, 1, array.length, i)

        expected_order_statistic = sorted(data)[i - 1]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))

    def test_select(self):
        array, data = get_random_array()
        i = random.randint(1, array.length)

        actual_order_statistic = select(array, 1, array.length, i)

        expected_order_statistic = sorted(data)[i - 1]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))
