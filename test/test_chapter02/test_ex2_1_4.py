import random
from unittest import TestCase

from chapter02.ex2_1_4 import binary_add
from test.test_datastructures.array_util import random_int_array


def _bits_to_number(bits):
    number = 0
    for bit in reversed(bits):
        number = 2 * number + bit
    return number


class Ex2_1_4Test(TestCase):
    def test_binary_add(self):
        n = random.randint(1, 20)
        array1, data1 = random_int_array(min_size=n, max_size=n, max_value=1)
        array2, data2 = random_int_array(min_size=n, max_size=n, max_value=1)
        number1 = _bits_to_number(data1)
        number2 = _bits_to_number(data2)
        actual_sum_bits = binary_add(array1, array2)
        actual_sum = _bits_to_number(actual_sum_bits.data)
        self.assertEqual(actual_sum, number1 + number2)
