import io
import itertools
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.exercise15_4_5 import lmis
from datastructures.array import Array
from test_chapter15.test_textbook15_4 import is_subsequence_of
from util import between


def is_monotonically_increasing(sequence):
    for i in between(2, sequence.length):
        if sequence[i] < sequence[i - 1]:
            return False
    return True


def get_maximum_lmis_length_bruteforce(sequence):
    max_length = 0
    for i in between(1, sequence.length):
        for subsequence in itertools.combinations(sequence, i):
            if is_monotonically_increasing(Array(subsequence)):
                max_length = len(subsequence)
    return max_length


class TestExercise15_4_5(TestCase):

    def test_lmis(self):
        sequence = get_random_array(max_value=10)
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            lmis(sequence)

        assert_that(sequence.is_modified(), is_(False))
        expected_maximum_length = get_maximum_lmis_length_bruteforce(sequence)
        actual_lmis = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_lmis.length, is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lmis, sequence))
        assert_that(is_monotonically_increasing(actual_lmis))
