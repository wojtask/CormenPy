from unittest import TestCase

from hamcrest import *

from array_util import get_random_unique_array
from chapter11.textbook_problem11_5 import perfect_hashing_init, perfect_hashing_search


class TestTextbookProblem11_5(TestCase):

    def test_perfect_hashing(self):
        keys, _ = get_random_unique_array(max_value=99)

        table, h = perfect_hashing_init(keys)

        for key in range(100):
            actual_found = perfect_hashing_search(table, key, h)
            if key in keys:
                assert_that(actual_found, is_(not_none()))
                j, j_ = actual_found
                assert_that(table[j][1][j_], is_(equal_to(key)))
            else:
                assert_that(actual_found, is_(none()))
