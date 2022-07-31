from chapter02.textbook2_1 import insertion_sort
from datastructures.array import Array
from util import between


def select_for_duplicates(A, p, r, i):
    n = r - p + 1
    if n == 1:
        return A[p]
    fives = Array(A[k:min(k + 5, r)] for k in between(p, r, step=5))
    for group in fives:
        insertion_sort(group)
    medians = Array(group[(group.length + 1) // 2] for group in fives)
    x = select_for_duplicates(medians, 1, medians.length, (medians.length + 1) // 2)
    q1, q2 = three_way_partition_around(A, p, r, x)
    k1 = q1 - p + 1
    k2 = q2 - p + 1
    if k1 <= i <= k2:
        return x
    elif i < k1:
        return select_for_duplicates(A, p, q1 - 1, i)
    else:
        return select_for_duplicates(A, q2 + 1, r, i - k2)


def three_way_partition_around(A, p, r, x):
    i = p
    j = p
    k = r
    while j <= k:
        if A[j] < x:
            A[i], A[j] = A[j], A[i]
            i += 1
            j += 1
        elif A[j] > x:
            A[j], A[k] = A[k], A[j]
            k -= 1
        else:
            j += 1
    return i, k
