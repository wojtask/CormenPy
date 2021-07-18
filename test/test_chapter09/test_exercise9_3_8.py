import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.exercise9_3_8 import two_arrays_median


class TestExercise9_3_8(TestCase):

    def test_two_arrays_median(self):
        n = random.randint(1, 20)
        array1 = get_random_array(size=n).sort()
        original1 = copy.deepcopy(array1)
        array2 = get_random_array(size=n).sort()
        original2 = copy.deepcopy(array2)

        actual_median = two_arrays_median(array1, 1, n, array2, 1, n)

        expected_median = (original1 + original2).sort()[n]
        assert_that(actual_median, is_(equal_to(expected_median)))
        assert_that(array1, is_(equal_to(original1)))
        assert_that(array2, is_(equal_to(original2)))
