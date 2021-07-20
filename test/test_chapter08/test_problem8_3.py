import copy
import random
import string
from unittest import TestCase

from hamcrest import *

from chapter08.problem8_3 import integers_sort, strings_sort
from datastructures.array import Array
from util import between


def generate_random_integers(size):
    for _ in between(1, size):
        sign = random.choice([-1, +1])
        exponent = random.randint(1, 20)
        yield sign * random.randint(10 ** (exponent - 1), 10 ** exponent - 1)


def generate_random_strings(size):
    for _ in between(1, size):
        string_length = random.randint(0, 10)
        yield ''.join(random.choice(string.ascii_lowercase) for _ in between(1, string_length))


class TestProblem8_3(TestCase):

    def test_integers_sort(self):
        size = random.randint(1, 20)
        array = Array(generate_random_integers(size))
        original = copy.deepcopy(array)

        integers_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))

    def test_strings_sort(self):
        size = random.randint(1, 50)
        array = Array(generate_random_strings(size))

        original = copy.deepcopy(array)

        strings_sort(array)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
