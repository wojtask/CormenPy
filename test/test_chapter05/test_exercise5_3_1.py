from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter05.exercise5_3_1 import randomize_in_place_


class TestExercise5_3_1(TestCase):

    def test_randomize_in_place_(self):
        array, elements = get_random_array()

        randomize_in_place_(array)

        assert_that(array.elements, contains_inanyorder(*elements))
