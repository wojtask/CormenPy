import random

from hamcrest import *

from array_util import get_random_array
from datastructures.array import Array
from datastructures.array_list import MultipleArrayList, SingleArrayList
from datastructures.list import List, SinglyLinkedNode, DoublyLinkedNode, XORNode, XORList, ListWithSentinel
from util import between


def get_random_singly_linked_list(min_size=1, max_size=20, max_value=999):
    keys = get_random_array(min_size=min_size, max_size=max_size, min_value=0, max_value=max_value)
    nodes = Array(SinglyLinkedNode(key) for key in keys)
    linked_list = List()
    prev_node = linked_list.head
    for node in nodes:
        if prev_node is None:
            linked_list.head = node
        else:
            prev_node.next = node
        prev_node = node
    return linked_list


def get_random_doubly_linked_list(min_size=1, max_size=20, max_value=999):
    keys = get_random_array(min_size=min_size, max_size=max_size, min_value=0, max_value=max_value)
    nodes = Array(DoublyLinkedNode(key) for key in keys)
    linked_list = List()
    prev_node = linked_list.head
    for node in nodes:
        if prev_node is None:
            linked_list.head = node
        else:
            prev_node.next = node
        node.prev = prev_node
        prev_node = node
    return linked_list


def get_random_doubly_linked_list_with_sentinel(min_size=1, max_size=20, max_value=999):
    keys = get_random_array(min_size=min_size, max_size=max_size, min_value=0, max_value=max_value)
    nodes = Array(DoublyLinkedNode(key) for key in keys)
    linked_list = ListWithSentinel()
    prev_node = linked_list.nil
    for node in nodes:
        prev_node.next = node
        node.prev = prev_node
        node.next = linked_list.nil
        linked_list.nil.prev = node
        prev_node = node
    return linked_list


def get_random_circular_singly_linked_list(min_size=1, max_size=20, max_value=999):
    linked_list = get_random_singly_linked_list(min_size=min_size, max_size=max_size, max_value=max_value)
    if linked_list.head is not None:
        prev_node = linked_list.head
        while prev_node.next is not None:
            prev_node = prev_node.next
        prev_node.next = linked_list.head
    return linked_list


def assert_doubly_linked_list_structure_consistent(linked_list):
    if linked_list.head is None:
        return

    assert_that(linked_list.head.prev, is_(any_of(none(), linked_list.head)))
    node = linked_list.head.next
    while node is not None and node is not linked_list.head:
        assert_that(node.prev.next, is_(node))
        if node.next is not None:
            assert_that(node.next.prev, is_(node))
        node = node.next


def assert_doubly_linked_list_with_sentinel_structure_consistent(linked_list):
    assert_that(linked_list.nil.next.prev, is_(linked_list.nil))
    assert_that(linked_list.nil.prev.next, is_(linked_list.nil))
    node = linked_list.nil.next
    while node is not linked_list.nil:
        assert_that(node.prev.next, is_(node))
        assert_that(node.next.prev, is_(node))
        node = node.next


def get_random_xor_linked_list(min_size=1, max_size=20, max_value=999):
    linked_list = XORList()
    size = random.randint(min_size, max_size)
    if size == 0:
        return linked_list

    keys = get_random_array(size=size, min_value=0, max_value=max_value)
    nodes = Array(XORNode(key, linked_list) for key in keys)

    prev_node = None
    curr_node = nodes[1]
    for next_node in nodes[2:]:
        curr_node.np = (id(prev_node) if prev_node is not None else 0) ^ id(next_node)
        next_node.np = id(curr_node)
        prev_node = curr_node
        curr_node = next_node
    linked_list.head = nodes[1]
    linked_list.tail = nodes[nodes.length]

    return linked_list


