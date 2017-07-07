import math

from datastructures.array import Array
from util import between, rbetween


def insertion_sort(A):
    for j in between(2, A.length):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = Array.of_length(n1 + 1)
    R = Array.of_length(n2 + 1)
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
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


def bubble_sort(A):
    for i in between(1, A.length):
        for j in rbetween(A.length, i + 1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]


def horner(a, x):
    y = 0.0
    i = a.length - 1
    while i >= 0:
        y = a[i] + x * y
        i = i - 1
    return y
