import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_1_3 import direct_address_search_, direct_address_insert_, direct_address_delete_
from datastructures.hash_table import ChainedElement
from hash_table_util import get_random_chained_direct_address_table, get_chained_hash_table_elements


class TestExercise11_1_3(TestCase):

    def test_direct_address_search_(self):
        table = get_random_chained_direct_address_table()
        key_to_find = random.randint(0, table.length - 1)

        actual_found = direct_address_search_(table, key_to_find)

        assert_that(table.is_modified(), is_(False))
        elements = get_chained_hash_table_elements(table)
        if key_to_find in (element.key for element in elements):
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))

    def test_direct_address_insert_(self):
        table = get_random_chained_direct_address_table()
        original = copy.deepcopy(table)
        new_key = random.randint(0, table.length - 1)
        new_element = ChainedElement(new_key)

        direct_address_insert_(table, new_element)

        actual_elements = get_chained_hash_table_elements(table)
        original_elements = get_chained_hash_table_elements(original)
        assert_that(actual_elements, contains_inanyorder(*original_elements, new_element))

    def test_chained_hash_delete_(self):
        table = get_random_chained_direct_address_table()
        # make sure the table is not empty
        original_elements = get_chained_hash_table_elements(table)
        if not original_elements:
            key = random.randint(0, table.length - 1)
            table[key] = ChainedElement(key)
            original_elements.append(table[key])
        element_to_delete = original_elements.random_choice()
        original = copy.deepcopy(table)
        expected_elements = get_chained_hash_table_elements(original)
        expected_elements.remove(element_to_delete)

        direct_address_delete_(table, element_to_delete)

        actual_elements = get_chained_hash_table_elements(table)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))
