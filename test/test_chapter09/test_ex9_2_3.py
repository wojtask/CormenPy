import random
from unittest import TestCase

from chapter09.ex9_2_3 import iterative_randomized_select
from test.test_datastructures.array_util import random_int_array


class Ex9_2_3Test(TestCase):
    def test_iterative_randomized_select(self):
        array, data = random_int_array()
        k = random.randint(1, array.length)
        x = iterative_randomized_select(array, 1, array.length, k)
        self.assertEqual(x, sorted(data)[k - 1])
