import random
from unittest import TestCase

from hamcrest import *

from chapter11.textbook11_1 import direct_address_search, direct_address_insert, direct_address_delete
from hash_table_util import get_random_direct_address_table
from util import Element


class TestTextbook11_1(TestCase):

    def test_direct_address_search(self):
        table, elements = get_random_direct_address_table()
        key_to_find = random.randint(0, table.length - 1)

        actual_found = direct_address_search(table, key_to_find)

        if key_to_find in [element.key for element in elements]:
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))

    def test_direct_address_insert(self):
        table, elements = get_random_direct_address_table()
        new_key = random.randint(0, table.length - 1)
        new_element = Element(new_key)

        direct_address_insert(table, new_element)

        assert_that(table[new_key], is_(equal_to(new_element)))

    def test_direct_address_delete(self):
        table, elements = get_random_direct_address_table()
        # make sure the table is not empty
        if not elements:
            key = random.randint(0, table.length - 1)
            elements.append(Element(key))
            table[key] = elements[0]
        element_to_delete = random.choice(elements)

        direct_address_delete(table, element_to_delete)

        assert_that(table[element_to_delete.key], is_(none()))
