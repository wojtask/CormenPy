import unittest

from chapter06.pr6_2 import multiary_parent, multiary_child, multiary_max_heapify, multiary_max_heap_insert, \
    multiary_heap_increase_key
from datastructures.heap import Heap
from util import scope


class MultiaryHeapTest(unittest.TestCase):
    def test_multiary_parent(self):
        self.assertEqual(4, multiary_parent(5, 21))
        self.assertEqual(5, multiary_parent(5, 22))

    def test_multiary_child(self):
        self.assertEqual(21, multiary_child(5, 4, 5))
        self.assertEqual(22, multiary_child(5, 5, 1))

    def test_multiary_parent_child(self):
        d, i = 8, 6
        for k in scope(1, d):
            self.assertEqual(i, multiary_parent(d, multiary_child(d, i, k)))

    def test_multiary_max_heapify(self):
        heap = Heap([1, 7, 30, 38, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 35, 18])
        multiary_max_heapify(heap, 4, 1)
        self.assertEqual([38, 7, 30, 35, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 1, 18], heap.data)
        self.assertEqual(16, heap.heap_size)

    def test_multiary_max_heap_insert(self):
        heap = Heap([38, 7, 30, 35, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 1, 18])
        heap.data.append(None)  # to increase the heap's capacity for the new element
        multiary_max_heap_insert(heap, 4, 40)
        self.assertEqual([40, 7, 30, 38, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 1, 18, 35], heap.data)
        self.assertEqual(17, heap.heap_size)

    def test_multiary_heap_increase_key(self):
        heap = Heap([38, 7, 30, 35, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 1, 18])
        multiary_heap_increase_key(heap, 4, 15, 40)
        self.assertEqual([40, 7, 30, 38, 22, 6, 3, 2, 5, 14, 29, 25, 24, 31, 35, 18], heap.data)
        self.assertEqual(16, heap.heap_size)
