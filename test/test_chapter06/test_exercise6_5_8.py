import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.exercise6_5_8 import merge_sorted_lists
from datastructures.array import Array
from datastructures.list import SinglyLinkedNode, List
from util import between


def get_random_sorted_singly_linked_list():
    size = random.randint(1, 5)
    keys = get_random_array(size=size).sort()
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


class TestExercise6_5_8(TestCase):

    def test_merge_sorted_lists(self):
        size = random.randint(1, 10)
        lists = Array(get_random_sorted_singly_linked_list() for _ in between(1, size))
        expected_list_keys = Array(linked_list.as_keys_array() for linked_list in lists)
        expected_elements = Array(key for list_keys in expected_list_keys for key in list_keys).sort()

        actual_merged = merge_sorted_lists(lists)

        actual_elements = actual_merged.as_keys_array()
        assert_that(actual_elements, is_(equal_to(expected_elements)))
