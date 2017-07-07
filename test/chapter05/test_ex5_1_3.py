import unittest

from chapter05.ex5_1_3 import unbiased_random


class Ex5_1_3Test(unittest.TestCase):
    def test_unbiased_random_correct_values(self):
        x = unbiased_random()
        self.assertTrue(x in [0, 1])

    def test_unbiased_random(self):
        zeros, ones = 0, 0
        for i in range(1000):
            x = unbiased_random()
            if x == 0:
                zeros += 1
            else:
                ones += 1
        self.assertTrue(abs(zeros - ones) <= 100)
