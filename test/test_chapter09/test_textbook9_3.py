import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.textbook9_3 import select


class TestTextbook9_3(TestCase):

    def test_select(self):
        array = get_random_array()
        original = copy.deepcopy(array)
        i = random.randint(1, array.length)

        actual_order_statistic = select(array, 1, array.length, i)

        expected_order_statistic = original.sort()[i]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))
