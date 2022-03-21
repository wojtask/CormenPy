import random
from unittest import TestCase

from hamcrest import *

from chapter10.textbook10_3 import allocate_object, free_object
from datastructures.array import Array
from datastructures.list import MultipleArrayList
from util import between


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


def assert_multiple_array_list_consistent(array_list):
    prev_idx = None
    idx = array_list.head
    while idx is not None:
        assert_that(array_list.prev[idx] == prev_idx)
        prev_idx = idx
        idx = array_list.next[idx]


class TestTextbook10_3(TestCase):

    def test_allocate_object(self):
        array_list = get_random_multiple_array_list()

        if array_list.free is None:
            assert_that(calling(allocate_object).with_args(array_list), raises(ValueError, 'out of space'))
        else:
            expected_free = array_list.free
            expected_keys = Array(array_list)
            expected_free_list_size = array_list.get_free_list_size() - 1

            actual_allocated = allocate_object(array_list)

            assert_that(actual_allocated, is_(equal_to(expected_free)))
            assert_multiple_array_list_consistent(array_list)
            actual_keys = Array(array_list)
            assert_that(actual_keys, is_(equal_to(expected_keys)))
            actual_free_list_size = array_list.get_free_list_size()
            assert_that(actual_free_list_size, is_(equal_to(expected_free_list_size)))

    def test_free_object(self):
        array_list = get_random_multiple_array_list()

        # the list is nonempty so let's delete the head element and prepare it for freeing
        cell_to_free = array_list.head
        if array_list.next[array_list.head] is not None:
            array_list.prev[array_list.next[array_list.head]] = None
        array_list.head = array_list.next[array_list.head]

        expected_keys = Array(array_list)
        expected_free_list_size = array_list.get_free_list_size() + 1

        free_object(array_list, cell_to_free)

        assert_that(array_list.free, is_(equal_to(cell_to_free)))
        assert_multiple_array_list_consistent(array_list)
        actual_keys = Array(array_list)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        actual_free_list_size = array_list.get_free_list_size()
        assert_that(actual_free_list_size, is_(equal_to(expected_free_list_size)))
