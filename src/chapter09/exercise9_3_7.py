from chapter09.textbook9_3 import select
from datastructures.array import Array
from util import between


def median_neighbors(A, k):
    n = A.length
    l = (n + 1) // 2 - (k - 1) // 2
    select(A, 1, n, l)
    select(A, l, n, k)
    return A[l:l + k - 1]


def closest_to_median(A, k):
    n = A.length
    x = select(A, 1, n, (n + 1) // 2)
    D = Array.indexed(1, n)
    for i in between(1, n):
        D[i] = abs(A[i] - x)
    dk = select(D, 1, n, k)
    C = set()
    for i in between(1, n):
        if abs(A[i] - x) <= dk:
            C.add(A[i])
    if len(C) == k + 1:
        C.remove(x + dk)
    return C
