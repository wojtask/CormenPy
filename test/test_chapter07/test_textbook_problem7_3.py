import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook_problem7_3 import stooge_sort


class TestTextbookProblem7_3(TestCase):

    def test_stooge_sort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        stooge_sort(array, 1, array.length)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
