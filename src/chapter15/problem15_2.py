import math

from datastructures.array import Array
from util import between


def break_lines(l, M):
    n = l.length
    L = Array.indexed(0, n)
    L[0] = 0
    for i in between(1, n):
        L[i] = L[i - 1] + l[i]
    c = Array.indexed(0, n)
    p = Array.indexed(1, n)
    c[0] = 0
    for j in between(1, n):
        c[j] = math.inf
        j0 = max(1, j - math.ceil(M / 2) + 1)
        for i in between(j0, j):
            extras = M - j + i - (L[j] - L[i - 1])
            if extras < 0:
                lc = math.inf
            elif j == n:
                lc = 0
            else:
                lc = extras ** 3
            if c[i - 1] + lc < c[j]:
                c[j] = c[i - 1] + lc
                p[j] = i
    return c, p


def print_lines(p, j):
    if p[j] > 1:
        print_lines(p, p[j] - 1)
    print(p[j])
