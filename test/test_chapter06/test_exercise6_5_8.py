import random
from unittest import TestCase

from hamcrest import *

from chapter06.exercise6_5_8 import merge_sorted_lists
from datastructures.array import Array
from datastructures.list import SNode, List
from list_util import get_linked_list_keys


def get_random_sorted_singly_linked_list():
    size = random.randint(1, 5)
    keys = sorted([random.randint(0, 999) for _ in range(size)])
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


class TestExercise6_5_8(TestCase):

    def test_merge_sorted_lists(self):
        size = random.randint(1, 10)
        lists = Array([get_random_sorted_singly_linked_list()[0] for _ in range(size)])
        expected_lists = [get_linked_list_keys(list_) for list_ in lists]
        expected_elements = sorted([element for list_ in expected_lists for element in list_])

        actual_merged = merge_sorted_lists(lists)

        actual_elements = get_linked_list_keys(actual_merged)
        assert_that(actual_elements, is_(equal_to(expected_elements)))
