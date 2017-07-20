import random
from unittest import TestCase

from chapter06.pr6_2 import multiary_parent, multiary_child, multiary_max_heapify, multiary_max_heap_insert, \
    multiary_heap_increase_key
from test_datastructures.heap_util import random_max_heap, assert_max_heap
from util import between


class Problem6_2Test(TestCase):
    def test_multiary_parent_child(self):
        d = random.randint(2, 7)
        i = random.randint(1, 30)

        for k in between(1, d):
            self.assertEqual(multiary_parent(d, multiary_child(d, i, k)), i)

    def test_multiary_max_heapify(self):
        ary = random.randint(2, 7)
        heap, data = random_max_heap(ary=ary)
        i = random.randint(1, heap.heap_size)
        heap[i] = data[i - 1] = random.randint(0, heap[i])  # randomly decrease value of randomly chosen element

        multiary_max_heapify(heap, ary, i)

        self.assertEqual(heap.heap_size, len(data))
        self.assertEqual(sorted(heap.data), sorted(data))
        assert_max_heap(heap, ary=ary)

    def test_multiary_max_heap_insert(self):
        ary = random.randint(2, 7)
        heap, data = random_max_heap(ary=ary)
        heap.data.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randint(0, 999)

        multiary_max_heap_insert(heap, ary, new_key)

        self.assertEqual(heap.heap_size, len(data) + 1)
        assert_max_heap(heap, ary=ary)
        expected_heap_keys = data + [new_key]
        self.assertEqual(sorted(heap.data), sorted(expected_heap_keys))

    def test_multiary_heap_increase_key(self):
        ary = random.randint(2, 7)
        heap, data = random_max_heap(ary=ary)
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randint(0, 999)
        real_new_key = max(old_key, new_key)

        multiary_heap_increase_key(heap, ary, i, new_key)

        assert_max_heap(heap, ary=ary)
        self.assertEqual(heap.heap_size, len(data))
        old_key_idx = data.index(old_key)
        expected_heap_keys = data[:old_key_idx] + [real_new_key] + data[old_key_idx + 1:]
        self.assertEqual(sorted(heap.data), sorted(expected_heap_keys))
