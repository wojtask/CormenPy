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
        original = copy.deepcopy(table)
        key_to_find = random.randint(0, table.length - 1)

        actual_found = direct_address_search_(table, key_to_find)

        actual_elements = get_chained_hash_table_elements(table)
        original_elements = get_chained_hash_table_elements(original)
        if key_to_find in [element.key for element in original_elements]:
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))
        assert_that(table, is_(equal_to(original)))
        assert_that(actual_elements, is_(equal_to(original_elements)))

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
        actual_elements = get_chained_hash_table_elements(table)
        if not actual_elements:
            key = random.randint(0, table.length - 1)
            table[key] = ChainedElement(key)
            actual_elements.append(table[key])
        element_to_delete = actual_elements[random.randint(1, actual_elements.length)]
        original = copy.deepcopy(table)
        original_elements = get_chained_hash_table_elements(original)
        original_elements.remove(element_to_delete)

        direct_address_delete_(table, element_to_delete)

        actual_elements = get_chained_hash_table_elements(table)
        assert_that(actual_elements, contains_inanyorder(*original_elements))
