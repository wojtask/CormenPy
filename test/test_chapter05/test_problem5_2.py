from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter05.problem5_2 import random_search


class TestProblem5_2(TestCase):

    def test_random_search(self):
        import random

        array, elements = get_random_array(min_size=10, max_size=20, max_value=20)
        v = random.randint(0, 20)

        actual_index = random_search(array, v)

        expected_indexes = [i + 1 for i, x in enumerate(elements) if x == v]
        if expected_indexes:
            assert_that(actual_index, is_in(expected_indexes))
        else:
            assert_that(actual_index, is_(none()))
