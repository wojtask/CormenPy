from unittest import TestCase

from chapter05.ex5_1_2 import random


class Ex5_1_2Test(TestCase):
    def test_random(self):
        x = random(10, 20)
        self.assertTrue(10 <= x <= 20)
