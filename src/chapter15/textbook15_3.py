import math

from datastructures.array import Array
from util import between


def recursive_matrix_chain(p, m, i, j):
    if i == j:
        return 0
    m[i, j] = math.inf
    for k in between(i, j - 1):
        q = recursive_matrix_chain(p, m, i, k) + recursive_matrix_chain(p, m, k + 1, j) + p[i - 1] * p[k] * p[j]
        if q < m[i, j]:
            m[i, j] = q
    return m[i, j]


def memoized_matrix_chain(p):
    n = p.length - 1
    m = Array(Array.indexed(1, n) for _ in between(1, n))
    for i in between(1, n):
        for j in between(i, n):
            m[i, j] = math.inf
    return lookup_chain(p, m, 1, n)


def lookup_chain(p, m, i, j):
    if m[i, j] < math.inf:
        return m[i, j]
    if i == j:
        m[i, j] = 0
    else:
        for k in between(i, j - 1):
            q = lookup_chain(p, m, i, k) + lookup_chain(p, m, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < m[i, j]:
                m[i, j] = q
    return m[i, j]
