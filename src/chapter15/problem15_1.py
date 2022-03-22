import math

from datastructures.array import Array
from util import between


def _distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def bitonic_tsp(P):
    n = P.length
    P.sort(key=lambda p: p.x)
    b = Array(Array.indexed(1, n) for _ in between(1, n))
    r = Array(Array.indexed(1, n) for _ in between(1, n))
    b[1, 1] = 0
    for j in between(2, n):
        for i in between(1, j):
            if i == 1 or i < j - 1:
                b[i, j] = b[i, j - 1] + _distance(P[j - 1], P[j])
                r[i, j] = j - 1
            else:
                b[i, j] = math.inf
                for k in between(1, i - 1):
                    q = b[k, i] + _distance(P[k], P[j])
                    if q < b[i, j]:
                        b[i, j] = q
                        r[i, j] = k
    return b, r


def print_bitonic_path(P, r):
    n = P.length
    print(P[n])
    print(P[n - 1])
    print_path(P, r, n - 1, n)


def print_path(P, r, i, j):
    if i < j and (i > 1 or r[i, j] > 1):
        print_path(P, r, i, r[i, j])
        print(P[r[i, j]])
    if i > j and (j > 1 or r[j, i] > 1):
        print(P[r[j, i]])
        print_path(P, r, r[j, i], j)
