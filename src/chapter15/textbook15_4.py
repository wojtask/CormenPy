from datastructures.array import Array
from util import between


def lcs_length(X, Y):
    m = X.length
    n = Y.length
    c = Array([Array.indexed(0, n) for _ in between(0, m)], start=0)
    b = Array([Array.indexed(1, n) for _ in between(1, m)])
    for i in between(1, m):
        c[i, 0] = 0
    for j in between(0, n):
        c[0, j] = 0
    for i in between(1, m):
        for j in between(1, n):
            if X[i] == Y[j]:
                c[i, j] = c[i - 1, j - 1] + 1
                b[i, j] = '↖'
            else:
                if c[i - 1, j] >= c[i, j - 1]:
                    c[i, j] = c[i - 1, j]
                    b[i, j] = '↑'
                else:
                    c[i, j] = c[i, j - 1]
                    b[i, j] = '←'
    return c, b


def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i, j] == '↖':
        print_lcs(b, X, i - 1, j - 1)
        print(X[i], end='')
    elif b[i, j] == '↑':
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)
