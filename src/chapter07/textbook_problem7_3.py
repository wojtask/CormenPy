import math


def stooge_sort(A, i, j):
    if A[i] > A[j]:
        A[i], A[j] = A[j], A[i]
    if i + 1 >= j:
        return
    k = math.floor((j - i + 1) / 3)
    stooge_sort(A, i, j - k)
    stooge_sort(A, i + k, j)
    stooge_sort(A, i, j - k)
