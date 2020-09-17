from datastructures.b_tree import disk_read, allocate_node, disk_write
from util import between, rbetween


def b_tree_search(x, k):
    i = 1
    while i <= x.n and k > x.key[i]:
        i += 1
    if i <= x.n and k == x.key[i]:
        return x, i
    if x.leaf:
        return None
    else:
        disk_read(x.c[i])
        return b_tree_search(x.c[i], k)


def b_tree_create(T, t=2):
    x = allocate_node(t)
    x.leaf = True
    x.n = 0
    disk_write(x)
    T.root = x


def b_tree_split_child(x, i, y, t=2):
    z = allocate_node(t)
    z.leaf = y.leaf
    z.n = t - 1
    for j in between(1, t - 1):
        z.key[j] = y.key[j + t]
    if not y.leaf:
        for j in between(1, t):
            z.c[j] = y.c[j + t]
    y.n = t - 1
    for j in rbetween(x.n + 1, i + 1):
        x.c[j + 1] = x.c[j]
    x.c[i + 1] = z
    for j in rbetween(x.n, i):
        x.key[j + 1] = x.key[j]
    x.key[i] = y.key[t]
    x.n += 1
    disk_write(y)
    disk_write(z)
    disk_write(x)
