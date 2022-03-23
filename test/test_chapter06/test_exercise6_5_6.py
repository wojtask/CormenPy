import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_6 import priority_enqueue, priority_dequeue, priority_push, priority_pop
from datastructures.array import Array
from datastructures.essential import Element
from datastructures.heap import PriorityQueueFIFO, PriorityQueueStack
from heap_util import get_random_min_heap, get_random_max_heap
from util import between


class TestExercise6_5_6(TestCase):

    def test_priority_enqueue(self):
        size = random.randint(5, 20)
        fifo_queue = PriorityQueueFIFO(Array.indexed(1, size))
        nelements = random.randint(1, size)

        for i in between(1, nelements):
            new_element = Element(None, 'element %d' % i)
            priority_enqueue(fifo_queue, new_element)

        for element in fifo_queue:
            assert_that(element.data, is_(equal_to('element %d' % element.key)))
        assert_that(fifo_queue.rank, is_(equal_to(nelements + 1)))

    def test_priority_dequeue(self):
        rank = 100
        min_heap = get_random_min_heap()
        fifo_queue = PriorityQueueFIFO(min_heap, heap_size=min_heap.heap_size, rank=rank)
        # transform the numbers in the queue to elements with keys and data
        expected_elements = Array()
        for i in between(1, fifo_queue.heap_size):
            fifo_queue[i] = Element(fifo_queue[i], 'element %d' % fifo_queue[i])
            expected_elements.append(fifo_queue[i])

        expected_deleted = min(fifo_queue, key=lambda e: e.key)
        expected_elements.remove(expected_deleted)

        actual_deleted = priority_dequeue(fifo_queue)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        assert_that(fifo_queue.rank, is_(equal_to(rank)))
        assert_that(fifo_queue, contains_inanyorder(*expected_elements))

    def test_priority_push(self):
        size = random.randint(5, 20)
        stack = PriorityQueueStack(Array.indexed(1, size))
        nelements = random.randint(1, size)

        for i in between(1, nelements):
            new_element = Element(None, 'element %d' % i)
            priority_push(stack, new_element)

        for element in stack:
            assert_that(element.data, is_(equal_to('element %d' % element.key)))
        assert_that(stack.rank, is_(equal_to(nelements + 1)))

    def test_priority_pop(self):
        rank = 100
        max_heap = get_random_max_heap()
        stack = PriorityQueueStack(max_heap, heap_size=max_heap.heap_size, rank=rank)
        # transform the numbers in the queue to elements with keys and data
        expected_elements = Array()
        for i in between(1, stack.heap_size):
            stack[i] = Element(stack[i], 'element %d' % stack[i])
            expected_elements.append(stack[i])

        expected_deleted = max(stack, key=lambda e: e.key)
        expected_elements.remove(expected_deleted)

        actual_deleted = priority_pop(stack)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        assert_that(stack.rank, is_(equal_to(rank)))
        assert_that(stack, contains_inanyorder(*expected_elements))
