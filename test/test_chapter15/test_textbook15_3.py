import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.textbook15_3 import recursive_matrix_chain, memoized_matrix_chain
from datastructures.array import Array
from test_chapter15.test_textbook15_2 import get_minimum_matrix_product_cost
from util import between


class TestTextbook15_3(TestCase):

    def test_recursive_matrix_chain(self):
        n = random.randint(1, 10)
        dimensions = get_random_array(size=n + 1, start=0)
        m = Array(Array.indexed(1, n) for _ in between(1, n))

        actual_minimum_cost = recursive_matrix_chain(dimensions, m, 1, n)

        assert_that(dimensions.is_modified(), is_(False))
        expected_minimum_cost = get_minimum_matrix_product_cost(dimensions, 1, n)
        assert_that(actual_minimum_cost, is_(equal_to(expected_minimum_cost)))

    def test_memoized_matrix_chain(self):
        n = random.randint(1, 10)
        dimensions = get_random_array(size=n + 1, start=0)

        actual_minimum_cost = memoized_matrix_chain(dimensions)

        assert_that(dimensions.is_modified(), is_(False))
        expected_minimum_cost = get_minimum_matrix_product_cost(dimensions, 1, n)
        assert_that(actual_minimum_cost, is_(equal_to(expected_minimum_cost)))
