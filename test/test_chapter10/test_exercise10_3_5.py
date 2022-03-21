from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_3_5 import compactify_list
from datastructures.array import Array
from test_chapter10.test_textbook10_3 import get_random_multiple_array_list


def make_free_list_doubly_linked(array_list):
    if not array_list.free:
        return
    x = array_list.free
    while array_list.next[x]:
        array_list.prev[array_list.next[x]] = x
        x = array_list.next[x]


class TestExercise10_3_5(TestCase):

    def test_compactify_list(self):
        array_list = get_random_multiple_array_list()
        make_free_list_doubly_linked(array_list)
        expected_keys = Array(array_list)
        expected_free_list_size = array_list.get_free_list_size()

        compactify_list(array_list)

        actual_keys = Array(array_list)
        actual_free_list_size = array_list.get_free_list_size()
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_that(actual_free_list_size, is_(equal_to(expected_free_list_size)))
