import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_7 import queue_push, queue_pop
from queue_util import get_queue_elements


class TestExercise10_1_7(TestCase):

    def test_queue_push(self):
        size = 5
        queue, _ = get_random_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        # if queue is full then make it empty
        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            queue.tail = queue.head

        x = random.randint(0, 999)
        expected_elements = get_queue_elements(queue) + [x]

        queue_push(queue, x)

        actual_elements = get_queue_elements(queue)
        assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_queue_pop(self):
        size = 5
        queue, _ = get_random_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        if queue.head == queue.tail:
            assert_that(calling(queue_pop).with_args(queue), raises(ValueError, 'underflow'))
        else:
            expected_elements = get_queue_elements(queue)
            del expected_elements[-1]
            expected_deleted = queue[queue.tail - 1]

            actual_deleted = queue_pop(queue)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_elements = get_queue_elements(queue)
            assert_that(actual_elements, is_(equal_to(expected_elements)))
