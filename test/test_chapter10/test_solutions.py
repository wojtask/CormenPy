import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter10.ex10_1_2 import left_stack_push, left_stack_pop, right_stack_push, right_stack_pop
from chapter10.ex10_1_4 import queue_empty, enqueue_, dequeue_
from chapter10.ex10_1_5 import head_enqueue, head_dequeue, tail_enqueue, tail_dequeue
from chapter10.ex10_1_6 import stack_enqueue, stack_dequeue
from chapter10.ex10_1_7 import queue_push, queue_pop
from chapter10.ex10_2_1 import singly_linked_list_insert, singly_linked_list_delete
from chapter10.ex10_2_2 import singly_linked_list_push, singly_linked_list_pop
from chapter10.ex10_2_3 import singly_linked_list_enqueue, singly_linked_list_dequeue
from chapter10.ex10_2_5 import circular_list_insert, circular_list_delete, circular_list_search
from chapter10.ex10_2_6 import circular_lists_union
from chapter10.ex10_2_7 import singly_linked_list_reverse
from chapter10.ex10_2_8 import xor_linked_list_search, xor_linked_list_insert, xor_linked_list_delete, \
    xor_linked_list_reverse
from chapter10.ex10_3_2 import single_array_allocate_object, single_array_free_object
from chapter10.ex10_4_3 import iterative_preorder_tree_walk
from chapter10.ex10_4_4 import tree_walk
from chapter10.ex10_4_5 import stackless_inorder_tree_walk
from datastructures.binary_tree import RootedTree
from datastructures.list import SNode, XorNode
from datastructures.rooted_tree import Node
from test_datastructures.array_util import random_int_array
from test_datastructures.list_util import random_int_singly_linked_list, linked_list_keys, random_int_circular_list, \
    circular_list_keys, random_int_xor_linked_list, xor_linked_list_keys, random_single_array_list, \
    single_array_list_keys, single_array_list_free_cells, assert_single_array_list_consistent
from test_datastructures.queue_util import get_queue_keys, get_stack_keys
from test_datastructures.tree_util import random_binary_search_tree, binary_tree_to_list


