import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.exercise9_3_5 import randomized_blackbox_select


class TestExercise9_3_5(TestCase):

    def test_randomized_blackbox_select(self):
        array = get_random_array()
        original = copy.deepcopy(array)
        k = random.randint(1, array.length)

        actual_order_statistic = randomized_blackbox_select(array, 1, array.length, k)

        expected_order_statistic = original.sort()[k]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))
