import math

from datastructures.array import Array
from util import between


def binary_add(A, B):
    n = A.length
    C = Array.indexed(1, n + 1)
    for i in between(1, n + 1):
        C[i] = 0
    for i in between(1, n):
        sum = A[i] + B[i] + C[i]
        C[i] = sum % 2
        C[i + 1] = math.floor(sum / 2)
    return C
