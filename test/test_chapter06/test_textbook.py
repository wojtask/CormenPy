import random
from unittest import TestCase

from chapter06.textbook import build_max_heap, heapsort, heap_maximum, heap_extract_max, heap_increase_key, \
    max_heap_insert
from datastructures.array import Array
from test.test_datastructures.array_util import random_int_array
from test.test_datastructures.heap_util import assert_max_heap


class Chapter06Test(TestCase):
    def test_heapsort(self):
        array, data = random_int_array()
        heapsort(array)
        expected_array = Array(sorted(data))
        self.assertEqual(array, expected_array)

    def test_heap_maximum(self):
        array, data = random_int_array()
        build_max_heap(array)
        actual_max = heap_maximum(array)
        self.assertEqual(actual_max, max(data))

    def test_extract_max(self):
        array, data = random_int_array()
        build_max_heap(array)
        actual_max = heap_extract_max(array)
        self.assertEqual(actual_max, max(data))
        assert_max_heap(array)
        self.assertEqual(array.heap_size, array.length - 1)
        actual_heap_keys = sorted(array[1:array.heap_size])
        expected_heap_keys = sorted(data)[:-1]
        self.assertEqual(actual_heap_keys, expected_heap_keys)

    def test_heap_increase_key(self):
        array, data = random_int_array()
        build_max_heap(array)
        i = random.randint(1, array.length)
        old_key = array[i]
        new_key = random.randrange(1000)
        if new_key < array[i]:
            with self.assertRaisesRegex(RuntimeError, 'new key is smaller than current key'):
                heap_increase_key(array, i, new_key)
        else:
            heap_increase_key(array, i, new_key)
            assert_max_heap(array)
            self.assertEqual(array.heap_size, array.length)
            old_key_index = data.index(old_key)
            expected_heap_keys = data[:old_key_index] + [new_key] + data[old_key_index + 1:]
            self.assertEqual(sorted(array.data), sorted(expected_heap_keys))

    def test_max_heap_insert(self):
        array, data = random_int_array()
        build_max_heap(array)
        array.data.append(None)  # to increase the heap's capacity for the new element
        array.length += 1
        new_key = random.randrange(1000)
        max_heap_insert(array, new_key)
        self.assertEqual(array.heap_size, array.length)
        assert_max_heap(array)
        expected_heap_keys = data + [new_key]
        self.assertEqual(sorted(array.data), sorted(expected_heap_keys))
