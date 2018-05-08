import random
from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_4_2 import hash_delete, hash_insert_
from hash_table_util import get_random_hash_table_linear_probing, get_hash_table_keys


class TestExercise11_4_2(TestCase):

    def test_hash_delete(self):
        table, keys, h = get_random_hash_table_linear_probing()
        # make sure the table is not empty
        if not keys:
            key = random.randint(0, 999)
            keys.append(key)
            table[h(key, 0, table.length)] = key
        key_to_delete = random.choice(keys)

        hash_delete(table, key_to_delete, h)

        actual_keys = get_hash_table_keys(table)
        keys.remove(key_to_delete)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_hash_insert_(self):
        table, keys, h = get_random_hash_table_linear_probing()
        new_key = random.randint(0, 999)

        if len(keys) == table.length:
            assert_that(calling(hash_insert_).with_args(table, new_key, h),
                        raises(RuntimeError, 'hash table overflow'))
        else:
            hash_insert_(table, new_key, h)

            actual_keys = get_hash_table_keys(table)
            keys.append(new_key)
            assert_that(actual_keys, contains_inanyorder(*keys))
