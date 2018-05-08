import math

from datastructures.array import Array
from util import between


def bucket_sort(A):
    n = A.length
    B = Array([[] for _ in range(n)], start=0)
    for i in between(1, n):
        B[math.floor(n * A[i])].append(A[i])
    for i in between(0, n - 1):
        _insertion_sort_list(B[i])
    _concatenate_lists(B, A)


def _insertion_sort_list(L):
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i] > key:
            L[i + 1] = L[i]
            i -= 1
        L[i + 1] = key


def _concatenate_lists(B, A):
    A.elements = [x for L in B for x in L]
