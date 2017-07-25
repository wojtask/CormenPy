import random

from hamcrest import *

from datastructures.list import List, Node


def random_int_doubly_linked_list(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value) for _ in range(size)]
    nodes = [Node(key) for key in keys]
    L = List()
    prev_node = L.head
    for node in nodes:
        if prev_node is None:
            L.head = node
        else:
            prev_node.next = node
        node.prev = prev_node
        prev_node = node
    return L, nodes, keys


def doubly_linked_list_keys(L):
    keys = []
    node = L.head
    while node is not None:
        keys.append(node.key)
        node = node.next
    return keys


def assert_prev_next_pointers_consistent(L):
    if L.head is None:
        return

    assert_that(L.head.prev, is_(none()))
    node = L.head.next
    while node is not None:
        assert_that(node.prev.next, is_(node))
        if node.next is not None:
            assert_that(node.next.prev, is_(node))
        node = node.next


def random_int_doubly_linked_list_with_sentinel(min_size=1, max_size=20, max_value=999):
    size = random.randint(min_size, max_size)
    keys = [random.randint(0, max_value) for _ in range(size)]
    nodes = [Node(key) for key in keys]
    L = List()
    L.nil = sentinel = Node(None)
    sentinel.prev = sentinel.next = sentinel
    prev_node = sentinel
    for node in nodes:
        prev_node.next = node
        node.prev = prev_node
        node.next = sentinel
        sentinel.prev = node
        prev_node = node
    return L, nodes, keys


def doubly_linked_list_with_sentinel_keys(L):
    keys = []
    node = L.nil.next
    while node is not L.nil:
        keys.append(node.key)
        node = node.next
    return keys


def assert_prev_next_pointers_consistent_with_sentinel(L):
    assert_that(L.nil.next.prev, is_(L.nil))
    assert_that(L.nil.prev.next, is_(L.nil))
    node = L.nil.next
    while node is not L.nil:
        assert_that(node.prev.next, is_(node))
        assert_that(node.next.prev, is_(node))
        node = node.next
