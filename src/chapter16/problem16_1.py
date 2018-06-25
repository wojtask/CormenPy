import math

from datastructures.array import Array
from util import rbetween, between


def greedy_make_change(n):
    C = Array.indexed(1, 6)
    d = Array([1, 2, 5, 10, 20, 50])
    for i in rbetween(d.length, 1):
        C[i] = math.floor(n / d[i])
        n %= d[i]
    return C


def make_change(n, d):
    c = Array.indexed(0, n)
    denom = Array.indexed(1, n)
    c[0] = 0
    for j in between(1, n):
        c[j] = math.inf
        for i in between(1, d.length):
            if j >= d[i] and 1 + c[j - d[i]] < c[j]:
                c[j] = 1 + c[j - d[i]]
                denom[j] = d[i]
    return c, denom


def print_change(n, denom):
    while n > 0:
        print(denom[n])
        n = n - denom[n]
