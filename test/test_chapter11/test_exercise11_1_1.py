from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_1_1 import direct_address_maximum
from datastructures.array import Array
from hash_table_util import get_random_direct_address_table


class TestExercise11_1_1(TestCase):

    def test_direct_address_maximum(self):
        table = get_random_direct_address_table()

        actual_maximum = direct_address_maximum(table)

        keys = Array(element.key for element in table if element is not None)
        if keys:
            expected_maximum = max(keys)
            assert_that(actual_maximum.key, is_(equal_to(expected_maximum)))
        else:
            assert_that(actual_maximum, is_(none()))
        assert_that(table.is_modified(), is_(False))
