from chapter06.textbook6_2 import max_heapify
from chapter06.textbook6_5 import heap_increase_key


def max_heap_delete(A, i):
    if A[i] >= A[A.heap_size]:
        A[i] = A[A.heap_size]
        A.heap_size -= 1
        max_heapify(A, i)
    else:
        heap_increase_key(A, i, A[A.heap_size])
        A.heap_size -= 1
