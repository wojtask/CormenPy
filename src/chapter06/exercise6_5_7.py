from chapter06.textbook6_1 import parent
from chapter06.textbook6_2 import max_heapify


def max_heap_delete(A, i):
    A[i], A[A.heap_size] = A[A.heap_size], A[i]
    A.heap_size -= 1
    max_heapify(A, i)
    while i > 1 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)
    return A[A.heap_size + 1]
