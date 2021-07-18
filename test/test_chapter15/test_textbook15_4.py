import io
import itertools
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter15.textbook15_4 import lcs_length, print_lcs
from datastructures.array import Array
from util import between


def is_subsequence_of(subsequence, sequence):
    pos = 1
    for c in subsequence:
        try:
            pos += sequence[pos:].index(c)
        except ValueError:
            return False
    return True


def get_maximum_lcs_length_bruteforce(sequence1, sequence2):
    max_length = 0
    for i in between(1, min(sequence1.length, sequence2.length)):
        for subsequence in itertools.combinations(sequence1, i):
            if is_subsequence_of(Array(subsequence), sequence2):
                max_length = len(subsequence)
    return max_length


class TestTextbook15_4(TestCase):

    def test_lcs_length(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in between(1, random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in between(1, random.randint(1, 10))))
        captured_output = io.StringIO()

        actual_maximum_lengths, optimal_solution = lcs_length(sequence1, sequence2)
        with redirect_stdout(captured_output):
            print_lcs(optimal_solution, sequence1, sequence1.length, sequence2.length)
            print()  # a blank line after the output

        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_lengths[sequence1.length, sequence2.length], is_(equal_to(expected_maximum_length)))
        actual_lcs = Array(captured_output.getvalue().splitlines()[0])
        assert_that(actual_lcs.length, is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lcs, sequence1))
        assert_that(is_subsequence_of(actual_lcs, sequence2))
