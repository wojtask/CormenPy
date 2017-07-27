import random
from unittest import TestCase

from hamcrest import *

from chapter10.textbook import stack_empty, push, pop, enqueue, dequeue, list_search, list_insert, list_delete, \
    list_delete_, list_search_, list_insert_
from datastructures.list import Node
from test_datastructures.array_util import random_int_array
from test_datastructures.list_util import random_int_doubly_linked_list, linked_list_keys, \
    random_int_doubly_linked_list_with_sentinel, doubly_linked_list_with_sentinel_keys, \
    assert_prev_next_pointers_consistent, assert_prev_next_pointers_consistent_with_sentinel
from test_datastructures.queue_util import get_stack_keys, get_queue_keys


class Textbook10Test(TestCase):

    def test_stack_empty(self):
        size = 3
        stack, _ = random_int_array(min_size=size, max_size=size)
        stack.top = random.randint(0, size)

        actual_empty = stack_empty(stack)

        if stack.top == 0:
            assert_that(actual_empty, is_(True))
        else:
            assert_that(actual_empty, is_(False))

    def test_push(self):
        size = 10
        stack, _ = random_int_array(min_size=size, max_size=size)
        stack.top = random.randint(0, size - 1)
        x = random.randint(0, 999)
        expected_keys = get_stack_keys(stack) + [x]

        push(stack, x)

        actual_keys = get_stack_keys(stack)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_pop(self):
        size = 10
        stack, _ = random_int_array(min_size=size, max_size=size)
        stack.top = random.randint(0, size)

        if stack.top == 0:
            assert_that(calling(pop).with_args(stack), raises(RuntimeError, 'underflow'))
        else:
            expected_keys = get_stack_keys(stack)
            del expected_keys[-1]
            expected_deleted = stack[stack.top]

            actual_deleted = pop(stack)

            assert_that(actual_deleted, is_(equal_to(expected_deleted)))
            actual_keys = get_stack_keys(stack)
            assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_enqueue(self):
        size = 10
        queue, _ = random_int_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        # if queue is full then make it empty
        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail + 1:
            queue.tail = queue.head

        x = random.randint(0, 999)
        expected_keys = get_queue_keys(queue) + [x]

        enqueue(queue, x)

        actual_keys = get_queue_keys(queue)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_dequeue(self):
        size = 10
        queue, _ = random_int_array(min_size=size, max_size=size)
        queue.head = random.randint(1, size)
        queue.tail = random.randint(1, size)

        # if queue is empty then make it full
        if queue.head == queue.tail:
            queue.tail = queue.tail - 1 if queue.tail > 1 else queue.length

        expected_keys = get_queue_keys(queue)
        del expected_keys[0]
        expected_deleted = queue[queue.head]

        actual_deleted = dequeue(queue)

        assert_that(actual_deleted, is_(equal_to(expected_deleted)))
        actual_keys = get_queue_keys(queue)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_list_search(self):
        list_, nodes, keys = random_int_doubly_linked_list(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = list_search(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))

    def test_list_insert(self):
        list_, nodes, keys = random_int_doubly_linked_list()
        new_key = random.randint(0, 999)
        new_node = Node(new_key)

        list_insert(list_, new_node)

        actual_keys = linked_list_keys(list_)
        expected_keys = [new_key] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent(list_)

    def test_list_delete(self):
        list_, nodes, keys = random_int_doubly_linked_list(max_size=5)
        node_idx = random.randrange(len(nodes))
        node_to_delete = nodes[node_idx]

        list_delete(list_, node_to_delete)

        actual_keys = linked_list_keys(list_)
        expected_keys = keys[:node_idx] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent(list_)

    def test_list_delete_(self):
        list_, nodes, keys = random_int_doubly_linked_list_with_sentinel(max_size=5)
        node_idx = random.randrange(len(nodes))
        node_to_delete = nodes[node_idx]

        list_delete_(list_, node_to_delete)

        actual_keys = doubly_linked_list_with_sentinel_keys(list_)
        expected_keys = keys[:node_idx] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent_with_sentinel(list_)

    def test_list_search_(self):
        list_, nodes, keys = random_int_doubly_linked_list_with_sentinel(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = list_search_(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(list_.nil))

    def test_list_insert_(self):
        list_, nodes, keys = random_int_doubly_linked_list_with_sentinel()
        new_key = random.randint(0, 999)
        new_node = Node(new_key)

        list_insert_(list_, new_node)

        actual_keys = doubly_linked_list_with_sentinel_keys(list_)
        expected_keys = [new_key] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent_with_sentinel(list_)
