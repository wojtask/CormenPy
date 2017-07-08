from chapter09.textbook import select
from datastructures.array import Array
from util import between


def median_neighbors(A, k):
    n = A.length
    x = select(A, 1, n, (n + 1) // 2)
    dist = Array.of_length(n)
    for i in between(1, n):
        dist[i] = abs(A[i] - x)
    y = select(dist, 1, n, k)
    M = set()
    for i in between(1, n):
        if abs(A[i] - x) <= y:
            M.add(A[i])
    if len(M) == k + 1:
        M.remove(x + y)
    return M
