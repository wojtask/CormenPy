import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_unique_array
from chapter09.problem9_3 import small_order_select


class TestProblem9_3(TestCase):

    def test_small_order_select(self):
        array = get_random_unique_array(max_size=50)
        original = copy.deepcopy(array)
        i = random.randint(1, array.length // 5 + 1)  # pick a small i

        actual_order_statistic = small_order_select(array, i)

        expected_order_statistic = original.sort()[i]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))
