import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter17.exercise17_3_6 import effective_stack_enqueue, effective_stack_dequeue
from queue_util import get_stack_elements


def get_queue_elements(stack1, stack2):
    return list(reversed(get_stack_elements(stack2))) + get_stack_elements(stack1)


class TestExercise17_3_6(TestCase):

    def test_effective_stack_enqueue(self):
        capacity = 5
        stack1, _ = get_random_array(min_size=capacity, max_size=capacity)
        stack1.top = random.randint(0, capacity - 1)
        stack2, _ = get_random_array(min_size=capacity, max_size=capacity)
        stack2.top = random.randint(0, capacity)
        x = random.randint(0, 999)
        expected_elements = get_queue_elements(stack1, stack2) + [x]

        effective_stack_enqueue(stack1, x)

        actual_elements = get_queue_elements(stack1, stack2)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_effective_stack_dequeue(self):
        capacity = 5
        stack1, _ = get_random_array(min_size=capacity, max_size=capacity)
        stack1.top = random.randint(0, capacity)
        stack2, _ = get_random_array(min_size=capacity, max_size=capacity)
        stack2.top = random.randint(0, capacity)

        if stack1.top == 0 and stack2.top == 0:
            assert_that(calling(effective_stack_dequeue).with_args(stack1, stack2), raises(ValueError, 'underflow'))
        else:
            expected_elements = get_queue_elements(stack1, stack2)
            del expected_elements[0]
            expected_deleted = stack2[stack2.top] if stack2.top > 0 else stack1[1]

            actual_deleted = effective_stack_dequeue(stack1, stack2)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_elements = get_queue_elements(stack1, stack2)
            assert_that(actual_elements, is_(equal_to(expected_elements)))
