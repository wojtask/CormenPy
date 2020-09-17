from datastructures.b_tree import disk_read, allocate_node, disk_write


def b_tree_search(x, k):
    i = 1
    while i <= x.n and k > x.key[i]:
        i = i + 1
    if i <= x.n and k == x.key[i]:
        return x, i
    if x.leaf:
        return None
    else:
        disk_read(x.c[i])
        return b_tree_search(x.c[i], k)


def b_tree_create(T):
    x = allocate_node()
    x.leaf = True
    x.n = 0
    disk_write(x)
    T.root = x
