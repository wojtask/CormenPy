from datastructures.standard_array import StandardArray
from util import between


def lcs_length_(X, Y):
    m = X.length
    n = Y.length
    if m < n:
        return lcs_length_(Y, X)
    c = StandardArray.of_length(n + 1)
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
