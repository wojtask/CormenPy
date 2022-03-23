import random
from unittest import TestCase

from hamcrest import *

from chapter15.exercise15_4_4 import lcs_length_, lcs_length__
from datastructures.array import Array
from test_chapter15.test_textbook15_4 import get_maximum_lcs_length_bruteforce
from util import between


class TestExercise15_4_4(TestCase):

    def test_lcs_length_(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in between(1, random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in between(1, random.randint(1, 10))))

        actual_maximum_length = lcs_length_(sequence1, sequence2)

        assert_that(sequence1.is_modified(), is_(False))
        assert_that(sequence2.is_modified(), is_(False))
        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))

    def test_lcs_length__(self):
        sequence1 = Array(''.join(random.choice('ABCD') for _ in between(1, random.randint(1, 10))))
        sequence2 = Array(''.join(random.choice('ABCD') for _ in between(1, random.randint(1, 10))))

        actual_maximum_length = lcs_length__(sequence1, sequence2)

        assert_that(sequence1.is_modified(), is_(False))
        assert_that(sequence2.is_modified(), is_(False))
        expected_maximum_length = get_maximum_lcs_length_bruteforce(sequence1, sequence2)
        assert_that(actual_maximum_length, is_(equal_to(expected_maximum_length)))
