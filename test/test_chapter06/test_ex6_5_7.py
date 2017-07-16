import random
from unittest import TestCase

from chapter06.ex6_5_7 import max_heap_delete
from chapter06.textbook import build_max_heap
from test.test_datastructures.array_util import random_int_array
from test.test_datastructures.heap_util import assert_max_heap


class Ex6_5_7Test(TestCase):
    def test_max_heap_delete(self):
        array, data = random_int_array()
        build_max_heap(array)
        i = random.randint(1, array.heap_size)
        key_to_delete = array[i]
        actual_deleted_key = max_heap_delete(array, i)
        self.assertEqual(actual_deleted_key, key_to_delete)
        self.assertEqual(array.heap_size, array.length - 1)
        assert_max_heap(array)
        deleted_key_index = data.index(actual_deleted_key)
        actual_heap_keys = data[:deleted_key_index] + data[deleted_key_index + 1:]
        expected_heap_keys = array[1:array.heap_size]
        self.assertEqual(sorted(actual_heap_keys), sorted(expected_heap_keys))
