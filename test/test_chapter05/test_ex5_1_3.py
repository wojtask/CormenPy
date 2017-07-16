from unittest import TestCase

from chapter05.ex5_1_3 import unbiased_random


class Ex5_1_3Test(TestCase):
    def test_unbiased_random(self):
        count = [0, 0]
        for i in range(1000):
            x = unbiased_random()
            self.assertIn(x, [0, 1])
            count[x] += 1
        self.assertTrue(abs(count[0] - count[1]) <= 100)
