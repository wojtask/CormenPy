import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_3_7 import sum_search


class TestExercise2_3_7(TestCase):

    def test_sum_search(self):
        array = get_random_array(max_value=20, unique=True)
        original = copy.deepcopy(array)
        sum_to_find = random.randint(0, 40)

        actual_found = sum_search(array, sum_to_find)

        all_sums = {x + y for x in original for y in original if y != x}
        expected_found = sum_to_find in all_sums
        assert_that(actual_found, is_(equal_to(expected_found)))
