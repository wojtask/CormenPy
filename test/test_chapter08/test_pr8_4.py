import random
from unittest import TestCase

from chapter08.pr8_4 import jugs_group, jugs_match
from datastructures.array import Array


class Problem8_4Test(TestCase):
    def test_jugs_group(self):
        n = random.randint(1, 20)
        reds_data = [random.randrange(1000) for _ in range(n)]
        blues_data = random.sample(reds_data, n)
        reds = Array(reds_data)
        blues = Array(blues_data)
        jugs_group(reds, blues)
        sorted_expected_reds = Array(sorted(reds_data))
        sorted_actual_reds = Array(sorted(reds.data))
        self.assertEqual(sorted_actual_reds, sorted_expected_reds)
        self.assertEqual(reds, blues)

    def test_jugs_match(self):
        n = random.randint(1, 20)
        reds_data = [random.randrange(1000) for _ in range(n)]
        blues_data = random.sample(reds_data, n)
        reds = Array(reds_data)
        blues = Array(blues_data)
        jugs_match(reds, blues, 1, n)
        sorted_expected_reds = Array(sorted(reds_data))
        sorted_actual_reds = Array(sorted(reds.data))
        self.assertEqual(sorted_actual_reds, sorted_expected_reds)
        self.assertEqual(reds, blues)
