from datastructures.array import Array
from util import between


def binary_add(A, B):
    n = A.length
    C = Array.indexed(0, n)
    carry = 0
    for i in between(0, n - 1):
        C[i] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) // 2
    C[n] = carry
    return C
