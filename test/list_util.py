import random

from hamcrest import *

from array_util import get_random_array
from datastructures.array import Array
from datastructures.list import List, SinglyLinkedNode, DoublyLinkedNode, XORNode, XORList, ListWithSentinel


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
