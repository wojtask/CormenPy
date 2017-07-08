import math

from datastructures.standard_array import StandardArray
from util import between, rbetween


def counting_sort(A, B, k):
    C = StandardArray.of_length(k + 1)
    for i in between(0, k):
        C[i] = 0
    for j in between(1, A.length):
        C[A[j]] = C[A[j]] + 1
    for i in between(1, k):
        C[i] = C[i] + C[i - 1]
    for j in rbetween(A.length, 1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1


def unstable_counting_sort(A, B, k):
    C = StandardArray.of_length(k + 1)
    for i in between(0, k):
        C[i] = 0
    for j in between(1, A.length):
        C[A[j]] = C[A[j]] + 1
    for i in between(1, k):
        C[i] = C[i] + C[i - 1]
    for j in between(1, A.length):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1


def radix_sort(A, d):
    for i in between(1, d):
        _stable_sort_on_digit(A, i)


def _stable_sort_on_digit(A, digit):
    A.data.sort(key=lambda x: _get_digit(x, digit))


def _get_digit(number, digit):
    power_of_10 = 10 ** (digit - 1)
    return number // power_of_10 % 10


def bucket_sort(A):
    n = A.length
    B = StandardArray([[] for _ in range(n)])
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
    A.data = [x for L in B for x in L]
