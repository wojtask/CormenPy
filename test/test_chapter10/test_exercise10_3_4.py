import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_3_4 import compact_list_allocate_object, compact_list_free_object
from datastructures.array import Array
from datastructures.list import MultipleArrayList
from test_chapter10.test_textbook10_3 import assert_multiple_array_list_consistent
from util import between


def get_random_compact_list(min_size=1, max_size=10, max_value=999):
    list_size = random.randint(min_size, max_size)
    array_size = random.randint(list_size, max_size)
    key, next, prev = Array.indexed(1, array_size), Array.indexed(1, array_size), Array.indexed(1, array_size)
    list_indexes = random.sample(between(1, list_size), list_size)

    head = prev_index = None
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


def assert_compact_list(compact_list):
    idx = compact_list.head
    nelements = 0
    max_idx = 0
    while idx is not None:
        nelements += 1
        max_idx = max(max_idx, idx)
        idx = compact_list.next[idx]
    assert_that(max_idx, is_(equal_to(nelements)))


class TestExercise10_3_4(TestCase):

    def test_compact_list_allocate_object(self):
        compact_list = get_random_compact_list()

        if compact_list.free is None:
            assert_that(calling(compact_list_allocate_object).with_args(compact_list),
                        raises(ValueError, 'out of space'))
        else:
            expected_free = compact_list.free
            expected_keys = Array(compact_list)
            expected_free_list_size = compact_list.get_free_list_size() - 1

            actual_allocated = compact_list_allocate_object(compact_list)

            assert_that(actual_allocated, is_(equal_to(expected_free)))
            assert_multiple_array_list_consistent(compact_list)
            assert_compact_list(compact_list)
            actual_keys = Array(compact_list)
            assert_that(actual_keys, is_(equal_to(expected_keys)))
            actual_free_list_size = compact_list.get_free_list_size()
            assert_that(actual_free_list_size, is_(equal_to(expected_free_list_size)))

    def test_compact_list_free_object(self):
        compact_list = get_random_compact_list()

        # the list is nonempty so let's delete the head element and prepare it for freeing
        cell_to_free = compact_list.head
        if compact_list.next[compact_list.head] is not None:
            compact_list.prev[compact_list.next[compact_list.head]] = None
        compact_list.head = compact_list.next[compact_list.head]

        expected_keys = Array(compact_list)
        expected_free = compact_list.free - 1 if compact_list.free is not None else compact_list.key.length
        expected_free_list_size = compact_list.get_free_list_size() + 1

        compact_list_free_object(compact_list, cell_to_free)

        assert_that(compact_list.free, is_(equal_to(expected_free)))
        assert_multiple_array_list_consistent(compact_list)
        assert_compact_list(compact_list)
        actual_keys = Array(compact_list)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        actual_free_list_size = compact_list.get_free_list_size()
        assert_that(actual_free_list_size, is_(equal_to(expected_free_list_size)))
