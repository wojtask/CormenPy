from unittest import TestCase

from chapter02.ex2_2_2 import selection_sort
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array


class Ex2_2_2Test(TestCase):
    def test_selection_sort(self):
        array, data = random_int_array()
        selection_sort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)
