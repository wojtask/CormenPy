import math

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
