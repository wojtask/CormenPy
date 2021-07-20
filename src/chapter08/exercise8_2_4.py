from datastructures.array import Array
from util import between


def counting_in_range(A, k, a, b):
    C = Array.indexed(0, k)
    for i in between(0, k):
        C[i] = 0
    for j in between(1, A.length):
        C[A[j]] += 1
    for i in between(1, k):
        C[i] = C[i] + C[i - 1]
    if 0 < a <= b <= k:
        return C[b] - C[a - 1]
    if 0 < a <= k < b:
        return C[k] - C[a - 1]
    if a <= 0 <= b <= k:
        return C[b]
    if a <= 0 <= k < b:
        return C[k]
    if a > k or b < 0:
        return 0
