import math

from datastructures.array import Array
from util import between


def _sort_by_x_coordinates(points):
    points.elements = sorted(points.elements, key=lambda p: p.x)


def _distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def bitonic_tsp(p):
    n = p.length
    _sort_by_x_coordinates(p)
    b = Array(Array.indexed(1, n) for _ in between(1, n))
    r = Array(Array.indexed(1, n) for _ in between(1, n))
    b[1, 1] = 0
    for j in between(2, n):
        for i in between(1, j):
            if i == 1 or i < j - 1:
                b[i, j] = b[i, j - 1] + _distance(p[j - 1], p[j])
                r[i, j] = j - 1
            else:
                b[i, j] = math.inf
                for k in between(1, i - 1):
                    q = b[k, i] + _distance(p[k], p[j])
                    if q < b[i, j]:
                        b[i, j] = q
                        r[i, j] = k
    return b, r


def print_bitonic_path(p, r):
    n = p.length
    print(p[n])
    print(p[n - 1])
    print_path(p, r, n - 1, n)


def print_path(p, r, i, j):
    if i < j and (i > 1 or r[i, j] > 1):
        print_path(p, r, i, r[i, j])
        print(p[r[i, j]])
    if i > j and (j > 1 or r[j, i] > 1):
        print(p[r[j, i]])
        print_path(p, r, r[j, i], j)
