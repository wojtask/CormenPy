import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter15.exercise15_4_2 import print_lcs_
from chapter15.textbook15_4 import lcs_length
from datastructures.array import Array
from test_chapter15.test_textbook15_4 import get_maximum_lcs_length_bruteforce, is_subsequence_of
from util import between


class TestExercise15_4_2(TestCase):

    def test_print_lcs_(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in between(1, random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in between(1, random.randint(1, 10))))
        captured_output = io.StringIO()

        actual_maximum_lengths, _ = lcs_length(sequence1, sequence2)
        with redirect_stdout(captured_output):
            print_lcs_(actual_maximum_lengths, sequence1, sequence2, sequence1.length, sequence2.length)
            print()  # a blank line after the output

        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_lengths[sequence1.length, sequence2.length], is_(equal_to(expected_maximum_length)))
        actual_lcs = Array(captured_output.getvalue().splitlines()[0])
        assert_that(actual_lcs.length, is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lcs, sequence1))
        assert_that(is_subsequence_of(actual_lcs, sequence2))
