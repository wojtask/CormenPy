from unittest import TestCase

from chapter02.textbook import *
from datastructures.array import Array
from datastructures.standard_array import StandardArray


class Chapter02Test(TestCase):
    def test_insertion_sort_singleton(self):
        array = Array([3])
        insertion_sort(array)
        expected_array = Array([3])
        self.assertEqual(expected_array, array)

    def test_insertion_sort_array(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        insertion_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(expected_array, array)

    def test_merge(self):
        array = Array([3, 5, 6, 8, 8, 9] + [1, 2, 6, 6, 7, 7])
        merge(array, 1, array.length // 2, array.length)
        expected_array = Array([1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9])
        self.assertEqual(expected_array, array)

    def test_merge_sort_singleton(self):
        array = Array([3])
        merge_sort(array, 1, array.length)
        expected_array = Array([3])
        self.assertEqual(expected_array, array)

    def test_merge_sort_array(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        merge_sort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(expected_array, array)

    def test_bubble_sort_singleton(self):
        array = Array([3])
        bubble_sort(array)
        expected_array = Array([3])
        self.assertEqual(expected_array, array)

    def test_bubble_sort_array(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        bubble_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(expected_array, array)

    def test_evaluate_polynomial_horner(self):
        coefficients = StandardArray([-1.5, 3.2, 1.6, 3.4, -5.0, 0.0, -1.0, 1.0])
        x = -2.0
        result = horner(coefficients, x)
        self.assertAlmostEqual(-300.7, result)
