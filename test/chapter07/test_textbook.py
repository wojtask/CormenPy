import unittest

from chapter07.textbook import *
from datastructures.array import Array


class Chapter07Test(unittest.TestCase):
    def setUp(self):
        self.data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        self.array = Array(self.data)

    def test_partition(self):
        pivot = partition(self.array, 1, self.array.length)
        self.assertEqual(11, pivot)
        expected_array = Array([5, 7, 2, 6, 8, 6, 6, 3, 1, 7, 8, 9])
        self.assertEqual(expected_array, self.array)

    def test_quicksort(self):
        quicksort(self.array, 1, self.array.length)
        expected_array = Array(sorted(self.data))
        self.assertEqual(expected_array, self.array)

    def test_randomized_partition(self):
        pivot = randomized_partition(self.array, 1, self.array.length)
        for i in between(1, pivot - 1):
            self.assertTrue(self.array[i] <= self.array[pivot])
        for i in between(pivot + 1, self.array.length):
            self.assertTrue(self.array[i] >= self.array[pivot])

    def test_randomized_quicksort(self):
        randomized_quicksort(self.array, 1, self.array.length)
        expected_array = Array(sorted(self.data))
        self.assertEqual(expected_array, self.array)

    def test_insertion_quicksort_test(self):
        insertion_quicksort(self.array, 1, self.array.length, 3)
        expected_array = Array(sorted(self.data))
        self.assertEqual(expected_array, self.array)

    def test_hoare_partition(self):
        pivot = hoare_partition(self.array, 1, self.array.length)
        self.assertEqual(3, pivot)
        expected_array = Array([1, 3, 2, 9, 6, 8, 6, 6, 7, 5, 7, 8])
        self.assertEqual(expected_array, self.array)

    def test_stooge_sort(self):
        stooge_sort(self.array, 1, self.array.length)
        expected_array = Array(sorted(self.data))
        self.assertEqual(expected_array, self.array)

    def test_quicksort_(self):
        quicksort_(self.array, 1, self.array.length)
        expected_array = Array(sorted(self.data))
        self.assertEqual(expected_array, self.array)

    def test_median_of_3_partition(self):
        pivot = median_of_3_partition(self.array, 1, self.array.length)
        for i in between(1, pivot - 1):
            self.assertTrue(self.array[i] <= self.array[pivot])
        for i in between(pivot + 1, self.array.length):
            self.assertTrue(self.array[i] >= self.array[pivot])
