import unittest

from chapter07.pr7_6 import fuzzy_sort, fuzzy_partition
from datastructures.array import Array

from util import scope


class Interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class FuzzySortTest(unittest.TestCase):
    def setUp(self):
        self.data = [
            Interval(5, 7),
            Interval(2, 9),
            Interval(6, 8),
            Interval(6, 6),
            Interval(1, 3),
            Interval(7, 8)
        ]
        self.array = Array(self.data)

    def test_fuzzy_sort(self):
        fuzzy_sort(self.array, 1, self.array.length)
        for i in scope(2, self.array.length):
            if self.array[i].a < self.array[i - 1].a:
                self.assertTrue(self.array[i].b >= self.array[i - 1].b)

    def test_fuzzy_partition(self):
        pivot1, pivot2 = fuzzy_partition(self.array, 1, self.array.length)
        for mid in scope(pivot1, pivot2):
            for left in scope(1, pivot1 - 1):
                self.assertTrue(self.array[left].b < self.array[mid].b)
            for right in scope(pivot2 + 1, self.array.length):
                self.assertTrue(self.array[right].a > self.array[mid].a)
