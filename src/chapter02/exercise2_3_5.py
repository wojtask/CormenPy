import math


def recursive_binary_search(A, v, low, high):
    if low > high:
        return None
    mid = math.floor((low + high) / 2)
    if v == A[mid]:
        return mid
    if v < A[mid]:
        return recursive_binary_search(A, v, low, mid - 1)
    else:
        return recursive_binary_search(A, v, mid + 1, high)


def iterative_binary_search(A, v):
    low = 1
    high = A.length
    while low <= high:
        mid = math.floor((low + high) / 2)
        if v == A[mid]:
            return mid
        if v < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None
