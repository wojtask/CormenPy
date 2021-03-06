import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_unique_array
from chapter11.exercise11_2_4 import in_place_chained_hash_insert, in_place_chained_hash_search, \
    in_place_chained_hash_delete
from datastructures.array import Array
from datastructures.hash_table import FreePosition
from util import Element


def assert_in_place_hash_table_clear(table):
    i = table.free
    assert_that(table[i].prev, is_(equal_to(-1)))
    free_positions = 0
    while i != -1:
        assert_that(table[i], not_(has_property('element')))
        free_positions += 1
        if table[i].next != -1:
            assert_that(table[table[i].next].prev, is_(equal_to(i)))
        i = table[i].next
    assert_that(free_positions, is_(equal_to(table.length)))


class TestExercise11_2_4(TestCase):

    def test_in_place_chained_hash_table(self):
        table_size = random.randint(1, 20)
        keys, _ = get_random_unique_array(max_size=table_size, max_value=99)
        elements = [Element(key) for key in keys]
        table = Array.indexed(0, table_size - 1)
        table.free = 0
        for i in range(table_size):
            table[i] = FreePosition(i - 1, i + 1)
        table[table_size - 1].next = -1
        h = lambda k, m: k % m

        for element in elements:
            in_place_chained_hash_insert(table, element, h)

        for key in range(100):
            actual_element = in_place_chained_hash_search(table, key, h)

            if key in keys:
                assert_that(actual_element.key, is_(equal_to(key)))
                in_place_chained_hash_delete(table, actual_element, h)
            else:
                assert_that(actual_element, is_(none()))

        assert_in_place_hash_table_clear(table)
