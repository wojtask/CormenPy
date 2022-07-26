import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.problem8_2 import bit_sort, counting_sort_in_place


class TestProblem8_2(TestCase):

    def test_bit_sort(self):
        array = get_random_array(max_value=1)
        original = copy.deepcopy(array)

        bit_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))

    def test_counting_sort_in_place(self):
        n = random.randint(1, 20)
        k = 20
        array = get_random_array(size=n, min_value=1, max_value=k)
        original = copy.deepcopy(array)

        counting_sort_in_place(array, k)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
