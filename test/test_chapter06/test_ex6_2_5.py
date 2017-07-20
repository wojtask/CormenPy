import random
from unittest import TestCase

from chapter06.ex6_2_5 import iterative_max_heapify
from test_datastructures.heap_util import random_max_heap, assert_max_heap


class Ex6_2_5Test(TestCase):
    def test_iterative_max_heapify(self):
        heap, data = random_max_heap()
        i = random.randint(1, heap.heap_size)
        heap[i] = data[i - 1] = random.randint(0, heap[i])  # randomly decrease value of randomly chosen element

        iterative_max_heapify(heap, i)

        self.assertEqual(heap.heap_size, len(data))
        self.assertEqual(sorted(heap.data), sorted(data))
        assert_max_heap(heap)
