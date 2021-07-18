import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.exercise6_5_8 import merge_sorted_lists
from datastructures.array import Array
from datastructures.list import SNode, List
from list_util import get_linked_list_keys
from util import between


def get_random_sorted_singly_linked_list():
    size = random.randint(1, 5)
    keys = get_random_array(size=size).sort()
    nodes = [SNode(key) for key in keys]
    list_ = List()
    prev_node = list_.head
    for node in nodes:
        if prev_node is None:
            list_.head = node
        else:
            prev_node.next = node
        prev_node = node
    return list_


class TestExercise6_5_8(TestCase):

    def test_merge_sorted_lists(self):
        size = random.randint(1, 10)
        lists = Array(get_random_sorted_singly_linked_list() for _ in between(1, size))
        expected_list_keys = Array(get_linked_list_keys(list_) for list_ in lists)
        expected_elements = Array(key for list_keys in expected_list_keys for key in list_keys).sort()

        actual_merged = merge_sorted_lists(lists)

        actual_elements = get_linked_list_keys(actual_merged)
        assert_that(actual_elements, is_(equal_to(expected_elements)))
