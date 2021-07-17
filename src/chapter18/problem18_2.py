from datastructures.b_tree import Node234, Tree234
from util import rbetween, between


def tree_2_3_4_create(T):
    x = Node234()
    x.height = 0
    x.n = 0
    T.root = x


def tree_2_3_4_search(x, k):
    i = 1
    while i <= x.n and k > x.key[i]:
        i += 1
    if i <= x.n and k == x.key[i]:
        return x, i
    if x.height == 0:
        return None
    else:
        return tree_2_3_4_search(x.c[i], k)


def tree_2_3_4_split_child(x, i, y):
    z = Node234()
    z.height = y.height
    z.n = 1
    z.key[1] = y.key[3]
    if y.height > 0:
        z.c[1] = y.c[3]
        z.c[2] = y.c[4]
    y.n = 1
    for j in rbetween(x.n + 1, i + 1):
        x.c[j + 1] = x.c[j]
    x.c[i + 1] = z
    for j in rbetween(x.n, i):
        x.key[j + 1] = x.key[j]
    x.key[i] = y.key[2]
    x.n += 1


def tree_2_3_4_insert(T, k):
    r = T.root
    if r.n == 3:
        s = Node234()
        T.root = s
        s.height = r.height + 1
        s.n = 0
        s.c[1] = r
        tree_2_3_4_split_child(s, 1, r)
        tree_2_3_4_insert_nonfull(s, k)
    else:
        tree_2_3_4_insert_nonfull(r, k)


def tree_2_3_4_insert_nonfull(x, k):
    i = x.n
    if x.height == 0:
        while i >= 1 and k < x.key[i]:
            x.key[i + 1] = x.key[i]
            i -= 1
        x.key[i + 1] = k
        x.n += 1
    else:
        while i >= 1 and k < x.key[i]:
            i -= 1
        i += 1
        if x.c[i].n == 3:
            tree_2_3_4_split_child(x, i, x.c[i])
            if k > x.key[i]:
                i += 1
        tree_2_3_4_insert_nonfull(x.c[i], k)


def tree_2_3_4_left_shift(x, i):
    for j in between(i, x.n - 1):
        x.key[j] = x.key[j + 1]
    if x.height > 0:
        for j in between(i, x.n):
            x.c[j] = x.c[j + 1]
    x.n -= 1


def tree_2_3_4_right_shift(x, i):
    x.n += 1
    for j in rbetween(x.n - 1, i):
        x.key[j + 1] = x.key[j]
    if x.height > 0:
        for j in rbetween(x.n, i):
            x.c[j + 1] = x.c[j]


def tree_2_3_4_left_rotate(x, i, y, z):
    y.n += 1
    y.key[y.n] = x.key[i]
    x.key[i] = z.key[1]
    if y.height > 0:
        y.c[y.n + 1] = z.c[1]
    tree_2_3_4_left_shift(z, 1)


def tree_2_3_4_right_rotate(x, i, y, z):
    tree_2_3_4_right_shift(z, 1)
    z.key[1] = x.key[i]
    x.key[i] = y.key[y.n]
    if z.height > 0:
        z.c[1] = y.c[y.n + 1]
    y.n -= 1


def tree_2_3_4_merge_children(x, i, y, z):
    y.n = 3
    y.key[2] = x.key[i]
    y.key[3] = z.key[1]
    if y.height > 0:
        y.c[3] = z.c[1]
        y.c[4] = z.c[2]
    tree_2_3_4_left_shift(x, i)
    x.c[i] = y


def tree_2_3_4_delete_minimum(x):
    if x.height == 0:
        min = x.key[1]
        tree_2_3_4_left_shift(x, 1)
        return min
    y = x.c[1]
    if y.n == 1:
        z = x.c[2]
        if z.n >= 2:
            tree_2_3_4_left_rotate(x, 1, y, z)
        else:
            tree_2_3_4_merge_children(x, 1, y, z)
    return tree_2_3_4_delete_minimum(y)


