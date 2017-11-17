from datastructures.array import Array
from util import between


def lcs_length_(X, Y):
    m = X.length
    n = Y.length
    if m < n:
        return lcs_length_(Y, X)
    c = Array([Array.indexed(0, n), Array.indexed(0, n)], start=0)
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
    c = Array.indexed(0, n)
    for j in between(0, n):
        c[j] = 0
    for i in between(1, m):
        p = c[0]
        for j in between(1, n):
            r = c[j]
            if X[i] == Y[j]:
                c[j] = p + 1
            else:
                c[j] = max(c[j], c[j - 1])
            p = r
    return c[n]
