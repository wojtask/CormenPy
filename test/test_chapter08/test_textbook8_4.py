import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter08.textbook8_4 import bucket_sort
from datastructures.array import Array
from util import between


class TestTextbook8_4(TestCase):

    def test_bucket_sort(self):
        n = random.randint(1, 20)
        array = Array(random.uniform(0, 1) for _ in between(1, n))
        original = copy.deepcopy(array)

        bucket_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
