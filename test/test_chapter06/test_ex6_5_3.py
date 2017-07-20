import random
from unittest import TestCase

from chapter06.ex6_5_3 import heap_minimum, heap_extract_min, heap_decrease_key, min_heap_insert
from test.test_datastructures.heap_util import assert_min_heap, random_min_heap


class Ex6_5_3Test(TestCase):
    def test_heap_minimum(self):
        heap, data = random_min_heap()

        actual_min = heap_minimum(heap)

        self.assertEqual(actual_min, min(data))

    def test_extract_min(self):
        heap, data = random_min_heap()
        actual_min = heap_extract_min(heap)
        self.assertEqual(actual_min, min(data))

        assert_min_heap(heap)

        self.assertEqual(heap.heap_size, len(data) - 1)
        actual_heap_keys = sorted(heap[1:heap.heap_size])
        expected_heap_keys = sorted(data)[1:]
        self.assertEqual(actual_heap_keys, expected_heap_keys)

    def test_heap_decrease_key(self):
        heap, data = random_min_heap()
        i = random.randint(1, heap.length)
        old_key = heap[i]
        new_key = random.randint(0, 999)

        if new_key > old_key:
            with self.assertRaisesRegex(RuntimeError, 'new key is larger than current key'):
                heap_decrease_key(heap, i, new_key)
        else:
            heap_decrease_key(heap, i, new_key)
            assert_min_heap(heap)
            self.assertEqual(heap.heap_size, len(data))
            old_key_idx = data.index(old_key)
            expected_heap_keys = data[:old_key_idx] + [new_key] + data[old_key_idx + 1:]
            self.assertEqual(sorted(heap.data), sorted(expected_heap_keys))

    def test_min_heap_insert(self):
        heap, data = random_min_heap()
        heap.data.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randint(0, 999)

        min_heap_insert(heap, new_key)

        self.assertEqual(heap.heap_size, heap.length)
        assert_min_heap(heap)
        expected_heap_keys = data + [new_key]
        self.assertEqual(sorted(heap.data), sorted(expected_heap_keys))
