import io
import itertools
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.exercise15_4_5 import lis_length, print_lis
from test_chapter15.test_textbook15_4 import is_subsequence_of
from util import between


def is_monotonically_increasing(sequence):
    for i in between(1, len(sequence) - 1):
        if sequence[i] < sequence[i - 1]:
            return False
    return True


def get_maximum_lis_length_bruteforce(sequence):
    max_length = 0
    for i in between(1, sequence.length):
        for subsequence in itertools.combinations(sequence, i):
            if is_monotonically_increasing(subsequence):
                max_length = len(subsequence)
    return max_length


class TestExercise15_4_5(TestCase):

    def test_lis_length(self):
        sequence, _ = get_random_array(max_value=10)
        captured_output = io.StringIO()

        actual_maximum_length, terms, last_term = lis_length(sequence)
        with redirect_stdout(captured_output):
            print_lis(terms, sequence, last_term)

        expected_maximum_length = get_maximum_lis_length_bruteforce(sequence)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))
        actual_lis = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(len(actual_lis), is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lis, sequence))
        assert_that(is_monotonically_increasing(actual_lis))
