import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter11.textbook_problem11_3 import quadratic_probing_search
from hash_table_util import get_random_hash_table_quadratic_probing, get_hash_table_keys


class TestTextbookProblem11_3(TestCase):

    def test_quadratic_probing_search(self):
        max_value = 10
        table, auxiliary_hash = get_random_hash_table_quadratic_probing(max_value=max_value)
        original = copy.deepcopy(table)
        original_keys = get_hash_table_keys(table)
        key_to_find = random.randint(0, max_value)

        actual_index = quadratic_probing_search(table, key_to_find, auxiliary_hash)

        if key_to_find in original_keys:
            assert_that(table[actual_index], is_(equal_to(key_to_find)))
        else:
            assert_that(actual_index, is_(none()))
        assert_that(table, is_(equal_to(original)))
