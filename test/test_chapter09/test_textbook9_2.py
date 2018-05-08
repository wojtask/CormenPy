import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.textbook9_2 import randomized_select


class TestTextbook9_2(TestCase):

    def test_randomized_select(self):
        array, elements = get_random_array()
        i = random.randint(1, array.length)

        actual_order_statistic = randomized_select(array, 1, array.length, i)

        expected_order_statistic = sorted(elements)[i - 1]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))
