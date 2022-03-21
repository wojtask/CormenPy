import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.textbook_problem10_3 import compact_list_search
from datastructures.array import Array
from test_chapter10.test_exercise10_3_4 import get_random_compact_list


def make_compact_list_keys_sorted(compact_list):
    array_length = compact_list.key.length
    sorted_keys = get_random_array(size=array_length).sort()
    x = compact_list.head
    i = 1
    while x:
        compact_list.key[x] = sorted_keys[i]
        x = compact_list.next[x]
        i += 1


class TestTextbookProblem10_3(TestCase):

    def test_compact_list_search(self):
        compact_list = get_random_compact_list(min_size=10, max_size=20, max_value=20)
        make_compact_list_keys_sorted(compact_list)
        expected_keys = Array(compact_list)
        expected_free_list_size = compact_list.get_free_list_size()
        key_to_find = random.randint(0, 20)

        actual_index = compact_list_search(compact_list, expected_keys.length, key_to_find)

        if key_to_find in expected_keys:
            assert_that(compact_list.key[actual_index], is_(equal_to(key_to_find)))
        else:
            assert_that(actual_index, is_(none()))
        actual_keys = Array(compact_list)
        actual_free_list_size = compact_list.get_free_list_size()
        assert_that(actual_keys, is_(equal_to(expected_keys)))
        assert_that(actual_free_list_size, is_(equal_to(expected_free_list_size)))
