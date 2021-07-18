import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_3_5 import recursive_binary_search, iterative_binary_search


class TestExercise2_3_5(TestCase):

    def test_recursive_binary_search(self):
        n = random.randint(1, 20)
        array = get_random_array(size=n, max_value=20).sort()
        original = copy.deepcopy(array)
        v = random.randint(0, 20)

        actual_index = recursive_binary_search(array, v, 1, n)

        if actual_index:
            assert_that(array[actual_index], is_(equal_to(v)))
        else:
            assert_that(v not in array)
        assert_that(array, is_(equal_to(original)))

    def test_iterative_binary_search(self):
        n = random.randint(1, 20)
        array = get_random_array(size=n, max_value=20).sort()
        original = copy.deepcopy(array)
        v = random.randint(0, 20)

        actual_index = iterative_binary_search(array, v)

        if actual_index:
            assert_that(array[actual_index], is_(equal_to(v)))
        else:
            assert_that(v not in array)
        assert_that(array, is_(equal_to(original)))
