import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_6 import priority_enqueue, priority_dequeue, priority_push, priority_pop
from datastructures.array import Array
from datastructures.heap import Heap
from heap_util import get_random_min_heap, get_random_max_heap
from util import Element, between


class TestExercise6_5_6(TestCase):

    def test_priority_enqueue(self):
        size = random.randint(5, 20)
        min_priority_queue = Heap(Array.indexed(1, size))
        min_priority_queue.heap_size = 0
        min_priority_queue.rank = 1
        nelements = random.randint(1, size)

        for i in between(1, nelements):
            new_element = Element(None, 'element ' + str(i))
            priority_enqueue(min_priority_queue, new_element)

        for element in min_priority_queue:
            assert_that(element.data, is_(equal_to('element ' + str(element.key))))

    def test_priority_dequeue(self):
        min_priority_queue = get_random_min_heap()
        # transform the numbers in the queue to elements with keys and data
        expected_elements = []
        for i in between(1, min_priority_queue.heap_size):
            min_priority_queue[i] = Element(min_priority_queue[i], 'element ' + str(min_priority_queue[i]))
            expected_elements.append(min_priority_queue[i])

        expected_deleted = min(min_priority_queue, key=lambda e: e.key)
        expected_elements.remove(expected_deleted)

        actual_deleted = priority_dequeue(min_priority_queue)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        assert_that(min_priority_queue, contains_inanyorder(*expected_elements))

    def test_priority_push(self):
        size = random.randint(5, 20)
        max_priority_queue = Heap(Array.indexed(1, size))
        max_priority_queue.heap_size = 0
        max_priority_queue.rank = 1
        nelements = random.randint(1, size)

        for i in between(1, nelements):
            new_element = Element(None, 'element ' + str(i))
            priority_push(max_priority_queue, new_element)

        for element in max_priority_queue:
            assert_that(element.data, is_(equal_to('element ' + str(element.key))))

    def test_priority_pop(self):
        max_priority_queue = get_random_max_heap()
        # transform the numbers in the queue to elements with keys and data
        expected_elements = []
        for i in between(1, max_priority_queue.heap_size):
            max_priority_queue[i] = Element(max_priority_queue[i], 'element ' + str(max_priority_queue[i]))
            expected_elements.append(max_priority_queue[i])

        expected_deleted = max(max_priority_queue, key=lambda e: e.key)
        expected_elements.remove(expected_deleted)

        actual_deleted = priority_pop(max_priority_queue)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        assert_that(max_priority_queue, contains_inanyorder(*expected_elements))
