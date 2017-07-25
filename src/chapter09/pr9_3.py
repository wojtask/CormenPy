from chapter02.textbook import insertion_sort
from chapter09.textbook import select
from datastructures.array import Array
from util import between


def small_order_select(A, i):
    _small_order_select(A, 1, A.length, i)
    return A[i]


def _small_order_select(A, p, r, i):
    n = r - p + 1
    m = n // 2
    if i >= m:
        return _select_with_swaps_registration(A, p, r, i)

    swaps = []
    for j in between(0, m - 1):
        if A[p + j] < A[p + m + j]:
            A[p + j], A[p + m + j] = A[p + m + j], A[p + j]
            swaps.append((p + j, p + m + j))

    swaps_performed = _small_order_select(A, p + m, r, i)
    swaps += swaps_performed
    for j, k in swaps_performed:
        if p + m <= j < k <= p + 2 * m - 1:
            A[j - m], A[k - m] = A[k - m], A[j - m]
            swaps.append((j - m, k - m))

    for j in between(0, i - 1):
        A[p + i + j], A[p + m + j] = A[p + m + j], A[p + i + j]
        swaps.append((p + i + j, p + m + j))

    swaps += _select_with_swaps_registration(A, p, p + 2 * i - 1, i)

    return swaps


def _select_with_swaps_registration(A, p, r, i):
    n = r - p + 1
    if n == 1:
        return []
    fives = [Array(A.data[k:min(k + 5, r)]) for k in range(p - 1, r, 5)]
    for group in fives:
        insertion_sort(group)
    medians = Array([group[(group.length + 1) // 2] for group in fives])
    x = select(medians, 1, medians.length, (medians.length + 1) // 2)
    swaps = []
    q = _partition_around_with_swaps_registration(A, p, r, x, swaps)
    k = q - p + 1
    if i < k:
        return swaps + _select_with_swaps_registration(A, p, q - 1, i)
    elif i > k:
        return swaps + _select_with_swaps_registration(A, q + 1, r, i - k)
    return swaps


def _partition_around_with_swaps_registration(A, p, r, x, swaps):
    q = p
    while A[q] != x:
        q += 1
    A[q], A[r] = A[r], A[q]
    swaps.append((q, r))
    i = p - 1
    for j in between(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            swaps.append((i, j))
    A[i + 1], A[r] = A[r], A[i + 1]
    swaps.append((i + 1, r))
    return i + 1
