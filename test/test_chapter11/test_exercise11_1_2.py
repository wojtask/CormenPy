import random
from unittest import TestCase

from hamcrest import *

from chapter11.exercise11_1_2 import bit_vector_search, bit_vector_insert, bit_vector_delete
from hash_table_util import get_random_bit_vector


class TestExercise11_1_2(TestCase):

    def test_bit_vector_search(self):
        bit_vector, keys = get_random_bit_vector()
        key_to_find = random.randint(0, bit_vector.length - 1)

        actual_found = bit_vector_search(bit_vector, key_to_find)

        if key_to_find in keys:
            assert_that(actual_found, is_(equal_to(1)))
        else:
            assert_that(actual_found, is_(equal_to(0)))

    def test_bit_vector_insert(self):
        bit_vector, keys = get_random_bit_vector()
        new_key = random.randint(0, bit_vector.length - 1)

        bit_vector_insert(bit_vector, new_key)

        assert_that(bit_vector[new_key], is_(equal_to(1)))

    def test_bit_vector_delete(self):
        bit_vector, keys = get_random_bit_vector()
        key_to_delete = random.randint(0, bit_vector.length - 1)

        bit_vector_delete(bit_vector, key_to_delete)

        assert_that(bit_vector[key_to_delete], is_(equal_to(0)))
