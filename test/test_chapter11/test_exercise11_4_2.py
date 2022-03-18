import random
from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_4_2 import hash_delete, hash_insert_
from hash_table_util import get_random_hash_table_linear_probing, get_hash_table_keys


class TestExercise11_4_2(TestCase):

    def test_hash_delete(self):
        table, h = get_random_hash_table_linear_probing()
        original_keys = get_hash_table_keys(table)
        # make sure the table is not empty
        if not original_keys:
            key = random.randint(0, 999)
            original_keys.append(key)
            table[h(key, 0)] = key
        key_to_delete = original_keys.random_choice()

        hash_delete(table, key_to_delete, h)

        actual_keys = get_hash_table_keys(table)
        original_keys.remove(key_to_delete)
        assert_that(actual_keys, contains_inanyorder(*original_keys))

    def test_hash_insert_(self):
        table, h = get_random_hash_table_linear_probing()
        original_keys = get_hash_table_keys(table)
        new_key = random.randint(0, 999)

        if original_keys.length == table.length:
            assert_that(calling(hash_insert_).with_args(table, new_key, h),
                        raises(ValueError, 'hash table overflow'))
        else:
            hash_insert_(table, new_key, h)

            actual_keys = get_hash_table_keys(table)
            assert_that(actual_keys, contains_inanyorder(*original_keys, new_key))
