from chapter09.textbook import select, partition_around


def randomized_blackbox_select(A, p, r, i):
    if p == r:
        return A[p]
    q = (p + r) // 2
    x = select(A, p, r, q)
    partition_around(A, p, r, x)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_blackbox_select(A, p, q - 1, i)
    else:
        return randomized_blackbox_select(A, q + 1, r, i - k)
