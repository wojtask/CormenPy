from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_3_5 import compactify_list
from list_util import get_random_multiple_array_list, get_multiple_array_list_keys, get_multiple_array_list_free_cells


def make_free_list_doubly_linked(list_):
    if not list_.free:
        return
    x = list_.free
    while list_.next[x]:
        list_.prev[list_.next[x]] = x
        x = list_.next[x]


class TestExercise10_3_5(TestCase):

    def test_compactify_list(self):
        list_ = get_random_multiple_array_list()
        make_free_list_doubly_linked(list_)
        expected_keys = get_multiple_array_list_keys(list_)
        expected_free_cells = get_multiple_array_list_free_cells(list_)

        compactify_list(list_)

        actual_keys = get_multiple_array_list_keys(list_)
        actual_free_cells = get_multiple_array_list_free_cells(list_)
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_that(actual_free_cells, is_(equal_to(expected_free_cells)))
