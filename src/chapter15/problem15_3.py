import math
from enum import Enum, auto

from datastructures.array import Array
from util import between


class EditOperation(Enum):
    COPY = auto()
    REPLACE = auto()
    DELETE = auto()
    INSERT = auto()
    TWIDDLE = auto()
    KILL = auto()


def edit_distance(x, y, cost):
    m = x.length
    n = y.length
    c = Array([Array.indexed(0, n) for _ in between(0, m)], start=0)
    op = Array([Array.indexed(0, n) for _ in between(0, m)], start=0)
    l = Array([Array.indexed(0, n) for _ in between(0, m)], start=0)
    r = Array([Array.indexed(0, n) for _ in between(0, m)], start=0)
    for i in between(0, m):
        c[i, 0] = i * cost[EditOperation.DELETE]
        (op[i, 0], l[i, 0], r[i, 0]) = ('delete', i - 1, 0)
    for j in between(1, n):
        c[0, j] = j * cost[EditOperation.INSERT]
        (op[0, j], l[0, j], r[0, j]) = ('insert ' + y[j], 0, j - 1)
    for i in between(1, m):
        for j in between(1, n):
            c[i, j] = math.inf
            if x[i] == y[j]:
                c[i, j] = c[i - 1, j - 1] + cost[EditOperation.COPY]
                (op[i, j], l[i, j], r[i, j]) = ('copy', i - 1, j - 1)
            if x[i] != y[j] and c[i - 1, j - 1] + cost[EditOperation.REPLACE] < c[i, j]:
                c[i, j] = c[i - 1, j - 1] + cost[EditOperation.REPLACE]
                (op[i, j], l[i, j], r[i, j]) = ('replace by ' + y[j], i - 1, j - 1)
            if c[i - 1, j] + cost[EditOperation.DELETE] < c[i, j]:
                c[i, j] = c[i - 1, j] + cost[EditOperation.DELETE]
                (op[i, j], l[i, j], r[i, j]) = ('delete', i - 1, j)
            if c[i, j - 1] + cost[EditOperation.INSERT] < c[i, j]:
                c[i, j] = c[i, j - 1] + cost[EditOperation.INSERT]
                (op[i, j], l[i, j], r[i, j]) = ('insert ' + y[j], i, j - 1)
            if i >= 2 and j >= 2 and x[i] == y[j - 1] and x[i - 1] == y[j] \
                    and c[i - 2, j - 2] + cost[EditOperation.TWIDDLE] < c[i, j]:
                c[i, j] = c[i - 2, j - 2] + cost[EditOperation.TWIDDLE]
                (op[i, j], l[i, j], r[i, j]) = ('twiddle', i - 2, j - 2)
    for k in between(0, m - 1):
        if c[k, n] + cost[EditOperation.KILL] < c[m, n]:
            c[m, n] = c[k, n] + cost[EditOperation.KILL]
            (op[m, n], l[m, n], r[m, n]) = ('kill', k, n)
    return c, op, l, r


def print_operations(op, l, r, i, j):
    if i > 0 or j > 0:
        print_operations(op, l, r, l[i, j], r[i, j])
        print(op[i, j])


def optimal_alignment(x, y):
    cost = {EditOperation.COPY: -1,
            EditOperation.REPLACE: 1,
            EditOperation.INSERT: 2,
            EditOperation.DELETE: 2,
            EditOperation.TWIDDLE: math.inf,
            EditOperation.KILL: math.inf}
    c, op, l, r = edit_distance(x, y, cost)
    return -c[x.length, y.length], op, l, r
