import random
from unittest import TestCase

from hamcrest import *

from chapter10.ex10_1_4 import queue_empty, enqueue_, dequeue_
from test_datastructures.array_util import random_int_array


class Solutions10Test(TestCase):

    def test_queue_empty(self):
        size = 5
        queue, _ = random_int_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        actual_empty = queue_empty(queue)

        if queue.head == queue.tail:
            assert_that(actual_empty, is_(True))
        else:
            assert_that(actual_empty, is_(False))

    def test_enqueue_(self):
        size = 5
        queue, _ = random_int_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        head_before_insert = queue.head
        tail_before_insert = queue.tail
        x = random.randint(0, 999)

        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            assert_that(calling(enqueue_).with_args(queue, x), raises(RuntimeError, 'overflow'))
        else:
            enqueue_(queue, x)

            expected_tail = tail_before_insert + 1 if tail_before_insert != queue.length else 1
            assert_that(queue.head, is_(equal_to(head_before_insert)))
            assert_that(queue.tail, is_(equal_to(expected_tail)))
            assert_that(queue[tail_before_insert], is_(equal_to(x)))

    def test_dequeue_(self):
        size = 5
        queue, _ = random_int_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        head_before_delete = queue.head
        tail_before_delete = queue.tail

        if queue.head == queue.tail:
            assert_that(calling(dequeue_).with_args(queue), raises(RuntimeError, 'underflow'))
        else:
            actual_deleted = dequeue_(queue)

            expected_head = head_before_delete + 1 if head_before_delete != queue.length else 1
            assert_that(queue.head, is_(equal_to(expected_head)))
            assert_that(queue.tail, is_(equal_to(tail_before_delete)))
            assert_that(actual_deleted, is_(equal_to(queue[head_before_delete])))