def _get_rooted_tree():
    nodes = [Node(key) for key in range(7)]
    nodes[0].left_child = nodes[1]
    nodes[1].right_sibling = nodes[2]
    nodes[2].right_sibling = nodes[3]
    nodes[1].left_child = nodes[4]
    nodes[3].left_child = nodes[5]
    nodes[5].right_sibling = nodes[6]
    return RootedTree(nodes[0])


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

    def test_singly_linked_list_enqueue(self):
        list_, nodes, keys = random_int_singly_linked_list()
        list_.tail = nodes[-1]
        x = random.randint(0, 999)

        singly_linked_list_enqueue(list_, x)

        actual_keys = linked_list_keys(list_)
        expected_keys = keys + [x]
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_dequeue(self):
        list_, nodes, keys = random_int_singly_linked_list(min_size=0, max_size=5)

        if list_.head is None:
            list_.tail = None
            assert_that(calling(singly_linked_list_dequeue).with_args(list_), raises(RuntimeError, 'underflow'))
        else:
            list_.tail = nodes[-1]

            actual_deleted = singly_linked_list_dequeue(list_)

            assert_that(actual_deleted, is_(equal_to(keys[0])))
            actual_keys = linked_list_keys(list_)
            expected_keys = keys[1:]
            assert_that(actual_keys, is_(equal_to(expected_keys)))
            if list_.head is None:
                assert_that(list_.tail, is_(none()))

    def test_circular_list_insert(self):
        list_, nodes, keys = random_int_circular_list(min_size=0, max_size=5)
        new_key = random.randint(0, 999)
        new_node = SNode(new_key)

        circular_list_insert(list_, new_node)

        actual_keys = circular_list_keys(list_)
        if nodes:
            expected_keys = [keys[0]] + [new_key] + keys[1:]
        else:
            expected_keys = [new_key]
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_circular_list_delete(self):
        list_, nodes, keys = random_int_circular_list(min_size=1, max_size=5)
        node_idx = random.randrange(len(nodes))
        node_to_delete = nodes[node_idx]

        circular_list_delete(list_, node_to_delete)

        actual_keys = circular_list_keys(list_)
        expected_keys = keys[:node_idx] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_circular_list_search(self):
        list_, nodes, keys = random_int_circular_list(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = circular_list_search(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))

    def test_circular_lists_union(self):
        list1, _, keys1 = random_int_circular_list()
        list2, _, keys2 = random_int_circular_list()

        actual_union = circular_lists_union(list1, list2)

        actual_keys = circular_list_keys(actual_union)
        expected_keys = keys1 + keys2
        assert_that(actual_keys, contains_inanyorder(*expected_keys))

    def test_singly_linked_list_reverse(self):
        list_, nodes, keys = random_int_singly_linked_list()

        singly_linked_list_reverse(list_)

        actual_keys = linked_list_keys(list_)
        expected_keys = list(reversed(keys))
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_xor_linked_list_search(self):
        list_, nodes, keys = random_int_xor_linked_list(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = xor_linked_list_search(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(none()))

    def test_xor_linked_list_insert(self):
        list_, nodes, keys = random_int_xor_linked_list(min_size=0, max_size=5)
        new_key = random.randint(0, 999)
        new_node = XorNode(new_key, list_)

        xor_linked_list_insert(list_, new_node)

        actual_keys = xor_linked_list_keys(list_)
        expected_keys = [new_key] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_xor_linked_list_delete(self):
        list_, nodes, keys = random_int_xor_linked_list(min_size=1, max_size=5)
        node_idx = random.randrange(len(nodes))
        node_to_delete = nodes[node_idx]

        xor_linked_list_delete(list_, node_to_delete)

        actual_keys = xor_linked_list_keys(list_)
        expected_keys = keys[:node_idx] + keys[node_idx + 1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_xor_linked_list_reverse(self):
        list_, nodes, keys = random_int_xor_linked_list(min_size=0, max_size=5)

        xor_linked_list_reverse(list_)

        actual_keys = xor_linked_list_keys(list_)
        expected_keys = list(reversed(keys))
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_single_array_allocate_object(self):
        list_ = random_single_array_list()

        if list_.free is None:
            assert_that(calling(single_array_allocate_object).with_args(list_), raises(RuntimeError, 'out of space'))
        else:
            expected_free = list_.free
            expected_keys = single_array_list_keys(list_)
            expected_free_cells = single_array_list_free_cells(list_) - 1

            actual_allocated = single_array_allocate_object(list_)

            assert_that(actual_allocated, is_(equal_to(expected_free)))
            assert_single_array_list_consistent(list_)
            actual_keys = single_array_list_keys(list_)
            assert_that(actual_keys, is_(equal_to(expected_keys)))
            actual_free_cells = single_array_list_free_cells(list_)
            assert_that(actual_free_cells, is_(equal_to(expected_free_cells)))

    def test_single_array_free_object(self):
        list_ = random_single_array_list()

        # the list is nonempty so let's delete the head element and prepare it for freeing
        cell_to_free = list_.head
        if list_.A[list_.head + 1] is not None:
            list_.A[list_.A[list_.head + 1] + 2] = None
        list_.head = list_.A[list_.head + 1]

        expected_keys = single_array_list_keys(list_)
        expected_free_cells = single_array_list_free_cells(list_) + 1

        single_array_free_object(list_, cell_to_free)

        assert_that(list_.free, is_(equal_to(cell_to_free)))
        assert_single_array_list_consistent(list_)
        actual_keys = single_array_list_keys(list_)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        actual_free_cells = single_array_list_free_cells(list_)
        assert_that(actual_free_cells, is_(equal_to(expected_free_cells)))


    def test_iterative_preorder_tree_walk(self):
        tree, _, _ = random_binary_search_tree()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            iterative_preorder_tree_walk(tree)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        expected_output = binary_tree_to_list(tree)
        assert_that(actual_output, is_(equal_to(expected_output)))

    def test_tree_walk(self):
        tree = _get_rooted_tree()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            tree_walk(tree.root)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        expected_output = [0, 1, 4, 2, 3, 5, 6]
        assert_that(actual_output, is_(equal_to(expected_output)))

    def test_stackless_inorder_tree_walk(self):
        tree, _, keys = random_binary_search_tree()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            stackless_inorder_tree_walk(tree)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        expected_output = sorted(keys)
        assert_that(actual_output, is_(equal_to(expected_output)))
