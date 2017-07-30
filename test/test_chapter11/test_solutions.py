from unittest import TestCase

from hamcrest import *

from chapter11.ex11_1_1 import direct_address_maximum
from hash_table_util import random_direct_address_table


class Solutions11Test(TestCase):

    def test_direct_address_maximum(self):
        table, elements = random_direct_address_table()

        actual_maximum = direct_address_maximum(table)

        if elements:
            expected_maximum = max([element.key for element in elements])
            assert_that(actual_maximum.key, is_(equal_to(expected_maximum)))
        else:
            assert_that(actual_maximum, is_(none()))
