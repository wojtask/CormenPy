import random
from unittest import TestCase

from hamcrest import *

from chapter10.ex10_1_2 import left_stack_push, left_stack_pop, right_stack_push, right_stack_pop
from chapter10.ex10_1_4 import queue_empty, enqueue_, dequeue_
from chapter10.ex10_1_5 import head_enqueue, head_dequeue, tail_enqueue, tail_dequeue
from chapter10.ex10_1_6 import stack_enqueue, stack_dequeue
from test_datastructures.array_util import random_int_array


class Solutions10Test(TestCase):

    def test_left_stack_push(self):
        size = 10
        array, data = random_int_array(min_size=size, max_size=size)
        left_top_before_insert = array.left_top = random.randint(0, size)
        right_top_before_insert = array.right_top = random.randint(array.left_top + 1, size + 1)
        x = random.randint(0, 999)

        if array.left_top == array.right_top - 1:
            assert_that(calling(left_stack_push).with_args(array, x), raises(RuntimeError, 'overflow'))
        else:
            left_stack_push(array, x)

            assert_that(array.left_top, is_(equal_to(left_top_before_insert + 1)))
            assert_that(array.right_top, is_(equal_to(right_top_before_insert)))
            assert_that(array[array.left_top], is_(equal_to(x)))

    def test_left_stack_pop(self):
        size = 10
        array, data = random_int_array(min_size=size, max_size=size)
        left_top_before_delete = array.left_top = random.randint(0, size)
        right_top_before_delete = array.right_top = random.randint(array.left_top + 1, size + 1)

        if array.left_top == 0:
            assert_that(calling(left_stack_pop).with_args(array), raises(RuntimeError, 'underflow'))
        else:
            actual_deleted = left_stack_pop(array)

            assert_that(array.left_top, is_(equal_to(left_top_before_delete - 1)))
            assert_that(array.right_top, is_(equal_to(right_top_before_delete)))
            assert_that(actual_deleted, is_(equal_to(array[left_top_before_delete])))

    def test_right_stack_push(self):
        size = 10
        array, data = random_int_array(min_size=size, max_size=size)
        left_top_before_insert = array.left_top = random.randint(0, size)
        right_top_before_insert = array.right_top = random.randint(array.left_top + 1, size + 1)
        x = random.randint(0, 999)

        if array.left_top == array.right_top - 1:
            assert_that(calling(right_stack_push).with_args(array, x), raises(RuntimeError, 'overflow'))
        else:
            right_stack_push(array, x)

            assert_that(array.left_top, is_(equal_to(left_top_before_insert)))
            assert_that(array.right_top, is_(equal_to(right_top_before_insert - 1)))
            assert_that(array[array.right_top], is_(equal_to(x)))

    def test_right_stack_pop(self):
        size = 10
        array, data = random_int_array(min_size=size, max_size=size)
        left_top_before_delete = array.left_top = random.randint(0, size)
        right_top_before_delete = array.right_top = random.randint(array.left_top + 1, size + 1)

        if array.right_top == array.length + 1:
            assert_that(calling(right_stack_pop).with_args(array), raises(RuntimeError, 'underflow'))
        else:
            actual_deleted = right_stack_pop(array)

            assert_that(array.left_top, is_(equal_to(left_top_before_delete)))
            assert_that(array.right_top, is_(equal_to(right_top_before_delete + 1)))
            assert_that(actual_deleted, is_(equal_to(array[right_top_before_delete])))

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
        head_before_insert = queue.head = random.randint(1, size)
        tail_before_insert = queue.tail = random.randint(1, size)
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
        head_before_delete = queue.head = random.randint(1, size)
        tail_before_delete = queue.tail = random.randint(1, size)

        if queue.head == queue.tail:
            assert_that(calling(dequeue_).with_args(queue), raises(RuntimeError, 'underflow'))
        else:
            actual_deleted = dequeue_(queue)

            expected_head = head_before_delete + 1 if head_before_delete != queue.length else 1
            assert_that(queue.head, is_(equal_to(expected_head)))
            assert_that(queue.tail, is_(equal_to(tail_before_delete)))
            assert_that(actual_deleted, is_(equal_to(queue[head_before_delete])))

    def test_head_enqueue(self):
        size = 5
        deque, _ = random_int_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is full then make it empty
        if (deque.head == 1 and deque.tail == deque.length) or deque.head == deque.tail - 1:
            deque.tail = deque.head

        head_before_insert = deque.head
        tail_before_insert = deque.tail
        x = random.randint(0, 999)

        head_enqueue(deque, x)

        expected_head = head_before_insert - 1 if head_before_insert != 1 else deque.length
        assert_that(deque.head, is_(equal_to(expected_head)))
        assert_that(deque.tail, is_(equal_to(tail_before_insert)))
        assert_that(deque[deque.head], is_(equal_to(x)))

    def test_head_dequeue(self):
        size = 5
        deque, _ = random_int_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is empty then make it full
        if deque.head == deque.tail:
            deque.tail = deque.tail - 1 if deque.tail > 1 else deque.length

        head_before_delete = deque.head
        tail_before_delete = deque.tail

        actual_deleted = head_dequeue(deque)

        expected_head = head_before_delete + 1 if head_before_delete != deque.length else 1
        assert_that(deque.head, is_(equal_to(expected_head)))
        assert_that(deque.tail, is_(equal_to(tail_before_delete)))
        assert_that(actual_deleted, is_(equal_to(deque[head_before_delete])))

    def test_tail_enqueue(self):
        size = 5
        deque, _ = random_int_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is full then make it empty
        if (deque.head == 1 and deque.tail == deque.length) or deque.head == deque.tail - 1:
            deque.tail = deque.head

        head_before_insert = deque.head
        tail_before_insert = deque.tail
        x = random.randint(0, 999)

        tail_enqueue(deque, x)

        expected_tail = tail_before_insert + 1 if tail_before_insert != deque.length else 1
        assert_that(deque.head, is_(equal_to(head_before_insert)))
        assert_that(deque.tail, is_(equal_to(expected_tail)))
        assert_that(deque[tail_before_insert], is_(equal_to(x)))

    def test_tail_dequeue(self):
        size = 5
        deque, _ = random_int_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is empty then make it full
        if deque.head == deque.tail:
            deque.tail = deque.tail - 1 if deque.tail > 1 else deque.length

        head_before_delete = deque.head
        tail_before_delete = deque.tail

        actual_deleted = tail_dequeue(deque)

        expected_tail = tail_before_delete - 1 if tail_before_delete != 1 else deque.length
        assert_that(deque.head, is_(equal_to(head_before_delete)))
        assert_that(deque.tail, is_(equal_to(expected_tail)))
        assert_that(actual_deleted, deque[deque.tail])

    def test_stack_enqueue(self):
        size = 5
        stack, _ = random_int_array(min_size=size, max_size=size)
        top_before_insert = stack.top = random.randint(0, size - 1)
        x = random.randint(0, 999)

        stack_enqueue(stack, x)

        assert_that(stack.top, is_(equal_to(top_before_insert + 1)))
        assert_that(stack[stack.top], is_(equal_to(x)))

    def test_stack_dequeue(self):
        size = 5
        stack, data = random_int_array(min_size=size, max_size=size)
        top_before_delete = stack.top = random.randint(0, size)

        if top_before_delete == 0:
            assert_that(calling(stack_dequeue).with_args(stack), raises(RuntimeError, 'underflow'))
        else:
            actual_deleted = stack_dequeue(stack)

            assert_that(stack.top, is_(equal_to(top_before_delete - 1)))
            assert_that(actual_deleted, is_(equal_to(data[0])))
