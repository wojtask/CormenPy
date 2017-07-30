import random
from unittest import TestCase

from hamcrest import *

from chapter11.ex11_1_1 import direct_address_maximum
from chapter11.ex11_1_2 import bit_vector_search, bit_vector_insert, bit_vector_delete
from chapter11.ex11_1_3 import direct_address_search_, direct_address_insert_, direct_address_delete_
from datastructures.hash_table import ChainedElement
from hash_table_util import random_direct_address_table, random_bit_vector, random_chained_direct_address_table, \
    get_chained_hash_table_elements


class Solutions11Test(TestCase):

    def test_direct_address_maximum(self):
        table, elements = random_direct_address_table()

        actual_maximum = direct_address_maximum(table)

        if elements:
            expected_maximum = max([element.key for element in elements])
            assert_that(actual_maximum.key, is_(equal_to(expected_maximum)))
        else:
            assert_that(actual_maximum, is_(none()))

    def test_bit_vector_search(self):
        bit_vector, keys = random_bit_vector()
        key_to_find = random.randint(0, bit_vector.length - 1)

        actual_found = bit_vector_search(bit_vector, key_to_find)

        if key_to_find in keys:
            assert_that(actual_found, is_(equal_to(1)))
        else:
            assert_that(actual_found, is_(equal_to(0)))

    def test_bit_vector_insert(self):
        bit_vector, keys = random_bit_vector()
        new_key = random.randint(0, bit_vector.length - 1)

        bit_vector_insert(bit_vector, new_key)

        assert_that(bit_vector[new_key], is_(equal_to(1)))

    def test_bit_vector_delete(self):
        bit_vector, keys = random_bit_vector()
        key_to_delete = random.randint(0, bit_vector.length - 1)

        bit_vector_delete(bit_vector, key_to_delete)

        assert_that(bit_vector[key_to_delete], is_(equal_to(0)))

    def test_direct_address_search_(self):
        table, elements = random_chained_direct_address_table()
        key_to_find = random.randint(0, table.length - 1)

        actual_found = direct_address_search_(table, key_to_find)

        if key_to_find in [element.key for element in elements]:
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))

    def test_direct_address_insert_(self):
        table, elements = random_chained_direct_address_table()
        new_key = random.randint(0, table.length - 1)
        new_element = ChainedElement(new_key)
        expected_elements = get_chained_hash_table_elements(table) + [new_element]

        direct_address_insert_(table, new_element)

        actual_elements = get_chained_hash_table_elements(table)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_chained_hash_delete_(self):
        table, elements = random_chained_direct_address_table()
        # make sure the table is not empty
        if not elements:
            key = random.randint(0, table.length - 1)
            elements.append(ChainedElement(key))
            table[key] = elements[0]
        element_to_delete = random.choice(elements)
        expected_elements = get_chained_hash_table_elements(table)
        expected_elements.remove(element_to_delete)

        direct_address_delete_(table, element_to_delete)

        actual_elements = get_chained_hash_table_elements(table)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))
