import math

from datastructures.array import Array
from util import between


def count_inversions(A, p, r):
    inversions = 0
    if p < r:
        q = (p + r) // 2
        inversions = inversions + count_inversions(A, p, q)
        inversions = inversions + count_inversions(A, q + 1, r)
        inversions = inversions + merge_inversions(A, p, q, r)
    return inversions


def merge_inversions(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = Array.of_length(n1 + 1)
    R = Array.of_length(n2 + 1)
    for i in between(1, n1):
        L[i] = A[p + i - 1]
    for j in between(1, n2):
        R[j] = A[q + j]
    L[n1 + 1] = R[n2 + 1] = math.inf
    i = j = 1
    inversions = 0
    for k in between(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
            inversions = inversions + n1 - i + 1
    return inversions
