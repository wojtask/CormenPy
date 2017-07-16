import random
from unittest import TestCase

import numpy

from chapter02.textbook import insertion_sort, merge_sort, bubble_sort, horner
from datastructures.array import Array
from datastructures.standard_array import StandardArray
from test.test_datastructures.array_util import random_int_array


class Chapter02Test(TestCase):
    def test_insertion_sort(self):
        array, data = random_int_array()
        insertion_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_merge_sort(self):
        array, data = random_int_array()
        merge_sort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_bubble_sort(self):
        array, data = random_int_array()
        bubble_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_horner(self):
        n = random.randint(1, 20)
        data = [random.uniform(-2.0, 2.0) for _ in range(n + 1)]
        coefficients = StandardArray(data)
        x = random.uniform(-2.0, 2.0)
        expected_result = numpy.polyval(list(reversed(data)), x)
        actual_result = horner(coefficients, x)
        self.assertAlmostEqual(actual_result, expected_result)
