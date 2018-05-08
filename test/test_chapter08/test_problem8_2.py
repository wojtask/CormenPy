import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.problem8_2 import bitwise_sort, counting_sort_in_place
from datastructures.array import Array


class TestProblem8_2(TestCase):

    def test_bitwise_sort(self):
        array, elements = get_random_array(max_value=1)

        bitwise_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_counting_sort_in_place(self):
        n = random.randint(1, 20)
        k = 20
        elements = [random.randint(1, k) for _ in range(n)]
        array = Array(elements)

        counting_sort_in_place(array, k)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
