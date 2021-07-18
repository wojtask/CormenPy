import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.problem8_5 import average_sort
from util import between


def assert_average_sorted(array, k):
    for i in between(1, array.length - k):
        assert_that(array[i], is_(less_than_or_equal_to(array[i + k])))


class TestProblem8_5(TestCase):

    def test_average_sort(self):
        array = get_random_array(min_size=2)
        original = copy.deepcopy(array)
        k = random.randint(1, array.length - 1)

        average_sort(array, k, 1, array.length)

        assert_average_sorted(array, k)
        assert_that(array, contains_inanyorder(*original))
