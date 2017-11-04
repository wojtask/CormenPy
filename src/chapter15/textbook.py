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
    return f_star, l_star, l


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
