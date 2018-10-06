import random
from unittest import TestCase

from hamcrest import *

from chapter17.textbook17_4 import table_insert
from datastructures.dynamic_table import DynamicTable


class TestTextbook17_4(TestCase):

    def test_table_insert(self):
        size = 20
        elements = [random.randint(0, 999) for _ in range(size)]
        T = DynamicTable()

        for i in range(size):
            table_insert(T, elements[i])

            assert_that(T.num, is_(equal_to(i + 1)))
            assert_that(T.num, is_(less_than_or_equal_to(T.size)))
            assert_that(T.num, is_(greater_than(T.size // 2)))

        actual_elements = T.table[:size]
        assert_that(actual_elements, is_(equal_to(elements)))
