from util import between


def nonincreasing_insertion_sort(A):
    for j in between(2, A.length):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
