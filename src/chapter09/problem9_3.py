import math

from chapter02.textbook2_1 import insertion_sort
from chapter09.textbook9_3 import select
from datastructures.array import Array
from util import between


def small_order_select(A, i):
    B = Array(A.elements)
    idx = _small_order_select(B, 1, B.length, i)
    return B[idx]


def _small_order_select(B, p, r, i):
    n = r - p + 1
    m = n // 2

    if i >= m:
        return _select_with_cascaded_swaps(B, n, p, r, i)

    for j in between(0, m - 1):
        if B[p + j] < B[p + m + j]:
            _cascaded_swap(B, n, p + j, p + m + j)

    if n % 2 == 1:
        _cascaded_align(B, n, p + m)
        m += 1
        n += 1
        r = B.length
        p = r - n + 1

    idx = _small_order_select(B, p + m, r, i)

    r = B.length
    q = idx - i + 1
    m = r - q + 1
    n = 2 * m
    p = r - n + 1

    for j in between(0, i - 1):
        _cascaded_swap(B, n, p + i + j, p + m + j)

    _select_with_cascaded_swaps(B, n, p, p + 2 * i - 1, i)

    return p + i - 1


def _select_with_cascaded_swaps(B, m, p, r, i):
    n = r - p + 1
    if n == 1:
        return p
    fives = Array(B[k:min(k + 5, r)] for k in between(p, r, step=5))
    for group in fives:
        insertion_sort(group)
    medians = Array(group[(group.length + 1) // 2] for group in fives)
    x = select(medians, 1, medians.length, (medians.length + 1) // 2)
    q = _partition_around_with_cascaded_swaps(B, m, p, r, x)
    k = q - p + 1
    if i == k:
        return q
    elif i < k:
        return _select_with_cascaded_swaps(B, m, p, q - 1, i)
    else:
        return _select_with_cascaded_swaps(B, m, q + 1, r, i - k)


def _partition_around_with_cascaded_swaps(B, m, p, r, x):
    q = p
    while B[q] != x:
        q += 1
    _cascaded_swap(B, m, q, r)
    i = p - 1
    for j in between(p, r - 1):
        if B[j] <= x:
            i += 1
            _cascaded_swap(B, m, i, j)
    _cascaded_swap(B, m, i + 1, r)
    return i + 1


def _cascaded_swap(B, m, i, j):
    while i >= 1 and j >= 1:
        B[i], B[j] = B[j], B[i]
        i -= m
        j -= m


def _cascaded_align(B, m, i):
    while i >= 1:
        B.insert(i, math.inf)
        i -= m
