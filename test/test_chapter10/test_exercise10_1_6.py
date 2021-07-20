import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_6 import stack_enqueue, stack_dequeue
from queue_util import get_stack_elements


class TestExercise10_1_6(TestCase):

    def test_stack_enqueue(self):
        size = 5
        stack = get_random_array(size=size)
        stack.top = random.randint(0, size - 1)
        x = random.randint(0, 999)
        expected_elements = get_stack_elements(stack) + [x]

        stack_enqueue(stack, x)

        actual_elements = get_stack_elements(stack)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_stack_dequeue(self):
        size = 5
        stack = get_random_array(size=size)
        stack.top = random.randint(0, size)

        if stack.top == 0:
            assert_that(calling(stack_dequeue).with_args(stack), raises(ValueError, 'underflow'))
        else:
            expected_elements = get_stack_elements(stack)
            expected_elements.remove(expected_elements[1])
            expected_deleted = stack[1]

            actual_deleted = stack_dequeue(stack)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_elements = get_stack_elements(stack)
            assert_that(actual_elements, is_(equal_to(expected_elements)))
