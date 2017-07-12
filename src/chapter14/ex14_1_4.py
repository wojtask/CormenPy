def os_key_rank(x, k):
    r = x.left.size + 1
    if k == x.key:
        return r
    if k < x.key:
        return os_key_rank(x.left, k)
    else:
        return os_key_rank(x.right, k) + r
