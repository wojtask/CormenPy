import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter17.exercise17_2_3 import increment_, reset, ResettableCounter
from test_chapter02.test_exercise2_1_4 import bits_to_number


class TestExercise17_2_3(TestCase):

    def test_increment_(self):
        k = random.randint(1, 8)
        highest = random.randint(-1, k - 1)
        if highest == -1:
            counter = ResettableCounter([0] * k)
        else:
            counter = ResettableCounter(get_random_array(size=highest, max_value=1) + [1] + [0] * (k - 1 - highest))
        counter.highest = highest
        original = copy.deepcopy(counter)

        increment_(counter)

        actual_n_plus_1 = bits_to_number(counter)
        n = bits_to_number(original)
        expected_n_plus_1 = (n + 1) % (2 ** k)
        assert_that(actual_n_plus_1, is_(equal_to(expected_n_plus_1)))
        if actual_n_plus_1 == 0:
            assert_that(counter.highest, is_(equal_to(-1)))
        else:
            assert_that(counter.highest, is_(greater_than_or_equal_to(highest)))
            assert_that(counter[counter.highest], is_(equal_to(1)))

    def test_reset(self):
        k = random.randint(1, 8)
        highest = random.randint(-1, k - 1)
        if highest == -1:
            counter = ResettableCounter([0] * k)
        else:
            counter = ResettableCounter(get_random_array(size=highest, max_value=1) + [1] + [0] * (k - 1 - highest))
        counter.highest = highest

        reset(counter)

        actual_zero = bits_to_number(counter)
        assert_that(actual_zero, is_(equal_to(0)))
        assert_that(counter.highest, is_(equal_to(-1)))
