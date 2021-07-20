import math

from datastructures.array import Array
from datastructures.matrix import Matrix
from util import between


def matrix_multiply(A, B):
    if A.columns != B.rows:
        raise ValueError('incompatible dimensions')
    else:
        C = Matrix.of_dimensions(A.rows, B.columns)
        for i in between(1, A.rows):
            for j in between(1, B.columns):
                C[i, j] = 0
                for k in between(1, A.columns):
                    C[i, j] = C[i, j] + A[i, k] * B[k, j]
        return C


def matrix_chain_order(p):
    n = p.length - 1
    m = Array(Array.indexed(1, n) for _ in between(1, n))
    s = Array(Array.indexed(1, n) for _ in between(1, n))
    for i in between(1, n):
        m[i, i] = 0
    for l in between(2, n):
        for i in between(1, n - l + 1):
            j = i + l - 1
            m[i, j] = math.inf
            for k in between(i, j - 1):
                q = m[i, k] + m[k + 1, j] + p[i - 1] * p[k] * p[j]
                if q < m[i, j]:
                    m[i, j] = q
                    s[i, j] = k
    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print('A' + str(i), end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s[i, j])
        print_optimal_parens(s, s[i, j] + 1, j)
        print(')', end='')
