def balance_factor(x):
    hl = hr = -1
    if x.left is not None:
        hl = x.left.h
    if x.right is not None:
        hr = x.right.h
    return -hl + hr


def height(x):
    hl = hr = -1
    if x.left is not None:
        hl = x.left.h
    if x.right is not None:
        hr = x.right.h
    return max(hl, hr) + 1


def avl_left_rotate(x):
    y = x.right
    x.right = y.left
    y.left = x
    x.h = height(x)
    y.h = height(y)
    return y


def avl_right_rotate(x):
    y = x.left
    x.left = y.right
    y.right = x
    x.h = height(x)
    y.h = height(y)
    return y


def balance(x):
    if balance_factor(x) == -2:
        if balance_factor(x.left) == 1:
            x.left = avl_left_rotate(x.left)
        return avl_right_rotate(x)
    if balance_factor(x) == 2:
        if balance_factor(x.right) == -1:
            x.right = avl_right_rotate(x.right)
        return avl_left_rotate(x)
    return x


def avl_subtree_insert(x, z):
    if x is None:
        return z
    if z.key < x.key:
        x.left = avl_subtree_insert(x.left, z)
    else:
        x.right = avl_subtree_insert(x.right, z)
    x.h = height(x)
    return balance(x)


def avl_insert(T, z):
    T.root = avl_subtree_insert(T.root, z)
