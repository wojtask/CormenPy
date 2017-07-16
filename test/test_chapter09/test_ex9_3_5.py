import random
from unittest import TestCase

from chapter09.ex9_3_5 import randomized_blackbox_select
from test.test_datastructures.array_util import random_int_array


class Ex9_3_5Test(TestCase):
    def test_randomized_blackbox_select(self):
        array, data = random_int_array()
        k = random.randint(1, array.length)
        x = randomized_blackbox_select(array, 1, array.length, k)
        self.assertEqual(x, sorted(data)[k - 1])
