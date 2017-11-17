import math

from datastructures.array import Array
from util import between


def lis_length_(X):
    n = X.length
    a = Array.indexed(0, n)
    b = Array.indexed(1, n)
    for i in between(0, n):
        a[i] = 0
    longest = 0
    for i in between(1, n):
        low = 1
        high = longest
        while low <= high:
            mid = math.floor((low + high) / 2)
            if X[i] < X[a[mid]]:
                high = mid - 1
            else:
                low = mid + 1
        a[low] = i
        b[i] = a[low - 1]
        if low > longest:
            longest = low
    return longest, b, a[longest]
