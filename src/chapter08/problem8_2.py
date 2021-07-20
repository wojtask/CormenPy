from datastructures.array import Array
from util import between


def bitwise_sort(A):
    n = A.length
    i = 1
    j = n
    while i < j:
        A[i], A[j] = A[j], A[i]
        while i <= n and A[i] == 0:
            i += 1
        while j >= 1 and A[j] == 1:
            j -= 1


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
