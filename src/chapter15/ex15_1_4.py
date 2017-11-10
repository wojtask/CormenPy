from datastructures.matrix import Matrix
from util import between


def fastest_way_(a, t, e, x, n):
    f = Matrix.of_dimensions(2, 2)
    l = Matrix.of_dimensions(2, n)
    f[1, 2] = e[1] + a[1, 1]
    f[2, 2] = e[2] + a[2, 1]
    for j in between(2, n):
        f[1, 1] = f[1, 2]
        f[2, 1] = f[2, 2]
        if f[1, 1] + a[1, j] <= f[2, 1] + t[2, j - 1] + a[1, j]:
            f[1, 2] = f[1, 1] + a[1, j]
            l[1, j] = 1
        else:
            f[1, 2] = f[2, 1] + t[2, j - 1] + a[1, j]
            l[1, j] = 2
        if f[2, 1] + a[2, j] <= f[1, 1] + t[1, j - 1] + a[2, j]:
            f[2, 2] = f[2, 1] + a[2, j]
            l[2, j] = 2
        else:
            f[2, 2] = f[1, 1] + t[1, j - 1] + a[2, j]
            l[2, j] = 1
    if f[1, 2] + x[1] <= f[2, 2] + x[2]:
        f_star = f[1, 2] + x[1]
        l_star = 1
    else:
        f_star = f[2, 2] + x[2]
        l_star = 2
    return f_star, l_star, l
