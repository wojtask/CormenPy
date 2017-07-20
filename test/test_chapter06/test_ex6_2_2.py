import random
from unittest import TestCase

from chapter06.ex6_2_2 import min_heapify
from test_datastructures.heap_util import random_min_heap, assert_min_heap


class Ex6_2_2Test(TestCase):
    def test_min_heapify(self):
        heap, data = random_min_heap()
        i = random.randint(1, heap.heap_size)
        heap[i] = data[i - 1] = random.randint(heap[i], 999)  # randomly increase value of randomly chosen element

        min_heapify(heap, i)

        self.assertEqual(heap.heap_size, len(data))
        self.assertEqual(sorted(heap.data), sorted(data))
        assert_min_heap(heap)
