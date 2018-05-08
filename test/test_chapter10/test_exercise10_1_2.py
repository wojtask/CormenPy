import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_2 import left_stack_push, left_stack_pop, right_stack_push, right_stack_pop


class TestExercise10_1_2(TestCase):

    def test_left_stack_push(self):
        size = 10
        array, _ = get_random_array(min_size=size, max_size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)
        x = random.randint(0, 999)

        if array.left_top == array.right_top - 1:
            assert_that(calling(left_stack_push).with_args(array, x), raises(RuntimeError, 'overflow'))
        else:
            expected_left_keys = array[1:array.left_top].elements + [x]
            expected_right_keys = array[array.right_top:array.length].elements

            left_stack_push(array, x)

            actual_left_elements = array[1:array.left_top].elements
            actual_right_elements = array[array.right_top:array.length].elements
            assert_that(actual_left_elements, is_(equal_to(expected_left_keys)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_keys)))

    def test_left_stack_pop(self):
        size = 10
        array, _ = get_random_array(min_size=size, max_size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)

        if array.left_top == 0:
            assert_that(calling(left_stack_pop).with_args(array), raises(RuntimeError, 'underflow'))
        else:
            expected_left_elements = array[1:array.left_top - 1].elements
            expected_right_elements = array[array.right_top:array.length].elements
            expected_deleted = array[array.left_top]

            actual_deleted = left_stack_pop(array)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))

            actual_left_elements = array[1:array.left_top].elements
            actual_right_elements = array[array.right_top:array.length].elements
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))

    def test_right_stack_push(self):
        size = 10
        array, _ = get_random_array(min_size=size, max_size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)
        x = random.randint(0, 999)

        if array.left_top == array.right_top - 1:
            assert_that(calling(right_stack_push).with_args(array, x), raises(RuntimeError, 'overflow'))
        else:
            expected_left_elements = array[1:array.left_top].elements
            expected_right_elements = [x] + array[array.right_top:array.length].elements

            right_stack_push(array, x)

            actual_left_elements = array[1:array.left_top].elements
            actual_right_elements = array[array.right_top:array.length].elements
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))

    def test_right_stack_pop(self):
        size = 10
        array, _ = get_random_array(min_size=size, max_size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)

        if array.right_top == array.length + 1:
            assert_that(calling(right_stack_pop).with_args(array), raises(RuntimeError, 'underflow'))
        else:
            expected_left_elements = array[1:array.left_top].elements
            expected_right_elements = array[array.right_top + 1:array.length].elements
            expected_deleted = array[array.right_top]

            actual_deleted = right_stack_pop(array)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))

            actual_left_elements = array[1:array.left_top].elements
            actual_right_elements = array[array.right_top:array.length].elements
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))
