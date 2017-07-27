import random

from hamcrest import *

from datastructures.list import List, Node, SNode, XorNode, XorList


def random_int_doubly_linked_list(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value) for _ in range(size)]
    nodes = [Node(key) for key in keys]
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


def linked_list_keys(list_):
    keys = []
    node = list_.head
    while node is not None:
        keys.append(node.key)
        node = node.next
    return keys


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


def random_int_doubly_linked_list_with_sentinel(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value) for _ in range(size)]
    nodes = [Node(key) for key in keys]
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


def doubly_linked_list_with_sentinel_keys(list_):
    keys = []
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


def random_int_singly_linked_list(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value) for _ in range(size)]
    nodes = [SNode(key) for key in keys]
    list_ = List()
    prev_node = list_.head
    for node in nodes:
        if prev_node is None:
            list_.head = node
        else:
            prev_node.next = node
        prev_node = node
    return list_, nodes, keys


def random_int_circular_list(min_size=1, max_size=20, max_value=999):
    list_, nodes, keys = random_int_singly_linked_list(min_size, max_size, max_value)
    if list_.head is not None:
        nodes[-1].next = list_.head
    return list_, nodes, keys


def circular_list_keys(list_):
    if list_.head is None:
        return []
    keys = [list_.head.key]
    node = list_.head.next
    while node is not list_.head:
        keys.append(node.key)
        node = node.next
    return keys


def random_int_xor_linked_list(min_size=1, max_size=20, max_value=999):
    list_ = XorList()
    size = random.randint(min_size, max_size)
    if size == 0:
        return list_, [], []

    keys = [random.randint(0, max_value) for _ in range(size)]
    nodes = [XorNode(key, list_) for key in keys]

    prev_node = None
    curr_node = nodes[0]
    for next_node in nodes[1:]:
        curr_node.np = (id(prev_node) if prev_node is not None else 0) ^ id(next_node)
        next_node.np = id(curr_node)
        prev_node = curr_node
        curr_node = next_node
    list_.head = nodes[0]
    list_.tail = nodes[-1]

    return list_, nodes, keys


def xor_linked_list_keys(list_):
    keys = []
    prev_node = None
    curr_node = list_.head
    while curr_node is not None:
        keys.append(curr_node.key)
        next_node_addr = curr_node.np ^ (id(prev_node) if prev_node is not None else 0)
        next_node = list_.addr_to_node[next_node_addr]
        prev_node = curr_node
        curr_node = next_node
    return keys
