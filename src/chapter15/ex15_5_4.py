import math

from datastructures.array import Array
from util import between


def effective_optimal_bst(p, q, n):
    e = Array([Array.indexed(0, n) for _ in between(1, n + 1)])
    w = Array([Array.indexed(0, n) for _ in between(1, n + 1)])
    root = Array([Array.indexed(1, n) for _ in between(1, n)])
    for i in between(1, n + 1):
        e[i, i - 1] = q[i - 1]
        w[i, i - 1] = q[i - 1]
    for i in between(1, n):
        w[i, i] = w[i, i - 1] + p[i] + q[i]
        e[i, i] = e[i, i - 1] + e[i + 1, i] + w[i, i]
        root[i, i] = i
    for l in between(2, n):
        for i in between(1, n - l + 1):
            j = i + l - 1
            e[i, j] = math.inf
            w[i, j] = w[i, j - 1] + p[j] + q[j]
            for r in between(root[i, j - 1], root[i + 1, j]):
                t = e[i, r - 1] + e[r + 1, j] + w[i, j]
                if t < e[i, j]:
                    e[i, j] = t
                    root[i, j] = r
    return e, root
