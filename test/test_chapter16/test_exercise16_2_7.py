import itertools
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.exercise16_2_7 import sets_reordering
from datastructures.array import Array
from util import between


def get_score(bases, exponents):
    score = 1
    n = bases.length
    for i in between(1, n):
        score *= bases[i] ** exponents[i]
    return score


def sets_reordering_bruteforce(bases, exponents):
    max_score = 1
    for exponents_reordering in itertools.permutations(exponents):
        max_score = max(max_score, get_score(bases, Array(exponents_reordering)))
    return max_score


class TestExercise16_2_7(TestCase):

    def test_sets_reordering(self):
        n = random.randint(1, 8)
        bases = get_random_array(size=n, min_value=1, max_value=10)
        exponents = get_random_array(size=n, min_value=1, max_value=10)

        sets_reordering(bases, exponents)

        actual_score = get_score(bases, exponents)
        expected_score = sets_reordering_bruteforce(bases, exponents)
        assert_that(actual_score, is_(equal_to(expected_score)))
