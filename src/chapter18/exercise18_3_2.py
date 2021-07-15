from datastructures.b_tree import disk_read, disk_write, free_node
from util import between, rbetween


def b_tree_left_shift(x, i):
    for j in between(i, x.n - 1):
        x.key[j] = x.key[j + 1]
    if not x.leaf:
        for j in between(i, x.n):
            x.c[j] = x.c[j + 1]
    x.n -= 1
    disk_write(x)


def b_tree_right_shift(x, i):
    x.n += 1
    for j in rbetween(x.n - 1, i):
        x.key[j + 1] = x.key[j]
    if not x.leaf:
        for j in rbetween(x.n, i):
            x.c[j + 1] = x.c[j]
    disk_write(x)


def b_tree_left_rotate(x, i, y, z):
    y.n += 1
    y.key[y.n] = x.key[i]
    x.key[i] = z.key[1]
    if not y.leaf:
        y.c[y.n + 1] = z.c[1]
    b_tree_left_shift(z, 1)
    disk_write(x)


def b_tree_right_rotate(x, i, y, z):
    b_tree_right_shift(z, 1)
    z.key[1] = x.key[i]
    x.key[i] = y.key[y.n]
    if not z.leaf:
        z.c[1] = y.c[y.n + 1]
    y.n -= 1
    disk_write(x)
    disk_write(y)


def b_tree_merge_children(x, i, y, z, t=2):
    y.n = 2 * t - 1
    y.key[t] = x.key[i]
    for j in between(1, t - 1):
        y.key[j + t] = z.key[j]
    if not y.leaf:
        for j in between(1, t):
            y.c[j + t] = z.c[j]
    b_tree_left_shift(x, i)
    x.c[i] = y
    disk_write(x)
    disk_write(y)
    free_node(z)


def b_tree_delete_minimum(x, t=2):
    if x.leaf:
        min = x.key[1]
        b_tree_left_shift(x, 1)
        return min
    y = x.c[1]
    disk_read(y)
    if y.n == t - 1:
        z = x.c[2]
        disk_read(z)
        if z.n >= t:
            b_tree_left_rotate(x, 1, y, z)
        else:
            b_tree_merge_children(x, 1, y, z, t)
    return b_tree_delete_minimum(y, t)


def b_tree_delete_maximum(x, t=2):
    if x.leaf:
        max = x.key[x.n]
        x.n -= 1
        disk_write(x)
        return max
    y = x.c[x.n + 1]
    disk_read(y)
    if y.n == t - 1:
        z = x.c[x.n]
        disk_read(z)
        if z.n >= t:
            b_tree_right_rotate(x, x.n, z, y)
        else:
            b_tree_merge_children(x, x.n, z, y, t)
            y = z
    return b_tree_delete_maximum(y, t)


def b_tree_safe_delete(x, k, t=2):
    i = 1
    while i <= x.n and k > x.key[i]:
        i += 1
    if i <= x.n and k == x.key[i]:
        if x.leaf:
            b_tree_left_shift(x, i)
        else:
            y = x.c[i]
            disk_read(y)
            if y.n >= t:
                x.key[i] = b_tree_delete_maximum(y, t)
                disk_write(x)
            else:
                z = x.c[i + 1]
                disk_read(z)
                if z.n >= t:
                    x.key[i] = b_tree_delete_minimum(z, t)
                    disk_write(x)
                else:
                    b_tree_merge_children(x, i, y, z, t)
                    b_tree_safe_delete(y, k, t)
    else:
        y = x.c[i]
        disk_read(y)
        if y.n == t - 1:
            z_L = z_R = None
            if i >= 2:
                z_L = x.c[i - 1]
                disk_read(z_L)
            if i <= x.n:
                z_R = x.c[i + 1]
                disk_read(z_R)
            if z_L is not None and z_L.n >= t:
                b_tree_right_rotate(x, i - 1, z_L, y)
            elif z_R is not None and z_R.n >= t:
                b_tree_left_rotate(x, i, y, z_R)
            elif z_L is not None:
                b_tree_merge_children(x, i - 1, z_L, y, t)
                y = z_L
            else:
                b_tree_merge_children(x, i, y, z_R, t)
        b_tree_safe_delete(y, k, t)


def b_tree_delete(T, k, t=2):
    r = T.root
    b_tree_safe_delete(r, k, t)
    if r.n == 0 and not r.leaf:
        T.root = r.c[1]
        free_node(r)
