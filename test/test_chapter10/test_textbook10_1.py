import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.textbook10_1 import stack_empty, push, pop, enqueue, dequeue
from datastructures.array import Array
from datastructures.queue import Queue
from datastructures.stack import Stack


class TestTextbook10_1(TestCase):

    def test_stack_empty(self):
        size = 3
        stack = Stack(get_random_array(size=size), top=random.randint(0, size))
        original = copy.deepcopy(stack)

        actual_empty = stack_empty(stack)

        if stack.top == 0:
            assert_that(actual_empty, is_(True))
        else:
            assert_that(actual_empty, is_(False))
        assert_that(stack, is_(equal_to(original)))

    def test_push(self):
        size = 10
        stack = Stack(get_random_array(size=size), top=random.randint(0, size - 1))
        x = random.randint(0, 999)
        expected_keys = Array(x, stack)

        push(stack, x)

        actual_keys = Array(stack)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_pop(self):
        size = 10
        stack = Stack(get_random_array(size=size), top=random.randint(0, size))

        if stack.top == 0:
            assert_that(calling(pop).with_args(stack), raises(ValueError, 'underflow'))
        else:
            expected_keys = Array(stack)
            expected_keys.pop(1)
            expected_deleted = stack[stack.top]

            actual_deleted = pop(stack)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_keys = Array(stack)
            assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_enqueue(self):
        size = 10
        queue = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))

        # if queue is full then make it empty
        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            queue.tail = queue.head

        x = random.randint(0, 999)
        expected_keys = Array(queue, x)

        enqueue(queue, x)

        actual_keys = Array(queue)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_dequeue(self):
        size = 10
        queue = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))

        # if queue is empty then make it full
        if queue.head == queue.tail:
            queue.tail = queue.tail - 1 if queue.tail > 1 else queue.length

        expected_keys = Array(queue)
        expected_keys.pop(1)
        expected_deleted = queue[queue.head]

        actual_deleted = dequeue(queue)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_keys = Array(queue)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
