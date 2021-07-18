import random
from unittest import TestCase

from hamcrest import *

from chapter11.textbook11_4 import hash_insert, hash_search
from hash_table_util import get_random_hash_table_linear_probing, get_hash_table_keys


class TestTextbook11_4(TestCase):

    def test_hash_insert(self):
        table, keys, h = get_random_hash_table_linear_probing()
        new_key = random.randint(0, 999)

        if keys.length == table.length:
            assert_that(calling(hash_insert).with_args(table, new_key, h),
                        raises(ValueError, 'hash table overflow'))
        else:
            hash_insert(table, new_key, h)

            actual_keys = get_hash_table_keys(table)
            assert_that(actual_keys, contains_inanyorder(*keys, new_key))

    def test_hash_search(self):
        max_value = 10
        table, keys, h = get_random_hash_table_linear_probing(max_value=max_value)
        key_to_find = random.randint(0, max_value)

        actual_index = hash_search(table, key_to_find, h)

        if key_to_find in keys:
            assert_that(table[actual_index], is_(equal_to(key_to_find)))
        else:
            assert_that(actual_index, is_(none()))
