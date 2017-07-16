import random
from unittest import TestCase

from chapter04.pr4_2 import missing_integer
from datastructures.array import Array


class Problem4_2Test(TestCase):
    def test_missing_integer(self):
        n = random.randint(1, 20)
        data = random.sample(range(n), n - 1)
        array = Array(data)
        missing = missing_integer(array)
        self.assertEqual(missing, [x for x in range(n) if x not in data][0])
