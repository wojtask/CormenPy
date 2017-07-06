import unittest

from chapter07.pr7_4 import quicksort__
from datastructures.array import Array


class Quicksort__Test(unittest.TestCase):
    def test_quicksort__(self):
        data = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        array = Array(data)
        quicksort__(array, 1, array.length)
        self.assertEqual(sorted(data), array.data)
