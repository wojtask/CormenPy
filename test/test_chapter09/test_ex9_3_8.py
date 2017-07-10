from unittest import TestCase

from chapter09.ex9_3_8 import two_arrays_median
from datastructures.array import Array


class Ex9_3_8Test(TestCase):
    def test_two_arrays_median(self):
        data1 = [1, 2, 3, 5, 6, 6, 6, 7, 7, 8, 8, 9]
        data2 = [1, 1, 5, 6, 7, 8, 8, 8, 9, 9, 9, 9]
        array1 = Array(data1)
        array2 = Array(data2)
        median = two_arrays_median(array1, 1, array1.length, array2, 1, array2.length)
        self.assertEqual(7, median)
