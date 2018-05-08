import random
from unittest import TestCase

from hamcrest import *

from chapter08.textbook8_4 import bucket_sort
from datastructures.array import Array


class TestTextbook8_4(TestCase):

    def test_bucket_sort(self):
        n = random.randint(1, 20)
        elements = [random.random() for _ in range(n)]
        array = Array(elements)

        bucket_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
