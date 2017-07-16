from unittest import TestCase

from chapter07.pr7_4 import quicksort__
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Problem7_4Test(TestCase):
    def test_quicksort__(self):
        array, data = random_int_array()
        quicksort__(array, 1, array.length)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
