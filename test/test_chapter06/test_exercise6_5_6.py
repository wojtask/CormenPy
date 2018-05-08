import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_6 import priority_enqueue, priority_dequeue, priority_push, priority_pop
from datastructures.array import Array
from heap_util import get_random_min_heap, get_random_max_heap
from util import Element


class TestExercise6_5_6(TestCase):

    def test_priority_enqueue(self):
        size = random.randint(5, 20)
        heap = Array.indexed(1, size)
        heap.heap_size = 0
        heap.rank = 1
        nelements = random.randint(1, size)

        for i in range(1, nelements + 1):
            new_element = Element(None, "element " + str(i))
            priority_enqueue(heap, new_element)

        for element in heap[1:heap.heap_size]:
            assert_that(element.data, is_(equal_to("element " + str(element.key))))

    def test_priority_dequeue(self):
        # create a random min heap of numbers
        heap, elements = get_random_min_heap()
        # and then transform the numbers to elements with keys and data
        expected_elements = []
        for i in range(1, heap.heap_size + 1):
            heap[i] = Element(heap[i], "element " + str(heap[i]))
            expected_elements.append(heap[i])

        expected_deleted = min([element for element in heap[1:heap.heap_size]], key=lambda e: e.key)
        expected_elements.remove(expected_deleted)

        actual_deleted = priority_dequeue(heap)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_elements = heap[1:heap.heap_size].elements
        assert_that(actual_elements, contains_inanyorder(*expected_elements))

    def test_priority_push(self):
        size = random.randint(5, 20)
        heap = Array.indexed(1, size)
        heap.heap_size = 0
        heap.rank = 1
        nelements = random.randint(1, size)

        for i in range(1, nelements + 1):
            new_element = Element(None, "element " + str(i))
            priority_push(heap, new_element)

        for element in heap[1:heap.heap_size]:
            assert_that(element.data, is_(equal_to("element " + str(element.key))))

    def test_priority_pop(self):
        # create a random max heap of numbers
        heap, elements = get_random_max_heap()
        # and then transform the numbers to elements with keys and data
        expected_elements = []
        for i in range(1, heap.heap_size + 1):
            heap[i] = Element(heap[i], "element " + str(heap[i]))
            expected_elements.append(heap[i])

        expected_deleted = max([element for element in heap[1:heap.heap_size]], key=lambda e: e.key)
        expected_elements.remove(expected_deleted)

        actual_deleted = priority_pop(heap)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_elements = heap[1:heap.heap_size].elements
        assert_that(actual_elements, contains_inanyorder(*expected_elements))
