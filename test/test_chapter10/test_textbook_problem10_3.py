import random
from unittest import TestCase

from hamcrest import *

from chapter10.textbook_problem10_3 import compact_list_search
from list_util import get_random_compact_list


def make_sorted_keys_in_multiple_array_list(list_):
    array_length = list_.key.length
    sorted_keys = sorted([random.randint(0, 999) for _ in range(array_length)])
    x = list_.head
    i = 0
    while x is not None:
        list_.key[x] = sorted_keys[i]
        x = list_.next[x]
        i += 1
    return sorted_keys[:i]


class TestTextbookProblem10_3(TestCase):

    def test_compact_list_search(self):
        list_ = get_random_compact_list(min_size=10, max_size=20, max_value=20)
        keys = make_sorted_keys_in_multiple_array_list(list_)
        key_to_find = random.randint(0, 20)

        actual_index = compact_list_search(list_, len(keys), key_to_find)

        if key_to_find in keys:
            assert_that(list_.key[actual_index], is_(equal_to(key_to_find)))
        else:
            assert_that(actual_index, is_(none()))
