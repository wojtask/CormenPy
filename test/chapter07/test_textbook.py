import unittest

from chapter07.textbook import *
from datastructures.array import Array


class QuicksortTest(unittest.TestCase):
    def setUp(self):
        self.data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        self.array = Array(self.data)

    def test_partition(self):
        pivot = partition(self.array, 1, self.array.length)
        self.assertEqual(11, pivot)
        self.assertEqual([5, 7, 2, 6, 8, 6, 6, 3, 1, 7, 8, 9], self.array.data)

    def test_quicksort(self):
        quicksort(self.array, 1, self.array.length)
        self.assertEqual(sorted(self.data), self.array.data)

    def test_randomized_partition(self):
        pivot = randomized_partition(self.array, 1, self.array.length)
        for i in scope(1, pivot):
            self.assertTrue(self.array[i] <= self.array[pivot])
        for i in scope(pivot + 1, self.array.length):
            self.assertTrue(self.array[i] >= self.array[pivot])

    def test_randomized_quicksort(self):
        randomized_quicksort(self.array, 1, self.array.length)
        self.assertEqual(sorted(self.data), self.array.data)

    def test_insertion_quicksort_test(self):
        insertion_quicksort(self.array, 1, self.array.length, 3)
        self.assertEqual(sorted(self.data), self.array.data)

    def test_hoare_partition(self):
        pivot = hoare_partition(self.array, 1, self.array.length)
        self.assertEqual(3, pivot)
        self.assertEqual([1, 3, 2, 9, 6, 8, 6, 6, 7, 5, 7, 8], self.array.data)

    def test_stooge_sort(self):
        stooge_sort(self.array, 1, self.array.length)
        self.assertEqual(sorted(self.data), self.array.data)

    def test_quicksort_(self):
        quicksort_(self.array, 1, self.array.length)
        self.assertEqual(sorted(self.data), self.array.data)

    def test_median_of_3_partition(self):
        pivot = median_of_3_partition(self.array, 1, self.array.length)
        for i in scope(1, pivot):
            self.assertTrue(self.array[i] <= self.array[pivot])
        for i in scope(pivot + 1, self.array.length):
            self.assertTrue(self.array[i] >= self.array[pivot])
