import math

from chapter06.textbook6_1 import left, right, parent
from datastructures.array import Array
from datastructures.ternary_tree import Node
from util import between, rbetween


def ternary_huffman(C):
    n = len(C)
    Q = _build_min_priority_queue(C)
    for i in between(1, math.floor(n / 2)):
        w = Node(None)
        w.left = x = _heap_extract_min(Q)
        w.middle = y = _heap_extract_min(Q)
        if i == 1 and n % 2 == 0:
            w.f = x.f + y.f
        else:
            w.right = z = _heap_extract_min(Q)
            w.f = x.f + y.f + z.f
        _min_heap_insert(Q, w)
    return _heap_extract_min(Q)


def _build_min_priority_queue(C):
    nodes = []
    for c in C:
        node = Node(None)
        node.data = c[0]
        node.f = c[1]
        nodes.append(node)
    A = Array(nodes)
    _build_min_heap(A)
    return A


def _build_min_heap(A):
    A.heap_size = A.length
    for i in rbetween(math.floor(A.length / 2), 1):
        _min_heapify(A, i)


def _min_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l].f < A[i].f:
        smallest = l
    else:
        smallest = i
    if r <= A.heap_size and A[r].f < A[smallest].f:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        _min_heapify(A, smallest)


def _heap_extract_min(A):
    min = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    _min_heapify(A, 1)
    return min


def _min_heap_insert(A, z):
    A.heap_size = A.heap_size + 1
    i = A.heap_size
    A[i] = z
    while i > 1 and A[parent(i)].f > A[i].f:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
