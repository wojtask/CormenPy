import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_1_4 import huge_array_search, huge_array_insert, huge_array_delete
from hash_table_util import get_random_huge_array, assert_huge_array_consistent
from queue_util import get_stack_elements
from util import Element


class TestExercise11_1_4(TestCase):

    def test_huge_array_search(self):
        max_value = 20
        table, stack, keys = get_random_huge_array(max_value=max_value)
        original_table = copy.deepcopy(table)
        original_stack = copy.deepcopy(stack)
        key_to_find = random.randint(0, max_value)

        actual_found = huge_array_search(table, stack, key_to_find)

        if key_to_find in keys:
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))
        assert_that(original_table, is_(equal_to(table)))
        assert_that(original_stack, is_(equal_to(stack)))

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
            stack.append(None)
        original_stack = copy.deepcopy(stack)
        new_element = Element(new_key)

        huge_array_insert(table, stack, new_element)

        actual_elements = get_stack_elements(stack)
        original_elements = get_stack_elements(original_stack)
        assert_that(actual_elements, contains_inanyorder(*original_elements, new_element))
        assert_huge_array_consistent(table, stack)

    def test_huge_array_delete(self):
        table, stack, keys = get_random_huge_array()
        # make sure the table is not empty
        if not keys:
            key = random.randint(0, table.length - 1)
            keys.append(key)
            stack[1] = Element(key)
            table[key] = stack.top = 1
        original_stack = copy.deepcopy(stack)
        expected_elements = get_stack_elements(original_stack)
        element_to_delete = expected_elements[random.randint(1, expected_elements.length)]
        expected_elements.remove(element_to_delete)

        huge_array_delete(table, stack, element_to_delete)

        actual_elements = get_stack_elements(stack)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))
        assert_huge_array_consistent(table, stack)
