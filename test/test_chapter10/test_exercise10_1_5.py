import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_5 import head_enqueue, head_dequeue, tail_enqueue, tail_dequeue
from datastructures.array import Array
from datastructures.queue import Queue


class TestExercise10_1_5(TestCase):

    def test_head_enqueue(self):
        size = 5
        deque = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))

        # if deque is full then make it empty
        if (deque.head == 1 and deque.tail == deque.length) or deque.head == deque.tail + 1:
            deque.tail = deque.head

        x = random.randint(0, 999)
        expected_elements = Array.of(x) + deque

        head_enqueue(deque, x)

        actual_elements = Array(deque)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_head_dequeue(self):
        size = 5
        deque = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))

        # if deque is empty then make it full
        if deque.head == deque.tail:
            deque.tail = deque.tail - 1 if deque.tail > 1 else deque.length

        expected_elements = Array(deque)
        expected_elements.pop(1)
        expected_deleted = deque[deque.head]

        actual_deleted = head_dequeue(deque)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_elements = Array(deque)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_tail_enqueue(self):
        size = 5
        deque = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))

        # if deque is full then make it empty
        if (deque.head == 1 and deque.tail == deque.length) or deque.head == deque.tail + 1:
            deque.tail = deque.head

        x = random.randint(0, 999)
        expected_elements = Array(deque) + Array.of(x)

        tail_enqueue(deque, x)

        actual_elements = Array(deque)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_tail_dequeue(self):
        size = 5
        deque = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))

        # if deque is empty then make it full
        if deque.head == deque.tail:
            deque.tail = deque.tail - 1 if deque.tail > 1 else deque.length

        expected_elements = Array(deque)
        expected_elements.pop(expected_elements.length)
        index_of_deleted_element = deque.tail - 1 if deque.tail > 1 else deque.length
        expected_deleted = deque[index_of_deleted_element]

        actual_deleted = tail_dequeue(deque)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_elements = Array(deque)
        assert_that(actual_elements, is_(equal_to(expected_elements)))
