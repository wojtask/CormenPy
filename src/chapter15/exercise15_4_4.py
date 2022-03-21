from datastructures.array import Array
from util import between


def lcs_length_(X, Y):
    m = X.length
    n = Y.length
    if m < n:
        return lcs_length_(Y, X)
    c = Array.of(Array.indexed(0, n), Array.indexed(0, n), start=0)
    for j in between(0, n):
        c[0, j] = 0
    c[1, 0] = 0
    for i in between(1, m):
        for j in between(1, n):
            if X[i] == Y[j]:
                c[1, j] = c[0, j - 1] + 1
            else:
                c[1, j] = max(c[1, j - 1], c[0, j])
        for j in between(1, n):
            c[0, j] = c[1, j]
    return c[1, n]


def lcs_length__(X, Y):
    m = X.length
    n = Y.length
    if m < n:
        return lcs_length__(Y, X)
    C = Array.indexed(0, n)
    for j in between(0, n):
        C[j] = 0
    for i in between(1, m):
        p = C[0]
        for j in between(1, n):
            r = C[j]
            if X[i] == Y[j]:
                C[j] = p + 1
            else:
                C[j] = max(C[j], C[j - 1])
            p = r
    return C[n]
