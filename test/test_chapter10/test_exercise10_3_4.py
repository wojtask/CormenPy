from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_3_4 import compact_list_allocate_object, compact_list_free_object
from datastructures.array import Array
from list_util import get_random_compact_list, assert_multiple_array_list_consistent, assert_compact_list


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
