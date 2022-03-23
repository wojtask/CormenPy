import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.exercise10_1_4 import queue_empty, enqueue_, dequeue_
from datastructures.array import Array
from datastructures.queue import Queue


class TestExercise10_1_4(TestCase):

    def test_queue_empty(self):
        size = 5
        queue = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))

        actual_empty = queue_empty(queue)

        assert_that(queue.is_modified(), is_(False))
        if queue.head == queue.tail:
            assert_that(actual_empty, is_(True))
        else:
            assert_that(actual_empty, is_(False))

    def test_enqueue_(self):
        size = 5
        queue = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))
        x = random.randint(0, 999)

        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            assert_that(calling(enqueue_).with_args(queue, x), raises(ValueError, 'overflow'))
        else:
            expected_elements = Array(queue) + Array.of(x)

            enqueue_(queue, x)

            actual_elements = Array(queue)
            assert_that(actual_elements, is_(equal_to(expected_elements)))

    def test_dequeue_(self):
        size = 5
        queue = Queue(get_random_array(size=size), head=random.randint(1, size), tail=random.randint(1, size))

        if queue.head == queue.tail:
            assert_that(calling(dequeue_).with_args(queue), raises(ValueError, 'underflow'))
        else:
            expected_elements = Array(queue)
            expected_elements.pop(1)
            expected_deleted = queue[queue.head]

            actual_deleted = dequeue_(queue)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_elements = Array(queue)
            assert_that(actual_elements, is_(equal_to(expected_elements)))
