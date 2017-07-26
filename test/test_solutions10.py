import random
from unittest import TestCase

from hamcrest import *

from chapter10.ex10_1_2 import left_stack_push, left_stack_pop, right_stack_push, right_stack_pop
from chapter10.ex10_1_4 import queue_empty, enqueue_, dequeue_
from chapter10.ex10_1_5 import head_enqueue, head_dequeue, tail_enqueue, tail_dequeue
from chapter10.ex10_1_6 import stack_enqueue, stack_dequeue
from chapter10.ex10_1_7 import queue_push, queue_pop
from chapter10.ex10_2_1 import singly_linked_list_insert, singly_linked_list_delete
from chapter10.ex10_2_2 import singly_linked_list_push, singly_linked_list_pop
from datastructures.list import SNode
from test_datastructures.array_util import random_int_array
from test_datastructures.list_util import random_int_singly_linked_list, linked_list_keys
from test_datastructures.queue_util import get_queue_keys, get_stack_keys


class Solutions10Test(TestCase):

    def test_left_stack_push(self):
        size = 10
        array, _ = random_int_array(min_size=size, max_size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)
        x = random.randint(0, 999)

        if array.left_top == array.right_top - 1:
            assert_that(calling(left_stack_push).with_args(array, x), raises(RuntimeError, 'overflow'))
        else:
            expected_left_keys = array[1:array.left_top].data + [x]
            expected_right_keys = array[array.right_top:array.length].data

            left_stack_push(array, x)

            actual_left_keys = array[1:array.left_top].data
            actual_right_keys = array[array.right_top:array.length].data
            assert_that(actual_left_keys, is_(equal_to(expected_left_keys)))
            assert_that(actual_right_keys, is_(equal_to(expected_right_keys)))

    def test_left_stack_pop(self):
        size = 10
        array, _ = random_int_array(min_size=size, max_size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)

        if array.left_top == 0:
            assert_that(calling(left_stack_pop).with_args(array), raises(RuntimeError, 'underflow'))
        else:
            expected_left_keys = array[1:array.left_top - 1].data
            expected_right_keys = array[array.right_top:array.length].data
            expected_deleted = array[array.left_top]

            actual_deleted = left_stack_pop(array)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))

            actual_left_keys = array[1:array.left_top].data
            actual_right_keys = array[array.right_top:array.length].data
            assert_that(actual_left_keys, is_(equal_to(expected_left_keys)))
            assert_that(actual_right_keys, is_(equal_to(expected_right_keys)))

    def test_right_stack_push(self):
        size = 10
        array, _ = random_int_array(min_size=size, max_size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)
        x = random.randint(0, 999)

        if array.left_top == array.right_top - 1:
            assert_that(calling(right_stack_push).with_args(array, x), raises(RuntimeError, 'overflow'))
        else:
            expected_left_keys = array[1:array.left_top].data
            expected_right_keys = [x] + array[array.right_top:array.length].data

            right_stack_push(array, x)

            actual_left_keys = array[1:array.left_top].data
            actual_right_keys = array[array.right_top:array.length].data
            assert_that(actual_left_keys, is_(equal_to(expected_left_keys)))
            assert_that(actual_right_keys, is_(equal_to(expected_right_keys)))

    def test_right_stack_pop(self):
        size = 10
        array, _ = random_int_array(min_size=size, max_size=size)
        array.left_top = random.randint(0, size)
        array.right_top = random.randint(array.left_top + 1, size + 1)

        if array.right_top == array.length + 1:
            assert_that(calling(right_stack_pop).with_args(array), raises(RuntimeError, 'underflow'))
        else:
            expected_left_keys = array[1:array.left_top].data
            expected_right_keys = array[array.right_top + 1:array.length].data
            expected_deleted = array[array.right_top]

            actual_deleted = right_stack_pop(array)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))

            actual_left_keys = array[1:array.left_top].data
            actual_right_keys = array[array.right_top:array.length].data
            assert_that(actual_left_keys, is_(equal_to(expected_left_keys)))
            assert_that(actual_right_keys, is_(equal_to(expected_right_keys)))

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
        x = random.randint(0, 999)

        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            assert_that(calling(enqueue_).with_args(queue, x), raises(RuntimeError, 'overflow'))
        else:
            expected_keys = get_queue_keys(queue) + [x]

            enqueue_(queue, x)

            actual_keys = get_queue_keys(queue)
            assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_dequeue_(self):
        size = 5
        queue, _ = random_int_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        if queue.head == queue.tail:
            assert_that(calling(dequeue_).with_args(queue), raises(RuntimeError, 'underflow'))
        else:
            expected_keys = get_queue_keys(queue)
            del expected_keys[0]
            expected_deleted = queue[queue.head]

            actual_deleted = dequeue_(queue)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_keys = get_queue_keys(queue)
            assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_head_enqueue(self):
        size = 5
        deque, _ = random_int_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is full then make it empty
        if (deque.head == 1 and deque.tail == deque.length) or deque.head == deque.tail + 1:
            deque.tail = deque.head

        x = random.randint(0, 999)
        expected_keys = [x] + get_queue_keys(deque)

        head_enqueue(deque, x)

        actual_keys = get_queue_keys(deque)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_head_dequeue(self):
        size = 5
        deque, _ = random_int_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is empty then make it full
        if deque.head == deque.tail:
            deque.tail = deque.tail - 1 if deque.tail > 1 else deque.length

        expected_keys = get_queue_keys(deque)
        del expected_keys[0]
        expected_deleted = deque[deque.head]

        actual_deleted = head_dequeue(deque)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_keys = get_queue_keys(deque)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_tail_enqueue(self):
        size = 5
        deque, _ = random_int_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is full then make it empty
        if (deque.head == 1 and deque.tail == deque.length) or deque.head == deque.tail + 1:
            deque.tail = deque.head

        x = random.randint(0, 999)
        expected_keys = get_queue_keys(deque) + [x]

        tail_enqueue(deque, x)

        actual_keys = get_queue_keys(deque)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_tail_dequeue(self):
        size = 5
        deque, _ = random_int_array(min_size=size, max_size=size)
        deque.head = random.randint(1, size)
        deque.tail = random.randint(1, size)

        # if deque is empty then make it full
        if deque.head == deque.tail:
            deque.tail = deque.tail - 1 if deque.tail > 1 else deque.length

        expected_keys = get_queue_keys(deque)
        del expected_keys[-1]
        expected_deleted = deque[deque.tail - 1]

        actual_deleted = tail_dequeue(deque)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_keys = get_queue_keys(deque)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_stack_enqueue(self):
        size = 5
        stack, _ = random_int_array(min_size=size, max_size=size)
        stack.top = random.randint(0, size - 1)
        x = random.randint(0, 999)
        expected_keys = get_stack_keys(stack) + [x]

        stack_enqueue(stack, x)

        actual_keys = get_stack_keys(stack)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_stack_dequeue(self):
        size = 5
        stack, _ = random_int_array(min_size=size, max_size=size)
        stack.top = random.randint(0, size)

        if stack.top == 0:
            assert_that(calling(stack_dequeue).with_args(stack), raises(RuntimeError, 'underflow'))
        else:
            expected_keys = get_stack_keys(stack)
            del expected_keys[0]
            expected_deleted = stack[1]

            actual_deleted = stack_dequeue(stack)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_keys = get_stack_keys(stack)
            assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_queue_push(self):
        size = 5
        queue, _ = random_int_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        # if queue is full then make it empty
        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            queue.tail = queue.head

        x = random.randint(0, 999)
        expected_keys = get_queue_keys(queue) + [x]

        queue_push(queue, x)

        actual_keys = get_queue_keys(queue)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_queue_pop(self):
        size = 5
        queue, _ = random_int_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        if queue.head == queue.tail:
            assert_that(calling(queue_pop).with_args(queue), raises(RuntimeError, 'underflow'))
        else:
            expected_keys = get_queue_keys(queue)
            del expected_keys[-1]
            expected_deleted = queue[queue.tail - 1]

            actual_deleted = queue_pop(queue)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_keys = get_queue_keys(queue)
            assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_insert(self):
        list_, nodes, keys = random_int_singly_linked_list()
        new_key = random.randint(0, 999)
        new_node = SNode(new_key)

        singly_linked_list_insert(list_, new_node)

        actual_keys = linked_list_keys(list_)
        expected_keys = [new_key] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_delete(self):
        list_, nodes, keys = random_int_singly_linked_list(max_size=5)
        node_idx = random.randrange(len(nodes))
        node_to_delete = nodes[node_idx]

        singly_linked_list_delete(list_, node_to_delete)

        actual_keys = linked_list_keys(list_)
        expected_keys = keys[:node_idx] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_push(self):
        list_, nodes, keys = random_int_singly_linked_list()
        x = random.randint(0, 999)

        singly_linked_list_push(list_, x)

        actual_keys = linked_list_keys(list_)
        expected_keys = [x] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_pop(self):
        list_, nodes, keys = random_int_singly_linked_list(max_size=5)

        actual_deleted = singly_linked_list_pop(list_)

        assert_that(actual_deleted, is_(equal_to(keys[0])))
        actual_keys = linked_list_keys(list_)
        expected_keys = keys[1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))
