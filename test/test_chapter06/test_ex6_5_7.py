import random
from unittest import TestCase

from chapter06.ex6_5_7 import max_heap_delete
from test.test_datastructures.heap_util import assert_max_heap, random_max_heap


class Ex6_5_7Test(TestCase):
    def test_max_heap_delete(self):
        heap, data = random_max_heap()
        i = random.randint(1, heap.heap_size)
        key_to_delete = heap[i]

        actual_deleted_key = max_heap_delete(heap, i)

        self.assertEqual(actual_deleted_key, key_to_delete)
        self.assertEqual(heap.heap_size, len(data) - 1)
        assert_max_heap(heap)
        deleted_key_idx = data.index(actual_deleted_key)
        actual_heap_keys = data[:deleted_key_idx] + data[deleted_key_idx + 1:]
        expected_heap_keys = heap[1:heap.heap_size]
        self.assertEqual(sorted(actual_heap_keys), sorted(expected_heap_keys))
