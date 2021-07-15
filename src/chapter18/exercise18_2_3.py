from datastructures.b_tree import disk_read


def b_tree_minimum(x):
    while not x.leaf:
        disk_read(x.c[1])
        x = x.c[1]
    return x.key[1]


def b_tree_maximum(x):
    while not x.leaf:
        disk_read(x.c[x.n + 1])
        x = x.c[x.n + 1]
    return x.key[x.n]


def b_tree_predecessor(T, x, i):
    if not x.leaf:
        disk_read(x.c[i])
        return b_tree_maximum(x.c[i])
    if i > 1:
        return x.key[i - 1]
    k = x.key[i]
    k_ = None
    y = T.root
    while y != x:
        j = 1
        while j <= y.n and k > y.key[j]:
            j += 1
        if j > 1:
            k_ = y.key[j - 1]
        disk_read(y.c[j])
        y = y.c[j]
    return k_
