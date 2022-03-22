import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_2 import left_stack_push, left_stack_pop, right_stack_push, right_stack_pop
from datastructures.array import Array
from datastructures.stack import DoubleStack


class TestExercise10_1_2(TestCase):

    def test_left_stack_push(self):
        size = 10
        left_top = random.randint(0, size)
        right_top = random.randint(left_top + 1, size + 1)
        double_stack = DoubleStack(get_random_array(size=size), left_top, right_top)
        x = random.randint(0, 999)

        if double_stack.left_top == double_stack.right_top - 1:
            assert_that(calling(left_stack_push).with_args(double_stack, x), raises(ValueError, 'overflow'))
        else:
            expected_left_keys = double_stack.get_left_stack_elements() + Array.of(x)
            expected_right_keys = double_stack.get_right_stack_elements()

            left_stack_push(double_stack, x)

            actual_left_elements = double_stack.get_left_stack_elements()
            actual_right_elements = double_stack.get_right_stack_elements()
            assert_that(actual_left_elements, is_(equal_to(expected_left_keys)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_keys)))

    def test_left_stack_pop(self):
        size = 10
        left_top = random.randint(0, size)
        right_top = random.randint(left_top + 1, size + 1)
        double_stack = DoubleStack(get_random_array(size=size), left_top, right_top)

        if double_stack.left_top == 0:
            assert_that(calling(left_stack_pop).with_args(double_stack), raises(ValueError, 'underflow'))
        else:
            expected_left_elements = double_stack.get_left_stack_elements()
            expected_left_elements.pop(expected_left_elements.length)
            expected_right_elements = double_stack.get_right_stack_elements()
            expected_deleted = double_stack[double_stack.left_top]

            actual_deleted = left_stack_pop(double_stack)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_left_elements = double_stack.get_left_stack_elements()
            actual_right_elements = double_stack.get_right_stack_elements()
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))

    def test_right_stack_push(self):
        size = 10
        left_top = random.randint(0, size)
        right_top = random.randint(left_top + 1, size + 1)
        double_stack = DoubleStack(get_random_array(size=size), left_top, right_top)
        x = random.randint(0, 999)

        if double_stack.left_top == double_stack.right_top - 1:
            assert_that(calling(right_stack_push).with_args(double_stack, x), raises(ValueError, 'overflow'))
        else:
            expected_left_elements = double_stack.get_left_stack_elements()
            expected_right_elements = Array.of(x) + double_stack.get_right_stack_elements()

            right_stack_push(double_stack, x)

            actual_left_elements = double_stack.get_left_stack_elements()
            actual_right_elements = double_stack.get_right_stack_elements()
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))

    def test_right_stack_pop(self):
        size = 10
        left_top = random.randint(0, size)
        right_top = random.randint(left_top + 1, size + 1)
        double_stack = DoubleStack(get_random_array(size=size), left_top, right_top)

        if double_stack.right_top == double_stack.length + 1:
            assert_that(calling(right_stack_pop).with_args(double_stack), raises(ValueError, 'underflow'))
        else:
            expected_left_elements = double_stack.get_left_stack_elements()
            expected_right_elements = double_stack.get_right_stack_elements()
            expected_right_elements.pop(1)
            expected_deleted = double_stack[double_stack.right_top]

            actual_deleted = right_stack_pop(double_stack)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_left_elements = double_stack.get_left_stack_elements()
            actual_right_elements = double_stack.get_right_stack_elements()
            assert_that(actual_left_elements, is_(equal_to(expected_left_elements)))
            assert_that(actual_right_elements, is_(equal_to(expected_right_elements)))
