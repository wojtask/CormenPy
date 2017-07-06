from chapter02.textbook import insertion_sort
from chapter05.ex5_1_2 import random
from datastructures.array import Array
from util import scope


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in scope(p, r - 1):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def randomized_partition(A, p, r):
    i = random(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)


def insertion_quicksort(A, p, r, k):
    if p < r:
        if r - p + 1 >= k:
            q = partition(A, p, r)
            insertion_quicksort(A, p, q - 1, k)
            insertion_quicksort(A, q + 1, r, k)
        else:
            nearly_sorted = Array(A.data[p - 1:r])
            insertion_sort(nearly_sorted)
            A.data[p - 1:r] = nearly_sorted.data


def hoare_partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        while True:
            j = j - 1
            if A[j] <= x:
                break
        while True:
            i = i + 1
            if A[i] >= x:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j


def stooge_sort(A, i, j):
    if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]
    if i + 1 >= j:
        return
    k = (j - i + 1) // 3
    stooge_sort(A, i, j - k)
    stooge_sort(A, i + k, j)
    stooge_sort(A, i, j - k)


def quicksort_(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort_(A, p, q - 1)
        p = q + 1


def median_of_3_partition(A, p, r):
    i1, i2, i3 = random(p, r), random(p, r), random(p, r)
    median = sorted([A[i1], A[i2], A[i3]])[1]
    if median == A[i1]:
        A[r], A[i1] = A[i1], A[r]
    elif median == A[i2]:
        A[r], A[i2] = A[i2], A[r]
    else:
        A[r], A[i3] = A[i3], A[r]
    return partition(A, p, r)
