from chapter06.textbook6_5 import max_heap_insert
from util import between


def build_max_heap_(A):
    A.heap_size = 1
    for i in between(2, A.length):
        max_heap_insert(A, A[i])
