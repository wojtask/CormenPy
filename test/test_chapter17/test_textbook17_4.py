import random
from unittest import TestCase

from hamcrest import *

from chapter17.textbook17_4 import table_insert, table_delete
from datastructures.dynamic_table import DynamicTable


class TestTextbook17_4(TestCase):

    def test_table_insert(self):
        nelements = 20
        elements = [random.randint(0, 999) for _ in range(nelements)]
        T = DynamicTable()

        for i in range(nelements):
            table_insert(T, elements[i])

            assert_that(T.num, is_(equal_to(i + 1)))
            assert_that(T.num, is_(greater_than(T.size // 2)))
            assert_that(T.num, is_(less_than_or_equal_to(T.size)))

        actual_elements = T.table[:nelements]
        assert_that(actual_elements, is_(equal_to(elements)))

    def test_table_delete(self):
        T = DynamicTable()
        nelements = T.num = 20
        T.table = [random.randint(0, 999) for _ in range(nelements)] + [None] * (32 - nelements)
        T.size = 32

        for i in range(nelements):
            index = random.randint(0, T.num - 1)
            table_delete(T, T.table[index])

            assert_that(T.num, is_(equal_to(nelements - 1 - i)))
            assert_that(T.num, is_(greater_than_or_equal_to(T.size // 4)))
            assert_that(T.num, is_(less_than_or_equal_to(T.size)))
