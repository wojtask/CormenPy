import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_2 import left_stack_push, left_stack_pop, right_stack_push, right_stack_pop
from datastructures.array import Array


def get_left_stack_elements(array):
    return array[:array.left_top]


def get_right_stack_elements(array):
    return array[array.right_top:]


class TestExercise10_1_2(TestCase):

    def test_left_stack_push(self):
        size = 10
        array = get_random_array(size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)
        x = random.randint(0, 999)

        if array.left_top == array.right_top - 1:
            assert_that(calling(left_stack_push).with_args(array, x), raises(ValueError, 'overflow'))
        else:
            expected_left_keys = get_left_stack_elements(array) + Array.of(x)
            expected_right_keys = get_right_stack_elements(array)

            left_stack_push(array, x)

            actual_left_elements = get_left_stack_elements(array)
            actual_right_elements = get_right_stack_elements(array)
            assert_that(actual_left_elements, is_(equal_to(expected_left_keys)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_keys)))

    def test_left_stack_pop(self):
        size = 10
        array = get_random_array(size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)

        if array.left_top == 0:
            assert_that(calling(left_stack_pop).with_args(array), raises(ValueError, 'underflow'))
        else:
            expected_left_elements = get_left_stack_elements(array)
            expected_left_elements.pop(expected_left_elements.length)
            expected_right_elements = get_right_stack_elements(array)
            expected_deleted = array[array.left_top]

            actual_deleted = left_stack_pop(array)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_left_elements = get_left_stack_elements(array)
            actual_right_elements = get_right_stack_elements(array)
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))

    def test_right_stack_push(self):
        size = 10
        array = get_random_array(size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)
        x = random.randint(0, 999)

        if array.left_top == array.right_top - 1:
            assert_that(calling(right_stack_push).with_args(array, x), raises(ValueError, 'overflow'))
        else:
            expected_left_elements = get_left_stack_elements(array)
            expected_right_elements = Array.of(x) + get_right_stack_elements(array)

            right_stack_push(array, x)

            actual_left_elements = get_left_stack_elements(array)
            actual_right_elements = get_right_stack_elements(array)
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))

    def test_right_stack_pop(self):
        size = 10
        array = get_random_array(size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)

        if array.right_top == array.length + 1:
            assert_that(calling(right_stack_pop).with_args(array), raises(ValueError, 'underflow'))
        else:
            expected_left_elements = get_left_stack_elements(array)
            expected_right_elements = get_right_stack_elements(array)
            expected_right_elements.pop(1)
            expected_deleted = array[array.right_top]

            actual_deleted = right_stack_pop(array)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_left_elements = get_left_stack_elements(array)
            actual_right_elements = get_right_stack_elements(array)
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))
