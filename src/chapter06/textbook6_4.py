from chapter06.textbook6_2 import max_heapify
from chapter06.textbook6_3 import build_max_heap
from util import rbetween


def heapsort(A):
    build_max_heap(A)
    for i in rbetween(A.length, 2):
        A[1], A[i] = A[i], A[1]
        A.heap_size -= 1
        max_heapify(A, 1)
