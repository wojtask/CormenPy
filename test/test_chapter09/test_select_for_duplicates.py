import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.select_for_duplicates import select_for_duplicates


class TestSelectForDuplicates(TestCase):

    def test_select_for_duplicates(self):
        array = get_random_array(min_value=0, max_value=4)
        original = copy.deepcopy(array)
        i = random.randint(1, array.length)

        actual_order_statistic = select_for_duplicates(array, 1, array.length, i)

        expected_order_statistic = original.sort()[i]
        assert_that(actual_order_statistic, is_(equal_to(expected_order_statistic)))
