import math

from chapter02.textbook2_1 import insertion_sort
from chapter09.textbook9_3 import select
from datastructures.array import Array
from util import between


def weighted_median_using_sorting(A, w):
    _sort_array_with_weights(A, w)
    weight_sum = 0.0
    i = 1
    while i <= A.length and weight_sum < 1 / 2:
        weight_sum += w[i]
        i += 1
    return A[i - 1]


def _sort_array_with_weights(A, w):
    elements_with_weights = sorted(zip(A, w), key=lambda x: x[0])
    A[:] = Array(x[0] for x in elements_with_weights)
    w[:] = Array(x[1] for x in elements_with_weights)


def weighted_median(A, w, p, r):
    if p == r:
        return A[p]
    _select_with_weights(A, w, p, r, (p + r) // 2)
    q = math.floor((p + r) / 2)
    WL = 0
    for i in between(p, q - 1):
        WL += w[i]
    WH = 1 - WL - w[q]
    if WL < 1 / 2 and WH <= 1 / 2:
        return A[q]
    if WL >= 1 / 2:
        w[q] += WH
        return weighted_median(A, w, p, q)
    else:
        w[q] += WL
        return weighted_median(A, w, q, r)


def _select_with_weights(A, w, p, r, i):
    n = r - p + 1
    if n == 1:
        return A[p]
    fives = Array(A[k:min(k + 5, r)] for k in between(p, r, step=5))
    for group in fives:
        insertion_sort(group)
    medians = Array(group[(group.length + 1) // 2] for group in fives)
    x = select(medians, 1, medians.length, (medians.length + 1) // 2)
    q = _partition_around_with_weights(A, w, p, r, x)
    k = q - p + 1
    if i == k:
        return x
    elif i < k:
        return _select_with_weights(A, w, p, q - 1, i)
    else:
        return _select_with_weights(A, w, q + 1, r, i - k)


def _partition_around_with_weights(A, w, p, r, x):
    q = p
    while A[q] != x:
        q += 1
    A[q], A[r] = A[r], A[q]
    w[q], w[r] = w[r], w[q]
    i = p - 1
    for j in between(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            w[i], w[j] = w[j], w[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    w[i + 1], w[r] = w[r], w[i + 1]
    return i + 1
