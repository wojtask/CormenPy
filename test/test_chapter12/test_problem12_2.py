import copy
import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter12.problem12_2 import bit_strings_sort
from datastructures.array import Array
from util import between


def random_bit_string():
    return ''.join(random.choice('01') for _ in between(1, random.randint(1, 10)))


class TestProblem12_2(TestCase):

    def test_bit_strings_sort(self):
        n = random.randint(1, 20)
        # generate a set of random non-empty bit strings of lengths <= 10
        array = Array({random_bit_string() for _ in between(1, n)})
        original = copy.deepcopy(array)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            bit_strings_sort(array)

        actual_output = Array(captured_output.getvalue().splitlines())
        expected_output = original.sort()
        assert_that(actual_output, is_(equal_to(expected_output)))
