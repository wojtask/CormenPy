from unittest import TestCase

from chapter09.ex9_3_7 import median_neighbors
from datastructures.array import Array


class Ex9_3_7Test(TestCase):
    def test_median_neighbors_1st_order(self):
        data = [5, 0, 15, 17, 4, 2, 6, 16, 3, 1]
        array = Array(data)
        neighbors = median_neighbors(array, 1)
        self.assertEqual({4}, neighbors)

    def test_median_neighbors_4th_order(self):
        data = [5, 0, 15, 17, 4, 2, 6, 16, 3, 1]
        array = Array(data)
        neighbors = median_neighbors(array, 4)
        self.assertTrue(neighbors == {2, 3, 4, 5} or neighbors == {3, 4, 5, 6})
