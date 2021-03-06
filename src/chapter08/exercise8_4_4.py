import math

from datastructures.array import Array
from util import between


def unit_circle_sort(A):
    n = A.length
    B = Array([[] for _ in range(n)], start=0)
    for i in between(1, n):
        d = math.sqrt(A[i].x ** 2 + A[i].y ** 2)
        B[math.ceil(d ** 2 * n) - 1].append((A[i], d))  # store distances with points; we'll sort by them later
    for i in between(0, n - 1):
        _insertion_sort_list_by_distance(B[i])
    _concatenate_lists_of_points(B, A)


def _insertion_sort_list_by_distance(L):
    for j in range(1, len(L)):
        key = L[j]
        i = j - 1
        while i >= 0 and L[i][1] > key[1]:
            L[i + 1] = L[i]
            i -= 1
        L[i + 1] = key


def _concatenate_lists_of_points(B, A):
    A.elements = [t[0] for L in B for t in L]
