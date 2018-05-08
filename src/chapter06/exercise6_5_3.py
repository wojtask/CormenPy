import math

from chapter06.exercise6_2_2 import min_heapify
from chapter06.textbook6_1 import parent


def heap_minimum(A):
    return A[1]


def heap_extract_min(A):
    if A.heap_size < 1:
        raise RuntimeError('heap underflow')
    min = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    min_heapify(A, 1)
    return min


def heap_decrease_key(A, i, key):
    if key > A[i]:
        raise RuntimeError('new key is larger than current key')
    A[i] = key
    while i > 1 and A[parent(i)] > A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def min_heap_insert(A, key):
    A.heap_size = A.heap_size + 1
    A[A.heap_size] = math.inf
    heap_decrease_key(A, A.heap_size, key)
