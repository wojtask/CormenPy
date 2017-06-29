import unittest

from chapter02.ex2_1_4 import *
from datastructures.array import Array


class BinaryAddTest(unittest.TestCase):
    def test_binary_add(self):
        bits1 = Array([0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1])
        bits2 = Array([0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1])
        number1 = self.bits_to_number(bits1)
        number2 = self.bits_to_number(bits2)
        sum_bits = binary_add(bits1, bits2)
        sum = self.bits_to_number(sum_bits)
        self.assertEqual(number1 + number2, sum)

    @staticmethod
    def bits_to_number(bits):
        number = 0
        for bit in reversed(bits.data):
            number = 2 * number + bit
        return number
