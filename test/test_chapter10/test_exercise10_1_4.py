import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_4 import queue_empty, enqueue_, dequeue_
from datastructures.array import Array
from queue_util import get_queue_elements


class TestExercise10_1_4(TestCase):

    def test_queue_empty(self):
        size = 5
        queue = get_random_array(size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        actual_empty = queue_empty(queue)

        if queue.head == queue.tail:
            assert_that(actual_empty, is_(True))
        else:
            assert_that(actual_empty, is_(False))

    def test_enqueue_(self):
        size = 5
        queue = get_random_array(size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)
        x = random.randint(0, 999)

        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            assert_that(calling(enqueue_).with_args(queue, x), raises(ValueError, 'overflow'))
        else:
            expected_elements = get_queue_elements(queue) + Array([x])

            enqueue_(queue, x)

            actual_elements = get_queue_elements(queue)
            assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_dequeue_(self):
        size = 5
        queue = get_random_array(size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        if queue.head == queue.tail:
            assert_that(calling(dequeue_).with_args(queue), raises(ValueError, 'underflow'))
        else:
            expected_elements = get_queue_elements(queue)
            expected_elements.remove(expected_elements[1])
            expected_deleted = queue[queue.head]

            actual_deleted = dequeue_(queue)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_elements = get_queue_elements(queue)
            assert_that(actual_elements, is_(equal_to(expected_elements)))
