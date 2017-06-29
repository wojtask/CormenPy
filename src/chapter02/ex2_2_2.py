from util import scope


def selection_sort(A):
    n = A.length
    for j in scope(1, n - 1):
        min = j
        for i in scope(j + 1, n):
            if A[i] < A[min]:
                min = i
        A[min], A[j] = A[j], A[min]
