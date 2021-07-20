import math

from datastructures.array import Array
from util import between


def young_extract_min(Y, m, n, i, j):
    if (i, j) == (m, n):
        y = Y[i, j]
        Y[i, j] = math.inf
        return y
    (i_, j_) = (i, j + 1)
    if i < m:
        if j == n or Y[i + 1, j] < Y[i, j + 1]:
            (i_, j_) = (i + 1, j)
    Y[i, j], Y[i_, j_] = Y[i_, j_], Y[i, j]
    return young_extract_min(Y, m, n, i_, j_)


def youngify(Y, i, j):
    (i_, j_) = (i, j)
    if i > 1 and Y[i - 1, j] > Y[i_, j_]:
        (i_, j_) = (i - 1, j)
    if j > 1 and Y[i, j - 1] > Y[i_, j_]:
        (i_, j_) = (i, j - 1)
    if (i_, j_) != (i, j):
        Y[i, j], Y[i_, j_] = Y[i_, j_], Y[i, j]
        youngify(Y, i_, j_)


def young_insert(Y, m, n, key):
    Y[m, n] = key
    youngify(Y, m, n)


def young_sort(A):
    n = int(math.sqrt(A.length))
    Y = Array(Array([math.inf] * n) for _ in between(1, n))
    for i in between(1, n ** 2):
        young_insert(Y, n, n, A[i])
    for i in between(1, n ** 2):
        A[i] = young_extract_min(Y, n, n, 1, 1)


def young_search(Y, m, n, v):
    i = 1
    j = n
    while i <= m and j >= 1:
        if v == Y[i, j]:
            return True
        if v > Y[i, j]:
            i += 1
        else:
            j -= 1
    return False
