import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter17.textbook17_1 import multipop, increment
from datastructures.array import Array
from test_chapter02.test_exercise2_1_4 import bits_to_number


class TestTextbook17_1(TestCase):

    def test_multipop(self):
        size = 15
        k = random.randint(1, size)
        stack, _ = get_random_array(min_size=size, max_size=size)
        stack.top = top = random.randint(0, size)

        multipop(stack, k)

        if k <= top:
            assert_that(stack.top, is_(equal_to(top - k)))
        else:
            assert_that(stack.top, is_(equal_to(0)))

    def test_increment(self):
        k = random.randint(1, 8)
        elements = [random.randint(0, 1) for _ in range(k)]
        array = Array(elements, start=0)

        increment(array)

        actual_n_plus_1 = bits_to_number(array.elements)
        n = bits_to_number(elements)
        expected_n_plus_1 = (n + 1) % (2 ** k)
        assert_that(actual_n_plus_1, is_(equal_to(expected_n_plus_1)))
