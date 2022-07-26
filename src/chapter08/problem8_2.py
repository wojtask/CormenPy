from datastructures.array import Array
from util import between


def bit_sort(A):
    i = 1
    for j in between(1, A.length):
        if A[j] == 0:
            A[i], A[j] = A[j], A[i]
            i += 1


def counting_sort_in_place(A, k):
    C = Array.indexed(0, k)
    for i in between(0, k):
        C[i] = 0
    for j in between(1, A.length):
        C[A[j]] += 1
    for i in between(1, k):
        C[i] += C[i - 1]
    C_ = Array(C, start=0)
    i = 1
    while i <= A.length - 1:
        key = A[i]
        if C_[key - 1] < i <= C_[key]:
            i += 1
        else:
            A[i], A[C[key]] = A[C[key]], A[i]
            C[key] -= 1
