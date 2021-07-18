from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_1_1 import direct_address_maximum
from datastructures.array import Array
from hash_table_util import get_random_direct_address_table


class TestExercise11_1_1(TestCase):

    def test_direct_address_maximum(self):
        table = get_random_direct_address_table()

        actual_maximum = direct_address_maximum(table)

        elements = Array(element for element in table if element)
        if elements:
            expected_maximum = max(element.key for element in elements)
            assert_that(actual_maximum.key, is_(equal_to(expected_maximum)))
        else:
            assert_that(actual_maximum, is_(none()))
