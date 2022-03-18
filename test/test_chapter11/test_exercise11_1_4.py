import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_1_4 import huge_array_search, huge_array_insert, huge_array_delete
from hash_table_util import get_random_huge_array, assert_huge_array_consistent
from util import Element


class TestExercise11_1_4(TestCase):

    def test_huge_array_search(self):
        max_value = 20
        huge_array, stack_array = get_random_huge_array(max_value=max_value)
        original_huge_array = copy.deepcopy(huge_array)
        original_stack_array = copy.deepcopy(stack_array)
        key_to_find = random.randint(0, max_value)

        actual_found = huge_array_search(huge_array, stack_array, key_to_find)

        if key_to_find in (element.key for element in stack_array[:stack_array.top]):
            assert_that(actual_found.key, is_(equal_to(key_to_find)))
        else:
            assert_that(actual_found, is_(none()))
        assert_that(original_huge_array, is_(equal_to(huge_array)))
        assert_that(original_stack_array, is_(equal_to(stack_array)))

    def test_huge_array_insert(self):
        huge_array, stack_array = get_random_huge_array()
        original_elements = stack_array[:stack_array.top]
        new_key = random.randint(0, huge_array.length - 1)
        # make sure the huge_array does not contain new_key
        if new_key in (element.key for element in original_elements):
            y = stack_array[stack_array.top]
            stack_array.top -= 1
            stack_array[huge_array[new_key]] = y
            huge_array[y.key] = huge_array[new_key]
            for element in original_elements:
                if element.key == new_key:
                    original_elements.remove(element)
        # also make sure there is space in stack_array for the new element
        if stack_array.top == stack_array.length:
            stack_array.append(None)
        new_element = Element(new_key)

        huge_array_insert(huge_array, stack_array, new_element)

        actual_keys = stack_array[:stack_array.top]
        assert_that(actual_keys, contains_inanyorder(*original_elements, new_element))
        assert_huge_array_consistent(huge_array, stack_array)

    def test_huge_array_delete(self):
        huge_array, stack_array = get_random_huge_array()
        # make sure the huge_array is not empty
        if stack_array.top == 0:
            key = random.randint(0, huge_array.length - 1)
            stack_array[1] = Element(key)
            huge_array[key] = stack_array.top = 1
        original_stack_array = copy.deepcopy(stack_array)
        element_to_delete = original_stack_array[random.randint(1, original_stack_array.top)]
        original_stack_array.remove(element_to_delete)
        original_stack_array.top -= 1
        expected_elements = original_stack_array[:original_stack_array.top]

        huge_array_delete(huge_array, stack_array, element_to_delete)

        actual_elements = stack_array[:stack_array.top]
        assert_that(actual_elements, contains_inanyorder(*expected_elements))
        assert_huge_array_consistent(huge_array, stack_array)
