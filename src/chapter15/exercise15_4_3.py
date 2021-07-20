import math

from datastructures.array import Array
from util import between


def memoized_lcs_length(X, Y):
    m = X.length
    n = Y.length
    c = Array((Array.indexed(0, n) for _ in between(0, m)), start=0)
    for i in between(0, m):
        for j in between(0, n):
            c[i, j] = math.inf
    return lookup_lcs(c, X, Y, m, n)


def lookup_lcs(c, X, Y, i, j):
    if c[i, j] < math.inf:
        return c[i, j]
    if i == 0 or j == 0:
        c[i, j] = 0
    elif X[i] == Y[j]:
        c[i, j] = lookup_lcs(c, X, Y, i - 1, j - 1) + 1
    else:
        c[i, j] = max(lookup_lcs(c, X, Y, i, j - 1), lookup_lcs(c, X, Y, i - 1, j))
    return c[i, j]
