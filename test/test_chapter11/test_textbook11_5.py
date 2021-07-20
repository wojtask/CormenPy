from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter11.textbook11_5 import perfect_hashing_init, perfect_hashing_search
from util import between


class TestTextbook11_5(TestCase):

    def test_perfect_hashing(self):
        max_value = 99
        keys = get_random_array(min_size=1, max_value=max_value, unique=True)

        table, h = perfect_hashing_init(keys)

        for key in between(0, max_value):
            actual_found = perfect_hashing_search(table, key, h)
            if key in keys:
                assert_that(actual_found, is_(not_none()))
                j, j_ = actual_found
                assert_that(table[j][1][j_], is_(equal_to(key)))
            else:
                assert_that(actual_found, is_(none()))
