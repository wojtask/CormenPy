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
    if y.left is not None:
        y.left.p = x
    y.p = x.p
    if x.p is not None:
        if x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
    y.left = x
    x.p = y
    x.h = height(x)
    y.h = height(y)


def avl_right_rotate(x):
    y = x.left
    x.left = y.right
    if y.right is not None:
        y.right.p = x
    y.p = x.p
    if x.p is not None:
        if x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
    y.right = x
    x.p = y
    x.h = height(x)
    y.h = height(y)


def balance(x):
    if balance_factor(x) == -2:
        if balance_factor(x.left) == 1:
            avl_left_rotate(x.left)
        avl_right_rotate(x)
        return x.p
    if balance_factor(x) == 2:
        if balance_factor(x.right) == -1:
            avl_right_rotate(x.right)
        avl_left_rotate(x)
        return x.p
    return x


def avl_insert(x, z):
    if x is None:
        return z
    if z.key < x.key:
        x.left = avl_insert(x.left, z)
        x.left.p = x
    else:
        x.right = avl_insert(x.right, z)
        x.right.p = x
    x.h = height(x)
    return balance(x)


def avl_insert_wrapper(T, z):
    T.root = avl_insert(T.root, z)
