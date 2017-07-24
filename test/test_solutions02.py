import random
from unittest import TestCase

import numpy
from hamcrest import *

from chapter02.ex2_1_2 import nonincreasing_insertion_sort
from chapter02.ex2_1_3 import linear_search
from chapter02.ex2_1_4 import binary_add
from chapter02.ex2_2_2 import selection_sort
from chapter02.ex2_3_2 import merge_
from chapter02.ex2_3_5 import recursive_binary_search, iterative_binary_search
from chapter02.ex2_3_7 import sum_search
from chapter02.pr2_3 import polynomial_evaluate
from chapter02.pr2_4 import count_inversions
from datastructures.array import Array
from datastructures.standard_array import StandardArray
from test_datastructures.array_util import random_int_array, random_unique_int_array


def bits_to_number(bits):
    return int(''.join(str(bit) for bit in reversed(bits)), 2)


class Solutions02Test(TestCase):

    def test_nonincreasing_insertion_sort(self):
        array, data = random_int_array()

        nonincreasing_insertion_sort(array)

        expected_array = Array(sorted(data, reverse=True))
        assert_that(array, is_(equal_to(expected_array)))

    def test_linear_search(self):
        array, data = random_int_array(min_size=10, max_size=20, max_value=20)
        v = random.randint(0, 20)

        actual_index = linear_search(array, v)

        try:
            expected_index = data.index(v) + 1
            assert_that(actual_index, is_(equal_to(expected_index)))
        except ValueError:
            assert_that(actual_index, is_(none()))

    def test_binary_add(self):
        n = random.randint(1, 20)
        array1, data1 = random_int_array(min_size=n, max_size=n, max_value=1)
        array2, data2 = random_int_array(min_size=n, max_size=n, max_value=1)

        actual_sum_bits = binary_add(array1, array2)

        actual_sum = bits_to_number(actual_sum_bits.data)
        number1 = bits_to_number(data1)
        number2 = bits_to_number(data2)
        expected_sum = number1 + number2
        assert_that(expected_sum, is_(equal_to(actual_sum)))

    def test_selection_sort(self):
        array, data = random_int_array()

        selection_sort(array)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_merge_(self):
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        data1 = sorted([random.randrange(1000) for _ in range(n1)])
        data2 = sorted([random.randrange(1000) for _ in range(n2)])
        array = Array(data1 + data2)

        merge_(array, 1, n1, n1 + n2)

        expected_array = Array(sorted(data1 + data2))
        assert_that(array, is_(equal_to(expected_array)))

    def test_recursive_binary_search(self):
        n = random.randint(1, 20)
        data = sorted([random.randrange(20) for _ in range(n)])
        array = Array(data)
        v = random.randint(0, 20)

        actual_index = recursive_binary_search(array, v, 1, n)

        expected_indexes = [i + 1 for i, x in enumerate(data) if x == v]
        if expected_indexes:
            assert_that(actual_index, is_in(expected_indexes))
        else:
            assert_that(actual_index, is_(none()))

    def test_iterative_binary_search(self):
        n = random.randint(1, 20)
        data = sorted([random.randrange(20) for _ in range(n)])
        array = Array(data)
        v = random.randint(0, 20)

        actual_index = iterative_binary_search(array, v)

        expected_indexes = [i + 1 for i, x in enumerate(data) if x == v]
        if expected_indexes:
            assert_that(actual_index, is_in(expected_indexes))
        else:
            assert_that(actual_index, is_(none()))

    def test_sum_search(self):
        array, data = random_unique_int_array(max_value=20)
        sum_to_find = random.randint(0, 40)

        actual_found = sum_search(array, sum_to_find)

        all_sums = {x + y for x in data for y in data if y != x}
        expected_found = sum_to_find in all_sums
        assert_that(actual_found, is_(equal_to(expected_found)))

    def test_polynomial_evaluate(self):
        n = random.randint(1, 20)
        data = [random.uniform(-2.0, 2.0) for _ in range(n + 1)]
        coefficients = StandardArray(data)
        x = random.uniform(-2.0, 2.0)

        actual_result = polynomial_evaluate(coefficients, x)

        expected_result = numpy.polyval(list(reversed(data)), x)
        assert_that(actual_result, is_(close_to(expected_result, 1e-7)))

    def test_count_inversions(self):
        array, data = random_int_array()

        actual_inversions = count_inversions(array, 1, array.length)

        expected_inversions = sum(len([y for y in data[i + 1:] if y < x]) for i, x in enumerate(data))
        assert_that(actual_inversions, is_(equal_to(expected_inversions)))
