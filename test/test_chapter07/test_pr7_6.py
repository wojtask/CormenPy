from unittest import TestCase

from chapter07.pr7_6 import fuzzy_sort, fuzzy_partition
from datastructures.array import Array

from util import between


class Interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Problem7_6Test(TestCase):
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
        for i in between(2, self.array.length):
            if self.array[i].a < self.array[i - 1].a:
                self.assertTrue(self.array[i].b >= self.array[i - 1].a)

    def test_fuzzy_partition(self):
        pivot1, pivot2 = fuzzy_partition(self.array, 1, self.array.length)
        for mid in between(pivot1, pivot2):
            for left in between(1, pivot1 - 1):
                self.assertTrue(self.array[left].b < self.array[mid].b)
            for right in between(pivot2 + 1, self.array.length):
                self.assertTrue(self.array[right].a > self.array[mid].a)
