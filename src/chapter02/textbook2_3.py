import math

from datastructures.array import Array
from util import between


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = Array.indexed(1, n1 + 1)
    R = Array.indexed(1, n2 + 1)
    for i in between(1, n1):
        L[i] = A[p + i - 1]
    for j in between(1, n2):
        R[j] = A[q + j]
    L[n1 + 1] = math.inf
    R[n2 + 1] = math.inf
    i = 1
    j = 1
    for k in between(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def merge_sort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
