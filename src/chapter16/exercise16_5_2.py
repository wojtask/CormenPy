from datastructures.array import Array
from util import between


def tasks_independent(A, k):
    C = Array.indexed(0, k)
    for i in between(0, k):
        C[i] = 0
    for j in between(1, A.length):
        C[A[j]] += 1
    for i in between(1, k):
        C[i] = C[i] + C[i - 1]
    for t in between(1, k):
        if C[t] > t:
            return False
    return True
