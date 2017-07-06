import unittest

from chapter08.textbook import *
from datastructures.array import Array


class CountingSortTest(unittest.TestCase):
    def test_counting_sort(self):
        data = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
        array = Array(data)
        sorted_array = Array.of_length(array.length)
        counting_sort(array, sorted_array, 6)
        self.assertEqual(sorted(data), sorted_array.data)

    def test_unstable_counting_sort(self):
        data = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
        array = Array(data)
        sorted_array = Array.of_length(array.length)
        unstable_counting_sort(array, sorted_array, 6)
        self.assertEqual(sorted(data), sorted_array.data)

    def test_radix_sort(self):
        data = [24015, 44036, 14014, 62027, 55033, 19012, 63032]
        array = Array(data)
        radix_sort(array, 5)
        self.assertEqual(sorted(data), array.data)

    def test_bucket_sort(self):
        data = [.15, .92, .56, .25, .66, .23, .9, .2, .45, .7, .39,
                .99, .3, .01, .33, .91, .65, .33, .21, .67, .16, .22]
        array = Array(data)
        bucket_sort(array)
        self.assertEqual(sorted(data), array.data)
