import random
from unittest import TestCase

from hamcrest import *

from chapter11.textbook_problem11_3 import quadratic_probing_search
from hash_table_util import get_random_hash_table_quadratic_probing


class TestTextbookProblem11_3(TestCase):

    def test_quadratic_probing_search(self):
        table, keys, _, auxiliary_hash = get_random_hash_table_quadratic_probing(max_value=10)
        key_to_find = random.randint(0, 10)

        actual_index = quadratic_probing_search(table, key_to_find, auxiliary_hash)

        if key_to_find in keys:
            assert_that(table[actual_index], is_(equal_to(key_to_find)))
        else:
            assert_that(actual_index, is_(none()))
