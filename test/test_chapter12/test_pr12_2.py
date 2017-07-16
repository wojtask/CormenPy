import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from chapter12.pr12_2 import bit_strings_sort
from datastructures.array import Array


def _random_bit_string():
    return ''.join(random.choice('01') for _ in range(random.randint(1, 10)))


class Problem12_2Test(TestCase):
    def test_bit_strings_sort(self):
        n = random.randint(1, 20)
        # generate a set of random non-empty bit strings of lengths <= 10
        bit_strings = {_random_bit_string() for _ in range(n)}
        array = Array(bit_strings)
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            bit_strings_sort(array)
        actual_output = captured_output.getvalue().splitlines()
        expected_output = sorted(bit_strings)
        self.assertEqual(actual_output, expected_output)
