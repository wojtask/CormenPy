import math

from chapter06.textbook6_1 import parent
from chapter06.textbook6_2 import max_heapify


def heap_maximum(A):
    return A[1]


def heap_extract_max(A):
    if A.heap_size < 1:
        raise ValueError('heap underflow')
    max = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    max_heapify(A, 1)
    return max


def heap_increase_key(A, i, key):
    if key < A[i]:
        raise ValueError('new key is smaller than current key')
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def max_heap_insert(A, key):
    A.heap_size += 1
    A[A.heap_size] = -math.inf
    heap_increase_key(A, A.heap_size, key)
