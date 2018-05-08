import random
from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_1_4 import huge_array_search, huge_array_insert, huge_array_delete
from hash_table_util import get_random_huge_array
from queue_util import get_stack_elements
from util import Element


class TestExercise11_1_4(TestCase):

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
            stack.elements.append(None)
            stack.length += 1
        new_element = Element(new_key)

        expected_elements = get_stack_elements(stack) + [new_element]

        huge_array_insert(table, stack, new_element)

        actual_elements = get_stack_elements(stack)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_huge_array_delete(self):
        table, stack, keys = get_random_huge_array()
        # make sure the table is not empty
        if not keys:
            key = random.randint(0, table.length - 1)
            keys.append(key)
            stack[1] = Element(key)
            table[key] = stack.top = 1
        expected_elements = get_stack_elements(stack)
        element_to_delete = random.choice(expected_elements)
        expected_elements.remove(element_to_delete)

        huge_array_delete(table, stack, element_to_delete)

        actual_elements = get_stack_elements(stack)
        assert_that(actual_elements, contains_inanyorder(*expected_elements))
