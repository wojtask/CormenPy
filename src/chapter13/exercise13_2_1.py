def right_rotate(T, x, sentinel=None):
    y = x.left
    x.left = y.right
    if y.right is not sentinel:
        y.right.p = x
    y.p = x.p
    if x.p is sentinel:
        T.root = y
    else:
        if x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
    y.right = x
    x.p = y
