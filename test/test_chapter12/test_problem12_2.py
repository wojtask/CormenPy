import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter12.problem12_2 import bit_strings_sort
from datastructures.array import Array


def random_bit_string():
    return ''.join(random.choice('01') for _ in range(random.randint(1, 10)))


class TestProblem12_2(TestCase):

    def test_bit_strings_sort(self):
        n = random.randint(1, 20)
        # generate a set of random non-empty bit strings of lengths <= 10
        bit_strings = {random_bit_string() for _ in range(n)}
        array = Array(bit_strings)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            bit_strings_sort(array)

        actual_output = captured_output.getvalue().splitlines()
        expected_output = sorted(bit_strings)
        assert_that(actual_output, is_(equal_to(expected_output)))
