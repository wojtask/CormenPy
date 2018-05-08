def iterative_os_select(x, i):
    while True:
        r = x.left.size + 1
        if i == r:
            return x
        if i < r:
            x = x.left
        else:
            x = x.right
            i -= r