def get_random_multiple_array_list(min_size=1, max_size=10, max_value=999):
    list_size = random.randint(min_size, max_size)
    array_size = random.randint(list_size, max_size)
    key, next, prev = Array.indexed(1, array_size), Array.indexed(1, array_size), Array.indexed(1, array_size)
    list_indexes = random.sample(between(1, array_size), list_size)

    head = prev_index = None
    for index in list_indexes:
        key[index] = random.randint(0, max_value)
        if prev_index is None:
            head = index
        else:
            next[prev_index] = index
            prev[index] = prev_index
        prev_index = index

    free_indexes = Array(i for i in between(1, array_size) if i not in list_indexes).shuffle()

    free = prev_free_index = None
    for free_index in free_indexes:
        if prev_free_index is None:
            free = free_index
        else:
            next[prev_free_index] = free_index
        prev_free_index = free_index

    return MultipleArrayList(key, next, prev, head, free)


def get_multiple_array_list_keys(array_list):
    idx = array_list.head
    keys = Array()
    while idx is not None:
        keys.append(array_list.key[idx])
        idx = array_list.next[idx]
    return keys


def get_multiple_array_list_free_cells(array_list):
    idx = array_list.free
    free_cells = 0
    while idx is not None:
        free_cells += 1
        idx = array_list.next[idx]
    return free_cells


def assert_multiple_array_list_consistent(array_list):
    prev_idx = None
    idx = array_list.head
    while idx is not None:
        assert_that(array_list.prev[idx] == prev_idx)
        prev_idx = idx
        idx = array_list.next[idx]


def get_random_single_array_list(min_size=1, max_size=10, max_value=999):
    list_size = random.randint(min_size, max_size)
    array_size = 3 * random.randint(list_size, max_size)
    A = Array.indexed(1, array_size)
    list_indexes = random.sample(between(1, array_size, step=3), list_size)

    head = prev_index = None
    for index in list_indexes:
        A[index] = random.randint(0, max_value)
        if prev_index is None:
            head = index
        else:
            A[prev_index + 1] = index
            A[index + 2] = prev_index
        prev_index = index

    free_indexes = Array(i for i in between(1, array_size, step=3) if i not in list_indexes).shuffle()

    free = prev_free_index = None
    for free_index in free_indexes:
        if prev_free_index is None:
            free = free_index
        else:
            A[prev_free_index + 1] = free_index
        prev_free_index = free_index

    return SingleArrayList(A, head, free)


def get_single_array_list_keys(array_list):
    idx = array_list.head
    keys = Array()
    while idx is not None:
        keys.append(array_list.A[idx])
        idx = array_list.A[idx + 1]
    return keys


def get_single_array_list_free_cells(array_list):
    idx = array_list.free
    free_cells = 0
    while idx is not None:
        free_cells += 1
        idx = array_list.A[idx + 1]
    return free_cells


def assert_single_array_list_consistent(array_list):
    prev_idx = None
    idx = array_list.head
    while idx is not None:
        assert_that(array_list.A[idx + 2] == prev_idx)
        prev_idx = idx
        idx = array_list.A[idx + 1]


def get_random_compact_list(min_size=1, max_size=10, max_value=999):
    list_size = random.randint(min_size, max_size)
    array_size = random.randint(list_size, max_size)
    key, next, prev = Array.indexed(1, array_size), Array.indexed(1, array_size), Array.indexed(1, array_size)
    list_indexes = random.sample(between(1, list_size), list_size)

    head = prev_index = None
    for index in list_indexes:
        key[index] = random.randint(0, max_value)
        if prev_index is None:
            head = index
        else:
            next[prev_index] = index
            prev[index] = prev_index
        prev_index = index

    free = list_size + 1 if list_size < array_size else None
    for free_index in between(list_size + 2, array_size):
        next[free_index - 1] = free_index

    return MultipleArrayList(key, next, prev, head, free)


def assert_compact_list(compact_list):
    idx = compact_list.head
    nelements = 0
    max_idx = 0
    while idx is not None:
        nelements += 1
        max_idx = max(max_idx, idx)
        idx = compact_list.next[idx]
    assert_that(max_idx, is_(equal_to(nelements)))
