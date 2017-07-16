import random
from unittest import TestCase

from chapter09.ex9_3_8 import two_arrays_median
from datastructures.array import Array


class Ex9_3_8Test(TestCase):
    def test_two_arrays_median(self):
        n = random.randint(1, 20)
        data1 = sorted([random.randrange(1000) for _ in range(n)])
        data2 = sorted([random.randrange(1000) for _ in range(n)])
        array1 = Array(data1)
        array2 = Array(data2)
        actual_median = two_arrays_median(array1, 1, n, array2, 1, n)
        self.assertEqual(actual_median, sorted(data1 + data2)[n - 1])
