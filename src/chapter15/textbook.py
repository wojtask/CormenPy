import math

from datastructures.matrix import Matrix
from util import between, rbetween


def fastest_way(a, t, e, x, n):
    f = Matrix.of_dimensions(2, n)
    l = Matrix.of_dimensions(2, n)
    f[1, 1] = e[1] + a[1, 1]
    f[2, 1] = e[2] + a[2, 1]
    for j in between(2, n):
        if f[1, j - 1] + a[1, j] <= f[2, j - 1] + t[2, j - 1] + a[1, j]:
            f[1, j] = f[1, j - 1] + a[1, j]
            l[1, j] = 1
        else:
            f[1, j] = f[2, j - 1] + t[2, j - 1] + a[1, j]
            l[1, j] = 2
        if f[2, j - 1] + a[2, j] <= f[1, j - 1] + t[1, j - 1] + a[2, j]:
            f[2, j] = f[2, j - 1] + a[2, j]
            l[2, j] = 2
        else:
            f[2, j] = f[1, j - 1] + t[1, j - 1] + a[2, j]
            l[2, j] = 1
    if f[1, n] + x[1] <= f[2, n] + x[2]:
        f_star = f[1, n] + x[1]
        l_star = 1
    else:
        f_star = f[2, n] + x[2]
        l_star = 2
    return f_star, l, l_star


def print_stations(l, l_star, n):
    i = l_star
    print('line ' + str(i) + ', station ' + str(n))
    for j in rbetween(n, 2):
        i = l[i, j]
        print('line ' + str(i) + ', station ' + str(j - 1))


def matrix_multiply(A, B):
    if A.columns != B.rows:
        raise RuntimeError('incompatible dimensions')
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
    m = Matrix.of_dimensions(n, n)
    s = Matrix.of_dimensions(n, n)
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


def recursive_matrix_chain(p, m, i, j):
    if i == j:
        return 0
    m[i, j] = math.inf
    for k in between(i, j - 1):
        q = recursive_matrix_chain(p, m, i, k) + recursive_matrix_chain(p, m, k + 1, j) + p[i - 1] * p[k] * p[j]
        if q < m[i, j]:
            m[i, j] = q
    return m[i, j]


def memoized_matrix_chain(p):
    n = p.length - 1
    m = Matrix.of_dimensions(n, n)
    for i in between(1, n):
        for j in between(i, n):
            m[i, j] = math.inf
    return lookup_chain(p, m, 1, n)


def lookup_chain(p, m, i, j):
    if m[i, j] < math.inf:
        return m[i, j]
    if i == j:
        m[i, j] = 0
    else:
        for k in between(i, j - 1):
            q = lookup_chain(p, m, i, k) + lookup_chain(p, m, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q < m[i, j]:
                m[i, j] = q
    return m[i, j]


def lcs_length(X, Y):
    m = X.length
    n = Y.length
    c = Matrix.of_dimensions(m + 1, n + 1, first_row=0, first_column=0)
    b = Matrix.of_dimensions(m, n)
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
