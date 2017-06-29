from util import scope


def nonincreasing_insertion_sort(A):
    for j in scope(2, A.length):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] < key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
