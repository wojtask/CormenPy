from unittest import TestCase

from chapter02.ex2_1_4 import binary_add
from datastructures.array import Array


def bits_to_number(bits):
    number = 0
    for bit in reversed(bits.data):
        number = 2 * number + bit
    return number


class Ex2_1_4Test(TestCase):
    def test_binary_add(self):
        bits1 = Array([0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1])
        bits2 = Array([0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1])
        number1 = bits_to_number(bits1)
        number2 = bits_to_number(bits2)
        sum_bits = binary_add(bits1, bits2)
        sum = bits_to_number(sum_bits)
        self.assertEqual(sum, number1 + number2)
