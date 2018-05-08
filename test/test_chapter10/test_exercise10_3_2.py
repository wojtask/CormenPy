from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_3_2 import single_array_allocate_object, single_array_free_object
from list_util import get_random_single_array_list, get_single_array_list_keys, get_single_array_list_free_cells, \
    assert_single_array_list_consistent


class TestExercise10_3_2(TestCase):

    def test_single_array_allocate_object(self):
        list_ = get_random_single_array_list()

        if list_.free is None:
            assert_that(calling(single_array_allocate_object).with_args(list_), raises(RuntimeError, 'out of space'))
        else:
            expected_free = list_.free
            expected_keys = get_single_array_list_keys(list_)
            expected_free_cells = get_single_array_list_free_cells(list_) - 1

            actual_allocated = single_array_allocate_object(list_)

            assert_that(actual_allocated, is_(equal_to(expected_free)))
            assert_single_array_list_consistent(list_)
            actual_keys = get_single_array_list_keys(list_)
            assert_that(actual_keys, is_(equal_to(expected_keys)))
            actual_free_cells = get_single_array_list_free_cells(list_)
            assert_that(actual_free_cells, is_(equal_to(expected_free_cells)))

    def test_single_array_free_object(self):
        list_ = get_random_single_array_list()

        # the list is nonempty so let's delete the head element and prepare it for freeing
        cell_to_free = list_.head
        if list_.A[list_.head + 1] is not None:
            list_.A[list_.A[list_.head + 1] + 2] = None
        list_.head = list_.A[list_.head + 1]

        expected_keys = get_single_array_list_keys(list_)
        expected_free_cells = get_single_array_list_free_cells(list_) + 1

        single_array_free_object(list_, cell_to_free)

        assert_that(list_.free, is_(equal_to(cell_to_free)))
        assert_single_array_list_consistent(list_)
        actual_keys = get_single_array_list_keys(list_)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        actual_free_cells = get_single_array_list_free_cells(list_)
        assert_that(actual_free_cells, is_(equal_to(expected_free_cells)))
