import math

from datastructures.array import Array
from util import between


def lmis_length(X):
    n = X.length
    a = Array.indexed(0, n)
    b = Array.indexed(1, n)
    for i in between(0, n):
        a[i] = 0
    m = 0
    for i in between(1, n):
        k = 1
        l = m
        while k <= l:
            j = math.floor((k + l) / 2)
            if X[a[j]] <= X[i]:
                k = j + 1
            else:
                l = j - 1
        a[k] = i
        b[i] = a[k - 1]
        if k > m:
            m = k
    return m, b, a[m]


def print_lmis(b, X, i):
    if b[i] > 0:
        print_lmis(b, X, b[i])
    print(X[i])
