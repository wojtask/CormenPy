import math

from datastructures.array import Array
from util import between


def checkerboard(n, p):
    g = Array(Array.indexed(1, n) for _ in between(1, n))
    m = Array(Array.indexed(1, n) for _ in between(1, n))
    for j in between(1, n):
        g[1, j] = 0
    for i in between(2, n):
        for j in between(1, n):
            g[i, j] = g[i - 1, j] + p((i - 1, j), (i, j))
            m[i, j] = j
            if j > 1 and g[i - 1, j - 1] + p((i - 1, j - 1), (i, j)) > g[i, j]:
                g[i, j] = g[i - 1, j - 1] + p((i - 1, j - 1), (i, j))
                m[i, j] = j - 1
            if j < n and g[i - 1, j + 1] + p((i - 1, j + 1), (i, j)) > g[i, j]:
                g[i, j] = g[i - 1, j + 1] + p((i - 1, j + 1), (i, j))
                m[i, j] = j + 1
    max_gain = -math.inf
    m_star = 1
    for j in between(1, n):
        if g[n, j] > max_gain:
            max_gain = g[n, j]
            m_star = j
    return max_gain, m, m_star


def print_moves(m, i, j):
    if i > 1:
        print_moves(m, i - 1, m[i, j])
    print('(' + str(i) + ', ' + str(j) + ')')
