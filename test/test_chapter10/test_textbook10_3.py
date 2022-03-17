from unittest import TestCase

from hamcrest import *

from chapter10.textbook10_3 import allocate_object, free_object
from datastructures.array import Array
from list_util import get_random_multiple_array_list, assert_multiple_array_list_consistent


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
