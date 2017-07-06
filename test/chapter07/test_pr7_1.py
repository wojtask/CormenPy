import unittest

from chapter07.pr7_1 import hoare_quicksort
from datastructures.array import Array


class HoareQuicksortTest(unittest.TestCase):
    def test_hoare_quicksort(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        hoare_quicksort(array, 1, array.length)
        self.assertEqual(sorted(data), array.data)
