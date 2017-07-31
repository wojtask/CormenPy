import math

from chapter02.textbook import insertion_sort
from chapter07.textbook import randomized_partition
from datastructures.array import Array
from util import between


def minimum(A):
    min = A[1]
    for i in between(2, A.length):
        if min > A[i]:
            min = A[i]
    return min


def minimum_maximum(A):
    n = A.length
    if n % 2 == 0:
        min = math.inf
        max = -math.inf
        i = 1
    else:
        min = max = A[1]
        i = 2
    while i < n:
        if A[i] < A[i + 1]:
            if A[i] < min:
                min = A[i]
            if A[i + 1] > max:
                max = A[i + 1]
        else:
            if A[i + 1] < min:
                min = A[i + 1]
            if A[i] > max:
                max = A[i]
        i += 2
    return min, max


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


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
