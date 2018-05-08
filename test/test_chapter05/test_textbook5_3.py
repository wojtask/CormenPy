from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter05.textbook5_3 import permute_by_sorting, randomize_in_place


class TestTextbook5_3(TestCase):

    def test_permute_by_sorting(self):
        array, elements = get_random_array()

        array = permute_by_sorting(array)

        assert_that(array.elements, contains_inanyorder(*elements))

    def test_randomize_in_place(self):
        array, elements = get_random_array()

        randomize_in_place(array)

        assert_that(array.elements, contains_inanyorder(*elements))
