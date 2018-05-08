import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.textbook9_3 import select


class TestTextbook9_3(TestCase):

    def test_select(self):
        array, elements = get_random_array()
        i = random.randint(1, array.length)

        actual_order_statistic = select(array, 1, array.length, i)

        expected_order_statistic = sorted(elements)[i - 1]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))
