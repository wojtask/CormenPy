import math

from datastructures.array import Array
from util import between


def edit_distance(x, y, cost):
    m = x.length
    n = y.length
    c = Array(Array.indexed(0, n) for _ in between(0, m))
    op = Array(Array.indexed(0, n) for _ in between(0, m))
    l = Array(Array.indexed(0, n) for _ in between(0, m))
    r = Array(Array.indexed(0, n) for _ in between(0, m))
    for i in between(0, m):
        c[i, 0] = i * cost['delete']
        (op[i, 0], l[i, 0], r[i, 0]) = ('delete', i - 1, 0)
    for j in between(1, n):
        c[0, j] = j * cost['insert']
        (op[0, j], l[0, j], r[0, j]) = ('insert ' + y[j], 0, j - 1)
    for i in between(1, m):
        for j in between(1, n):
            c[i, j] = math.inf
            if x[i] == y[j]:
                c[i, j] = c[i - 1, j - 1] + cost['copy']
                (op[i, j], l[i, j], r[i, j]) = ('copy', i - 1, j - 1)
            if x[i] != y[j] and c[i - 1, j - 1] + cost['replace'] < c[i, j]:
                c[i, j] = c[i - 1, j - 1] + cost['replace']
                (op[i, j], l[i, j], r[i, j]) = ('replace by ' + y[j], i - 1, j - 1)
            if c[i - 1, j] + cost['delete'] < c[i, j]:
                c[i, j] = c[i - 1, j] + cost['delete']
                (op[i, j], l[i, j], r[i, j]) = ('delete', i - 1, j)
            if c[i, j - 1] + cost['insert'] < c[i, j]:
                c[i, j] = c[i, j - 1] + cost['insert']
                (op[i, j], l[i, j], r[i, j]) = ('insert ' + y[j], i, j - 1)
            if i >= 2 and j >= 2 and x[i] == y[j - 1] and x[i - 1] == y[j] \
                    and c[i - 2, j - 2] + cost['twiddle'] < c[i, j]:
                c[i, j] = c[i - 2, j - 2] + cost['twiddle']
                (op[i, j], l[i, j], r[i, j]) = ('twiddle', i - 2, j - 2)
    for k in between(0, m - 1):
        if c[k, n] + cost['kill'] < c[m, n]:
            c[m, n] = c[k, n] + cost['kill']
            (op[m, n], l[m, n], r[m, n]) = ('kill', k, n)
    return c, op, l, r


def print_operations(op, l, r, i, j):
    if i > 0 or j > 0:
        print_operations(op, l, r, l[i, j], r[i, j])
        print(op[i, j])


def optimal_alignment(x, y):
    cost = {'copy': -1, 'replace': 1, 'insert': 2, 'delete': 2, 'twiddle': math.inf, 'kill': math.inf}
    c, op, l, r = edit_distance(x, y, cost)
    return -c[x.length, y.length], op, l, r
