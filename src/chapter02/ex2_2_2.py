from util import between


def selection_sort(A):
    n = A.length
    for j in between(1, n - 1):
        min = j
        for i in between(j + 1, n):
            if A[i] < A[min]:
                min = i
        A[min], A[j] = A[j], A[min]
