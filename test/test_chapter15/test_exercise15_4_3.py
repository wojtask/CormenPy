import random
from unittest import TestCase

from hamcrest import *

from chapter15.exercise15_4_3 import memoized_lcs_length
from datastructures.array import Array
from test_chapter15.test_textbook15_4 import get_maximum_lcs_length_bruteforce


class TestExercise15_4_3(TestCase):

    def test_memoized_lcs_length(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in range(random.randint(1, 10))))

        actual_maximum_length = memoized_lcs_length(sequence1, sequence2)

        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))
