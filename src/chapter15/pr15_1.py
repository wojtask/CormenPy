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
    b = Array([Array.indexed(1, n) for _ in between(1, n)])
    r = Array([Array.indexed(1, n) for _ in between(1, n)])
    b[1, 2] = _distance(p[1], p[2])
    r[1, 2] = 1
    for j in between(3, n):
        for i in between(1, j - 2):
            b[i, j] = b[i, j - 1] + _distance(p[j - 1], p[j])
            r[i, j] = j - 1
        b[j - 1, j] = math.inf
        for k in between(1, j - 2):
            q = b[k, j - 1] + _distance(p[k], p[j])
            if q < b[j - 1, j]:
                b[j - 1, j] = q
                r[j - 1, j] = k
    b[n, n] = b[n - 1, n] + _distance(p[n - 1], p[n])
    return b, r


def print_bitonic_tour(p, r):
    n = p.length
    print(p[n])
    print(p[n - 1])
    print_bitonic_path(p, r, n - 1, n)


def print_bitonic_path(p, r, i, j):
    if i < j:
        k = r[i, j]
        if i > 1 or k > 1:
            print_bitonic_path(p, r, i, k)
            print(p[k])
    else:
        k = r[j, i]
        if j > 1 or k > 1:
            print(p[k])
            print_bitonic_path(p, r, k, j)
