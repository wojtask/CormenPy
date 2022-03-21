import math

from chapter06.exercise6_2_2 import min_heapify
from chapter06.exercise6_5_3 import heap_extract_min, min_heap_insert
from datastructures.binary_tree import HuffmanNode
from datastructures.heap import Heap
from util import between, rbetween


def huffman(C):
    n = len(C)
    Q = _build_min_priority_queue(C)
    for i in between(1, n - 1):
        z = HuffmanNode()
        z.left = x = heap_extract_min(Q)
        z.right = y = heap_extract_min(Q)
        z.f = x.f + y.f
        min_heap_insert(Q, z)
    return heap_extract_min(Q)


def _build_min_priority_queue(C):
    A = Heap(HuffmanNode(c[0], c[1]) for c in C)
    _build_min_heap(A)
    return A


def _build_min_heap(A):
    A.heap_size = A.length
    for i in rbetween(math.floor(A.length / 2), 1):
        min_heapify(A, i)
