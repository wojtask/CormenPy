import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_3 import singly_linked_list_enqueue, singly_linked_list_dequeue
from datastructures.array import Array
from list_util import get_random_singly_linked_list


class TestExercise10_2_3(TestCase):

    def test_singly_linked_list_enqueue(self):
        linked_list = get_random_singly_linked_list()
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()
        linked_list.tail = original_nodes[original_nodes.length]
        x = random.randint(0, 999)

        singly_linked_list_enqueue(linked_list, x)

        actual_keys = linked_list.as_keys_array()
        expected_keys = original_keys + Array.of(x)
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_dequeue(self):
        linked_list = get_random_singly_linked_list(min_size=0, max_size=5)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()

        if linked_list.head is None:
            linked_list.tail = None
            assert_that(calling(singly_linked_list_dequeue).with_args(linked_list), raises(ValueError, 'underflow'))
        else:
            linked_list.tail = original_nodes[original_keys.length]

            actual_deleted = singly_linked_list_dequeue(linked_list)

            assert_that(actual_deleted, is_(equal_to(original_keys[1])))
            actual_keys = linked_list.as_keys_array()
            original_keys.pop(1)
            assert_that(actual_keys, is_(equal_to(original_keys)))
            if linked_list.head is None:
                assert_that(linked_list.tail, is_(none()))
