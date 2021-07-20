import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_7 import queue_push, queue_pop
from datastructures.array import Array
from queue_util import get_queue_elements


class TestExercise10_1_7(TestCase):

    def test_queue_push(self):
        size = 5
        queue = get_random_array(size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        # if queue is full then make it empty
        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            queue.tail = queue.head

        x = random.randint(0, 999)
        expected_elements = get_queue_elements(queue) + Array([x])

        queue_push(queue, x)

        actual_elements = get_queue_elements(queue)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_queue_pop(self):
        size = 5
        queue = get_random_array(size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        if queue.head == queue.tail:
            assert_that(calling(queue_pop).with_args(queue), raises(ValueError, 'underflow'))
        else:
            expected_elements = get_queue_elements(queue)
            expected_elements.remove(expected_elements[expected_elements.length])
            index_of_deleted_element = queue.tail - 1 if queue.tail > 1 else queue.length
            expected_deleted = queue[index_of_deleted_element]

            actual_deleted = queue_pop(queue)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_elements = get_queue_elements(queue)
            assert_that(actual_elements, is_(equal_to(expected_elements)))
