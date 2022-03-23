import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_1_4 import binary_add


def bits_to_number(bits):
    return int(''.join(str(bit) for bit in reversed(bits)), 2)


class TestExercise2_1_4(TestCase):

    def test_binary_add(self):
        n = random.randint(1, 20)
        array1 = get_random_array(size=n, max_value=1)
        array2 = get_random_array(size=n, max_value=1)

        actual_sum_bits = binary_add(array1, array2)

        actual_sum = bits_to_number(actual_sum_bits)
        number1 = bits_to_number(array1)
        number2 = bits_to_number(array2)
        expected_sum = number1 + number2
        assert_that(expected_sum, is_(equal_to(actual_sum)))
        assert_that(array1.is_modified(), is_(False))
        assert_that(array2.is_modified(), is_(False))
