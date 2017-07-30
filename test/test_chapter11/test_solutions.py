import random
from unittest import TestCase

from hamcrest import *

from chapter11.ex11_1_1 import direct_address_maximum
from chapter11.ex11_1_2 import bit_vector_search, bit_vector_insert, bit_vector_delete
from hash_table_util import random_direct_address_table, random_bit_vector


class Solutions11Test(TestCase):

    def test_direct_address_maximum(self):
        table, elements = random_direct_address_table()

        actual_maximum = direct_address_maximum(table)

        if elements:
            expected_maximum = max([element.key for element in elements])
            assert_that(actual_maximum.key, is_(equal_to(expected_maximum)))
        else:
            assert_that(actual_maximum, is_(none()))

    def test_bit_vector_search(self):
        bit_vector, keys = random_bit_vector()
        key_to_find = random.randint(0, bit_vector.length - 1)

        actual_found = bit_vector_search(bit_vector, key_to_find)

        if key_to_find in keys:
            assert_that(actual_found, is_(equal_to(1)))
        else:
            assert_that(actual_found, is_(equal_to(0)))

    def test_bit_vector_insert(self):
        bit_vector, keys = random_bit_vector()
        new_key = random.randint(0, bit_vector.length - 1)

        bit_vector_insert(bit_vector, new_key)

        assert_that(bit_vector[new_key], is_(equal_to(1)))

    def test_bit_vector_delete(self):
        bit_vector, keys = random_bit_vector()
        key_to_delete = random.randint(0, bit_vector.length - 1)

        bit_vector_delete(bit_vector, key_to_delete)

        assert_that(bit_vector[key_to_delete], is_(equal_to(0)))
