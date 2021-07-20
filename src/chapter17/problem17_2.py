from chapter02.exercise2_3_5 import iterative_binary_search
from chapter02.textbook2_3 import merge
from datastructures.array import Array
from util import between


def dynamic_binary_search(A, x):
    k = A.length
    for i in between(0, k - 1):
        if A.length != 0:
            j = iterative_binary_search(A[i], x)
            if j is not None:
                return i, j
    return None


def dynamic_binary_insert(A, x):
    B = Array(x)
    i = 0
    while A[i].length != 0:
        B = Array(A[i].elements + B.elements)
        merge(B, 1, A[i].length, B.length)
        A[i] = Array()
        i += 1
    A[i] = Array(B.elements)


def dynamic_binary_delete(A, x):
    i = 0
    while A[i].length == 0:
        i += 1
    y = A[i][2 ** i]
    j = -1
    l = None
    while l is None:
        j += 1
        l = iterative_binary_search(A[j], x)
    A[j][l] = y
    while l > 1 and A[j][l] < A[j][l - 1]:
        A[j][l], A[j][l - 1] = A[j][l - 1], A[j][l]
    while l < A[j].length and A[j][l] > A[j][l + 1]:
        A[j][l], A[j][l + 1] = A[j][l + 1], A[j][l]
    for r in between(0, i - 1):
        A[r] = Array.indexed(1, 2 ** r)
        for t in between(1, 2 ** r):
            A[r][t] = A[i][2 ** r - 1 + t]
    A[i] = Array()
