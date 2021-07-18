import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_3 import singly_linked_list_enqueue, singly_linked_list_dequeue
from datastructures.array import Array
from list_util import get_random_singly_linked_list, get_linked_list_keys


class TestExercise10_2_3(TestCase):

    def test_singly_linked_list_enqueue(self):
        list_, nodes, keys = get_random_singly_linked_list()
        list_.tail = nodes[nodes.length]
        x = random.randint(0, 999)

        singly_linked_list_enqueue(list_, x)

        actual_keys = get_linked_list_keys(list_)
        expected_keys = keys + Array([x])
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_dequeue(self):
        list_, nodes, keys = get_random_singly_linked_list(min_size=0, max_size=5)

        if list_.head is None:
            list_.tail = None
            assert_that(calling(singly_linked_list_dequeue).with_args(list_), raises(ValueError, 'underflow'))
        else:
            list_.tail = nodes[nodes.length]

            actual_deleted = singly_linked_list_dequeue(list_)

            assert_that(actual_deleted, is_(equal_to(keys[1])))
            actual_keys = get_linked_list_keys(list_)
            assert_that(actual_keys, is_(equal_to(keys[2:])))
            if list_.head is None:
                assert_that(list_.tail, is_(none()))
