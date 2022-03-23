import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter09.exercise9_3_8 import two_arrays_median


class TestExercise9_3_8(TestCase):

    def test_two_arrays_median(self):
        n = random.randint(1, 20)
        array1 = get_random_array(size=n).sort().save_state()
        array2 = get_random_array(size=n).sort().save_state()

        actual_median = two_arrays_median(array1, 1, n, array2, 1, n)

        assert_that(array1.is_modified(), is_(False))
        assert_that(array2.is_modified(), is_(False))
        expected_median = (array1 + array2).sort()[n]
        assert_that(actual_median, is_(equal_to(expected_median)))
