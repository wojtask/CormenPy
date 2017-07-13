from chapter09.textbook import partition_around, select


def _get_median_blackbox(A, p, r):
    n = r - p + 1
    return select(A, p, r, (n + 1) // 2)


def randomized_blackbox_select(A, p, r, i):
    if p == r:
        return A[p]
    x = _get_median_blackbox(A, p, r)
    partition_around(A, p, r, x)
    q = (p + r) // 2
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_blackbox_select(A, p, q - 1, i)
    else:
        return randomized_blackbox_select(A, q + 1, r, i - k)
