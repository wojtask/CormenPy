import math

from chapter06.exercise6_5_3 import heap_extract_min, min_heap_insert
from chapter16.textbook16_3 import HuffmanNode, _build_min_heap
from datastructures.heap import Heap
from util import between


class TernaryHuffmanNode(HuffmanNode):
    def __init__(self, character=None, frequency=0):
        super().__init__(character, frequency)
        self.middle = None


def ternary_huffman(C):
    n = len(C)
    if n % 2 == 0:
        C.add(('#', 0))
    Q = _build_min_priority_queue(C)
    for i in between(1, math.floor(n / 2)):
        w = TernaryHuffmanNode()
        w.left = x = heap_extract_min(Q)
        w.middle = y = heap_extract_min(Q)
        w.right = z = heap_extract_min(Q)
        w.f = x.f + y.f + z.f
        min_heap_insert(Q, w)
    return heap_extract_min(Q)


def _build_min_priority_queue(C):
    A = Heap(TernaryHuffmanNode(c[0], c[1]) for c in C)
    _build_min_heap(A)
    return A
