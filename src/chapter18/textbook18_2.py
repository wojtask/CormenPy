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


def b_tree_insert(T, k, t=2):
    r = T.root
    if r.n == 2 * t - 1:
        s = allocate_node(t)
        T.root = s
        s.leaf = False
        s.n = 0
        s.c[1] = r
        b_tree_split_child(s, 1, r, t)
        b_tree_insert_nonfull(s, k, t)
    else:
        b_tree_insert_nonfull(r, k, t)


def b_tree_insert_nonfull(x, k, t=2):
    i = x.n
    if x.leaf:
        while i >= 1 and k < x.key[i]:
            x.key[i + 1] = x.key[i]
            i -= 1
        x.key[i + 1] = k
        x.n += 1
        disk_write(x)
    else:
        while i >= 1 and k < x.key[i]:
            i -= 1
        i += 1
        disk_read(x.c[i])
        if x.c[i].n == 2 * t - 1:
            b_tree_split_child(x, i, x.c[i], t)
            if k > x.key[i]:
                i += 1
        b_tree_insert_nonfull(x.c[i], k, t)
