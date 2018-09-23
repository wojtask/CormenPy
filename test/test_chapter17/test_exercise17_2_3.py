import random
from unittest import TestCase

from hamcrest import *

from chapter17.exercise17_2_3 import increment_, reset
from datastructures.array import Array
from test_chapter02.test_exercise2_1_4 import bits_to_number


class TestExercise17_2_3(TestCase):

    def test_increment_(self):
        k = random.randint(1, 8)
        highest = random.randint(-1, k - 1)
        if highest == -1:
            elements = [0] * k
        else:
            elements = [random.randint(0, 1) for _ in range(highest)] + [1] + [0] * (k - 1 - highest)
        array = Array(elements, start=0)
        array.highest = highest

        increment_(array)

        actual_n_plus_1 = bits_to_number(array.elements)
        n = bits_to_number(elements)
        expected_n_plus_1 = (n + 1) % (2 ** k)
        assert_that(actual_n_plus_1, is_(equal_to(expected_n_plus_1)))
        if actual_n_plus_1 == 0:
            assert_that(array.highest, is_(equal_to(-1)))
        else:
            assert_that(array.highest, is_(greater_than_or_equal_to(highest)))
            assert_that(array[array.highest], is_(equal_to(1)))

    def test_reset(self):
        k = random.randint(1, 8)
        highest = random.randint(-1, k - 1)
        if highest == -1:
            elements = [0] * k
        else:
            elements = [random.randint(0, 1) for _ in range(highest)] + [1] + [0] * (k - 1 - highest)
        array = Array(elements, start=0)
        array.highest = highest

        reset(array)

        actual_zero = bits_to_number(array.elements)
        assert_that(actual_zero, is_(equal_to(0)))
        assert_that(array.highest, is_(equal_to(-1)))
