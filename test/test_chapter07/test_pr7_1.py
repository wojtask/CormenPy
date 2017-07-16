from unittest import TestCase

from chapter07.pr7_1 import hoare_quicksort
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Problem7_1Test(TestCase):
    def test_hoare_quicksort(self):
        array, data = random_int_array()
        hoare_quicksort(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
