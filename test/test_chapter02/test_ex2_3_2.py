import random
from unittest import TestCase

from chapter02.ex2_3_2 import merge_
from datastructures.array import Array


class Ex2_3_2Test(TestCase):
    def test_merge_(self):
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        data1 = sorted([random.randrange(1000) for _ in range(n1)])
        data2 = sorted([random.randrange(1000) for _ in range(n2)])
        array = Array(data1 + data2)
        merge_(array, 1, n1, n1 + n2)
        expected_array = Array(sorted(data1 + data2))
        self.assertEqual(array, expected_array)
