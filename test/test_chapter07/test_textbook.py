import random
from unittest import TestCase

from chapter07.textbook import quicksort, randomized_quicksort, insertion_quicksort, stooge_sort, quicksort_, \
    median_of_3_partition
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Chapter07Test(TestCase):
    def test_quicksort(self):
        array, data = random_int_array()
        quicksort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_randomized_quicksort(self):
        array, data = random_int_array()
        randomized_quicksort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_insertion_quicksort(self):
        array, data = random_int_array(min_size=2)
        k = random.randint(1, array.length)
        insertion_quicksort(array, 1, array.length, k)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_stooge_sort(self):
        array, data = random_int_array()
        stooge_sort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_quicksort_(self):
        array, data = random_int_array()
        quicksort_(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_median_of_3_partition(self):
        array, data = random_int_array()
        pivot = median_of_3_partition(array, 1, array.length)
        for x in array[1:pivot]:
            self.assertTrue(x <= array[pivot])
        for x in array[pivot + 1:array.length]:
            self.assertTrue(x >= array[pivot])
