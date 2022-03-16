import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_6 import stack_enqueue, stack_dequeue
from datastructures.array import Array
from datastructures.stack import Stack


class TestExercise10_1_6(TestCase):

    def test_stack_enqueue(self):
        size = 5
        stack = Stack(get_random_array(size=size), top=random.randint(0, size - 1))
        x = random.randint(0, 999)
        expected_elements = Array(x, stack)

        stack_enqueue(stack, x)

        actual_elements = Array(stack)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_stack_dequeue(self):
        size = 5
        stack = Stack(get_random_array(size=size), top=random.randint(0, size))

        if stack.top == 0:
            assert_that(calling(stack_dequeue).with_args(stack), raises(ValueError, 'underflow'))
        else:
            expected_elements = Array(stack)
            expected_elements.remove(expected_elements[expected_elements.length])
            expected_deleted = stack[1]

            actual_deleted = stack_dequeue(stack)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_elements = Array(stack)
            assert_that(actual_elements, is_(equal_to(expected_elements)))
