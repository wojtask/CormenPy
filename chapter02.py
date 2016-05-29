from util import irange


def insertion_sort(A):
    for j in irange(2, A.length):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def nonincreasing_insertion_sort(A):
    for j in irange(2, A.length):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
