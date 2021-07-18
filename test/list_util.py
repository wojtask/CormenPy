import random

from hamcrest import *

from array_util import get_random_array
from datastructures.array import Array
from datastructures.array_list import MultipleArrayList, SingleArrayList
from datastructures.list import List, Node, SNode, XORNode, XORList
from util import between


def get_random_doubly_linked_list(min_size=1, max_size=20, max_value=999):
    keys = get_random_array(min_size=min_size, max_size=max_size, min_value=0, max_value=max_value)
    nodes = Array(Node(key) for key in keys)
    list_ = List()
    prev_node = list_.head
    for node in nodes:
        if prev_node is None:
            list_.head = node
        else:
            prev_node.next = node
        node.prev = prev_node
        prev_node = node
    return list_, nodes, keys


def get_linked_list_keys(list_):
    keys = []
    node = list_.head
    while node is not None:
        keys.append(node.key)
        node = node.next
    return Array(keys)


def assert_prev_next_pointers_consistent(list_):
    if list_.head is None:
        return

    assert_that(list_.head.prev, is_(none()))
    node = list_.head.next
    while node is not None:
        assert_that(node.prev.next, is_(node))
        if node.next is not None:
            assert_that(node.next.prev, is_(node))
        node = node.next


def get_random_doubly_linked_list_with_sentinel(min_size=1, max_size=20, max_value=999):
    keys = get_random_array(min_size=min_size, max_size=max_size, min_value=0, max_value=max_value)
    nodes = Array(Node(key) for key in keys)
    list_ = List()
    list_.nil = sentinel = Node(None)
    sentinel.prev = sentinel.next = sentinel
    prev_node = sentinel
    for node in nodes:
        prev_node.next = node
        node.prev = prev_node
        node.next = sentinel
        sentinel.prev = node
        prev_node = node
    return list_, nodes, keys


def get_doubly_linked_list_with_sentinel_keys(list_):
    keys = Array()
    node = list_.nil.next
    while node is not list_.nil:
        keys.append(node.key)
        node = node.next
    return keys


def assert_prev_next_pointers_consistent_with_sentinel(list_):
    assert_that(list_.nil.next.prev, is_(list_.nil))
    assert_that(list_.nil.prev.next, is_(list_.nil))
    node = list_.nil.next
    while node is not list_.nil:
        assert_that(node.prev.next, is_(node))
        assert_that(node.next.prev, is_(node))
        node = node.next


def get_random_singly_linked_list(min_size=1, max_size=20, max_value=999):
    keys = get_random_array(min_size=min_size, max_size=max_size, min_value=0, max_value=max_value)
    nodes = Array(SNode(key) for key in keys)
    list_ = List()
    prev_node = list_.head
    for node in nodes:
        if prev_node is None:
            list_.head = node
        else:
            prev_node.next = node
        prev_node = node
    return list_, nodes, keys


def get_random_circular_list(min_size=1, max_size=20, max_value=999):
    list_, nodes, keys = get_random_singly_linked_list(min_size, max_size, max_value)
    if list_.head is not None:
        nodes[nodes.length].next = list_.head
    return list_, nodes, keys


def get_circular_list_keys(list_):
    if list_.head is None:
        return Array()
    keys = [list_.head.key]
    node = list_.head.next
    while node is not list_.head:
        keys.append(node.key)
        node = node.next
    return Array(keys)


def get_random_xor_linked_list(min_size=1, max_size=20, max_value=999):
    list_ = XORList()
    size = random.randint(min_size, max_size)
    if size == 0:
        return list_, Array(), Array()

    keys = get_random_array(min_size=size, max_size=size, min_value=0, max_value=max_value)
    nodes = Array(XORNode(key, list_) for key in keys)

    prev_node = None
    curr_node = nodes[1]
    for next_node in nodes[2:]:
        curr_node.np = (id(prev_node) if prev_node is not None else 0) ^ id(next_node)
        next_node.np = id(curr_node)
        prev_node = curr_node
        curr_node = next_node
    list_.head = nodes[1]
    list_.tail = nodes[nodes.length]

    return list_, nodes, keys


