from unittest import TestCase

from chapter06.pr6_2 import multiary_parent, multiary_child, multiary_max_heapify, multiary_max_heap_insert, \
    multiary_heap_increase_key
from datastructures.heap import Heap
from util import between


class Problem6_2Test(TestCase):
    def test_multiary_parent(self):
        self.assertEqual(multiary_parent(5, 21), 4)
        self.assertEqual(multiary_parent(5, 22), 5)

    def test_multiary_child(self):
        self.assertEqual(multiary_child(5, 4, 5), 21)
        self.assertEqual(multiary_child(5, 5, 1), 22)

    def test_multiary_parent_child(self):
        d, i = 8, 6
        for k in between(1, d):
            self.assertEqual(multiary_parent(d, multiary_child(d, i, k)), i)

    def test_multiary_max_heapify(self):
        heap = Heap([1, 7, 30, 38, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 35, 18])
        multiary_max_heapify(heap, 4, 1)
        expected_heap = Heap([38, 7, 30, 35, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 1, 18])
        self.assertEqual(heap, expected_heap)

    def test_multiary_max_heap_insert(self):
        heap = Heap([38, 7, 30, 35, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 1, 18])
        heap.data.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        multiary_max_heap_insert(heap, 4, 40)
        expected_heap = Heap([40, 7, 30, 38, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 1, 18, 35])
        self.assertEqual(heap, expected_heap)

    def test_multiary_heap_increase_key(self):
        heap = Heap([38, 7, 30, 35, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 1, 18])
        multiary_heap_increase_key(heap, 4, 15, 40)
        expected_heap = Heap([40, 7, 30, 38, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 35, 18])
        self.assertEqual(heap, expected_heap)
