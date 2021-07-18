import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter10.textbook_problem10_3 import compact_list_search
from list_util import get_random_compact_list


def make_sorted_keys_in_multiple_array_list(list_):
    array_length = list_.key.length
    sorted_keys = get_random_array(size=array_length).sort()
    x = list_.head
    i = 1
    while x:
        list_.key[x] = sorted_keys[i]
        x = list_.next[x]
        i += 1
    return sorted_keys[:i - 1]


class TestTextbookProblem10_3(TestCase):

    def test_compact_list_search(self):
        list_ = get_random_compact_list(min_size=10, max_size=20, max_value=20)
        keys = make_sorted_keys_in_multiple_array_list(list_)
        key_to_find = random.randint(0, 20)

        actual_index = compact_list_search(list_, keys.length, key_to_find)

        if key_to_find in keys:
            assert_that(list_.key[actual_index], is_(equal_to(key_to_find)))
        else:
            assert_that(actual_index, is_(none()))
