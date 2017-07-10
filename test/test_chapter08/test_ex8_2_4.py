from unittest import TestCase

from chapter08.ex8_2_4 import counting_in_range
from datastructures.array import Array


class Ex8_2_4Test(TestCase):
    def setUp(self):
        data = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
        self.array = Array(data)

    def test_counting_in_range_entirely_outside_array(self):
        cnt = counting_in_range(self.array, 6, -2, -1)
        self.assertEqual(0, cnt)

    def test_counting_in_range_entirely_inside_array(self):
        cnt = counting_in_range(self.array, 6, 1, 5)
        self.assertEqual(7, cnt)

    def test_counting_in_range_left_outside_array(self):
        cnt = counting_in_range(self.array, 6, -2, 3)
        self.assertEqual(8, cnt)

    def test_counting_in_range_right_outside_array(self):
        cnt = counting_in_range(self.array, 6, 3, 12)
        self.assertEqual(5, cnt)

    def test_counting_in_range_surrounding_array(self):
        cnt = counting_in_range(self.array, 6, -4, 16)
        self.assertEqual(11, cnt)
