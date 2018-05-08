import random
from unittest import TestCase

from hamcrest import *

from chapter11.textbook11_2 import chained_hash_insert, chained_hash_search, chained_hash_delete
from datastructures.hash_table import ChainedElement
from hash_table_util import get_random_chained_hash_table, get_chained_hash_table_elements


class TestTextbook11_2(TestCase):

    def test_chained_hash_insert(self):
        table, elements, h = get_random_chained_hash_table()
        new_key = random.randint(0, 999)
        new_element = ChainedElement(new_key)

        chained_hash_insert(table, new_element, h)

        actual_elements = get_chained_hash_table_elements(table)
        elements.append(new_element)
        assert_that(actual_elements, contains_inanyorder(*elements))

    def test_chained_hash_search(self):
        table, elements, h = get_random_chained_hash_table(max_value=10)
        key_to_find = random.randint(0, 10)

        actual_found = chained_hash_search(table, key_to_find, h)

        if key_to_find in [element.key for element in elements]:
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))

    def test_chained_hash_delete(self):
        table, elements, h = get_random_chained_hash_table()
        # make sure the table is not empty
        if not elements:
            key = random.randint(0, 999)
            elements.append(ChainedElement(key))
            table[h(key, table.length)] = elements[0]
        element_to_delete = random.choice(elements)

        chained_hash_delete(table, element_to_delete, h)

        actual_elements = get_chained_hash_table_elements(table)
        elements.remove(element_to_delete)
        assert_that(actual_elements, contains_inanyorder(*elements))
