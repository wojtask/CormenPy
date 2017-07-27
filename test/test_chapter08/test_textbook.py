import random
from unittest import TestCase

from hamcrest import *

from chapter08.textbook import counting_sort, unstable_counting_sort, radix_sort, bucket_sort
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Textbook08Test(TestCase):

    def test_counting_sort(self):
        k = 20
        array, data = random_int_array(max_value=k)
        actual_sorted_array = Array.of_length(array.length)

        counting_sort(array, actual_sorted_array, k)

        expected_array = Array(sorted(data))
        assert_that(actual_sorted_array, is_(equal_to(expected_array)))

    def test_unstable_counting_sort(self):
        k = 20
        array, data = random_int_array(max_value=k)
        actual_sorted_array = Array.of_length(array.length)

        unstable_counting_sort(array, actual_sorted_array, k)

        expected_array = Array(sorted(data))
        assert_that(actual_sorted_array, is_(equal_to(expected_array)))

    def test_radix_sort(self):
        d = 5
        array, data = random_int_array(max_value=10 ** d - 1)

        radix_sort(array, d)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_bucket_sort(self):
        n = random.randint(1, 20)
        data = [random.random() for _ in range(n)]
        array = Array(data)

        bucket_sort(array)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))
