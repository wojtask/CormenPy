import copy
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.textbook_exercise2_3_4 import recursive_insertion_sort


class TestTextbookExercise2_3_4(TestCase):

    def test_recursive_insertion_sort(self):
        array = get_random_array()
        original = copy.deepcopy(array)

        recursive_insertion_sort(array, array.length)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
