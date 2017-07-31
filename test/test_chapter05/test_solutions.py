from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter05.ex5_1_2 import random
from chapter05.ex5_1_3 import unbiased_random
from chapter05.ex5_3_1 import randomize_in_place_
from chapter05.pr5_2 import random_search


class Solutions05Test(TestCase):

    def test_random(self):
        lower_bound = 10
        upper_bound = 20

        x = random(lower_bound, upper_bound)

        assert_that(x, is_(greater_than_or_equal_to(lower_bound)))
        assert_that(x, is_(less_than_or_equal_to(upper_bound)))

    def test_unbiased_random(self):
        samples = 1000
        count = [0, 0]
        for _ in range(samples):
            x = unbiased_random()
            assert_that(x, is_in([0, 1]))
            count[x] += 1

        assert_that(count[0], is_(close_to(count[1], samples // 10)))

    def test_randomize_in_place_(self):
        array, data = get_random_array()

        randomize_in_place_(array)

        assert_that(array.data, contains_inanyorder(*data))

    def test_random_search(self):
        import random

        array, data = get_random_array(min_size=10, max_size=20, max_value=20)
        v = random.randint(0, 20)

        actual_index = random_search(array, v)

        expected_indexes = [i + 1 for i, x in enumerate(data) if x == v]
        if expected_indexes:
            assert_that(actual_index, is_in(expected_indexes))
        else:
            assert_that(actual_index, is_(none()))
