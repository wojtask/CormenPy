import random
from unittest import TestCase

from hamcrest import *

from chapter10.textbook import stack_empty, push, pop, enqueue, dequeue, list_search, list_insert, list_delete, \
    list_delete_, list_search_, list_insert_
from datastructures.list import Node
from test_datastructures.array_util import random_int_array
from test_datastructures.list_util import random_int_doubly_linked_list, doubly_linked_list_keys, \
    random_int_doubly_linked_list_with_sentinel, doubly_linked_list_with_sentinel_keys, \
    assert_prev_next_pointers_consistent, assert_prev_next_pointers_consistent_with_sentinel


class Textbook10Test(TestCase):

    def test_stack_empty(self):
        stack, _ = random_int_array(min_size=3, max_size=3)
        stack.top = random.randint(0, 3)

        actual_empty = stack_empty(stack)

        if stack.top == 0:
            assert_that(actual_empty, is_(True))
        else:
            assert_that(actual_empty, is_(False))

    def test_push(self):
        stack, _ = random_int_array(min_size=10, max_size=10)
        top_before_insert = stack.top = random.randint(0, 9)
        x = random.randint(0, 999)

        push(stack, x)

        assert_that(stack.top, is_(equal_to(top_before_insert + 1)))
        assert_that(stack[stack.top], is_(equal_to(x)))

    def test_pop(self):
        stack, _ = random_int_array(min_size=10, max_size=10)
        top_before_delete = stack.top = random.randint(0, 10)

        if top_before_delete == 0:
            assert_that(calling(pop).with_args(stack), raises(RuntimeError, 'underflow'))
        else:
            actual_deleted = pop(stack)

            expected_deleted = stack[top_before_delete]
            assert_that(stack.top, is_(equal_to(top_before_delete - 1)))
            assert_that(actual_deleted, is_(equal_to(expected_deleted)))

    def test_enqueue(self):
        queue, _ = random_int_array(min_size=10, max_size=10)
        queue.head = random.randint(1, 10)
        queue.tail = random.randint(1, 10)

        # if Q is full then make it empty
        if (queue.head == 1 and queue.tail == queue.length) or queue.head == queue.tail - 1:
            queue.tail = queue.head

        head_before_insert = queue.head
        tail_before_insert = queue.tail
        x = random.randint(0, 999)

        enqueue(queue, x)

        expected_tail = tail_before_insert + 1 if tail_before_insert != queue.length else 1
        assert_that(queue.head, is_(equal_to(head_before_insert)))
        assert_that(queue.tail, is_(equal_to(expected_tail)))
        assert_that(queue[tail_before_insert], is_(equal_to(x)))

    def test_dequeue(self):
        queue, _ = random_int_array(min_size=10, max_size=10)
        queue.head = random.randint(1, 10)
        queue.tail = random.randint(1, 10)

        # if Q is empty then make it full
        if queue.head == queue.tail:
            queue.tail = queue.tail - 1 if queue.tail > 1 else queue.length

        head_before_delete = queue.head
        tail_before_delete = queue.tail

        actual_deleted = dequeue(queue)

        expected_head = head_before_delete + 1 if head_before_delete != queue.length else 1
        assert_that(queue.head, is_(equal_to(expected_head)))
        assert_that(queue.tail, is_(equal_to(tail_before_delete)))
        assert_that(actual_deleted, is_(equal_to(queue[head_before_delete])))

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

        actual_keys = doubly_linked_list_keys(list_)
        expected_keys = [new_key] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent(list_)

    def test_list_delete(self):
        list_, nodes, keys = random_int_doubly_linked_list(max_size=5)
        node_to_delete = random.choice(nodes)

        list_delete(list_, node_to_delete)

        actual_keys = doubly_linked_list_keys(list_)
        expected_keys = keys
        expected_keys.remove(node_to_delete.key)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_prev_next_pointers_consistent(list_)

    def test_list_delete_(self):
        list_, nodes, keys = random_int_doubly_linked_list_with_sentinel(max_size=5)
        node_to_delete = random.choice(nodes)

        list_delete_(list_, node_to_delete)

        actual_keys = doubly_linked_list_with_sentinel_keys(list_)
        expected_keys = keys
        expected_keys.remove(node_to_delete.key)
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