def get_xor_linked_list_keys(list_):
    keys = []
    prev_node = None
    curr_node = list_.head
    while curr_node is not None:
        keys.append(curr_node.key)
        next_node_addr = curr_node.np ^ (id(prev_node) if prev_node is not None else 0)
        next_node = list_.addr_to_node[next_node_addr]
        prev_node = curr_node
        curr_node = next_node
    return Array(keys)


def get_random_multiple_array_list(min_size=1, max_size=10, max_value=999):
    list_size = random.randint(min_size, max_size)
    array_size = random.randint(list_size, max_size)
    key, next, prev = Array.indexed(1, array_size), Array.indexed(1, array_size), Array.indexed(1, array_size)
    list_indexes = random.sample(between(1, array_size), list_size)

    head = None
    prev_index = None
    for index in list_indexes:
        key[index] = random.randint(0, max_value)
        if prev_index is None:
            head = index
        else:
            next[prev_index] = index
            prev[index] = prev_index
        prev_index = index

    free_indexes = [i for i in between(1, array_size) if i not in list_indexes]
    random.shuffle(free_indexes)

    free = None
    prev_free_index = None
    for free_index in free_indexes:
        if prev_free_index is None:
            free = free_index
        else:
            next[prev_free_index] = free_index
        prev_free_index = free_index

    return MultipleArrayList(key, next, prev, head, free)


def get_multiple_array_list_keys(list_):
    idx = list_.head
    keys = []
    while idx is not None:
        keys.append(list_.key[idx])
        idx = list_.next[idx]
    return keys


def get_multiple_array_list_free_cells(list_):
    idx = list_.free
    free_cells = 0
    while idx is not None:
        free_cells += 1
        idx = list_.next[idx]
    return free_cells


def assert_multiple_array_list_consistent(list_):
    prev_idx = None
    idx = list_.head
    while idx is not None:
        assert_that(list_.prev[idx] == prev_idx)
        prev_idx = idx
        idx = list_.next[idx]


def get_random_single_array_list(min_size=1, max_size=10, max_value=999):
    list_size = random.randint(min_size, max_size)
    array_size = 3 * random.randint(list_size, max_size)
    A = Array.indexed(1, array_size)
    list_indexes = random.sample(range(1, array_size + 1, 3), list_size)

    head = None
    prev_index = None
    for index in list_indexes:
        A[index] = random.randint(0, max_value)
        if prev_index is None:
            head = index
        else:
            A[prev_index + 1] = index
            A[index + 2] = prev_index
        prev_index = index

    free_indexes = [i for i in range(1, array_size + 1, 3) if i not in list_indexes]
    random.shuffle(free_indexes)

    free = None
    prev_free_index = None
    for free_index in free_indexes:
        if prev_free_index is None:
            free = free_index
        else:
            A[prev_free_index + 1] = free_index
        prev_free_index = free_index

    return SingleArrayList(A, head, free)


def get_single_array_list_keys(list_):
    idx = list_.head
    keys = []
    while idx is not None:
        keys.append(list_.A[idx])
        idx = list_.A[idx + 1]
    return Array(keys)


def get_single_array_list_free_cells(list_):
    idx = list_.free
    free_cells = 0
    while idx is not None:
        free_cells += 1
        idx = list_.A[idx + 1]
    return free_cells


def assert_single_array_list_consistent(list_):
    prev_idx = None
    idx = list_.head
    while idx is not None:
        assert_that(list_.A[idx + 2] == prev_idx)
        prev_idx = idx
        idx = list_.A[idx + 1]


def get_random_compact_list(min_size=1, max_size=10, max_value=999):
    list_size = random.randint(min_size, max_size)
    array_size = random.randint(list_size, max_size)
    key, next, prev = Array.indexed(1, array_size), Array.indexed(1, array_size), Array.indexed(1, array_size)
    list_indexes = random.sample(between(1, list_size), list_size)

    head = None
    prev_index = None
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


def assert_compact_list(list_):
    idx = list_.head
    nelements = 0
    max_idx = 0
    while idx is not None:
        nelements += 1
        max_idx = max(max_idx, idx)
        idx = list_.next[idx]
    assert_that(max_idx, is_(equal_to(nelements)))
