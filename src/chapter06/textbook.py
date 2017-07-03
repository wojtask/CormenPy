import math

from util import rscope, scope


def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    A.heap_size = A.length
    for i in rscope(A.length // 2, 1):
        max_heapify(A, i)


def heapsort(A):
    build_max_heap(A)
    for i in rscope(A.length, 2):
        A[1], A[i] = A[i], A[1]
        A.heap_size = A.heap_size - 1
        max_heapify(A, 1)


def heap_maximum(A):
    return A[1]


def heap_extract_max(A):
    if A.heap_size < 1:
        raise RuntimeError("heap underflow")
    max = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    max_heapify(A, 1)
    return max


def heap_increase_key(A, i, key):
    if key < A[i]:
        raise RuntimeError("new key is smaller than current key")
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def max_heap_insert(A, key):
    A.heap_size = A.heap_size + 1
    A[A.heap_size] = -math.inf
    heap_increase_key(A, A.heap_size, key)


def build_max_heap_(A):
    A.heap_size = 1
    for i in scope(2, A.length):
        max_heap_insert(A, A[i])
