import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_1_3 import linear_search


class TestExercise2_1_3(TestCase):

    def test_linear_search(self):
        array, elements = get_random_array(min_size=10, max_size=20, max_value=20)
        v = random.randint(0, 20)

        actual_index = linear_search(array, v)

        try:
            expected_index = elements.index(v) + 1
            assert_that(actual_index, is_(equal_to(expected_index)))
        except ValueError:
            assert_that(actual_index, is_(none()))
