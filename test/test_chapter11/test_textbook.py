import random
from unittest import TestCase

from hamcrest import *

from chapter11.textbook import direct_address_search, direct_address_insert, direct_address_delete, chained_hash_insert, \
    chained_hash_search, chained_hash_delete, hash_insert, hash_search, quadratic_probing_search
from datastructures.hash_table import Element, ChainedElement
from hash_table_util import get_random_direct_address_table, get_chained_hash_table_elements, get_random_chained_hash_table, \
    get_random_hash_table_linear_probing, get_hash_table_keys, get_random_hash_table_quadratic_probing


class Textbook11Test(TestCase):

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

    def test_hash_insert(self):
        table, keys, h = get_random_hash_table_linear_probing()
        new_key = random.randint(0, 999)

        if len(keys) == table.length:
            assert_that(calling(hash_insert).with_args(table, new_key, h),
                        raises(RuntimeError, 'hash table overflow'))
        else:
            hash_insert(table, new_key, h)

            actual_keys = get_hash_table_keys(table)
            keys.append(new_key)
            assert_that(actual_keys, contains_inanyorder(*keys))

    def test_hash_search(self):
        table, keys, h = get_random_hash_table_linear_probing(max_value=10)
        key_to_find = random.randint(0, 10)

        actual_index = hash_search(table, key_to_find, h)

        if key_to_find in keys:
            assert_that(table[actual_index], is_(equal_to(key_to_find)))
        else:
            assert_that(actual_index, is_(none()))

    def test_quadratic_probing_search(self):
        table, keys, _, auxiliary_hash = get_random_hash_table_quadratic_probing(max_value=10)
        key_to_find = random.randint(0, 10)

        actual_index = quadratic_probing_search(table, key_to_find, auxiliary_hash)

        if key_to_find in keys:
            assert_that(table[actual_index], is_(equal_to(key_to_find)))
        else:
            assert_that(actual_index, is_(none()))