def tree_2_3_4_delete_maximum(x):
    if x.height == 0:
        max = x.key[x.n]
        x.n -= 1
        return max
    y = x.c[x.n + 1]
    if y.n == 1:
        z = x.c[x.n]
        if z.n >= 2:
            tree_2_3_4_right_rotate(x, x.n, z, y)
        else:
            tree_2_3_4_merge_children(x, x.n, z, y)
            y = z
    return tree_2_3_4_delete_maximum(y)


def tree_2_3_4_safe_delete(x, k):
    i = 1
    while i <= x.n and k > x.key[i]:
        i += 1
    if i <= x.n and k == x.key[i]:
        if x.height == 0:
            tree_2_3_4_left_shift(x, i)
        else:
            y = x.c[i]
            if y.n >= 2:
                x.key[i] = tree_2_3_4_delete_maximum(y)
            else:
                z = x.c[i + 1]
                if z.n >= 2:
                    x.key[i] = tree_2_3_4_delete_minimum(z)
                else:
                    tree_2_3_4_merge_children(x, i, y, z)
                    tree_2_3_4_safe_delete(y, k)
    else:
        y = x.c[i]
        if y.n == 1:
            z_L = z_R = None
            if i >= 2:
                z_L = x.c[i - 1]
            if i <= x.n:
                z_R = x.c[i + 1]
            if z_L is not None and z_L.n >= 2:
                tree_2_3_4_right_rotate(x, i - 1, z_L, y)
            elif z_R is not None and z_R.n >= 2:
                tree_2_3_4_left_rotate(x, i, y, z_R)
            elif z_L is not None:
                tree_2_3_4_merge_children(x, i - 1, z_L, y)
                y = z_L
            else:
                tree_2_3_4_merge_children(x, i, y, z_R)
        tree_2_3_4_safe_delete(y, k)


def tree_2_3_4_delete(T, k):
    r = T.root
    tree_2_3_4_safe_delete(r, k)
    if r.n == 0 and r.height > 0:
        T.root = r.c[1]


def tree_2_3_4_join(T_, T__, k):
    if T_.root.n == 0:
        tree_2_3_4_insert(T__, k)
        return T__
    if T__.root.n == 0:
        tree_2_3_4_insert(T_, k)
        return T_
    h_ = T_.root.height
    h__ = T__.root.height
    if h_ < h__:
        x = tree_2_3_4_insert_at(T__, k, height=h_ + 1)
        x.c[1] = T_.root
        return T__
    if h_ > h__:
        x = tree_2_3_4_insert_at(T_, k, height=h__ + 1)
        x.c[x.n + 1] = T__.root
        return T_
    T = Tree234()
    tree_2_3_4_create(T)
    tree_2_3_4_insert(T, k)
    T.root.height = h_ + 1
    T.root.c[1] = T_.root
    T.root.c[2] = T__.root
    return T


def tree_2_3_4_insert_at(T, k, height):
    r = T.root
    if r.n == 3:
        s = Node234()
        T.root = s
        s.height = r.height + 1
        s.n = 0
        s.c[1] = r
        tree_2_3_4_split_child(s, 1, r)
        return tree_2_3_4_insert_nonfull_at(s, k, height)
    else:
        return tree_2_3_4_insert_nonfull_at(r, k, height)


def tree_2_3_4_insert_nonfull_at(x, k, height):
    i = x.n
    if x.height == height:
        x.n += 1
        x.c[x.n + 1] = x.c[x.n]
        while i >= 1 and k < x.key[i]:
            x.key[i + 1] = x.key[i]
            x.c[i + 1] = x.c[i]
            i -= 1
        x.key[i + 1] = k
        return x
    else:
        while i >= 1 and k < x.key[i]:
            i -= 1
        i += 1
        if x.c[i].n == 3:
            tree_2_3_4_split_child(x, i, x.c[i])
            if k > x.key[i]:
                i += 1
        return tree_2_3_4_insert_nonfull_at(x.c[i], k, height)
