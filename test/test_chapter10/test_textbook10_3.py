from unittest import TestCase

from hamcrest import *

from chapter10.textbook10_3 import allocate_object, free_object
from list_util import get_random_multiple_array_list, get_multiple_array_list_keys, get_multiple_array_list_free_cells,\
    assert_multiple_array_list_consistent


class TestTextbook10_3(TestCase):

    def test_allocate_object(self):
        list_ = get_random_multiple_array_list()

        if list_.free is None:
            assert_that(calling(allocate_object).with_args(list_), raises(RuntimeError, 'out of space'))
        else:
            expected_free = list_.free
            expected_keys = get_multiple_array_list_keys(list_)
            expected_free_cells = get_multiple_array_list_free_cells(list_) - 1

            actual_allocated = allocate_object(list_)

            assert_that(actual_allocated, is_(equal_to(expected_free)))
            assert_multiple_array_list_consistent(list_)
            actual_keys = get_multiple_array_list_keys(list_)
            assert_that(actual_keys, is_(equal_to(expected_keys)))
            actual_free_cells = get_multiple_array_list_free_cells(list_)
            assert_that(actual_free_cells, is_(equal_to(expected_free_cells)))

    def test_free_object(self):
        list_ = get_random_multiple_array_list()

        # the list is nonempty so let's delete the head element and prepare it for freeing
        cell_to_free = list_.head
        if list_.next[list_.head] is not None:
            list_.prev[list_.next[list_.head]] = None
        list_.head = list_.next[list_.head]

        expected_keys = get_multiple_array_list_keys(list_)
        expected_free_cells = get_multiple_array_list_free_cells(list_) + 1

        free_object(list_, cell_to_free)

        assert_that(list_.free, is_(equal_to(cell_to_free)))
        assert_multiple_array_list_consistent(list_)
        actual_keys = get_multiple_array_list_keys(list_)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        actual_free_cells = get_multiple_array_list_free_cells(list_)
        assert_that(actual_free_cells, is_(equal_to(expected_free_cells)))
