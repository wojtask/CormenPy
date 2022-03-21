from datastructures.array import Array
from util import between, rbetween


def fastest_way(a, t, e, x, n):
    f = Array.of(Array.indexed(1, n), Array.indexed(1, n))
    l = Array.of(Array.indexed(1, n), Array.indexed(1, n))
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
