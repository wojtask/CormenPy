from unittest import TestCase

from chapter05.ex5_1_2 import random


class Ex5_1_2Test(TestCase):
    def test_random_correct_values(self):
        x = random(10, 100)
        self.assertTrue(10 <= x <= 100)
