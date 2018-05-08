import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook_exercise7_4_5 import insertion_quicksort
from datastructures.array import Array


class TestTextbookExercise7_4_5(TestCase):

    def test_insertion_quicksort(self):
        array, elements = get_random_array(min_size=2)
        k = random.randint(1, array.length)

        insertion_quicksort(array, 1, array.length, k)

        expected_array = Array(sorted(elements))
        assert_that(array, is_(equal_to(expected_array)))
