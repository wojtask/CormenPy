def iterative_os_select(x, i):
    r = x.left.size + 1
    while r != i:
        if i < r:
            x = x.left
        else:
            x = x.right
            i -= r
        r = x.left.size + 1
    return x
