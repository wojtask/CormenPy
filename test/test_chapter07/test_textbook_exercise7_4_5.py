import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter07.textbook_exercise7_4_5 import insertion_quicksort


class TestTextbookExercise7_4_5(TestCase):

    def test_insertion_quicksort(self):
        array = get_random_array(min_size=2)
        original = copy.deepcopy(array)
        k = random.randint(1, array.length)

        insertion_quicksort(array, 1, array.length, k)

        expected_array = original.sort()
        assert_that(array, is_(equal_to(expected_array)))
