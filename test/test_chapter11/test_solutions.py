import random
from unittest import TestCase

from hamcrest import *

from chapter11.ex11_1_1 import direct_address_maximum
from chapter11.ex11_1_2 import bit_vector_search, bit_vector_insert, bit_vector_delete
from chapter11.ex11_1_3 import direct_address_search_, direct_address_insert_, direct_address_delete_
from chapter11.ex11_1_4 import huge_array_search, huge_array_insert, huge_array_delete
from chapter11.ex11_4_2 import hash_delete, hash_insert_
from datastructures.hash_table import ChainedElement, Element
from hash_table_util import get_random_direct_address_table, get_random_bit_vector, get_random_chained_direct_address_table, \
    get_chained_hash_table_elements, get_random_hash_table_linear_probing, get_hash_table_keys, get_random_huge_array
from queue_util import get_stack_keys


class Solutions11Test(TestCase):

    def test_direct_address_maximum(self):
        table, elements = get_random_direct_address_table()

        actual_maximum = direct_address_maximum(table)

        if elements:
            expected_maximum = max([element.key for element in elements])
            assert_that(actual_maximum.key, is_(equal_to(expected_maximum)))
        else:
            assert_that(actual_maximum, is_(none()))

    def test_bit_vector_search(self):
        bit_vector, keys = get_random_bit_vector()
        key_to_find = random.randint(0, bit_vector.length - 1)

        actual_found = bit_vector_search(bit_vector, key_to_find)

        if key_to_find in keys:
            assert_that(actual_found, is_(equal_to(1)))
        else:
            assert_that(actual_found, is_(equal_to(0)))

    def test_bit_vector_insert(self):
        bit_vector, keys = get_random_bit_vector()
        new_key = random.randint(0, bit_vector.length - 1)

        bit_vector_insert(bit_vector, new_key)

        assert_that(bit_vector[new_key], is_(equal_to(1)))

    def test_bit_vector_delete(self):
        bit_vector, keys = get_random_bit_vector()
        key_to_delete = random.randint(0, bit_vector.length - 1)

        bit_vector_delete(bit_vector, key_to_delete)

        assert_that(bit_vector[key_to_delete], is_(equal_to(0)))

    def test_direct_address_search_(self):
        table, elements = get_random_chained_direct_address_table()
        key_to_find = random.randint(0, table.length - 1)

        actual_found = direct_address_search_(table, key_to_find)

        if key_to_find in [element.key for element in elements]:
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))

    def test_direct_address_insert_(self):
        table, elements = get_random_chained_direct_address_table()
        new_key = random.randint(0, table.length - 1)
        new_element = ChainedElement(new_key)

        direct_address_insert_(table, new_element)

        actual_elements = get_chained_hash_table_elements(table)
        elements.append(new_element)
        assert_that(actual_elements, contains_inanyorder(*elements))

    def test_chained_hash_delete_(self):
        table, elements = get_random_chained_direct_address_table()
        # make sure the table is not empty
        if not elements:
            key = random.randint(0, table.length - 1)
            elements.append(ChainedElement(key))
            table[key] = elements[0]
        element_to_delete = random.choice(elements)

        direct_address_delete_(table, element_to_delete)

        actual_elements = get_chained_hash_table_elements(table)
        elements.remove(element_to_delete)
        assert_that(actual_elements, contains_inanyorder(*elements))

    def test_huge_array_search(self):
        table, stack, keys = get_random_huge_array(max_value=20)
        key_to_find = random.randint(0, 19)

        actual_found = huge_array_search(table, stack, key_to_find)

        if key_to_find in keys:
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))

    def test_huge_array_insert(self):
        table, stack, keys = get_random_huge_array()
        new_key = random.randint(0, table.length - 1)
        # make sure the table does not contain new_key
        if new_key in keys:
            y = stack[stack.top]
            stack.top -= 1
            stack[table[new_key]] = y
            table[y.key] = table[new_key]
        # also make sure there is a space in stack for the new element
        if stack.top == stack.length:
            stack.data.append(None)
            stack.length += 1
        new_element = Element(new_key)

        expected_elements = get_stack_keys(stack) + [new_element]

        huge_array_insert(table, stack, new_element)

        actual_elements = get_stack_keys(stack)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_huge_array_delete(self):
        table, stack, keys = get_random_huge_array()
        # make sure the table is not empty
        if not keys:
            key = random.randint(0, table.length - 1)
            keys.append(key)
            stack[1] = Element(key)
            table[key] = stack.top = 1
        expected_elements = get_stack_keys(stack)
        element_to_delete = random.choice(expected_elements)
        expected_elements.remove(element_to_delete)

        huge_array_delete(table, stack, element_to_delete)

        actual_elements = get_stack_keys(stack)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_hash_delete(self):
        table, keys, h = get_random_hash_table_linear_probing()
        # make sure the table is not empty
        if not keys:
            key = random.randint(0, 999)
            keys.append(key)
            table[h(key, 0, table.length)] = key
        key_to_delete = random.choice(keys)

        hash_delete(table, key_to_delete, h)

        actual_keys = get_hash_table_keys(table)
        keys.remove(key_to_delete)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_hash_insert_(self):
        table, keys, h = get_random_hash_table_linear_probing()
        new_key = random.randint(0, 999)

        if len(keys) == table.length:
            assert_that(calling(hash_insert_).with_args(table, new_key, h),
                        raises(RuntimeError, 'hash table overflow'))
        else:
            hash_insert_(table, new_key, h)

            actual_keys = get_hash_table_keys(table)
            keys.append(new_key)
            assert_that(actual_keys, contains_inanyorder(*keys))
