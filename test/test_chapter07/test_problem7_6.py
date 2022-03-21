import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter07.problem7_6 import fuzzy_sort
from datastructures.array import Array
from datastructures.essential import Interval
from util import between


class TestProblem7_6(TestCase):

    def test_fuzzy_sort(self):
        n = random.randint(1, 20)
        endpoints_list = Array((random.randint(0, 20), random.randint(0, 20)) for _ in between(1, n))
        array = Array(Interval(min(endpoints), max(endpoints)) for endpoints in endpoints_list)
        original = copy.deepcopy(array)

        fuzzy_sort(array, 1, array.length)

        for i in between(2, n):
            if array[i].low < array[i - 1].low:
                assert_that(array[i].high, is_(greater_than_or_equal_to(array[i - 1].low)))
        assert_that(array, contains_inanyorder(*original))
