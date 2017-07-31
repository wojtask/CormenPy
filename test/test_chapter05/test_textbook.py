from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter05.textbook import permute_by_sorting, randomize_in_place


class Textbook05Test(TestCase):

    def test_permute_by_sorting(self):
        array, data = get_random_array()

        array = permute_by_sorting(array)

        assert_that(array.data, contains_inanyorder(*data))

    def test_randomize_in_place(self):
        array, data = get_random_array()

        randomize_in_place(array)

        assert_that(array.data, contains_inanyorder(*data))
