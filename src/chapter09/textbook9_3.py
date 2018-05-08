from chapter02.textbook2_1 import insertion_sort
from datastructures.array import Array
from util import between


def select(A, p, r, i):
    n = r - p + 1
    if n == 1:
        return A[p]
    fives = [Array(A.elements[k:min(k + 5, r)]) for k in range(p - 1, r, 5)]
    for group in fives:
        insertion_sort(group)
    medians = Array([group[(group.length + 1) // 2] for group in fives])
    x = select(medians, 1, medians.length, (medians.length + 1) // 2)
    q = partition_around(A, p, r, x)
    k = q - p + 1
    if i == k:
        return x
    elif i < k:
        return select(A, p, q - 1, i)
    else:
        return select(A, q + 1, r, i - k)


def partition_around(A, p, r, x):
    q = p
    while A[q] != x:
        q += 1
    A[q], A[r] = A[r], A[q]
    i = p - 1
    for j in between(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
