import unittest

from chapter08.pr8_4 import jugs_group, jugs_match, jugs_partition
from datastructures.array import Array
from util import between


class Problem8_4Test(unittest.TestCase):
    def test_jugs_group(self):
        red_jugs = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        blue_jugs = [6, 5, 9, 7, 3, 8, 2, 6, 8, 6, 7, 1]
        red = Array(red_jugs)
        blue = Array(blue_jugs)
        jugs_group(red, blue)
        sorted_expected_reds = Array(sorted(red_jugs))
        sorted_actual_reds = Array(sorted(red.data))
        self.assertEqual(sorted_expected_reds, sorted_actual_reds)
        self.assertEqual(red, blue)

    def test_jugs_match(self):
        red_jugs = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        blue_jugs = [6, 5, 9, 7, 3, 8, 2, 6, 8, 6, 7, 1]
        red = Array(red_jugs)
        blue = Array(blue_jugs)
        jugs_match(red, blue, 1, red.length)
        sorted_expected_reds = Array(sorted(red_jugs))
        sorted_actual_reds = Array(sorted(red.data))
        self.assertEqual(sorted_expected_reds, sorted_actual_reds)
        self.assertEqual(red, blue)

    def test_jugs_partition(self):
        red_jugs = [5, 7, 9, 2, 6, 8, 6, 6, 3, 1, 7, 8]
        blue_jugs = [6, 5, 9, 7, 3, 8, 2, 6, 8, 6, 7, 1]
        red = Array(red_jugs)
        blue = Array(blue_jugs)
        pivot = jugs_partition(red, blue, 1, red.length)
        sorted_expected_reds = Array(sorted(red_jugs))
        sorted_actual_reds = Array(sorted(red.data))
        self.assertEqual(sorted_expected_reds, sorted_actual_reds)
        for i in between(1, pivot - 1):
            self.assertTrue(red[i] <= red[pivot])
            self.assertTrue(blue[i] <= blue[pivot])
        for i in between(pivot + 1, red.length):
            self.assertTrue(red[i] >= red[pivot])
            self.assertTrue(blue[i] >= blue[pivot])
