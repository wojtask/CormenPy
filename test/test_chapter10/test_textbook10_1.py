import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.textbook10_1 import stack_empty, push, pop, enqueue, dequeue
from queue_util import get_stack_elements, get_queue_elements


class TestTextbook10_1(TestCase):

    def test_stack_empty(self):
        size = 3
        stack = get_random_array(size=size)
        stack.top = random.randint(0, size)

        actual_empty = stack_empty(stack)

        if stack.top == 0:
            assert_that(actual_empty, is_(True))
        else:
            assert_that(actual_empty, is_(False))

    def test_push(self):
        size = 10
        stack = get_random_array(size=size)
        stack.top = random.randint(0, size - 1)
        x = random.randint(0, 999)
        expected_keys = get_stack_elements(stack) + [x]

        push(stack, x)

        actual_keys = get_stack_elements(stack)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_pop(self):
        size = 10
        stack = get_random_array(size=size)
        stack.top = random.randint(0, size)

        if stack.top == 0:
            assert_that(calling(pop).with_args(stack), raises(ValueError, 'underflow'))
        else:
            expected_keys = get_stack_elements(stack)
            expected_keys.remove(expected_keys[expected_keys.length])
            expected_deleted = stack[stack.top]

            actual_deleted = pop(stack)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_keys = get_stack_elements(stack)
            assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_enqueue(self):
        size = 10
        queue = get_random_array(size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        # if queue is full then make it empty
        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            queue.tail = queue.head

        x = random.randint(0, 999)
        expected_keys = get_queue_elements(queue) + [x]

        enqueue(queue, x)

        actual_keys = get_queue_elements(queue)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_dequeue(self):
        size = 10
        queue = get_random_array(size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        # if queue is empty then make it full
        if queue.head == queue.tail:
            queue.tail = queue.tail - 1 if queue.tail > 1 else queue.length

        expected_keys = get_queue_elements(queue)
        expected_keys.remove(expected_keys[1])
        expected_deleted = queue[queue.head]

        actual_deleted = dequeue(queue)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_keys = get_queue_elements(queue)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
