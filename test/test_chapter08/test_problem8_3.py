import random
import string
from unittest import TestCase

from hamcrest import *

from chapter08.problem8_3 import integers_sort, strings_sort
from datastructures.array import Array


class TestProblem8_3(TestCase):

    def test_integers_sort(self):
        size = random.randint(1, 20)
        elements = []
        for _ in range(size):
            sign = random.choice([-1, +1])
            exponent = random.randint(1, 20)
            elements.append(sign * random.randint(10 ** (exponent - 1), 10 ** exponent - 1))
        array = Array(elements)

        integers_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))

    def test_strings_sort(self):
        size = random.randint(1, 50)
        elements = []
        for _ in range(size):
            string_length = random.randint(0, 10)
            elements.append(''.join(random.choice(string.ascii_lowercase) for _ in range(string_length)))
        array = Array(elements)

        strings_sort(array)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
