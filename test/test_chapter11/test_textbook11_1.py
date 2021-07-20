import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter11.textbook11_1 import direct_address_search, direct_address_insert, direct_address_delete
from datastructures.array import Array
from hash_table_util import get_random_direct_address_table
from util import Element


def get_direct_access_table_elements(table):
    return Array(element for element in table if element)


class TestTextbook11_1(TestCase):

    def test_direct_address_search(self):
        table = get_random_direct_address_table()
        original = copy.deepcopy(table)
        key_to_find = random.randint(0, table.length - 1)

        actual_found = direct_address_search(table, key_to_find)

        actual_elements = get_direct_access_table_elements(table)
        if key_to_find in Array(element.key for element in actual_elements):
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))
        assert_that(table, is_(equal_to(original)))

    def test_direct_address_insert(self):
        table = get_random_direct_address_table()
        original = copy.deepcopy(table)
        new_key = random.randint(0, table.length - 1)
        new_element = Element(new_key)

        direct_address_insert(table, new_element)

        assert_that(table[new_key], is_(equal_to(new_element)))
        actual_elements = get_direct_access_table_elements(table)
        original_elements = get_direct_access_table_elements(original)
        if original[new_key]:  # no new key has in fact been inserted
            assert_that(actual_elements, contains_inanyorder(*original_elements))
        else:
            assert_that(actual_elements, contains_inanyorder(*original_elements, new_element))

    def test_direct_address_delete(self):
        table = get_random_direct_address_table()
        # make sure the table is not empty
        actual_elements = get_direct_access_table_elements(table)
        if not actual_elements:
            key = random.randint(0, table.length - 1)
            table[key] = Element(key)
            actual_elements.append(table[key])
        element_to_delete = actual_elements[random.randint(1, actual_elements.length)]
        original = copy.deepcopy(table)
        expected_elements = get_direct_access_table_elements(original)
        expected_elements.remove(element_to_delete)

        direct_address_delete(table, element_to_delete)

        assert_that(table[element_to_delete.key], is_(none()))
        actual_elements = get_direct_access_table_elements(table)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))
