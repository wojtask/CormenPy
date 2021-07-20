import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter11.textbook11_2 import chained_hash_insert, chained_hash_search, chained_hash_delete
from datastructures.array import Array
from datastructures.hash_table import ChainedElement
from hash_table_util import get_random_chained_hash_table, get_chained_hash_table_elements


class TestTextbook11_2(TestCase):

    def test_chained_hash_insert(self):
        table, h = get_random_chained_hash_table()
        original = copy.deepcopy(table)
        new_key = random.randint(0, 999)
        new_element = ChainedElement(new_key)

        chained_hash_insert(table, new_element, h)

        actual_elements = get_chained_hash_table_elements(table)
        original_elements = get_chained_hash_table_elements(original)
        assert_that(actual_elements, contains_inanyorder(*original_elements, new_element))

    def test_chained_hash_search(self):
        table, h = get_random_chained_hash_table(max_value=10)
        original = copy.deepcopy(table)
        key_to_find = random.randint(0, 10)

        actual_found = chained_hash_search(table, key_to_find, h)

        actual_elements = get_chained_hash_table_elements(table)
        original_elements = get_chained_hash_table_elements(original)
        if key_to_find in Array(element.key for element in original_elements):
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))
        assert_that(actual_elements, is_(equal_to(original_elements)))
        assert_that(table, is_(equal_to(original)))

    def test_chained_hash_delete(self):
        table, h = get_random_chained_hash_table()
        actual_elements = get_chained_hash_table_elements(table)
        # make sure the table is not empty
        if not actual_elements:
            key = random.randint(0, 999)
            e = ChainedElement(key)
            table[h(key, table.length)] = e
            actual_elements.append(e)
        element_to_delete = actual_elements[random.randint(1, actual_elements.length)]
        original = copy.deepcopy(table)
        expected_elements = get_chained_hash_table_elements(original)
        expected_elements.remove(element_to_delete)

        chained_hash_delete(table, element_to_delete, h)

        actual_elements = get_chained_hash_table_elements(table)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))
