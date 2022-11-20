from chapter06.textbook6_2 import max_heapify
from util import rbetween


def build_max_heap(A):
    A.heap_size = A.length
    for i in rbetween(A.length // 2, 1):
        max_heapify(A, i)
