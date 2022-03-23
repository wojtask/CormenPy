import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter05.problem5_2 import random_search


class TestProblem5_2(TestCase):

    def test_random_search(self):
        array = get_random_array(min_size=10, max_size=20, max_value=20)
        v = random.randint(0, 20)

        actual_index = random_search(array, v)

        if actual_index:
            assert_that(array[actual_index], is_(equal_to(v)))
        else:
            assert_that(v not in array)
        assert_that(array.is_modified(), is_(False))
