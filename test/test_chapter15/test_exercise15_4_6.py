import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.exercise15_4_6 import lmis_length, print_lmis
from datastructures.array import Array
from test_chapter15.test_exercise15_4_5 import get_maximum_lmis_length_bruteforce, is_monotonically_increasing
from test_chapter15.test_textbook15_4 import is_subsequence_of


class TestExercise15_4_6(TestCase):

    def test_lis_length_(self):
        sequence = get_random_array(max_value=10)
        captured_output = io.StringIO()

        actual_maximum_length, terms, last_term = lmis_length(sequence)
        with redirect_stdout(captured_output):
            print_lmis(terms, sequence, last_term)

        assert_that(sequence.is_modified(), is_(False))
        expected_maximum_length = get_maximum_lmis_length_bruteforce(sequence)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))
        actual_lis = Array(int(x) for x in captured_output.getvalue().splitlines())
        assert_that(actual_lis.length, is_(equal_to(expected_maximum_length)))
        assert_that(is_subsequence_of(actual_lis, sequence))
        assert_that(is_monotonically_increasing(actual_lis))
