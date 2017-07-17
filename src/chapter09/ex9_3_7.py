import math

from chapter09.textbook import select
from datastructures.array import Array
from util import between


def median_neighbors(A, k):
    n = A.length
    m = math.floor((n + 1) / 2)
    leftmost = select(A, 1, n, m - math.floor((k - 1) / 2))
    rightmost = select(A, 1, n, m + math.ceil((k - 1) / 2))
    N = set()
    for i in between(1, n):
        if leftmost <= A[i] <= rightmost:
            N.add(A[i])
    return N


def median_nearest(A, k):
    n = A.length
    x = select(A, 1, n, math.floor((n + 1) / 2))
    dist = Array.of_length(n)
    for i in between(1, n):
        dist[i] = abs(A[i] - x)
    y = select(dist, 1, n, k)
    N = set()
    for i in between(1, n):
        if abs(A[i] - x) <= y:
            N.add(A[i])
    if len(N) == k + 1:
        N.remove(x + y)
    return N
