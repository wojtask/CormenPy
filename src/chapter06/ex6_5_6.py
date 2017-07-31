import math

from chapter06.textbook import parent, left, right
from util import Element


def priority_enqueue(Q, x):
    x.key = Q.rank
    _min_heap_insert_element(Q, x)
    Q.rank += 1


def _min_heap_insert_element(A, x):
    A.heap_size = A.heap_size + 1
    A[A.heap_size] = Element(math.inf)
    _heap_decrease_element_key(A, A.heap_size, x)


def _heap_decrease_element_key(A, i, x):
    if x.key > A[i].key:
        raise RuntimeError('new key is larger than current key')
    A[i] = x
    while i > 1 and A[parent(i)].key > A[i].key:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def priority_dequeue(Q):
    return _heap_extract_min_element(Q)


def _heap_extract_min_element(A):
    if A.heap_size < 1:
        raise RuntimeError('heap underflow')
    min = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    _min_heapify_element(A, 1)
    return min


def _min_heapify_element(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l].key < A[i].key:
        smallest = l
    else:
        smallest = i
    if r <= A.heap_size and A[r].key < A[smallest].key:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        _min_heapify_element(A, smallest)


def priority_push(Q, x):
    x.key = Q.rank
    _max_heap_insert_element(Q, x)
    Q.rank += 1


def _max_heap_insert_element(A, x):
    A.heap_size += 1
    A[A.heap_size] = Element(-math.inf)
    _heap_increase_element_key(A, A.heap_size, x)


def _heap_increase_element_key(A, i, x):
    if x.key < A[i].key:
        raise RuntimeError('new key is smaller than current key')
    A[i] = x
    while i > 1 and A[parent(i)].key < A[i].key:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def priority_pop(Q):
    return _heap_extract_max_element(Q)


def _heap_extract_max_element(A):
    if A.heap_size < 1:
        raise RuntimeError('heap underflow')
    max = A[1]
    A[1] = A[A.heap_size]
    A.heap_size = A.heap_size - 1
    _max_heapify_element(A, 1)
    return max


def _max_heapify_element(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l].key > A[i].key:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r].key > A[largest].key:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        _max_heapify_element(A, largest)
