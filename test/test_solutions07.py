import random
from unittest import TestCase

from hamcrest import *

from chapter07.pr7_1 import hoare_quicksort
from chapter07.pr7_4 import quicksort__
from chapter07.pr7_6 import fuzzy_sort
from datastructures.array import Array
from datastructures.interval import Interval
from test_datastructures.array_util import random_int_array


class Solutions07Test(TestCase):

    def test_hoare_quicksort(self):
        array, data = random_int_array()

        hoare_quicksort(array, 1, array.length)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_quicksort__(self):
        array, data = random_int_array()

        quicksort__(array, 1, array.length)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_fuzzy_sort(self):
        n = random.randint(1, 20)
        endpoints_list = [sorted([random.randint(0, 20), random.randint(0, 20)]) for _ in range(n)]
        data = [Interval(*endpoints) for endpoints in endpoints_list]
        array = Array(data)

        fuzzy_sort(array, 1, array.length)

        for i in range(2, n + 1):
            if array[i].low < array[i - 1].low:
                assert_that(array[i].high, is_(greater_than_or_equal_to(array[i - 1].low)))
