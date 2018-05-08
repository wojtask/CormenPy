import math

from chapter09.textbook9_3 import select


def quantiles(A, p, r, k):
    if k == 1:
        return set()
    n = r - p + 1
    q1 = p + math.floor(math.floor(k / 2) * (n / k))
    q2 = p + math.floor(math.ceil(k / 2) * (n / k))
    select(A, p, r, q1 - p + 1)
    if q1 != q2:
        select(A, q1 + 1, r, q2 - q1)
    L = quantiles(A, p, q1 - 1, math.floor(k / 2))
    R = quantiles(A, q2 + 1, r, math.floor(k / 2))
    return L | {A[q1], A[q2]} | R
