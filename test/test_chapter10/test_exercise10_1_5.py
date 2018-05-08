import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_5 import head_enqueue, head_dequeue, tail_enqueue, tail_dequeue
from queue_util import get_queue_elements


class TestExercise10_1_5(TestCase):

    def test_head_enqueue(self):
        size = 5
        deque, _ = get_random_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is full then make it empty
        if (deque.head == 1 and deque.tail == deque.length) or deque.head == deque.tail + 1:
            deque.tail = deque.head

        x = random.randint(0, 999)
        expected_elements = [x] + get_queue_elements(deque)

        head_enqueue(deque, x)

        actual_elements = get_queue_elements(deque)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_head_dequeue(self):
        size = 5
        deque, _ = get_random_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is empty then make it full
        if deque.head == deque.tail:
            deque.tail = deque.tail - 1 if deque.tail > 1 else deque.length

        expected_elements = get_queue_elements(deque)
        del expected_elements[0]
        expected_deleted = deque[deque.head]

        actual_deleted = head_dequeue(deque)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_elements = get_queue_elements(deque)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_tail_enqueue(self):
        size = 5
        deque, _ = get_random_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is full then make it empty
        if (deque.head == 1 and deque.tail == deque.length) or deque.head == deque.tail + 1:
            deque.tail = deque.head

        x = random.randint(0, 999)
        expected_elements = get_queue_elements(deque) + [x]

        tail_enqueue(deque, x)

        actual_elements = get_queue_elements(deque)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_tail_dequeue(self):
        size = 5
        deque, _ = get_random_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is empty then make it full
        if deque.head == deque.tail:
            deque.tail = deque.tail - 1 if deque.tail > 1 else deque.length

        expected_elements = get_queue_elements(deque)
        del expected_elements[-1]
        expected_deleted = deque[deque.tail - 1]

        actual_deleted = tail_dequeue(deque)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_elements = get_queue_elements(deque)
        assert_that(actual_elements, is_(equal_to(expected_elements)))
