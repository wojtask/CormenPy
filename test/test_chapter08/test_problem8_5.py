import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.problem8_5 import average_sort


def assert_average_sorted(elements, k):
    for i in range(len(elements) - k):
        assert_that(elements[i], is_(less_than_or_equal_to(elements[i + k])))


class TestProblem8_5(TestCase):

    def test_average_sort(self):
        array, elements = get_random_array(min_size=2)
        k = random.randint(1, array.length - 1)

        average_sort(array, k, 1, array.length)

        assert_that(array.elements, contains_inanyorder(*elements))
        assert_average_sorted(array.elements, k)
