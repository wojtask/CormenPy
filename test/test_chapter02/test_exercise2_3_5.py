import random
from unittest import TestCase

from hamcrest import *

from chapter02.exercise2_3_5 import recursive_binary_search, iterative_binary_search
from datastructures.array import Array


class TestExercise2_3_5(TestCase):

    def test_recursive_binary_search(self):
        n = random.randint(1, 20)
        elements = sorted([random.randrange(20) for _ in range(n)])
        array = Array(elements)
        v = random.randint(0, 20)

        actual_index = recursive_binary_search(array, v, 1, n)

        expected_indexes = [i + 1 for i, x in enumerate(elements) if x == v]
        if expected_indexes:
            assert_that(actual_index, is_in(expected_indexes))
        else:
            assert_that(actual_index, is_(none()))

    def test_iterative_binary_search(self):
        n = random.randint(1, 20)
        elements = sorted([random.randrange(20) for _ in range(n)])
        array = Array(elements)
        v = random.randint(0, 20)

        actual_index = iterative_binary_search(array, v)

        expected_indexes = [i + 1 for i, x in enumerate(elements) if x == v]
        if expected_indexes:
            assert_that(actual_index, is_in(expected_indexes))
        else:
            assert_that(actual_index, is_(none()))
