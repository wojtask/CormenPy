import math
import random
from unittest import TestCase

from chapter06.ex6_2_2 import min_heapify
from chapter06.ex6_5_3 import heap_minimum, heap_extract_min, heap_decrease_key, min_heap_insert
from test.test_datastructures.array_util import random_int_array
from test.test_datastructures.heap_util import assert_min_heap
from util import rbetween


def build_min_heap(A):
    A.heap_size = A.length
    for i in rbetween(math.floor(A.length / 2), 1):
        min_heapify(A, i)


class Ex6_5_3Test(TestCase):
    def test_heap_minimum(self):
        array, data = random_int_array()
        build_min_heap(array)
        actual_min = heap_minimum(array)
        self.assertEqual(actual_min, min(data))

    def test_extract_min(self):
        array, data = random_int_array()
        build_min_heap(array)
        actual_min = heap_extract_min(array)
        self.assertEqual(actual_min, min(data))
        assert_min_heap(array)
        self.assertEqual(array.heap_size, array.length - 1)
        actual_heap_keys = sorted(array[1:array.heap_size])
        expected_heap_keys = sorted(data)[1:]
        self.assertEqual(actual_heap_keys, expected_heap_keys)

    def test_heap_decrease_key(self):
        array, data = random_int_array()
        build_min_heap(array)
        i = random.randint(1, array.length)
        old_key = array[i]
        new_key = random.randrange(1000)
        if new_key > array[i]:
            with self.assertRaisesRegex(RuntimeError, 'new key is larger than current key'):
                heap_decrease_key(array, i, new_key)
        else:
            heap_decrease_key(array, i, new_key)
            assert_min_heap(array)
            self.assertEqual(array.heap_size, array.length)
            old_key_index = data.index(old_key)
            expected_heap_keys = data[:old_key_index] + [new_key] + data[old_key_index + 1:]
            self.assertEqual(sorted(array.data), sorted(expected_heap_keys))

    def test_min_heap_insert(self):
        array, data = random_int_array()
        build_min_heap(array)
        array.data.append(None)  # to increase the heap's capacity for the new element
        array.length += 1
        new_key = random.randrange(1000)
        min_heap_insert(array, new_key)
        self.assertEqual(array.heap_size, array.length)
        assert_min_heap(array)
        expected_heap_keys = data + [new_key]
        self.assertEqual(sorted(array.data), sorted(expected_heap_keys))
