from unittest import TestCase

from hamcrest import *

from chapter05.textbook import permute_by_sorting, randomize_in_place
from test_datastructures.array_util import random_int_array


class Textbook05Test(TestCase):

    def test_permute_by_sorting(self):
        array, data = random_int_array()

        array = permute_by_sorting(array)

        assert_that(array.data, contains_inanyorder(*data))

    def test_randomize_in_place(self):
        array, data = random_int_array()

        randomize_in_place(array)

        assert_that(array.data, contains_inanyorder(*data))
