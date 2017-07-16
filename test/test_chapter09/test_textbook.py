import random
from unittest import TestCase

from chapter09.textbook import minimum, minimum_maximum, randomized_select, select
from test.test_datastructures.array_util import random_int_array


class Chapter09Test(TestCase):
    def test_minimum(self):
        array, data = random_int_array()
        actual_min = minimum(array)
        self.assertEqual(actual_min, min(data))

    def test_minimum_maximum(self):
        array, data = random_int_array()
        actual_min, actual_max = minimum_maximum(array)
        self.assertEqual(actual_min, min(data))
        self.assertEqual(actual_max, max(data))

    def test_randomized_select(self):
        array, data = random_int_array()
        k = random.randint(1, array.length)
        x = randomized_select(array, 1, array.length, k)
        self.assertEqual(x, sorted(data)[k - 1])

    def test_select(self):
        array, data = random_int_array()
        k = random.randint(1, array.length)
        x = select(array, 1, array.length, k)
        self.assertEqual(x, sorted(data)[k - 1])
