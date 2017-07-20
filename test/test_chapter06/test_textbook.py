import random
from unittest import TestCase

from chapter06.textbook import heapsort, heap_maximum, heap_extract_max, heap_increase_key, max_heap_insert
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array
from test.test_datastructures.heap_util import assert_max_heap, random_max_heap


class Chapter06Test(TestCase):
    def test_heapsort(self):
        array, data = random_int_array()

        heapsort(array)

        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_heap_maximum(self):
        heap, data = random_max_heap()

        actual_max = heap_maximum(heap)

        self.assertEqual(actual_max, max(data))

    def test_extract_max(self):
        heap, data = random_max_heap()
        actual_max = heap_extract_max(heap)
        self.assertEqual(actual_max, max(data))

        assert_max_heap(heap)

        self.assertEqual(heap.heap_size, len(data) - 1)
        actual_heap_keys = sorted(heap[1:heap.heap_size])
        expected_heap_keys = sorted(data)[:-1]
        self.assertEqual(actual_heap_keys, expected_heap_keys)

    def test_heap_increase_key(self):
        heap, data = random_max_heap()
        i = random.randint(1, heap.length)
        old_key = heap[i]
        new_key = random.randrange(1000)

        if new_key < old_key:
            with self.assertRaisesRegex(RuntimeError, 'new key is smaller than current key'):
                heap_increase_key(heap, i, new_key)
        else:
            heap_increase_key(heap, i, new_key)
            assert_max_heap(heap)
            self.assertEqual(heap.heap_size, len(data))
            old_key_idx = data.index(old_key)
            expected_heap_keys = data[:old_key_idx] + [new_key] + data[old_key_idx + 1:]
            self.assertEqual(sorted(heap.data), sorted(expected_heap_keys))

    def test_max_heap_insert(self):
        heap, data = random_max_heap()
        heap.data.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        max_heap_insert(heap, new_key)

        self.assertEqual(heap.heap_size, len(data) + 1)
        assert_max_heap(heap)
        expected_heap_keys = data + [new_key]
        self.assertEqual(sorted(heap.data), sorted(expected_heap_keys))
