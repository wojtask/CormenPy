from util import between, rbetween


def bubble_sort(A):
    for i in between(1, A.length):
        for j in rbetween(A.length, i + 1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
