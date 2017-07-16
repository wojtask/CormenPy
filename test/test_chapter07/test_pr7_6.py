import random
from unittest import TestCase

from chapter07.pr7_6 import fuzzy_sort
from datastructures.array import Array


class Interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Problem7_6Test(TestCase):
    def test_fuzzy_sort(self):
        n = random.randint(1, 20)
        endpoints_list = [sorted([random.randint(0, 20), random.randint(0, 20)]) for _ in range(n)]
        data = [Interval(endpoints[0], endpoints[1]) for endpoints in endpoints_list]
        array = Array(data)
        fuzzy_sort(array, 1, array.length)
        for i in range(2, n + 1):
            if array[i].a < array[i - 1].a:
                self.assertTrue(array[i].b >= array[i - 1].a)
